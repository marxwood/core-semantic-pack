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
        "required_declarations",
        "phases",
        "required_questions",
        "invariants",
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
    if set(record.get("participants", {})) != {
        "semantic_authority_source",
        "semantic_pack_provider",
        "runtime_consumer",
        "environment_authority",
    }:
        fail(f"{file_name}: participant boundary is incomplete")
    phase_ids = [phase.get("id") for phase in record.get("phases", []) if isinstance(phase, dict)]
    if phase_ids != [
        "identity-binding",
        "capability-proof",
        "authority-boundary",
        "conformance-evaluation",
        "synchronization-commitment",
        "adoption-decision",
    ]:
        fail(f"{file_name}: handshake phases are incomplete or out of order")
    if set(record.get("outcomes", {})) != {"accepted", "conditional", "rejected"}:
        fail(f"{file_name}: outcomes must be exactly accepted, conditional, and rejected")
    prompt_surface = record.get("prompt_surface", {})
    if prompt_surface.get("authoritative") is not False:
        fail(f"{file_name}: Handshake Prompt must remain non-authoritative")
    if len(record.get("required_questions", [])) < 8:
        fail(f"{file_name}: adoption handshake must expose all material handshake questions")
    if len(record.get("failure_states", [])) < 7:
        fail(f"{file_name}: adoption handshake failure semantics are incomplete")

physical_files = {
    path.relative_to(ROOT).as_posix()
    for path in HANDSHAKE_ROOT.glob("H*-contract.yaml")
}
if indexed_files != physical_files:
    fail("semantic-contracts/handshakes/index.yaml: indexed and physical contract files differ")

record = load_mapping(EXAMPLE_RECORD_PATH)
contract_ref = record.get("contract", {})
if contract_ref.get("id") not in seen_ids:
    fail("examples/semantic-os-adoption-handshake-record.yaml: unknown handshake contract ID")
if record.get("decision", {}).get("outcome") not in {"accepted", "conditional", "rejected"}:
    fail("examples/semantic-os-adoption-handshake-record.yaml: invalid decision outcome")
if record.get("semantic_environment", {}).get("floating_latest") is not False:
    fail("examples/semantic-os-adoption-handshake-record.yaml: floating latest must be false")

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

print("\nPASS: Semantic Handshake contracts preserve explicit, version-bound adoption.")
