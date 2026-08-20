#!/usr/bin/env python3
"""Structural validator for the Core Semantic Pack.

This validator checks repository integrity and declared semantic references.
It does not determine truth, domain validity, or runtime behavioral conformance.
"""

from __future__ import annotations

import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

import yaml


ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []
warnings: list[str] = []


def relpath(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def fail(message: str) -> None:
    errors.append(message)


def warn(message: str) -> None:
    warnings.append(message)


def load_yaml(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - defensive reporting
        fail(f"{relpath(path)}: YAML parse failed: {exc}")
        return None


def require_file(path_text: str) -> Path | None:
    path = ROOT / path_text
    if not path.exists():
        fail(f"Missing declared path: {path_text}")
        return None
    return path


def duplicate_ids(label: str, ids: Iterable[str]) -> None:
    counts = Counter(ids)
    for value, count in sorted(counts.items()):
        if count > 1:
            fail(f"Duplicate {label} ID {value!r} appears {count} times")


def require_fields(record: dict[str, Any], fields: Iterable[str], where: str) -> None:
    for field in fields:
        if field not in record:
            fail(f"{where}: missing required field {field!r}")


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


# Parse every YAML document first.
yaml_files = sorted(ROOT.rglob("*.yaml"))
loaded: dict[str, Any] = {}
for path in yaml_files:
    loaded[relpath(path)] = load_yaml(path)

pack = loaded.get("pack.yaml")
if not isinstance(pack, dict):
    fail("pack.yaml must contain a mapping")
    pack = {}

# Concepts and concept index.
concept_index = loaded.get("concepts/index.yaml") or {}
concept_records: list[dict[str, Any]] = []
concept_files: list[str] = []
indexed_concepts: list[str] = []

for group in concept_index.get("groups", []):
    where = "concepts/index.yaml group"
    require_fields(group, ["layer", "file", "concepts"], where)
    file_name = group.get("file")
    if not isinstance(file_name, str):
        continue
    concept_files.append(file_name)
    indexed_concepts.extend(group.get("concepts", []))
    catalog = loaded.get(file_name)
    if not isinstance(catalog, dict):
        fail(f"{file_name}: concept catalog is missing or invalid")
        continue
    records = catalog.get("concepts")
    if not isinstance(records, list):
        fail(f"{file_name}: 'concepts' must be a list")
        continue
    catalog_ids = [record.get("id") for record in records if isinstance(record, dict)]
    if catalog_ids != group.get("concepts", []):
        fail(f"{file_name}: concept order/content differs from concepts/index.yaml")
    for record in records:
        if not isinstance(record, dict):
            fail(f"{file_name}: concept record must be a mapping")
            continue
        require_fields(
            record,
            [
                "id",
                "name",
                "version",
                "status",
                "kind",
                "definition",
                "answers",
                "what_it_is_not",
                "required_relations",
                "conditional_relations",
                "boundaries",
                "derivation",
                "layer",
            ],
            f"{file_name}:{record.get('id', '<unknown>')}",
        )
        if record.get("layer") != group.get("layer"):
            fail(f"{file_name}:{record.get('id')}: layer does not match index group")
        concept_records.append(record)

concept_ids = {record.get("id") for record in concept_records if isinstance(record.get("id"), str)}
duplicate_ids("concept", [record.get("id") for record in concept_records if isinstance(record.get("id"), str)])
if set(indexed_concepts) != concept_ids:
    missing = sorted(concept_ids - set(indexed_concepts))
    extra = sorted(set(indexed_concepts) - concept_ids)
    if missing:
        fail(f"concepts/index.yaml omits concepts: {missing}")
    if extra:
        fail(f"concepts/index.yaml references missing concepts: {extra}")

# Relations.
relation_catalog = loaded.get("relations/core-relations.yaml") or {}
relation_records = relation_catalog.get("relations", [])
if not isinstance(relation_records, list):
    fail("relations/core-relations.yaml: 'relations' must be a list")
    relation_records = []
relation_ids = {record.get("id") for record in relation_records if isinstance(record, dict)}
duplicate_ids("relation", [record.get("id") for record in relation_records if isinstance(record, dict)])

for record in relation_records:
    if not isinstance(record, dict):
        fail("relations/core-relations.yaml: relation record must be a mapping")
        continue
    rid = record.get("id", "<unknown>")
    require_fields(
        record,
        ["id", "name", "version", "status", "source", "target", "definition", "direction", "provenance", "authority_effect"],
        f"relation:{rid}",
    )
    for side in ("source", "target"):
        for ref in as_list(record.get(side)):
            if ref == "core:any" or (isinstance(ref, str) and ref.startswith("semantic-category:")):
                continue
            if ref not in concept_ids:
                fail(f"relation:{rid}: unknown {side} concept {ref!r}")
    inverse = record.get("inverse")
    if inverse:
        if inverse not in relation_ids:
            fail(f"relation:{rid}: unknown inverse {inverse!r}")

relation_by_id = {record["id"]: record for record in relation_records if isinstance(record, dict) and "id" in record}
for rid, record in relation_by_id.items():
    inverse = record.get("inverse")
    if inverse and relation_by_id.get(inverse, {}).get("inverse") != rid:
        fail(f"relation:{rid}: inverse {inverse!r} is not reciprocal")

# Boundaries.
boundary_catalog = loaded.get("boundaries/core-boundaries.yaml") or {}
boundary_records = boundary_catalog.get("boundaries", [])
if not isinstance(boundary_records, list):
    fail("boundaries/core-boundaries.yaml: 'boundaries' must be a list")
    boundary_records = []
boundary_ids = {record.get("id") for record in boundary_records if isinstance(record, dict)}
duplicate_ids("boundary", [record.get("id") for record in boundary_records if isinstance(record, dict)])
failure_codes = [record.get("failure_code") for record in boundary_records if isinstance(record, dict)]
duplicate_ids("boundary failure code", [code for code in failure_codes if isinstance(code, str)])

preloaded_pattern_ids = {
    record.get("id")
    for path_text, record in loaded.items()
    if path_text.startswith("patterns/") and path_text.endswith(".yaml") and isinstance(record, dict)
}

def valid_semantic_category(ref: Any) -> bool:
    return isinstance(ref, str) and (
        ref in concept_ids
        or ref in preloaded_pattern_ids
        or ref.startswith("semantic-category:")
        or ref.startswith("architecture.")
        or ref.startswith("example.")
    )

for record in boundary_records:
    if not isinstance(record, dict):
        fail("boundaries/core-boundaries.yaml: boundary record must be a mapping")
        continue
    bid = record.get("id", "<unknown>")
    require_fields(
        record,
        ["id", "version", "status", "left", "relation", "right", "rule", "rationale", "failure_code", "severity", "applies_to"],
        f"boundary:{bid}",
    )
    for side in ("left", "right"):
        ref = record.get(side)
        if not valid_semantic_category(ref):
            fail(f"boundary:{bid}: unknown {side} category {ref!r}")

# Concept references.
for record in concept_records:
    cid = record.get("id", "<unknown>")
    for rid in record.get("required_relations", []) + record.get("conditional_relations", []):
        if rid not in relation_ids:
            fail(f"concept:{cid}: unknown relation {rid!r}")
    for bid in record.get("boundaries", []):
        if bid not in boundary_ids:
            fail(f"concept:{cid}: unknown boundary {bid!r}")

# Question contracts and index.
question_index = loaded.get("questions/index.yaml") or {}
question_records: list[dict[str, Any]] = []
indexed_questions: list[str] = []
for item in question_index.get("families", []):
    require_fields(item, ["id", "file"], "questions/index.yaml family")
    qid = item.get("id")
    file_name = item.get("file")
    if isinstance(qid, str):
        indexed_questions.append(qid)
    if not isinstance(file_name, str):
        continue
    record = loaded.get(file_name)
    if not isinstance(record, dict):
        fail(f"{file_name}: question contract is missing or invalid")
        continue
    if record.get("id") != qid:
        fail(f"{file_name}: ID differs from questions/index.yaml")
    require_fields(
        record,
        [
            "id",
            "version",
            "status",
            "family",
            "canonical_questions",
            "requires_concepts",
            "requires_relations",
            "must_preserve",
            "answer_requirements",
            "failure_states",
            "consequence_on_failure",
        ],
        file_name,
    )
    for ref in record.get("requires_concepts", []):
        if ref not in concept_ids:
            fail(f"{file_name}: unknown concept {ref!r}")
    for ref in record.get("requires_relations", []):
        if ref not in relation_ids:
            fail(f"{file_name}: unknown relation {ref!r}")
    for ref in record.get("must_preserve", []):
        if ref not in boundary_ids:
            fail(f"{file_name}: unknown boundary {ref!r}")
    question_records.append(record)

question_ids = {record.get("id") for record in question_records if isinstance(record.get("id"), str)}
duplicate_ids("question family", indexed_questions)
if set(indexed_questions) != question_ids:
    fail("questions/index.yaml does not exactly match the question contract files")

# Patterns.
pattern_paths = sorted(
    path for path in ROOT.glob("patterns/*.yaml")
    if path.name != "index.yaml"
)
pattern_records = [loaded.get(relpath(path)) for path in pattern_paths]
pattern_records = [record for record in pattern_records if isinstance(record, dict)]
pattern_ids = {record.get("id") for record in pattern_records if isinstance(record.get("id"), str)}
duplicate_ids("pattern", [record.get("id") for record in pattern_records if isinstance(record.get("id"), str)])

for record in pattern_records:
    pid = record.get("id", "<unknown>")
    require_fields(record, ["id", "version", "status", "kind", "definition", "not_a_primitive"], f"pattern:{pid}")
    if record.get("not_a_primitive") is not True:
        fail(f"pattern:{pid}: v0.1 patterns must explicitly declare not_a_primitive: true")
    for ref in record.get("composes_concepts", []):
        if ref not in concept_ids:
            fail(f"pattern:{pid}: unknown concept {ref!r}")
    for ref in record.get("required_relations", []):
        if ref not in relation_ids:
            fail(f"pattern:{pid}: unknown relation {ref!r}")
    for ref in record.get("detects_boundaries", []):
        if ref not in boundary_ids:
            fail(f"pattern:{pid}: unknown boundary {ref!r}")

# Lifecycle.
status_catalog = loaded.get("lifecycle/status-families.yaml") or {}
status_families = status_catalog.get("families", [])
if not isinstance(status_families, list):
    fail("lifecycle/status-families.yaml: 'families' must be a list")
    status_families = []
duplicate_ids(
    "status family",
    [record.get("id") for record in status_families if isinstance(record, dict) and isinstance(record.get("id"), str)],
)
transition_catalog = loaded.get("lifecycle/transition-rules.yaml") or {}
for item in transition_catalog.get("forbidden_implicit_transitions", []):
    boundary = item.get("boundary")
    if boundary not in boundary_ids:
        fail(f"lifecycle/transition-rules.yaml: unknown boundary {boundary!r}")

# Conformance rules.
rule_catalog = loaded.get("conformance/rules.yaml") or {}
rule_records = rule_catalog.get("rules", [])
if not isinstance(rule_records, list):
    fail("conformance/rules.yaml: 'rules' must be a list")
    rule_records = []
rule_ids = {record.get("id") for record in rule_records if isinstance(record, dict)}
duplicate_ids("conformance rule", [record.get("id") for record in rule_records if isinstance(record, dict)])

for record in rule_records:
    if not isinstance(record, dict):
        fail("conformance/rules.yaml: rule must be a mapping")
        continue
    rid = record.get("id", "<unknown>")
    require_fields(record, ["id", "version", "status", "scope", "requirement", "failure"], f"rule:{rid}")
    for field in ("required_concepts",):
        for ref in as_list(record.get(field)):
            if ref not in concept_ids:
                fail(f"rule:{rid}: unknown concept {ref!r}")
    for field in ("required_relations", "requires_one_of_relations", "required_relation"):
        for ref in as_list(record.get(field)):
            if ref not in relation_ids:
                fail(f"rule:{rid}: unknown relation {ref!r}")
    for field in ("boundaries", "boundary"):
        for ref in as_list(record.get(field)):
            if ref not in boundary_ids:
                fail(f"rule:{rid}: unknown boundary {ref!r}")
    required_pattern = record.get("required_pattern")
    if required_pattern and required_pattern not in pattern_ids:
        fail(f"rule:{rid}: unknown pattern {required_pattern!r}")

# Fixtures.
fixture_paths = sorted(ROOT.glob("conformance/fixtures/*/*.yaml"))
fixture_records: list[dict[str, Any]] = []
fixture_ids: set[str] = set()
for path in fixture_paths:
    path_text = relpath(path)
    record = loaded.get(path_text)
    if not isinstance(record, dict):
        fail(f"{path_text}: fixture must be a mapping")
        continue
    require_fields(record, ["id", "version", "status", "description", "expected", "objects", "relations", "expectations"], path_text)
    fid = record.get("id")
    if isinstance(fid, str):
        if fid in fixture_ids:
            fail(f"Duplicate fixture ID {fid!r}")
        fixture_ids.add(fid)
    expected = record.get("expected")
    if expected not in {"valid", "invalid"}:
        fail(f"{path_text}: expected must be 'valid' or 'invalid'")
    object_records = record.get("objects", [])
    object_ids = [item.get("id") for item in object_records if isinstance(item, dict)]
    duplicate_ids(f"{path_text} object", [oid for oid in object_ids if isinstance(oid, str)])
    object_id_set = set(object_ids)
    for item in object_records:
        if not isinstance(item, dict):
            fail(f"{path_text}: object must be a mapping")
            continue
        require_fields(item, ["id", "type"], f"{path_text}:object")
        object_type = item.get("type")
        if isinstance(object_type, str) and object_type.startswith("core.") and object_type not in concept_ids:
            fail(f"{path_text}: unknown Core object type {object_type!r}")
    for edge in record.get("relations", []):
        if not isinstance(edge, dict):
            fail(f"{path_text}: relation edge must be a mapping")
            continue
        require_fields(edge, ["relation", "source", "target"], f"{path_text}:edge")
        edge_relation = edge.get("relation")
        if edge_relation not in relation_ids:
            fail(f"{path_text}: unknown relation {edge_relation!r}")
        if edge.get("source") not in object_id_set:
            fail(f"{path_text}: edge source {edge.get('source')!r} is not a fixture object")
        if edge.get("target") not in object_id_set:
            fail(f"{path_text}: edge target {edge.get('target')!r} is not a fixture object")
    expectations = record.get("expectations", {})
    for ref in expectations.get("rules_pass", []) + expectations.get("rules_fail", []):
        if ref not in rule_ids:
            fail(f"{path_text}: unknown expected rule {ref!r}")
    for ref in expectations.get("boundaries_triggered", []):
        if ref not in boundary_ids:
            fail(f"{path_text}: unknown expected boundary {ref!r}")
    if expected == "valid":
        if expectations.get("rules_fail") or expectations.get("boundaries_triggered"):
            fail(f"{path_text}: valid fixture must not declare failures or triggered boundaries")
    elif not expectations.get("rules_fail") and not expectations.get("boundaries_triggered"):
        fail(f"{path_text}: invalid fixture must declare an expected failure or boundary")
    fixture_records.append(record)

# Coverage.
coverage = loaded.get("conformance/coverage.yaml") or {}
covered_boundaries: list[str] = []
for item in coverage.get("boundary_coverage", []):
    boundary = item.get("boundary")
    covered_boundaries.append(boundary)
    if boundary not in boundary_ids:
        fail(f"conformance/coverage.yaml: unknown boundary {boundary!r}")
    for fixture in item.get("covered_by", []):
        if fixture not in fixture_ids:
            fail(f"conformance/coverage.yaml: unknown fixture {fixture!r}")
duplicate_ids("coverage boundary", [bid for bid in covered_boundaries if isinstance(bid, str)])
if set(covered_boundaries) != boundary_ids:
    missing = sorted(boundary_ids - set(covered_boundaries))
    extra = sorted(set(covered_boundaries) - boundary_ids)
    if missing:
        fail(f"conformance/coverage.yaml omits boundaries: {missing}")
    if extra:
        fail(f"conformance/coverage.yaml includes unknown boundaries: {extra}")

covered_questions: list[str] = []
for item in coverage.get("question_coverage", []):
    qid = item.get("question_family")
    covered_questions.append(qid)
    if qid not in question_ids:
        fail(f"conformance/coverage.yaml: unknown question family {qid!r}")
    for fixture in item.get("covered_by", []):
        if fixture not in fixture_ids:
            fail(f"conformance/coverage.yaml: unknown fixture {fixture!r}")
if set(covered_questions) != question_ids:
    fail("conformance/coverage.yaml must list every Core question family")

# Mappings.
mapping = loaded.get("mappings/generic-agentic/mapping.yaml") or {}
for item in mapping.get("mappings", []):
    for ref in item.get("may_realize", []):
        if ref not in concept_ids:
            fail(f"generic agentic mapping: unknown concept {ref!r}")
    for ref in item.get("may_project_pattern", []):
        if ref not in pattern_ids:
            fail(f"generic agentic mapping: unknown pattern {ref!r}")

# Composition examples.
semantic_request = loaded.get("composition/semantic-request.example.yaml") or {}
for ref in semantic_request.get("semantic_request", {}).get("questions", []):
    if ref not in question_ids:
        fail(f"semantic request example: unknown question family {ref!r}")

resolved_pack = loaded.get("composition/resolved-pack.example.yaml") or {}
for ref in resolved_pack.get("resolved_pack", {}).get("provides_question_families", []):
    if ref not in question_ids:
        fail(f"resolved pack example: unknown question family {ref!r}")

# Examples.
example_paths = sorted(ROOT.glob("examples/*.yaml"))
for path in example_paths:
    path_text = relpath(path)
    record = loaded.get(path_text)
    if not isinstance(record, dict):
        continue
    object_ids = {item.get("id") for item in record.get("objects", []) if isinstance(item, dict)}
    for item in record.get("objects", []):
        object_type = item.get("type")
        if isinstance(object_type, str) and object_type.startswith("core.") and object_type not in concept_ids:
            fail(f"{path_text}: unknown Core object type {object_type!r}")
    for edge in record.get("relations", []):
        relation = edge.get("relation")
        if relation not in relation_ids:
            fail(f"{path_text}: unknown relation {relation!r}")
        if edge.get("source") not in object_ids or edge.get("target") not in object_ids:
            fail(f"{path_text}: relation endpoint is missing from example objects")
    for ref in record.get("critical_boundaries", []):
        if ref not in boundary_ids:
            fail(f"{path_text}: unknown critical boundary {ref!r}")

# Pack manifest.
for path_text in pack.get("entrypoints", {}).values():
    require_file(path_text)

for ref in pack.get("question_families", []):
    if ref not in question_ids:
        fail(f"pack.yaml: unknown question family {ref!r}")
for ref in pack.get("patterns", []):
    if ref not in pattern_ids:
        fail(f"pack.yaml: unknown pattern {ref!r}")

valid_fixtures = [record for record in fixture_records if record.get("expected") == "valid"]
invalid_fixtures = [record for record in fixture_records if record.get("expected") == "invalid"]
actual_counts = {
    "concepts": len(concept_ids),
    "relations": len(relation_ids),
    "boundaries": len(boundary_ids),
    "question_families": len(question_ids),
    "patterns": len(pattern_ids),
    "status_families": len(status_families),
    "conformance_rules": len(rule_ids),
    "valid_fixtures": len(valid_fixtures),
    "invalid_fixtures": len(invalid_fixtures),
}
if pack.get("counts") != actual_counts:
    fail(f"pack.yaml counts differ from repository: declared={pack.get('counts')} actual={actual_counts}")

# Release candidate.
release = loaded.get("release/0.1.0.yaml") or {}
if release.get("pack") != pack.get("id") or release.get("version") != pack.get("version"):
    fail("release/0.1.0.yaml does not identify the pack.yaml ID and version")
if release.get("counts") != actual_counts:
    fail("release/0.1.0.yaml counts differ from repository")
for group in release.get("includes", {}).values():
    for path_text in as_list(group):
        require_file(path_text)
if release.get("release_status") == "experimental-candidate" and release.get("git_commit") is None:
    warn("release/0.1.0.yaml: git_commit is unset, as expected before merge/tagging")

# Orphan and coverage diagnostics.
usage: defaultdict[str, int] = defaultdict(int)
for record in relation_records:
    for ref in as_list(record.get("source")) + as_list(record.get("target")):
        if ref in concept_ids:
            usage[ref] += 1
for record in question_records:
    for ref in record.get("requires_concepts", []):
        usage[ref] += 1
for record in pattern_records:
    for ref in record.get("composes_concepts", []):
        usage[ref] += 1
for cid in sorted(concept_ids):
    if usage[cid] == 0:
        warn(f"Concept {cid!r} is not referenced by a relation, question, or pattern")

for item in coverage.get("boundary_coverage", []):
    if not item.get("covered_by"):
        warn(f"Boundary {item.get('boundary')!r} has no fixture coverage")
    elif item.get("coverage") == "positive-separation-only":
        warn(f"Boundary {item.get('boundary')!r} has positive-only fixture coverage")

# Report.
print("Core Semantic Pack structural validation")
print(f"  YAML files:            {len(yaml_files)}")
print(f"  Concepts:              {len(concept_ids)}")
print(f"  Relations:             {len(relation_ids)}")
print(f"  Boundaries:            {len(boundary_ids)}")
print(f"  Question families:     {len(question_ids)}")
print(f"  Patterns:              {len(pattern_ids)}")
print(f"  Status families:       {len(status_families)}")
print(f"  Conformance rules:     {len(rule_ids)}")
print(f"  Valid fixtures:        {len(valid_fixtures)}")
print(f"  Invalid fixtures:      {len(invalid_fixtures)}")
print(f"  Warnings:              {len(warnings)}")
print(f"  Errors:                {len(errors)}")

if warnings:
    print("\nWarnings:")
    for message in warnings:
        print(f"  - {message}")

if errors:
    print("\nErrors:")
    for message in errors:
        print(f"  - {message}")
    sys.exit(1)

print("\nPASS: all structural references and declared counts are consistent.")
