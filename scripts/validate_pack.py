#!/usr/bin/env python3
"""Structural and canonical-notation validator for the Core Semantic Pack.

The validator distinguishes registry identity fields from semantic authoring
fields. It validates deterministic canonical resolution, repository topology,
question atomicity, taxonomy-only families, and every checked authoring surface.
It does not determine truth, domain validity, or runtime behavior.
"""

from __future__ import annotations

import re
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


def require_fields(record: dict[str, Any], fields: Iterable[str], where: str) -> None:
    for field in fields:
        if field not in record:
            fail(f"{where}: missing required field {field!r}")


def duplicate_values(label: str, values: Iterable[str]) -> None:
    for value, count in sorted(Counter(values).items()):
        if count > 1:
            fail(f"Duplicate {label} {value!r} appears {count} times")


def strings(value: Any, where: str) -> list[str]:
    if not isinstance(value, list):
        fail(f"{where}: must be a list")
        return []
    result = []
    for item in value:
        if not isinstance(item, str) or not item:
            fail(f"{where}: entries must be non-empty strings")
        else:
            result.append(item)
    return result


def reject_registry_ids(values: Iterable[str], where: str) -> None:
    for value in values:
        if value.startswith("core.") or value.startswith("semantic-category:") or value.startswith("architecture."):
            fail(f"{where}: legacy registry ID {value!r} is not valid canonical authoring notation")


def index_unique(records: Iterable[dict[str, Any]], field: str, label: str) -> dict[str, dict[str, Any]]:
    values = [record.get(field) for record in records if isinstance(record.get(field), str)]
    duplicate_values(label, values)
    return {record[field]: record for record in records if isinstance(record.get(field), str)}


yaml_paths = sorted(ROOT.rglob("*.yaml"))
loaded = {relpath(path): load_yaml(path) for path in yaml_paths}


# Concepts and the concept index bridge.
concept_index = loaded.get("concepts/index.yaml")
if not isinstance(concept_index, dict):
    fail("concepts/index.yaml must contain a mapping")
    concept_index = {}

concept_records: list[dict[str, Any]] = []
for group in concept_index.get("groups", []):
    if not isinstance(group, dict):
        fail("concepts/index.yaml: each group must be a mapping")
        continue
    require_fields(group, ["layer", "file", "concepts"], "concepts/index.yaml group")
    file_name = group.get("file")
    catalog = loaded.get(file_name) if isinstance(file_name, str) else None
    if not isinstance(catalog, dict) or not isinstance(catalog.get("concepts"), list):
        fail(f"{file_name}: missing or invalid concept catalog")
        continue
    records = [record for record in catalog["concepts"] if isinstance(record, dict)]
    bridge = group.get("concepts", [])
    expected = [{"symbol": record.get("symbol"), "id": record.get("id")} for record in records]
    if bridge != expected:
        fail(f"{file_name}: concept symbol/ID order differs from concepts/index.yaml")
    concept_records.extend(records)

for record in concept_records:
    where = str(record.get("id", "concept record"))
    require_fields(record, ["id", "symbol", "version", "status", "kind", "definition", "required_relations", "conditional_relations", "boundaries", "derivation", "layer"], where)
    for forbidden in ("name", "answers", "what_it_is_not"):
        if forbidden in record:
            fail(f"{where}: legacy field {forbidden!r} must not remain")
    symbol = record.get("symbol")
    if not isinstance(symbol, str) or not re.fullmatch(r"[A-Z][A-Za-z0-9]*", symbol):
        fail(f"{where}: concept symbol must be PascalCase")

concept_by_id = index_unique(concept_records, "id", "concept ID")
concept_by_symbol = index_unique(concept_records, "symbol", "concept symbol")


# Reference-only categories are explicit but are never Core primitives.
reference_catalog = loaded.get("references/non-core-symbols.yaml")
if not isinstance(reference_catalog, dict) or not isinstance(reference_catalog.get("references"), list):
    fail("references/non-core-symbols.yaml: missing or invalid reference-only registry")
    reference_records: list[dict[str, Any]] = []
else:
    reference_records = [record for record in reference_catalog["references"] if isinstance(record, dict)]

for record in reference_records:
    where = str(record.get("id", "reference-only record"))
    require_fields(record, ["id", "symbol", "kind", "core_primitive", "definition"], where)
    if record.get("core_primitive") is not False:
        fail(f"{where}: reference-only symbol must declare core_primitive: false")
    symbol = record.get("symbol")
    if not isinstance(symbol, str) or not re.fullmatch(r"[A-Z][A-Za-z0-9]*", symbol):
        fail(f"{where}: reference-only symbol must be PascalCase")

reference_by_id = index_unique(reference_records, "id", "reference-only ID")
reference_by_symbol = index_unique(reference_records, "symbol", "reference-only symbol")


