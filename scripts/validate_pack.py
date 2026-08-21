#!/usr/bin/env python3
"""Structural validator for the Core Semantic Pack.

Checks repository integrity, atomic Semantic Question Contract structure,
family taxonomy consistency, cross-references, manifests, and fixtures.

It does not determine truth, domain validity, or runtime behavioral conformance.
"""

from __future__ import annotations

import sys
from collections import Counter
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
    except Exception as exc:
        fail(f"{relpath(path)}: YAML parse failed: {exc}")
        return None


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def duplicate_ids(label: str, ids: Iterable[str]) -> None:
    counts = Counter(ids)
    for value, count in sorted(counts.items()):
        if count > 1:
            fail(f"Duplicate {label} ID {value!r} appears {count} times")


def require_fields(record: dict[str, Any], fields: Iterable[str], where: str) -> None:
    for field in fields:
        if field not in record:
            fail(f"{where}: missing required field {field!r}")


yaml_files = sorted(ROOT.rglob("*.yaml"))
loaded = {relpath(path): load_yaml(path) for path in yaml_files}

pack = loaded.get("pack.yaml")
if not isinstance(pack, dict):
    fail("pack.yaml must contain a mapping")
    pack = {}

concept_index = loaded.get("concepts/index.yaml") or {}
concept_records: list[dict[str, Any]] = []
for group in concept_index.get("groups", []):
    file_name = group.get("file")
    if not isinstance(file_name, str):
        fail("concepts/index.yaml: group file must be a string")
        continue
    catalog = loaded.get(file_name)
    if not isinstance(catalog, dict) or not isinstance(catalog.get("concepts"), list):
        fail(f"{file_name}: missing/invalid concept catalog")
        continue
    records = catalog["concepts"]
    expected = group.get("concepts", [])
    actual = [r.get("id") for r in records if isinstance(r, dict)]
    if actual != expected:
        fail(f"{file_name}: concept IDs/order differ from concepts/index.yaml")
    concept_records.extend(r for r in records if isinstance(r, dict))

concept_ids = {r.get("id") for r in concept_records if isinstance(r.get("id"), str)}
duplicate_ids("concept", [r["id"] for r in concept_records if isinstance(r.get("id"), str)])

relation_catalog = loaded.get("relations/core-relations.yaml") or {}
relation_records = relation_catalog.get("relations", [])
if not isinstance(relation_records, list):
    fail("relations/core-relations.yaml: relations must be a list")
    relation_records = []
relation_ids = {r.get("id") for r in relation_records if isinstance(r, dict)}
relation_by_id = {r["id"]: r for r in relation_records if isinstance(r, dict) and isinstance(r.get("id"), str)}
duplicate_ids("relation", relation_ids)

boundary_catalog = loaded.get("boundaries/core-boundaries.yaml") or {}
boundary_records = boundary_catalog.get("boundaries", [])
if not isinstance(boundary_records, list):
    fail("boundaries/core-boundaries.yaml: boundaries must be a list")
    boundary_records = []
boundary_ids = {r.get("id") for r in boundary_records if isinstance(r, dict)}
duplicate_ids("boundary", boundary_ids)

qindex = loaded.get("questions/index.yaml")
if not isinstance(qindex, dict):
    fail("questions/index.yaml must contain a mapping")
    qindex = {}

model = qindex.get("question_model", {})
required_model = {
    "atomic_contract": True,
    "one_canonical_question_per_contract": True,
    "family_authority": "taxonomy-only",
    "multi_family_membership": True,
    "family_requirements_inherited": False,
}
for key, value in required_model.items():
    if model.get(key) != value:
        fail(f"questions/index.yaml: question_model.{key} must be {value!r}")

family_index = qindex.get("families", [])
contract_index = qindex.get("contracts", [])
if not isinstance(family_index, list):
    fail("questions/index.yaml: families must be a list")
    family_index = []
if not isinstance(contract_index, list):
    fail("questions/index.yaml: contracts must be a list")
    contract_index = []

