# Core Semantic Pack

A runtime-neutral semantic kernel for correction-capable human-agentic systems.

The Core Semantic Pack defines the minimal, stable, domain-neutral semantic distinctions required for systems to preserve meaning across perception, reasoning, memory, governance, action, and `StateChange`.

It is not a universal ontology, runtime framework, workflow engine, agent configuration, database schema, or tool registry. It is a composable semantic kernel intended to remain stable while domain models, execution architectures, and runtimes evolve around it.

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
- `OperationalSuccess != GoalProgress`

It also treats answerability as a core architectural property: material system behavior should remain traceable enough to answer what is known, why an action is being taken, which goal it advances, what authorized it, what changed, and whether the system is still moving toward the intended state.

## Atomic question contracts

The unit of answerability is one canonical question:

```text
one question = one independently resolvable Semantic Question Contract
```

Question families are taxonomy and discovery views only. They do not define or donate semantic requirements to their members. A question may be classified into multiple families without duplicating its contract.

See [`questions/`](questions/) and [`docs/question-contract-model.md`](docs/question-contract-model.md).

## Repository map

| Area | Responsibility |
|---|---|
| [`pack.yaml`](pack.yaml) | Pack identity, scope, guarantees, question model, and composition rules |
| [`concepts/`](concepts/) | Candidate Core primitives grouped by semantic layer |
| [`relations/`](relations/) | Typed relations that form the semantic graph |
| [`boundaries/`](boundaries/) | Anti-collapse rules and semantic safety properties |
| [`questions/`](questions/) | Atomic question contracts plus taxonomy-only family views |
| [`patterns/`](patterns/) | Composite structures built from Core primitives |
| [`lifecycle/`](lifecycle/) | Separate lifecycle and status families |
| [`composition/`](composition/) | Rules for Domain, Regime, and Execution composition |
| [`mappings/`](mappings/) | Non-authoritative architecture mappings |
| [`conformance/`](conformance/) | Rules, coverage, and valid/invalid semantic fixtures |
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
```

The validator checks structural integrity, IDs, references, question atomicity, family/contract membership, indexes, and release manifests. It does not determine semantic truth and is not the source of semantic authority.

## Status

Working reference specification / non-canonical.