# Patterns are non-primitive referencable semantic objects.
pattern_records: list[dict[str, Any]] = []
for path in sorted(ROOT.glob("patterns/*.yaml")):
    record = loaded.get(relpath(path))
    if isinstance(record, dict):
        pattern_records.append(record)

for record in pattern_records:
    where = str(record.get("id", "pattern record"))
    require_fields(record, ["id", "symbol", "version", "status", "kind", "definition", "not_a_primitive"], where)
    if record.get("not_a_primitive") is not True:
        fail(f"{where}: pattern must declare not_a_primitive: true")
    if "name" in record:
        fail(f"{where}: redundant name field must not remain")
    symbol = record.get("symbol")
    if not isinstance(symbol, str) or not re.fullmatch(r"[A-Z][A-Za-z0-9]*", symbol):
        fail(f"{where}: pattern symbol must be PascalCase")

pattern_by_id = index_unique(pattern_records, "id", "pattern ID")
pattern_by_symbol = index_unique(pattern_records, "symbol", "pattern symbol")


# Unqualified symbols used as semantic types must resolve without ambiguity.
type_symbol_sources: dict[str, list[str]] = {}
for label, index in (
    ("concept", concept_by_symbol),
    ("reference-only", reference_by_symbol),
    ("pattern", pattern_by_symbol),
):
    for symbol in index:
        type_symbol_sources.setdefault(symbol, []).append(label)
for symbol, sources in sorted(type_symbol_sources.items()):
    if len(sources) > 1:
        fail(f"Ambiguous semantic type symbol {symbol!r} appears in {', '.join(sources)} namespaces")
if "Any" in type_symbol_sources:
    fail("Any is reserved meta-notation and must not be registered as a semantic object")


def resolve_type(value: Any, where: str, *, allow_any: bool = False) -> bool:
    if not isinstance(value, str) or not value:
        fail(f"{where}: semantic type reference must be a non-empty string")
        return False
    reject_registry_ids([value], where)
    if value == "Any":
        if not allow_any:
            fail(f"{where}: reserved Any meta-symbol is not valid here")
            return False
        return True
    sources = type_symbol_sources.get(value, [])
    if len(sources) != 1:
        fail(f"{where}: unknown or ambiguous semantic type symbol {value!r}")
        return False
    return True


# Relations: stable identity plus unique lowerCamelCase canonical symbol.
relation_catalog = loaded.get("relations/core-relations.yaml")
if not isinstance(relation_catalog, dict) or not isinstance(relation_catalog.get("relations"), list):
    fail("relations/core-relations.yaml: missing or invalid relation catalog")
    relation_records: list[dict[str, Any]] = []
else:
    relation_records = [record for record in relation_catalog["relations"] if isinstance(record, dict)]

for record in relation_records:
    where = str(record.get("id", "relation record"))
    require_fields(record, ["id", "symbol", "version", "status", "source", "target", "definition", "direction", "provenance", "authority_effect"], where)
    if "name" in record:
        fail(f"{where}: redundant name field must not remain")
    symbol = record.get("symbol")
    if not isinstance(symbol, str) or not re.fullmatch(r"[a-z][A-Za-z0-9]*", symbol):
        fail(f"{where}: relation symbol must be lowerCamelCase")
    for endpoint in strings(record.get("source"), f"{where}.source"):
        resolve_type(endpoint, f"{where}.source", allow_any=True)
    for endpoint in strings(record.get("target"), f"{where}.target"):
        resolve_type(endpoint, f"{where}.target", allow_any=True)

relation_by_id = index_unique(relation_records, "id", "relation ID")
relation_by_symbol = index_unique(relation_records, "symbol", "relation symbol")
for record in relation_records:
    inverse = record.get("inverse")
    if inverse is not None:
        reject_registry_ids([inverse], f"{record['id']}.inverse")
        if inverse not in relation_by_symbol:
            fail(f"{record['id']}: unknown inverse relation symbol {inverse!r}")
        elif relation_by_symbol[inverse].get("inverse") != record.get("symbol"):
            fail(f"{record['id']}: inverse relation {inverse!r} is not reciprocal")


def resolve_relation(value: Any, where: str) -> bool:
    if not isinstance(value, str):
        fail(f"{where}: relation reference must be a string")
        return False
    reject_registry_ids([value], where)
    if value not in relation_by_symbol:
        fail(f"{where}: unknown relation symbol {value!r}")
        return False
    return True


# Boundaries: exact expression maps to one stable record and operands resolve.
boundary_catalog = loaded.get("boundaries/core-boundaries.yaml")
if not isinstance(boundary_catalog, dict) or not isinstance(boundary_catalog.get("boundaries"), list):
    fail("boundaries/core-boundaries.yaml: missing or invalid boundary catalog")
    boundary_records: list[dict[str, Any]] = []