family_ids = [x.get("id") for x in family_index if isinstance(x, dict) and isinstance(x.get("id"), str)]
contract_ids = [x.get("id") for x in contract_index if isinstance(x, dict) and isinstance(x.get("id"), str)]
duplicate_ids("question family", family_ids)
duplicate_ids("question contract", contract_ids)

family_set = set(family_ids)
contract_set = set(contract_ids)
family_records: dict[str, dict[str, Any]] = {}
contract_records: dict[str, dict[str, Any]] = {}

for item in family_index:
    if not isinstance(item, dict):
        fail("questions/index.yaml: family index item must be a mapping")
        continue
    require_fields(item, ["id", "file", "canonical_member_count", "related_member_count"], "questions/index.yaml family")
    file_name = item.get("file")
    rec = loaded.get(file_name) if isinstance(file_name, str) else None
    if not isinstance(rec, dict):
        fail(f"{file_name}: family file missing or invalid")
        continue
    fid = item.get("id")
    if rec.get("id") != fid:
        fail(f"{file_name}: family ID differs from index")
    require_fields(rec, ["id", "version", "status", "kind", "family", "purpose", "authority", "canonical_members", "related_members", "member_count"], file_name)
    if rec.get("kind") != "question-family":
        fail(f"{file_name}: kind must be question-family")
    auth = rec.get("authority", {})
    if auth.get("class") != "taxonomy-only":
        fail(f"{file_name}: family authority must be taxonomy-only")
    if auth.get("defines_question_requirements") is not False:
        fail(f"{file_name}: family must not define question requirements")
    if auth.get("requirements_are_inherited") is not False:
        fail(f"{file_name}: family requirements must not be inherited")
    forbidden = {"requires", "requires_concepts", "requires_relations", "must_preserve", "answer_contract", "answer_requirements", "failure_contract", "failure_states", "consequence_on_failure"}
    for field in forbidden:
        if field in rec:
            fail(f"{file_name}: taxonomy-only family contains semantic requirement field {field!r}")
    canonical = rec.get("canonical_members", [])
    related = rec.get("related_members", [])
    members = canonical + related
    if len(members) != len(set(members)):
        fail(f"{file_name}: duplicate member across canonical/related lists")
    if rec.get("member_count") != len(members):
        fail(f"{file_name}: member_count does not match lists")
    if item.get("canonical_member_count") != len(canonical):
        fail(f"{file_name}: canonical_member_count differs from index")
    if item.get("related_member_count") != len(related):
        fail(f"{file_name}: related_member_count differs from index")
    for qid in members:
        if qid not in contract_set:
            fail(f"{file_name}: unknown question contract {qid!r}")
    family_records[fid] = rec

