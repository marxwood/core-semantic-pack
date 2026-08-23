#!/usr/bin/env python3
"""Validate Core Semantic Pack handshake contracts and illustrative records."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
HANDSHAKE_ROOT = ROOT / "semantic-contracts" / "handshakes"
INDEX_PATH = HANDSHAKE_ROOT / "index.yaml"
EXAMPLE_RECORD_PATH = ROOT / "examples" / "semantic-os-adoption-handshake-record.yaml"
errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def load_mapping(path: Path) -> dict[str, Any]:
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"{path.relative_to(ROOT)}: YAML parse failed: {exc}")
        return {}
    if not isinstance(value, dict):
        fail(f"{path.relative_to(ROOT)}: expected a mapping")
        return {}
    return value


index = load_mapping(INDEX_PATH)
model = index.get("handshake_model", {})
required_model = {
    "explicit_adoption_required": True,
    "prompt_is_authoritative": False,
    "consumption_is_governance": False,
    "accepted_binding_is_version_pinned": True,
    "upstream_updates_require_revalidation": True,
    "single_invocation_complete_procedure": True,
    "intermediate_conditional_is_terminal": False,
    "native_capabilities_exhausted_before_extension": True,
    "operational_fitness_required": True,
    "handshake_authorizes_new_software": False,
}
if model != required_model:
    fail("semantic-contracts/handshakes/index.yaml: handshake_model does not preserve the required adoption invariants")

entries = index.get("handshakes", [])
if not isinstance(entries, list) or not entries:
    fail("semantic-contracts/handshakes/index.yaml: handshakes must be a non-empty list")
    entries = []

expected_fields = {"order", "symbol", "id", "file"}
indexed_files: set[str] = set()
seen_orders: set[str] = set()
seen_ids: set[str] = set()
seen_symbols: set[str] = set()
contract_versions: dict[str, str] = {}

expected_phases = [
    "identity-binding",
    "semantic-obligation-resolution",
    "runtime-self-inspection",
    "capability-resolution",
    "realization-selection",
    "operational-fitness",
    "authority-enforcement-boundary",
    "behavioral-proof",
    "synchronization-commitment",
    "adoption-decision",
    "revalidation-triggers",
]
expected_resolution_order = [
    "native",
    "mappable",
    "composable",
    "externally-available",
    "missing",
    "incompatible",
]
expected_fitness_states = {"fit", "fit-with-bounds", "insufficient", "unknown"}

for entry in entries:
    if not isinstance(entry, dict) or set(entry) != expected_fields:
        fail("semantic-contracts/handshakes/index.yaml: each entry must contain only order, symbol, id, and file")
        continue
    order = entry.get("order")
    file_name = entry.get("file")
    if not isinstance(order, str) or not re.fullmatch(r"H[1-9][0-9]*", order):
        fail(f"handshake index entry has invalid order {order!r}")
    if not isinstance(file_name, str) or not re.fullmatch(
        r"semantic-contracts/handshakes/H[1-9][0-9]*-[a-z0-9-]+-contract\.yaml", file_name or ""
    ):
        fail(f"handshake index entry has invalid contract path {file_name!r}")
        continue
    if not Path(file_name).name.startswith(f"{order}-"):
        fail(f"{file_name}: filename order does not match index order {order!r}")
    indexed_files.add(file_name)
    for seen, value, label in (
        (seen_orders, order, "order"),
        (seen_ids, entry.get("id"), "ID"),
        (seen_symbols, entry.get("symbol"), "symbol"),
    ):
        if value in seen:
            fail(f"duplicate handshake {label} {value!r}")
        seen.add(value)

    path = ROOT / file_name
    record = load_mapping(path)
    for field in (
        "id",
        "version",
        "status",
        "kind",
        "order",
        "symbol",
        "definition",
        "participants",
        "procedure_execution",
        "required_declarations",
        "capability_resolution",
        "operational_fitness",
        "phases",
        "required_questions",
        "invariants",
        "behavioral_proof",
        "acceptance",
        "outcomes",
        "handshake_record",
        "prompt_surface",
        "failure_states",
        "derivation",
    ):
        if field not in record:
            fail(f"{file_name}: missing required field {field!r}")
    for field in ("id", "symbol", "order"):
        if record.get(field) != entry.get(field):
            fail(f"{file_name}: {field} differs from index")
    if record.get("kind") != "semantic-handshake-contract":
        fail(f"{file_name}: kind must be 'semantic-handshake-contract'")
    if isinstance(record.get("id"), str) and isinstance(record.get("version"), str):
        contract_versions[record["id"]] = record["version"]
    if set(record.get("participants", {})) != {
        "semantic_authority_source",
        "semantic_pack_provider",
        "runtime_consumer",
        "environment_authority",
    }:
        fail(f"{file_name}: participant boundary is incomplete")

    procedure = record.get("procedure_execution", {})
    if procedure.get("single_invocation") is not True:
        fail(f"{file_name}: H1 must execute as one complete invocation")
    if procedure.get("automatic_continuation") is not True:
        fail(f"{file_name}: H1 must automatically continue through applicable phases")
    if procedure.get("final_decision_only_after_all_phases") is not True:
        fail(f"{file_name}: final decision must occur only after all applicable phases")
    if procedure.get("intermediate_conditional_is_terminal") is not False:
        fail(f"{file_name}: intermediate conditional findings must not terminate H1")

    phase_ids = [phase.get("id") for phase in record.get("phases", []) if isinstance(phase, dict)]
    if phase_ids != expected_phases:
        fail(f"{file_name}: handshake phases are incomplete or out of order")

    resolution = record.get("capability_resolution", {})
    if resolution.get("resolution_order") != expected_resolution_order:
        fail(f"{file_name}: capability resolution order must be runtime-native-first")
    software_policy = resolution.get("new_software_policy", {})
    if software_policy.get("handshake_may_implement") is not False:
        fail(f"{file_name}: H1 must not implement new runtime software")
    if software_policy.get("handshake_may_authorize") is not False:
        fail(f"{file_name}: H1 must not authorize new runtime software")

    fitness = record.get("operational_fitness", {})
    if set(fitness.get("fitness_states", {})) != expected_fitness_states:
        fail(f"{file_name}: operational fitness states are incomplete")

    if set(record.get("outcomes", {})) != {"accepted", "conditional", "rejected"}:
        fail(f"{file_name}: outcomes must be exactly accepted, conditional, and rejected")
    prompt_surface = record.get("prompt_surface", {})
    if prompt_surface.get("authoritative") is not False:
        fail(f"{file_name}: Handshake Prompt must remain non-authoritative")
    if "complete" not in str(prompt_surface.get("execution_requirement", "")).lower():
        fail(f"{file_name}: Handshake Prompt must require completion of the full H1 procedure")
    if len(record.get("required_questions", [])) < 16:
        fail(f"{file_name}: complete adoption procedure must expose all material handshake questions")
    if len(record.get("failure_states", [])) < 12:
        fail(f"{file_name}: complete adoption procedure failure semantics are incomplete")

physical_files = {
    path.relative_to(ROOT).as_posix()
    for path in HANDSHAKE_ROOT.glob("H*-contract.yaml")
}
if indexed_files != physical_files:
    fail("semantic-contracts/handshakes/index.yaml: indexed and physical contract files differ")

record = load_mapping(EXAMPLE_RECORD_PATH)
contract_ref = record.get("contract", {})
contract_id = contract_ref.get("id")
if contract_id not in seen_ids:
    fail("examples/semantic-os-adoption-handshake-record.yaml: unknown handshake contract ID")
elif contract_ref.get("version") != contract_versions.get(contract_id):
    fail("examples/semantic-os-adoption-handshake-record.yaml: handshake contract version is stale")
if record.get("decision", {}).get("outcome") not in {"accepted", "conditional", "rejected"}:
    fail("examples/semantic-os-adoption-handshake-record.yaml: invalid decision outcome")
if record.get("semantic_environment", {}).get("floating_latest") is not False:
    fail("examples/semantic-os-adoption-handshake-record.yaml: floating latest must be false")
for field in (
    "workload",
    "semantic_obligations",
    "runtime_capabilities",
    "capability_resolution",
    "operational_fitness",
    "execution_claim",
    "behavioral_proof",
    "revalidation_triggers",
):
    if field not in record:
        fail(f"examples/semantic-os-adoption-handshake-record.yaml: missing complete-procedure field {field!r}")

for item in record.get("capability_resolution", []):
    if isinstance(item, dict) and item.get("realization_class") not in expected_resolution_order:
        fail("examples/semantic-os-adoption-handshake-record.yaml: invalid realization_class")
for item in record.get("operational_fitness", []):
    if isinstance(item, dict) and item.get("state") not in expected_fitness_states:
        fail("examples/semantic-os-adoption-handshake-record.yaml: invalid operational fitness state")

format_paths = list(HANDSHAKE_ROOT.rglob("*")) + [
    EXAMPLE_RECORD_PATH,
    ROOT / "examples" / "handshake-prompts" / "semantic-os-adoption.md",
    Path(__file__),
]
for path in sorted(format_paths):
    if not path.is_file() or path.suffix not in {".yaml", ".md", ".py"}:
        continue
    text = path.read_text(encoding="utf-8")
    if text and not text.endswith("\n"):
        fail(f"{path.relative_to(ROOT)}: file must end with a newline")
    if re.search(r"[ \t]+$", text, re.MULTILINE):
        fail(f"{path.relative_to(ROOT)}: trailing whitespace is forbidden")
    if "\n\n\n" in text:
        fail(f"{path.relative_to(ROOT)}: more than one consecutive blank line is forbidden")

print("Core Semantic Pack handshake validation")
print(f"  Contracts: {len(indexed_files)}")
print(f"  Errors:    {len(errors)}")

if errors:
    print("\nErrors:")
    for message in errors:
        print(f"  - {message}")
    sys.exit(1)

print("\nPASS: Semantic Handshake contracts preserve complete, runtime-native-first, version-bound adoption.")