else:
    boundary_records = [record for record in boundary_catalog["boundaries"] if isinstance(record, dict)]

for record in boundary_records:
    where = str(record.get("id", "boundary record"))
    require_fields(record, ["id", "expression", "version", "status", "left", "operator", "right", "rule", "rationale", "failure_code", "severity", "applies_to"], where)
    if record.get("operator") != "!=":
        fail(f"{where}: boundary operator must be '!='")
    left, right = record.get("left"), record.get("right")
    resolve_type(left, f"{where}.left")
    resolve_type(right, f"{where}.right")
    expected = f"{left} != {right}"
    if record.get("expression") != expected:
        fail(f"{where}: expression must exactly agree with operands ({expected!r})")
    if "relation" in record or "name" in record:
        fail(f"{where}: legacy relation/name field must not remain")

boundary_by_id = index_unique(boundary_records, "id", "boundary ID")
boundary_by_expression = index_unique(boundary_records, "expression", "boundary expression")


def resolve_boundary(value: Any, where: str) -> bool:
    if not isinstance(value, str):
        fail(f"{where}: boundary reference must be a string")
        return False
    reject_registry_ids([value], where)
    if value not in boundary_by_expression:
        fail(f"{where}: unknown boundary expression {value!r}")
        return False
    return True


# Validate canonical semantic references inside concept and pattern records now
# that all relevant indexes exist.
for record in concept_records:
    where = record["id"]
    for field in ("required_relations", "conditional_relations"):
        for value in strings(record.get(field), f"{where}.{field}"):
            resolve_relation(value, f"{where}.{field}")
    for value in strings(record.get("boundaries"), f"{where}.boundaries"):
        resolve_boundary(value, f"{where}.boundaries")
    for value in strings(record.get("not_equivalent_to", []), f"{where}.not_equivalent_to"):
        resolve_type(value, f"{where}.not_equivalent_to")
    if "exclusions" in record:
        strings(record["exclusions"], f"{where}.exclusions")

for record in pattern_records:
    where = record["id"]
    composes = record.get("composes", {})
    if composes:
        if not isinstance(composes, dict):
            fail(f"{where}.composes: must be a mapping")
        else:
            for value in strings(composes.get("concepts", []), f"{where}.composes.concepts"):
                if value not in concept_by_symbol:
                    fail(f"{where}.composes.concepts: unknown Core concept symbol {value!r}")
                resolve_type(value, f"{where}.composes.concepts")
            for value in strings(composes.get("relations", []), f"{where}.composes.relations"):
                resolve_relation(value, f"{where}.composes.relations")
    for value in strings(record.get("detects_boundaries", []), f"{where}.detects_boundaries"):
        resolve_boundary(value, f"{where}.detects_boundaries")
    for forbidden in ("composes_concepts", "required_relations"):
        if forbidden in record:
            fail(f"{where}: legacy pattern field {forbidden!r} must not remain")


# Atomic Questions organized under exactly one primary family.
question_index = loaded.get("questions/index.yaml")
if not isinstance(question_index, dict):
    fail("questions/index.yaml must contain a mapping")
    question_index = {}

required_question_model = {
    "atomic_contract": True,
    "one_canonical_question_per_contract": True,
    "one_primary_family_per_question": True,
    "family_authority": "taxonomy-only",
    "independently_resolvable": True,
    "family_requirements_inherited": False,
    "canonical_question_resolution": "exact",
    "related_questions_expand_automatically": False,
}
model = question_index.get("question_model", {})
for key, expected in required_question_model.items():
    if model.get(key) != expected:
        fail(f"questions/index.yaml: question_model.{key} must be {expected!r}")
if "multi_family_membership" in model:
    fail("questions/index.yaml: superseded multi_family_membership field must not remain")

family_entries = question_index.get("families", [])
question_entries = question_index.get("questions", [])
if "contracts" in question_index:
    fail("questions/index.yaml: use questions, not legacy contracts index")
if not isinstance(family_entries, list):
    fail("questions/index.yaml: families must be a list")
    family_entries = []
if not isinstance(question_entries, list):
    fail("questions/index.yaml: questions must be a list")
    question_entries = []