canonical_questions: list[str] = []
for item in contract_index:
    if not isinstance(item, dict):
        fail("questions/index.yaml: contract index item must be a mapping")
        continue
    require_fields(item, ["id", "file", "canonical_question", "primary_family"], "questions/index.yaml contract")
    file_name = item.get("file")
    rec = loaded.get(file_name) if isinstance(file_name, str) else None
    if not isinstance(rec, dict):
        fail(f"{file_name}: atomic question contract missing or invalid")
        continue
    qid = item.get("id")
    if rec.get("id") != qid:
        fail(f"{file_name}: question ID differs from index")
    require_fields(rec, ["id", "version", "status", "kind", "canonical_question", "classification", "requires", "must_preserve", "answer_contract", "failure_contract", "composition"], file_name)
    if rec.get("kind") != "semantic-question-contract":
        fail(f"{file_name}: kind must be semantic-question-contract")
    cq = rec.get("canonical_question")
    if not isinstance(cq, str) or not cq.strip():
        fail(f"{file_name}: canonical_question must be one non-empty string")
    else:
        canonical_questions.append(cq)
        if item.get("canonical_question") != cq:
            fail(f"{file_name}: canonical question differs from index")
    cls = rec.get("classification", {})
    primary = cls.get("primary_family")
    families = cls.get("families")
    if primary not in family_set:
        fail(f"{file_name}: unknown primary family {primary!r}")
    if not isinstance(families, list) or not families:
        fail(f"{file_name}: classification.families must be a non-empty list")
        families = []
    if primary not in families:
        fail(f"{file_name}: primary family must be included in classification.families")
    for fid in families:
        if fid not in family_set:
            fail(f"{file_name}: unknown family {fid!r}")
    if item.get("primary_family") != primary:
        fail(f"{file_name}: primary family differs from index")

    req = rec.get("requires", {})
    concepts = req.get("concepts", [])
    relations = req.get("relations", [])
    if not isinstance(concepts, list) or not isinstance(relations, list):
        fail(f"{file_name}: requires.concepts and requires.relations must be lists")
        concepts, relations = [], []
    for cid in concepts:
        if cid not in concept_ids:
            fail(f"{file_name}: unknown required concept {cid!r}")
    for rid in relations:
        if rid not in relation_ids:
            fail(f"{file_name}: unknown required relation {rid!r}")

    boundaries = rec.get("must_preserve", {}).get("boundaries", [])
    if not isinstance(boundaries, list):
        fail(f"{file_name}: must_preserve.boundaries must be a list")
        boundaries = []
    for bid in boundaries:
        if bid not in boundary_ids:
            fail(f"{file_name}: unknown required boundary {bid!r}")

    minimum = rec.get("answer_contract", {}).get("minimum_requirements")
    failures = rec.get("failure_contract", {}).get("failure_states")
    consequence = rec.get("failure_contract", {}).get("consequence_on_failure")
    if not isinstance(minimum, list) or not minimum:
        fail(f"{file_name}: answer_contract.minimum_requirements must be non-empty")
    if not isinstance(failures, list) or not failures:
        fail(f"{file_name}: failure_contract.failure_states must be non-empty")
    if not isinstance(consequence, dict) or not consequence:
        fail(f"{file_name}: consequence_on_failure must be a non-empty mapping")

    comp = rec.get("composition", {})
    if comp.get("independently_resolvable") is not True:
        fail(f"{file_name}: contract must be independently_resolvable")
    if comp.get("requirements_inherited_from_family") is not False:
        fail(f"{file_name}: contract must not inherit requirements from family")

    cset = set(concepts)
    for rid in relations:
        r = relation_by_id.get(rid)
        if not r:
            continue
        sources = set(as_list(r.get("source")))
        targets = set(as_list(r.get("target")))
        source_ok = "core:any" in sources or any(isinstance(s, str) and s.startswith("semantic-category:") for s in sources) or bool(sources & cset)
        target_ok = "core:any" in targets or any(isinstance(t, str) and t.startswith("semantic-category:") for t in targets) or bool(targets & cset)
        if not source_ok or not target_ok:
            fail(f"{file_name}: required relation {rid!r} endpoints are not represented by required concepts")

    contract_records[qid] = rec

duplicate_ids("canonical question", canonical_questions)

for qid, rec in contract_records.items():
    cls = rec["classification"]
    primary = cls["primary_family"]
    for fid in cls["families"]:
        fam = family_records.get(fid)
        if fam and qid not in fam.get("canonical_members", []) and qid not in fam.get("related_members", []):
            fail(f"{qid}: declares family {fid} but family does not list the contract")
    fam = family_records.get(primary)
    if fam and qid not in fam.get("canonical_members", []):
        fail(f"{qid}: primary family {primary} must list it as canonical_member")

for fid, fam in family_records.items():
    for qid in fam.get("canonical_members", []):
        rec = contract_records.get(qid)
        if rec and rec.get("classification", {}).get("primary_family") != fid:
            fail(f"{fid}: canonical member {qid} does not declare this primary family")
    for qid in fam.get("related_members", []):
        rec = contract_records.get(qid)
        if rec:
            cls = rec.get("classification", {})
            if fid not in cls.get("families", []):
                fail(f"{fid}: related member {qid} does not classify itself into this family")
            if cls.get("primary_family") == fid:
                fail(f"{fid}: related member {qid} incorrectly uses this as primary family")

legacy_family_paths = [ROOT / "questions" / f"{name}.yaml" for name in ("ontological", "state", "epistemic", "interpretive", "teleological", "agency", "governance", "memory", "reflective")]
for path in legacy_family_paths:
    if path.exists():
        fail(f"{relpath(path)}: legacy family-level requirement bundle must be removed")

