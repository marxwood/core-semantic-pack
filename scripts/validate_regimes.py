#!/usr/bin/env python3
"""Structural validator for the Core Semantic Pack Regime subsystem.

The validator checks:

- the five ordered Canon-derived Regime identities;
- R1-R5 definition filenames;
- the five Canon-required matrix sections;
- separation of Regime definitions from Regime contracts;
- the `*-contract.yaml` naming rule;
- explicit switching and comparative-evaluation discipline;
- Domain / Regime / Execution composition boundaries;
- dedicated Regime fixtures.

It does not determine real-world Validity and does not make the exploratory
matrix enumerations canonical.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
REGIME_ROOT = ROOT / "semantic" / "concepts" / "epistemic" / "regimes"
CONTRACT_ROOT = REGIME_ROOT / "contracts"
FIXTURE_ROOT = REGIME_ROOT / "fixtures"

errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def load_yaml(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"{path.relative_to(ROOT)}: YAML parse failed: {exc}")
        return None


def require_mapping(record: Any, path: Path) -> dict[str, Any]:
    if not isinstance(record, dict):
        fail(f"{path.relative_to(ROOT)}: expected a mapping")
        return {}
    return record


def require_fields(record: dict[str, Any], fields: list[str], where: str) -> None:
    for field in fields:
        if field not in record:
            fail(f"{where}: missing required field {field!r}")


def as_list(value: Any, where: str) -> list[Any]:
    if not isinstance(value, list):
        fail(f"{where}: expected a list")
        return []
    return value


pack_path = ROOT / "pack.yaml"
pack = require_mapping(load_yaml(pack_path), pack_path)

entrypoints = pack.get("entrypoints")
if not isinstance(entrypoints, dict):
    fail("pack.yaml: entrypoints must be a mapping")
else:
    expected = "semantic/concepts/epistemic/regimes/index.yaml"
    if entrypoints.get("regimes") != expected:
        fail(f"pack.yaml: regimes entrypoint must be {expected!r}")

regime_model = pack.get("regime_model")
if not isinstance(regime_model, dict):
    fail("pack.yaml: regime_model must be a mapping")
    regime_model = {}

if regime_model.get("definitions_in_core") is not True:
    fail("pack.yaml: Regime definitions must be in Core")
if regime_model.get("externally_extensible") is not False:
    fail("pack.yaml: Core Regime set must not be externally extensible")
if regime_model.get("domain_redefinable") is not False:
    fail("pack.yaml: Domain Packs must not redefine Core Regimes")
if regime_model.get("execution_contract_selects") is not True:
    fail("pack.yaml: Execution Contracts must select Core Regimes")

expected_order = [
    (1, "core.regime.open", "OpenRegime", "Open", "R1-open.yaml"),
    (2, "core.regime.disciplined", "DisciplinedRegime", "Disciplined", "R2-disciplined.yaml"),
    (3, "core.regime.adversarial", "AdversarialRegime", "Adversarial", "R3-adversarial.yaml"),
    (4, "core.regime.high-assurance", "HighAssuranceRegime", "High-Assurance", "R4-high-assurance.yaml"),
    (5, "core.regime.locked", "LockedRegime", "Locked", "R5-locked.yaml"),
]
expected_ids = {item[1] for item in expected_order}

declared_ids = set(as_list(regime_model.get("canonical_set"), "pack.yaml regime_model.canonical_set"))
if declared_ids != expected_ids:
    fail(f"pack.yaml: canonical Regime set differs: {sorted(declared_ids)!r}")

concept_index_path = ROOT / "semantic" / "concepts" / "index.yaml"
concept_index = require_mapping(load_yaml(concept_index_path), concept_index_path)
concept_entries = concept_index.get("concepts", [])
regime_entries = [
    entry for entry in concept_entries
    if isinstance(entry, dict) and entry.get("symbol") == "Regime"
]
if len(regime_entries) != 1:
    fail("semantic/concepts/index.yaml: Regime must appear exactly once")
elif regime_entries[0].get("file") != "semantic/concepts/epistemic/regime.yaml":
    fail("semantic/concepts/index.yaml: Regime path is incorrect")

relation_index_path = ROOT / "semantic" / "relations" / "index.yaml"
relation_index = require_mapping(load_yaml(relation_index_path), relation_index_path)
relation_symbols = {
    entry.get("symbol")
    for entry in relation_index.get("relations", [])
    if isinstance(entry, dict)
}
for symbol in ("evaluatedUnder", "escalatesTo"):
    if symbol not in relation_symbols:
        fail(f"semantic/relations/index.yaml: missing {symbol}")

index_path = REGIME_ROOT / "index.yaml"
index = require_mapping(load_yaml(index_path), index_path)
entries = index.get("regimes", [])
if not isinstance(entries, list):
    fail("Regime index: regimes must be a list")
    entries = []

if len(entries) != 5:
    fail(f"Regime index: expected 5 definitions, found {len(entries)}")

required_matrix_components = {
    "claim_classes",
    "evidence_classes",
    "evaluation_rules",
    "invalidation_rules",
    "escalation_rules",
}

for expected, entry in zip(expected_order, entries):
    order, expected_id, expected_symbol, expected_name, expected_filename = expected

    if not isinstance(entry, dict):
        fail("Regime index: each entry must be a mapping")
        continue

    require_fields(entry, ["id", "file", "symbol", "canonical_name", "order"], "Regime index entry")

    expected_path = f"semantic/concepts/epistemic/regimes/{expected_filename}"
    if entry.get("id") != expected_id:
        fail(f"Regime index order {order}: expected ID {expected_id!r}")
    if entry.get("symbol") != expected_symbol:
        fail(f"Regime index order {order}: expected symbol {expected_symbol!r}")
    if entry.get("canonical_name") != expected_name:
        fail(f"Regime index order {order}: expected canonical_name {expected_name!r}")
    if entry.get("order") != order:
        fail(f"Regime index: {expected_id} must declare order {order}")
    if entry.get("file") != expected_path:
        fail(f"Regime index: {expected_id} must resolve to {expected_path}")

    path = ROOT / expected_path
    record = require_mapping(load_yaml(path), path)

    require_fields(
        record,
        [
            "id",
            "version",
            "status",
            "kind",
            "symbol",
            "canonical_name",
            "canonical_summary",
            "purpose",
            "authority",
            "matrix",
            "invariants",
            "derivation",
        ],
        expected_path,
    )

    if record.get("id") != expected_id:
        fail(f"{expected_path}: ID differs from index")
    if record.get("symbol") != expected_symbol:
        fail(f"{expected_path}: symbol differs from index")
    if record.get("canonical_name") != expected_name:
        fail(f"{expected_path}: canonical_name differs from index")
    if record.get("status") != "exploratory":
        fail(f"{expected_path}: matrix-bearing Regime record must remain exploratory")

    authority = record.get("authority")
    if not isinstance(authority, dict):
        fail(f"{expected_path}: authority must be a mapping")
    else:
        if authority.get("regime_identity") != "canon-derived":
            fail(f"{expected_path}: Regime identity must be canon-derived")
        if authority.get("enumerative_matrix") != "exploratory-derivation-candidate":
            fail(f"{expected_path}: enumerative matrix must remain exploratory")
        if authority.get("may_be_redefined_by_domain") is not False:
            fail(f"{expected_path}: Domain redefinition must be false")
        if authority.get("may_be_redefined_by_execution_contract") is not False:
            fail(f"{expected_path}: Execution Contract redefinition must be false")

    matrix = record.get("matrix")
    if not isinstance(matrix, dict):
        fail(f"{expected_path}: matrix must be a mapping")
        continue

    if set(matrix) != required_matrix_components:
        fail(
            f"{expected_path}: matrix components must be exactly "
            f"{sorted(required_matrix_components)!r}"
        )

    for component in required_matrix_components:
        if not isinstance(matrix.get(component), dict):
            fail(f"{expected_path}: {component} must be a mapping")

    invalidation = matrix.get("invalidation_rules", {})
    if isinstance(invalidation, dict):
        if invalidation.get("preserve_referability") is not True:
            fail(f"{expected_path}: invalidation must preserve referability")
        if invalidation.get("preserve_trace") is not True:
            fail(f"{expected_path}: invalidation must preserve trace")
        if invalidation.get("deletion_is_invalidation") is not False:
            fail(f"{expected_path}: deletion must not equal invalidation")

    escalation = matrix.get("escalation_rules", {})
    if isinstance(escalation, dict):
        if escalation.get("explicit_switch_required") is not True:
            fail(f"{expected_path}: escalation must require explicit switching")
        if escalation.get("prior_outcomes_retained") is not True:
            fail(f"{expected_path}: prior Regime outcomes must be retained")

# Regime definition folder must contain only ordered definitions, navigation,
# contracts, fixtures, and README.
root_yaml_names = {path.name for path in REGIME_ROOT.glob("*.yaml")}
expected_root_yaml_names = {"index.yaml"} | {item[4] for item in expected_order}
if root_yaml_names != expected_root_yaml_names:
    fail(
        "Regime root YAML files must be exactly index.yaml plus R1-R5 definitions; "
        f"found {sorted(root_yaml_names)!r}"
    )

expected_contract_files = {
    "evaluation-contract.yaml",
    "switching-contract.yaml",
    "conformance-contract.yaml",
}
actual_contract_files = {path.name for path in CONTRACT_ROOT.glob("*.yaml")}
if actual_contract_files != expected_contract_files:
    fail(
        "Regime contracts must be exactly the three *-contract.yaml files; "
        f"found {sorted(actual_contract_files)!r}"
    )

for path in sorted(CONTRACT_ROOT.glob("*.yaml")):
    if not path.name.endswith("-contract.yaml"):
        fail(f"{path.relative_to(ROOT)}: Regime contract filename must end in -contract.yaml")
    record = require_mapping(load_yaml(path), path)
    require_fields(record, ["id", "version", "status", "kind", "symbol"], str(path.relative_to(ROOT)))
    if record.get("kind") != "regime-contract":
        fail(f"{path.relative_to(ROOT)}: kind must be regime-contract")

contract_index = index.get("contracts")
if not isinstance(contract_index, dict):
    fail("Regime index: contracts must be a mapping")
else:
    expected_contract_paths = {
        "evaluation": "semantic/concepts/epistemic/regimes/contracts/evaluation-contract.yaml",
        "switching": "semantic/concepts/epistemic/regimes/contracts/switching-contract.yaml",
        "conformance": "semantic/concepts/epistemic/regimes/contracts/conformance-contract.yaml",
    }
    if contract_index != expected_contract_paths:
        fail("Regime index: contract paths do not match the governed contracts/ layout")

switch_path = CONTRACT_ROOT / "switching-contract.yaml"
switching = require_mapping(load_yaml(switch_path), switch_path)
for required in (
    "canonical_requirements",
    "required_switch_record",
    "comparative_evaluation",
    "candidate_escalation_graph",
    "forbidden",
):
    if required not in switching:
        fail(f"switching-contract.yaml: missing {required}")

if switching.get("comparative_evaluation", {}).get("is_not_a_switch") is not True:
    fail("switching-contract.yaml: comparative evaluation must remain distinct from switching")

conformance_path = CONTRACT_ROOT / "conformance-contract.yaml"
conformance = require_mapping(load_yaml(conformance_path), conformance_path)
rules = conformance.get("rules", [])
if not isinstance(rules, list):
    fail("conformance-contract.yaml: rules must be a list")
    rules = []

failure_codes = {
    rule.get("failure")
    for rule in rules
    if isinstance(rule, dict) and isinstance(rule.get("failure"), str)
}
if len(failure_codes) != 8:
    fail("conformance-contract.yaml: expected eight distinct Regime failure codes")

# Composition must bind Core Regimes, not register a Regime Pack component.
def contains_legacy_regime_pack(value: Any) -> bool:
    if isinstance(value, str):
        return value.strip().lower() == "regime-pack"
    if isinstance(value, list):
        return any(contains_legacy_regime_pack(item) for item in value)
    if isinstance(value, dict):
        return any(contains_legacy_regime_pack(item) for item in value.values())
    return False

for relative in (
    "pack.yaml",
    "semantic/composition/composition-model.yaml",
    "semantic/composition/compatibility-rules.yaml",
    "semantic/composition/resolved-pack.example.yaml",
):
    record = load_yaml(ROOT / relative)
    if contains_legacy_regime_pack(record):
        fail(f"{relative}: legacy Regime Pack component remains")

composition_readme = (ROOT / "semantic/composition/README.md").read_text(encoding="utf-8")
if "+\nRegime Pack" in composition_readme or "+ Regime Pack" in composition_readme:
    fail("semantic/composition/README.md: legacy Regime Pack composition formula remains")

resolved_path = ROOT / "semantic" / "composition" / "resolved-pack.example.yaml"
resolved = require_mapping(load_yaml(resolved_path), resolved_path).get("resolved_pack", {})
if not isinstance(resolved, dict):
    fail("resolved-pack.example.yaml: resolved_pack must be a mapping")
else:
    component_types = {
        component.get("type")
        for component in resolved.get("components", [])
        if isinstance(component, dict)
    }
    if "regime-pack" in component_types:
        fail("resolved-pack.example.yaml: Regime Pack must not be a component")

    binding = resolved.get("regime_binding")
    if not isinstance(binding, dict):
        fail("resolved-pack.example.yaml: regime_binding is required")
    else:
        primary = binding.get("primary", {})
        if not isinstance(primary, dict) or primary.get("id") not in expected_ids:
            fail("resolved-pack.example.yaml: primary Regime is unknown")

request_path = ROOT / "semantic" / "composition" / "semantic-request.example.yaml"
request = require_mapping(load_yaml(request_path), request_path).get("semantic_request", {})
if not isinstance(request, dict):
    fail("semantic-request.example.yaml: semantic_request must be a mapping")
else:
    selection = request.get("regime_selection")
    if not isinstance(selection, dict):
        fail("semantic-request.example.yaml: regime_selection is required")
    else:
        primary = selection.get("primary", {})
        if not isinstance(primary, dict) or primary.get("id") not in expected_ids:
            fail("semantic-request.example.yaml: primary Regime is unknown")
        for comparative in selection.get("comparative", []):
            if not isinstance(comparative, dict) or comparative.get("id") not in expected_ids:
                fail("semantic-request.example.yaml: comparative Regime is unknown")

# Dedicated fixtures.
fixture_paths = sorted(FIXTURE_ROOT.glob("*.yaml"))
if len(fixture_paths) != 6:
    fail(f"Regime fixtures: expected 6 files, found {len(fixture_paths)}")

for path in fixture_paths:
    fixture = require_mapping(load_yaml(path), path)
    expected = fixture.get("expected")
    declared_failures = set(fixture.get("expected_failures", []))
    unknown = declared_failures - failure_codes
    if unknown:
        fail(f"{path.relative_to(ROOT)}: unknown expected failures {sorted(unknown)!r}")

    detected: set[str] = set()

    claim = fixture.get("claim")
    if isinstance(claim, dict):
        regime = claim.get("regime")
        if not isinstance(regime, dict) or regime.get("id") not in expected_ids:
            detected.add("missing-regime-context")

    previous_regime = fixture.get("previous_regime")
    current_regime = fixture.get("current_regime")
    if previous_regime and current_regime and previous_regime != current_regime:
        if fixture.get("switch_record") in (None, {}):
            detected.add("silent-regime-switch")

    declared_regime = fixture.get("declared_regime")
    if isinstance(declared_regime, dict):
        if declared_regime.get("defined_by") == "domain-pack":
            detected.add("domain-defines-regime")
        if declared_regime.get("id") not in expected_ids:
            detected.add("unknown-or-domain-defined-regime")

    stored_validity = fixture.get("stored_validity")
    evaluations = fixture.get("evaluations")
    if isinstance(evaluations, list) and len(evaluations) > 1:
        if isinstance(stored_validity, dict) and stored_validity.get("regime") is None:
            detected.add("cross-regime-validity-collapse")
            detected.add("missing-regime-context")

    projection = fixture.get("projection")
    if isinstance(projection, dict):
        if projection.get("regime_context_visible") is False or projection.get("universalizes_validity") is True:
            detected.add("projection-hides-regime-context")
        if projection.get("collapses_to_single_truth_score") is True:
            detected.add("cross-regime-validity-collapse")

    if expected == "valid":
        if declared_failures:
            fail(f"{path.relative_to(ROOT)}: valid fixture declares failures")
        if detected:
            fail(f"{path.relative_to(ROOT)}: valid fixture violates {sorted(detected)!r}")
    elif expected == "invalid":
        if not declared_failures:
            fail(f"{path.relative_to(ROOT)}: invalid fixture must declare failures")
        missing = declared_failures - detected
        if missing:
            fail(
                f"{path.relative_to(ROOT)}: validator did not detect declared failures "
                f"{sorted(missing)!r}"
            )
    else:
        fail(f"{path.relative_to(ROOT)}: expected must be valid or invalid")

# The supplementary Regime specification must not exist: Regime architecture is
# integrated directly into CORE-SEMANTIC-PACK.md.
if (ROOT / "CORE-SEMANTIC-PACK-REGIMES.md").exists():
    fail("CORE-SEMANTIC-PACK-REGIMES.md must not exist; Regime architecture belongs in CORE-SEMANTIC-PACK.md")

main_spec = (ROOT / "CORE-SEMANTIC-PACK.md").read_text(encoding="utf-8")
for required_text in (
    "# 19. Canonical Regimes",
    "R1 — Open",
    "R2 — Disciplined",
    "R3 — Adversarial",
    "R4 — High-Assurance",
    "R5 — Locked",
):
    if required_text not in main_spec:
        fail(f"CORE-SEMANTIC-PACK.md: missing integrated Regime text {required_text!r}")

if errors:
    print("Regime validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("Regime validation passed.")
print("- Ordered Core Regime definitions: 5")
print("- Regime contracts: 3")
print(f"- Dedicated Regime fixtures: {len(fixture_paths)}")
print("- Regime identities remain Canon-derived.")
print("- Enumerative matrices remain exploratory derivation candidates.")