family_records: list[dict[str, Any]] = []
family_path_set: set[str] = set()
for entry in family_entries:
    if not isinstance(entry, dict):
        fail("questions/index.yaml: family entries must be mappings")
        continue
    require_fields(entry, ["symbol", "id", "file", "question_count", "related_question_count"], "questions/index.yaml family")
    file_name = entry.get("file")
    record = loaded.get(file_name) if isinstance(file_name, str) else None
    if not isinstance(record, dict):
        fail(f"{file_name}: family file missing or invalid")
        continue
    family_path_set.add(file_name)
    require_fields(record, ["id", "symbol", "version", "status", "kind", "purpose", "authority", "questions", "related_questions"], file_name)
    if record.get("id") != entry.get("id") or record.get("symbol") != entry.get("symbol"):
        fail(f"{file_name}: family ID/symbol differs from index")
    if record.get("kind") != "question-family":
        fail(f"{file_name}: kind must be question-family")
    symbol = record.get("symbol")
    if not isinstance(symbol, str) or not re.fullmatch(r"[a-z][a-z0-9-]*", symbol):
        fail(f"{file_name}: family symbol must be a lowercase slug")
    authority = record.get("authority", {})
    if authority.get("class") != "taxonomy-only" or authority.get("defines_question_requirements") is not False or authority.get("requirements_are_inherited") is not False:
        fail(f"{file_name}: family must be taxonomy-only and must not define/inherit requirements")
    forbidden = {"requires", "must_preserve", "answer_contract", "failure_contract", "canonical_members", "related_members", "member_count", "family", "name"}
    for field in forbidden:
        if field in record:
            fail(f"{file_name}: legacy or semantic-requirement field {field!r} must not remain")
    primary = strings(record.get("questions"), f"{file_name}.questions")
    related = strings(record.get("related_questions"), f"{file_name}.related_questions")
    if len(primary + related) != len(set(primary + related)):
        fail(f"{file_name}: duplicate question across questions/related_questions")
    if entry.get("question_count") != len(primary) or entry.get("related_question_count") != len(related):
        fail(f"{file_name}: family counts differ from index")
    family_records.append(record)

family_by_id = index_unique(family_records, "id", "question family ID")
family_by_symbol = index_unique(family_records, "symbol", "question family symbol")

question_records: list[dict[str, Any]] = []
question_path_by_id: dict[str, str] = {}
for entry in question_entries:
    if not isinstance(entry, dict):
        fail("questions/index.yaml: question entries must be mappings")
        continue
    require_fields(entry, ["canonical_question", "id", "family", "file"], "questions/index.yaml question")
    file_name = entry.get("file")
    record = loaded.get(file_name) if isinstance(file_name, str) else None
    if not isinstance(record, dict):
        fail(f"{file_name}: atomic question file missing or invalid")
        continue
    require_fields(record, ["id", "version", "status", "kind", "canonical_question", "family", "requires", "must_preserve", "answer_contract", "failure_contract"], file_name)
    for forbidden in ("classification", "composition", "name", "symbol"):
        if forbidden in record:
            fail(f"{file_name}: superseded question field {forbidden!r} must not remain")
    if record.get("id") != entry.get("id") or record.get("canonical_question") != entry.get("canonical_question") or record.get("family") != entry.get("family"):
        fail(f"{file_name}: question identity/reference/family differs from index")
    if record.get("kind") != "semantic-question-contract":
        fail(f"{file_name}: kind must be semantic-question-contract")
    canonical = record.get("canonical_question")
    if not isinstance(canonical, str) or not canonical.strip():
        fail(f"{file_name}: canonical_question must be exactly one non-empty string")
    family = record.get("family")
    if family not in family_by_symbol:
        fail(f"{file_name}: unknown primary family symbol {family!r}")
    expected_parent = f"questions/families/{family}/"
    if not isinstance(file_name, str) or not file_name.startswith(expected_parent) or file_name.endswith("/family.yaml"):
        fail(f"{file_name}: question must live under its declared primary family")

    requires = record.get("requires", {})
    concepts = strings(requires.get("concepts") if isinstance(requires, dict) else None, f"{file_name}.requires.concepts")
    relations = strings(requires.get("relations") if isinstance(requires, dict) else None, f"{file_name}.requires.relations")
    reject_registry_ids(concepts, f"{file_name}.requires.concepts")
    reject_registry_ids(relations, f"{file_name}.requires.relations")
    for value in concepts:
        if value not in concept_by_symbol:
            fail(f"{file_name}: unknown required Core concept symbol {value!r}")
    for value in relations:
        resolve_relation(value, f"{file_name}.requires.relations")
    for value in strings(record.get("must_preserve"), f"{file_name}.must_preserve"):
        resolve_boundary(value, f"{file_name}.must_preserve")

    minimum = record.get("answer_contract", {}).get("minimum_requirements")
    failures = record.get("failure_contract", {}).get("failure_states")
    consequence = record.get("failure_contract", {}).get("consequence_on_failure")
    if not isinstance(minimum, list) or not minimum:
        fail(f"{file_name}: answer_contract.minimum_requirements must be non-empty")
    if not isinstance(failures, list) or not failures:
        fail(f"{file_name}: failure_contract.failure_states must be non-empty")
    if not isinstance(consequence, dict) or not consequence:
        fail(f"{file_name}: failure_contract.consequence_on_failure must be non-empty")

    required_concepts = set(concepts)
    for relation_symbol in relations:
        relation = relation_by_symbol.get(relation_symbol)
        if not relation:
            continue
        for endpoint_name in ("source", "target"):
            endpoints = set(as_list(relation.get(endpoint_name)))
            represented = "Any" in endpoints or bool(endpoints & required_concepts) or any(
                endpoint in reference_by_symbol or endpoint in pattern_by_symbol for endpoint in endpoints
            )
            if not represented:
                fail(f"{file_name}: relation {relation_symbol!r} {endpoint_name} endpoints are not represented by required concepts")

    question_records.append(record)
    if isinstance(record.get("id"), str) and isinstance(file_name, str):
        question_path_by_id[record["id"]] = file_name

