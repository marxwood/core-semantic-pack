# Core Semantic Pack

A runtime-neutral semantic kernel for correction-capable human-agentic systems.

The Core Semantic Pack defines the minimal, stable, domain-neutral semantic distinctions required for systems to preserve meaning across perception, reasoning, memory, governance, action, and `StateChange`.

It is not a universal ontology, runtime framework, workflow engine, agent configuration, database schema, or tool registry. It is a composable semantic kernel intended to remain stable while domain models, execution architectures, and runtimes evolve around it.

## Canonical semantic notation

Registry records retain stable IDs for identity, versioning, migration, and release reconstruction. Human-agent authoring surfaces use canonical semantics:

```text
core.desired-state                   ↔ DesiredState
core.rel.authorized-by               ↔ authorizedBy
core.boundary.action-not-intent      ↔ Action != Intent
core.question.explain-action-purpose ↔ Why is this being done?
```

There is no separate human-label or question-slug semantic layer in v0.1. Repository paths are serialization details. See [`docs/semantic-notation.md`](docs/semantic-notation.md).

## Atomic semantic artifacts

The repository follows one structural invariant:

```text
one referencable semantic object = one file
```

Concepts, Relations, Boundaries, and Questions are independently inspectable artifacts. Their indexes are registry/navigation bridges only: stable IDs carry registry identity, canonical symbols, expressions, and questions carry semantic reference, and paths carry serialization location.

## Core responsibilities

The pack is designed to preserve distinctions such as:

- `Claim != Evidence`
- `Projection != State`
- `Capability != Authority`
- `Validation != Admission`
- `Review != Binding`
- `Goal != DesiredState`
- `Action != StateChange`
- `Process != ExecutionContract`
- `OperationalSuccess != Progress`

It also treats answerability as a core architectural property: material system behavior should remain traceable enough to answer what is known, why an action is being taken, which goal it advances, what authorized it, what changed, and whether the system is still moving toward the intended state.

## Atomic question contracts

The unit of answerability is one canonical question:

```text
one question = one independently resolvable Semantic Question Contract
```

Question families are taxonomy and discovery views only. Each question has exactly one primary family and one complete contract stored under that family. Another family may list the canonical question as related without duplicating it or donating requirements.

Question contracts use readable canonical references:

```yaml
canonical_question: Why is this being done?
family: teleological

requires:
  concepts:
    - Action
    - Intent
    - Goal
    - DesiredState
  relations:
    - realizes
    - advances

must_preserve:
  - Action != Intent
  - Intent != Goal
```

See [`semantic/questions/`](semantic/questions/) and [`docs/question-contract-model.md`](docs/question-contract-model.md).

## Semantic Handshakes

A runtime is not governed by the Semantic OS merely because it can retrieve or read a Semantic Pack. Governance begins through an explicit, evidence-bearing, version-bound Semantic Handshake.

The first contract, `SemanticOSAdoptionHandshake`, establishes:

- exact Pack, runtime, provider, adapter, environment, and authority identities;
- the difference between context consumption and behavioral enforcement;
- the boundary between upstream semantic authority and environment-local semantic authority;
- version pinning, semantic diff, compatibility validation, explicit update acceptance, and rollback;
- an `accepted`, `conditional`, or `rejected` adoption decision;
- a reconstructable Handshake Record.

Handshake Prompts are portable invocation surfaces. They may vary by runtime or model, but they are non-authoritative and cannot weaken the underlying Contract.

See [`semantic-contracts/handshakes/`](semantic-contracts/handshakes/) and the [illustrative adoption prompt](examples/handshake-prompts/semantic-os-adoption.md).

## Repository map

| Area | Responsibility |
|---|---|
| [`pack.yaml`](pack.yaml) | Pack identity, scope, guarantees, question model, and composition rules |
| [`semantic/`](semantic/) | Governed semantic source and semantic governance rules |
| [`semantic/concepts/`](semantic/concepts/) | Atomic candidate Core primitives organized by semantic layer |
| [`semantic/relations/`](semantic/relations/) | Typed relations that form the semantic graph |
| [`semantic/boundaries/`](semantic/boundaries/) | Anti-collapse rules and semantic safety properties |
| [`semantic/questions/`](semantic/questions/) | Atomic questions organized under taxonomy-only primary families |
| [`semantic-contracts/handshakes/`](semantic-contracts/handshakes/) | Runtime-neutral pre-adoption contracts and their registry |
| [`semantic/references/`](semantic/references/) | Explicit non-Core comparison categories used by structured notation |
| [`semantic/patterns/`](semantic/patterns/) | Composite structures built from Core primitives |
| [`semantic/lifecycle/`](semantic/lifecycle/) | Separate lifecycle and status families |
| [`semantic/composition/`](semantic/composition/) | Rules for Domain, Regime, and Execution composition |
| [`mappings/`](mappings/) | Non-authoritative architecture mappings |
| [`semantic/conformance/`](semantic/conformance/) | Rules, coverage, and valid/invalid semantic fixtures |
| [`examples/`](examples/) | Illustrative, non-authoritative semantic traces |
| [`release/`](release/) | Versioned release manifest and known limitations |
| [`docs/`](docs/) | Derivation, terminology, record format, repository-shape decisions, and open questions |

## Specification

See [CORE-SEMANTIC-PACK.md](CORE-SEMANTIC-PACK.md) for the working v0.1 architectural specification.

The Markdown specification explains the architecture. The repository records materialize that architecture into referencable concepts, relations, boundaries, atomic question contracts, patterns, and conformance evidence.

## Validate the pack

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_pack.py
python scripts/validate_handshakes.py
```

The validator checks registry identity, canonical-symbol uniqueness and resolution, boundary expressions, question atomicity and family topology, all checked authoring surfaces, indexes, fixtures, and release manifests. It does not determine semantic truth and is not the source of semantic authority.

## Status

Working reference specification / non-canonical.