for transient in [ROOT / ".bootstrap", ROOT / ".github/workflows/apply-question-refactor.yml"]:
    if transient.exists():
        fail(f"{relpath(transient)}: transient refactor artifact must not remain in the pack")

pattern_records = [loaded[relpath(path)] for path in sorted(ROOT.glob("patterns/*.yaml")) if isinstance(loaded.get(relpath(path)), dict)]
pattern_ids = {r.get("id") for r in pattern_records if isinstance(r.get("id"), str)}

status_catalog = loaded.get("lifecycle/status-families.yaml") or {}
status_families = status_catalog.get("families", [])
if not isinstance(status_families, list):
    status_families = []
    fail("lifecycle/status-families.yaml: families must be a list")

rule_catalog = loaded.get("conformance/rules.yaml") or {}
rules = rule_catalog.get("rules", [])
if not isinstance(rules, list):
    rules = []
    fail("conformance/rules.yaml: rules must be a list")
rule_ids = {r.get("id") for r in rules if isinstance(r, dict)}

fixture_records = []
for path in sorted(ROOT.glob("conformance/fixtures/*/*.yaml")):
    rec = loaded.get(relpath(path))
    if isinstance(rec, dict):
        fixture_records.append(rec)

valid_fixtures = [r for r in fixture_records if r.get("expected") == "valid"]
invalid_fixtures = [r for r in fixture_records if r.get("expected") == "invalid"]

semantic_request = loaded.get("composition/semantic-request.example.yaml") or {}
for qid in semantic_request.get("semantic_request", {}).get("questions", []):
    if qid not in contract_set:
        fail(f"composition/semantic-request.example.yaml: unknown atomic question {qid!r}")

resolved = loaded.get("composition/resolved-pack.example.yaml") or {}
for qid in resolved.get("resolved_pack", {}).get("provides_questions", []):
    if qid not in contract_set:
        fail(f"composition/resolved-pack.example.yaml: unknown atomic question {qid!r}")

actual_counts = {
    "concepts": len(concept_ids),
    "relations": len(relation_ids),
    "boundaries": len(boundary_ids),
    "question_families": len(family_set),
    "question_contracts": len(contract_set),
    "patterns": len(pattern_ids),
    "status_families": len(status_families),
    "conformance_rules": len(rule_ids),
    "valid_fixtures": len(valid_fixtures),
    "invalid_fixtures": len(invalid_fixtures),
}

if pack.get("counts") != actual_counts:
    fail(f"pack.yaml counts differ from repository: declared={pack.get('counts')} actual={actual_counts}")

pqm = pack.get("question_model", {})
if pqm.get("atomic_contracts") is not True:
    fail("pack.yaml: question_model.atomic_contracts must be true")
if pqm.get("families_taxonomy_only") is not True:
    fail("pack.yaml: question_model.families_taxonomy_only must be true")
if pqm.get("family_requirements_inherited") is not False:
    fail("pack.yaml: family requirements must not be inherited")

for fid in pack.get("question_families", []):
    if fid not in family_set:
        fail(f"pack.yaml: unknown question family {fid!r}")

release = loaded.get("release/0.1.0.yaml") or {}
if release.get("pack") != pack.get("id") or release.get("version") != pack.get("version"):
    fail("release/0.1.0.yaml does not identify pack.yaml ID/version")
if release.get("counts") != actual_counts:
    fail("release/0.1.0.yaml counts differ from repository")
if release.get("release_status") == "experimental-candidate" and release.get("git_commit") is None:
    warn("release/0.1.0.yaml: git_commit is unset, as expected before merge/tagging")

print("Core Semantic Pack structural validation")
print(f"  YAML files:            {len(yaml_files)}")
print(f"  Concepts:              {len(concept_ids)}")
print(f"  Relations:             {len(relation_ids)}")
print(f"  Boundaries:            {len(boundary_ids)}")
print(f"  Question families:     {len(family_set)}")
print(f"  Question contracts:    {len(contract_set)}")
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

print("\nPASS: atomic question model and structural references are consistent.")