question_by_id = index_unique(question_records, "id", "question ID")
question_by_canonical = index_unique(question_records, "canonical_question", "canonical question")

for record in question_records:
    canonical = record["canonical_question"]
    family = record["family"]
    family_record = family_by_symbol.get(family)
    if family_record and canonical not in family_record.get("questions", []):
        fail(f"{record['id']}: primary family {family!r} does not list its canonical question")

primary_occurrences = Counter(canonical for family in family_records for canonical in family.get("questions", []))
for canonical in question_by_canonical:
    if primary_occurrences[canonical] != 1:
        fail(f"Canonical question {canonical!r} must appear in exactly one family.questions list")
for family in family_records:
    for canonical in family.get("questions", []):
        question = question_by_canonical.get(canonical)
        if not question:
            fail(f"{family['id']}: unknown canonical question {canonical!r}")
        elif question.get("family") != family.get("symbol"):
            fail(f"{family['id']}: question {canonical!r} declares a different primary family")
    for canonical in family.get("related_questions", []):
        question = question_by_canonical.get(canonical)
        if not question:
            fail(f"{family['id']}: unknown related canonical question {canonical!r}")
        elif question.get("family") == family.get("symbol"):
            fail(f"{family['id']}: related question {canonical!r} is already local to this family")

expected_related = {"reflective": ["Has the Goal changed?"]}
for family in family_records:
    expected = expected_related.get(family["symbol"], [])
    if family.get("related_questions") != expected:
        fail(f"{family['id']}: related_questions must match the canonical v0.1 family architecture")

# Physical topology and serialization/index agreement.
if (ROOT / "questions/contracts").exists():
    fail("questions/contracts: legacy contracts hierarchy must not remain")
for path in sorted((ROOT / "questions/families").glob("*.yaml")):
    fail(f"{relpath(path)}: family file must live at questions/families/<family>/family.yaml")
actual_family_paths = {relpath(path) for path in (ROOT / "questions/families").glob("*/family.yaml")}
actual_question_paths = {
    relpath(path)
    for path in (ROOT / "questions/families").glob("*/*.yaml")
    if path.name != "family.yaml"
}
if actual_family_paths != family_path_set:
    fail("questions/index.yaml: indexed family paths differ from physical family files")
if actual_question_paths != set(question_path_by_id.values()):
    fail("questions/index.yaml: indexed question paths differ from physical atomic question files")

# Concept-to-question links resolve only by exact canonical value.
for record in concept_records:
    for canonical in strings(record.get("helps_answer", []), f"{record['id']}.helps_answer"):
        if canonical not in question_by_canonical:
            fail(f"{record['id']}: helps_answer contains unknown canonical question {canonical!r}")
if not (ROOT / "docs/canonical-question-gaps.md").is_file():
    fail("docs/canonical-question-gaps.md: audited non-exact concept question gaps must be retained for review")


# Status families and lifecycle semantic references.
status_catalog = loaded.get("lifecycle/status-families.yaml") or {}
status_records = status_catalog.get("families", [])
if not isinstance(status_records, list):
    fail("lifecycle/status-families.yaml: families must be a list")
    status_records = []
status_records = [record for record in status_records if isinstance(record, dict)]
for record in status_records:
    where = str(record.get("id", "status family"))
    require_fields(record, ["id", "symbol", "purpose", "values"], where)
    if "name" in record:
        fail(f"{where}: redundant name field must not remain")
    symbol = record.get("symbol")
    if not isinstance(symbol, str) or not re.fullmatch(r"[A-Z][A-Za-z0-9]*", symbol):
        fail(f"{where}: status-family symbol must be PascalCase")
    for value in strings(record.get("applies_to", []), f"{where}.applies_to"):
        resolve_type(value, f"{where}.applies_to")
status_by_id = index_unique(status_records, "id", "status-family ID")
status_by_symbol = index_unique(status_records, "symbol", "status-family symbol")
for distinction in status_catalog.get("status_distinctions", []):
    if not isinstance(distinction, dict):
        fail("lifecycle/status-families.yaml: status_distinctions entries must be mappings")
        continue
    for side in ("left", "right"):
        if distinction.get(side) not in status_by_symbol:
            fail(f"lifecycle/status-families.yaml: unknown status-family symbol {distinction.get(side)!r}")

transition_rules = loaded.get("lifecycle/transition-rules.yaml") or {}
for item in transition_rules.get("families", []):
    if item.get("family") not in status_by_symbol:
        fail(f"lifecycle/transition-rules.yaml: unknown status-family symbol {item.get('family')!r}")
for item in transition_rules.get("forbidden_implicit_transitions", []):
    for field in ("trigger", "must_not_imply"):
        resolve_type(item.get(field), f"lifecycle/transition-rules.yaml.{field}")
    resolve_boundary(item.get("boundary"), "lifecycle/transition-rules.yaml.boundary")


# Conformance rules use canonical symbols internally.
rule_catalog = loaded.get("conformance/rules.yaml") or {}
rule_records = rule_catalog.get("rules", [])
if not isinstance(rule_records, list):
    fail("conformance/rules.yaml: rules must be a list")
    rule_records = []
rule_records = [record for record in rule_records if isinstance(record, dict)]
for record in rule_records:
    where = str(record.get("id", "conformance rule"))
    require_fields(record, ["id", "symbol", "version", "status", "requirement", "failure"], where)
    if "name" in record:
        fail(f"{where}: redundant name field must not remain")
    symbol = record.get("symbol")
    if not isinstance(symbol, str) or not re.fullmatch(r"[A-Z][A-Za-z0-9]*", symbol):
        fail(f"{where}: conformance-rule symbol must be PascalCase")
    scope = record.get("scope")
    if scope is not None:
        if not isinstance(scope, dict) or not ({"types", "category"} & set(scope)):
            fail(f"{where}.scope: must separate canonical types or a non-semantic category")
        elif "types" in scope:
            for value in strings(scope["types"], f"{where}.scope.types"):
                resolve_type(value, f"{where}.scope.types")
    for field in ("required_relations", "requires_one_of_relations"):
        for value in strings(record.get(field, []), f"{where}.{field}"):
            resolve_relation(value, f"{where}.{field}")
    for value in strings(record.get("required_concepts", []), f"{where}.required_concepts"):
        if value not in concept_by_symbol:
            fail(f"{where}.required_concepts: unknown Core concept symbol {value!r}")
    if record.get("required_pattern") is not None and record["required_pattern"] not in pattern_by_symbol:
        fail(f"{where}: unknown pattern symbol {record['required_pattern']!r}")
    for value in strings(record.get("boundaries", []), f"{where}.boundaries"):
        resolve_boundary(value, f"{where}.boundaries")
    chain = record.get("required_chain", [])
    if not isinstance(chain, list):
        fail(f"{where}.required_chain: must be a list of structured triples")
    for triple in chain:
        if not isinstance(triple, dict) or set(triple) != {"source", "relation", "target"}:
            fail(f"{where}.required_chain: each entry must contain source, relation, and target")
            continue
        resolve_type(triple["source"], f"{where}.required_chain.source")
        resolve_relation(triple["relation"], f"{where}.required_chain.relation")
        resolve_type(triple["target"], f"{where}.required_chain.target")
    for legacy in ("required_relation", "boundary"):
        if legacy in record:
            fail(f"{where}: legacy singular reference field {legacy!r} must not remain")

rule_by_id = index_unique(rule_records, "id", "conformance-rule ID")
rule_by_symbol = index_unique(rule_records, "symbol", "conformance-rule symbol")


def resolve_rule(value: Any, where: str) -> bool:
    if not isinstance(value, str):
        fail(f"{where}: conformance-rule reference must be a string")
        return False
    reject_registry_ids([value], where)
    if value not in rule_by_symbol:
        fail(f"{where}: unknown conformance-rule symbol {value!r}")
        return False
    return True


# Fixtures validate readable object types, relations, boundaries, and rule symbols.
fixture_records: list[dict[str, Any]] = []
fixture_by_id: dict[str, dict[str, Any]] = {}
for path in sorted(ROOT.glob("conformance/fixtures/*/*.yaml")):
    file_name = relpath(path)
    record = loaded.get(file_name)
    if not isinstance(record, dict):
        continue
    fixture_records.append(record)
    fixture_id = record.get("id")
    if isinstance(fixture_id, str):
        if fixture_id in fixture_by_id:
            fail(f"Duplicate fixture ID {fixture_id!r}")
        fixture_by_id[fixture_id] = record
    object_ids = {obj.get("id") for obj in record.get("objects", []) if isinstance(obj, dict)}
    for obj in record.get("objects", []):
        if isinstance(obj, dict):
            resolve_type(obj.get("type"), f"{file_name}.objects.type")
            represented_as = obj.get("attributes", {}).get("represented_as")
            if represented_as is not None:
                resolve_type(represented_as, f"{file_name}.objects.attributes.represented_as")
    for edge in record.get("relations", []):
        if not isinstance(edge, dict):
            fail(f"{file_name}.relations: entries must be mappings")
            continue
        resolve_relation(edge.get("relation"), f"{file_name}.relations.relation")
        if edge.get("source") not in object_ids or edge.get("target") not in object_ids:
            fail(f"{file_name}: relation references an unknown fixture object")
    expectations = record.get("expectations", {})
    for field in ("rules_pass", "rules_fail"):
        for value in strings(expectations.get(field, []), f"{file_name}.expectations.{field}"):
            resolve_rule(value, f"{file_name}.expectations.{field}")
    for value in strings(expectations.get("boundaries_triggered", []), f"{file_name}.expectations.boundaries_triggered"):
        resolve_boundary(value, f"{file_name}.expectations.boundaries_triggered")

valid_fixtures = [record for record in fixture_records if record.get("expected") == "valid"]
invalid_fixtures = [record for record in fixture_records if record.get("expected") == "invalid"]
if len(valid_fixtures) + len(invalid_fixtures) != len(fixture_records):
    fail("conformance fixtures: expected must be either valid or invalid")


# Example trace, mappings, coverage, and composition are authoring surfaces.
example = loaded.get("examples/patent-portfolio-trace.yaml") or {}
example_object_ids = {obj.get("id") for obj in example.get("objects", []) if isinstance(obj, dict)}
for obj in example.get("objects", []):
    if isinstance(obj, dict):
        resolve_type(obj.get("type"), "examples/patent-portfolio-trace.yaml.objects.type")
for edge in example.get("relations", []):
    if isinstance(edge, dict):
        resolve_relation(edge.get("relation"), "examples/patent-portfolio-trace.yaml.relations.relation")
        if edge.get("source") not in example_object_ids or edge.get("target") not in example_object_ids:
            fail("examples/patent-portfolio-trace.yaml: relation references an unknown object")
for value in strings(example.get("critical_boundaries", []), "examples/patent-portfolio-trace.yaml.critical_boundaries"):
    resolve_boundary(value, "examples/patent-portfolio-trace.yaml.critical_boundaries")

mapping = loaded.get("mappings/generic-agentic/mapping.yaml") or {}
for item in mapping.get("mappings", []):
    for value in strings(item.get("may_realize", []), "mappings/generic-agentic/mapping.yaml.may_realize"):
        if value not in concept_by_symbol:
            fail(f"mappings/generic-agentic/mapping.yaml: unknown Core concept symbol {value!r}")
    for value in strings(item.get("may_project_pattern", []), "mappings/generic-agentic/mapping.yaml.may_project_pattern"):
        if value not in pattern_by_symbol:
            fail(f"mappings/generic-agentic/mapping.yaml: unknown pattern symbol {value!r}")

coverage = loaded.get("conformance/coverage.yaml") or {}
for item in coverage.get("boundary_coverage", []):
    resolve_boundary(item.get("boundary"), "conformance/coverage.yaml.boundary")
    for fixture_id in strings(item.get("covered_by", []), "conformance/coverage.yaml.covered_by"):
        if fixture_id not in fixture_by_id:
            fail(f"conformance/coverage.yaml: unknown fixture ID {fixture_id!r}")
for item in coverage.get("question_coverage", []):
    if item.get("question_family") not in family_by_symbol:
        fail(f"conformance/coverage.yaml: unknown question-family symbol {item.get('question_family')!r}")

semantic_request = loaded.get("composition/semantic-request.example.yaml") or {}
for canonical in strings(semantic_request.get("semantic_request", {}).get("questions", []), "composition/semantic-request.example.yaml.questions"):
    reject_registry_ids([canonical], "composition/semantic-request.example.yaml.questions")
    if canonical not in question_by_canonical:
        fail(f"composition/semantic-request.example.yaml: unknown canonical question {canonical!r}")

resolved_pack = loaded.get("composition/resolved-pack.example.yaml") or {}
for canonical in strings(resolved_pack.get("resolved_pack", {}).get("provides_questions", []), "composition/resolved-pack.example.yaml.provides_questions"):
    reject_registry_ids([canonical], "composition/resolved-pack.example.yaml.provides_questions")
    if canonical not in question_by_canonical:
        fail(f"composition/resolved-pack.example.yaml: unknown canonical question {canonical!r}")

composition_model = loaded.get("composition/composition-model.yaml") or {}
for layer in composition_model.get("layers", []):
    for value in strings(layer.get("requires", []), "composition/composition-model.yaml.requires"):
        resolve_type(value, "composition/composition-model.yaml.requires")


# Manifests: registry identity stays ID-based; semantic lists are canonical.
pack = loaded.get("pack.yaml")
if not isinstance(pack, dict):
    fail("pack.yaml must contain a mapping")
    pack = {}

if pack.get("entrypoints", {}).get("references") != "references/non-core-symbols.yaml":
    fail("pack.yaml: references entrypoint must identify the reference-only registry")
for family in strings(pack.get("question_families", []), "pack.yaml.question_families"):
    if family not in family_by_symbol:
        fail(f"pack.yaml: unknown question-family symbol {family!r}")
for pattern in strings(pack.get("patterns", []), "pack.yaml.patterns"):
    if pattern not in pattern_by_symbol:
        fail(f"pack.yaml: unknown pattern symbol {pattern!r}")

pack_question_model = pack.get("question_model", {})
required_pack_model = {
    "atomic_contracts": True,
    "one_canonical_question_per_contract": True,
    "one_primary_family_per_question": True,
    "families_taxonomy_only": True,
    "family_requirements_inherited": False,
    "canonical_question_resolution": "exact",
}
for key, expected in required_pack_model.items():
    if pack_question_model.get(key) != expected:
        fail(f"pack.yaml: question_model.{key} must be {expected!r}")

actual_counts = {
    "concepts": len(concept_by_id),
    "relations": len(relation_by_id),
    "boundaries": len(boundary_by_id),
    "question_families": len(family_by_id),
    "question_contracts": len(question_by_id),
    "patterns": len(pattern_by_id),
    "status_families": len(status_by_id),
    "conformance_rules": len(rule_by_id),
    "valid_fixtures": len(valid_fixtures),
    "invalid_fixtures": len(invalid_fixtures),
    "reference_only_symbols": len(reference_by_id),
}
if pack.get("counts") != actual_counts:
    fail(f"pack.yaml counts differ from repository: declared={pack.get('counts')} actual={actual_counts}")

release = loaded.get("release/0.1.0.yaml") or {}
if release.get("pack") != pack.get("id") or release.get("version") != pack.get("version"):
    fail("release/0.1.0.yaml does not identify pack.yaml ID/version")
if release.get("counts") != actual_counts:
    fail("release/0.1.0.yaml counts differ from repository")
question_includes = release.get("includes", {}).get("questions", [])
if "questions/contracts/" in question_includes:
    fail("release/0.1.0.yaml: legacy questions/contracts path must not remain")
if "questions/families/" not in question_includes:
    fail("release/0.1.0.yaml: family-organized question path must be included")
if release.get("release_status") == "experimental-candidate" and release.get("git_commit") is None:
    warn("release/0.1.0.yaml: git_commit is unset, as expected before merge/tagging")


# Repository-wide invariants from the final addendum.
for transient in (ROOT / ".bootstrap", ROOT / ".github/workflows/apply-question-refactor.yml"):
    if transient.exists():
        fail(f"{relpath(transient)}: transient refactor artifact must not remain")
legacy_goal_progress = "Goal" + "Progress"
for path in sorted(ROOT.rglob("*")):
    if path.is_file() and path.suffix in {".yaml", ".md", ".py"} and path.name != "_canonical_notation_migration.py":
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if re.search(rf"\b{legacy_goal_progress}\b", text):
            fail(f"{relpath(path)}: undeclared {legacy_goal_progress} pseudo-symbol must use Progress")


print("Core Semantic Pack canonical notation validation")
print(f"  YAML files:              {len(yaml_paths)}")
print(f"  Concepts:                {len(concept_by_id)}")
print(f"  Relations:               {len(relation_by_id)}")
print(f"  Boundaries:              {len(boundary_by_id)}")
print(f"  Reference-only symbols:  {len(reference_by_id)}")
print(f"  Question families:       {len(family_by_id)}")
print(f"  Question contracts:      {len(question_by_id)}")
print(f"  Patterns:                {len(pattern_by_id)}")
print(f"  Status families:         {len(status_by_id)}")
print(f"  Conformance rules:       {len(rule_by_id)}")
print(f"  Valid fixtures:          {len(valid_fixtures)}")
print(f"  Invalid fixtures:        {len(invalid_fixtures)}")
print(f"  Warnings:                {len(warnings)}")
print(f"  Errors:                  {len(errors)}")

if warnings:
    print("\nWarnings:")
    for message in warnings:
        print(f"  - {message}")

if errors:
    print("\nErrors:")
    for message in errors:
        print(f"  - {message}")
    sys.exit(1)

print("\nPASS: registry identities and canonical semantic references are consistent.")
