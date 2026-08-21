# Core Semantic Pack

A runtime-neutral semantic kernel for correction-capable human-agentic systems.

The Core Semantic Pack defines the minimal, stable, domain-neutral semantic distinctions required for
systems to preserve meaning across perception, reasoning, memory, governance, action, and `StateChange`.

It is not a universal ontology, runtime framework, workflow engine, agent configuration, database schema, or
tool registry. It is a composable semantic kernel intended to remain stable while domain models, execution
architectures, and runtimes evolve around it.

## Canonical semantic notation

Registry records retain stable IDs for identity, versioning, migration, and release reconstruction.
Human-agent authoring surfaces use canonical semantics:

```text
core.desired-state                   ↔ DesiredState
core.rel.authorized-by               ↔ authorizedBy
core.boundary.action-not-intent      ↔ Action != Intent
core.question.explain-action-purpose ↔ Why is this being done?
core.regime.disciplined              ↔ Disciplined
```

There is no separate human-label or question-slug semantic layer in v0.1. Repository paths are serialization
details. See [`docs/semantic-notation.md`](docs/semantic-notation.md).

## Atomic semantic artifacts

The repository follows one structural invariant:

```text
one referencable semantic object = one file
```

Concepts, Relations, Boundaries, and Questions are independently inspectable artifacts. Their indexes are
registry/navigation bridges only: stable IDs carry registry identity, canonical symbols, expressions, and
questions carry semantic reference, and paths carry serialization location.

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

It also treats answerability as a core architectural property: material system behavior should remain
traceable enough to answer what is known, why an action is being taken, which goal it advances, what
authorized it, what changed, and whether the system is still moving toward the intended state.

## Core Regimes

The Core includes one domain-independent Regime system derived from the System Momentum Canon:

```text
Open
Disciplined
Adversarial
High-Assurance
Locked
```

Regimes govern how Claims may be admitted, evaluated, contested, invalidated, and escalated.

They do not:

- redefine meaning;
- execute Actions;
- create Authority;
- replace Execution Contracts;
- belong to Domain Packs.

The five identities and canonical summaries derive from the Canon. The detailed machine-readable matrices
are explicitly marked as exploratory candidates reconstructed from the February 2026 Regime work and are
intended for later Canon review.

See:

- [`CORE-SEMANTIC-PACK-REGIMES.md`](CORE-SEMANTIC-PACK-REGIMES.md)
- [`semantic/concepts/epistemic/regimes/`](semantic/concepts/epistemic/regimes/)
- [`docs/regime-canon-gap-ledger.md`](docs/regime-canon-gap-ledger.md)

## Atomic question contracts

The unit of answerability is one canonical question:

```text
one question = one independently resolvable Semantic Question Contract
```

Question families are taxonomy and discovery views only. Each question has exactly one primary family and
one complete contract stored under that family. Another family may list the canonical question as related
without duplicating it or donating requirements.

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

See [`semantic/questions/`](semantic/questions/) and
[`docs/question-contract-model.md`](docs/question-contract-model.md).

## Composition

The composition model is:

```text
Core Semantic Pack
  + Domain Semantic Pack(s)
  + Execution Contract
  + Core Regime selection
  = Resolved Semantic Pack
```

There is no independently authored `Regime Pack`.

Domain Packs are open-ended, independently authored Core-compatible meaning extensions. Execution Contracts
select and apply Core Regimes for concrete Processes. A resolved pack records the exact Regime IDs,
versions, comparative evaluations, and switch history.

## Repository map

| Area | Responsibility |
|---|---|
| [`pack.yaml`](pack.yaml) | Pack identity, scope, guarantees, question model, Regime model, and composition rules |
| [`semantic/`](semantic/) | Governed semantic source and semantic governance rules |
| [`semantic/concepts/`](semantic/concepts/) | Atomic candidate Core primitives organized by semantic layer |
| [`semantic/concepts/epistemic/regimes/`](semantic/concepts/epistemic/regimes/) | Five Core Regimes, matrices, switching, conformance, and fixtures |
| [`semantic/relations/`](semantic/relations/) | Typed relations that form the semantic graph |
| [`semantic/boundaries/`](semantic/boundaries/) | Anti-collapse rules and semantic safety properties |
| [`semantic/questions/`](semantic/questions/) | Atomic questions organized under taxonomy-only primary families |
| [`semantic/references/`](semantic/references/) | Explicit non-Core comparison categories used by structured notation |
| [`semantic/patterns/`](semantic/patterns/) | Composite structures built from Core primitives |
| [`semantic/lifecycle/`](semantic/lifecycle/) | Separate lifecycle and status families |
| [`semantic/composition/`](semantic/composition/) | Rules for Core, Domain, Execution, Regime selection, and resolution |
| [`mappings/`](mappings/) | Non-authoritative architecture mappings |
| [`semantic/conformance/`](semantic/conformance/) | General rules, coverage, and valid/invalid semantic fixtures |
| [`examples/`](examples/) | Illustrative, non-authoritative semantic traces |
| [`release/`](release/) | Versioned release manifest and known limitations |
| [`docs/`](docs/) | Derivation, terminology, Regime gap ledger, record format, and open questions |

## Specification

See [CORE-SEMANTIC-PACK.md](CORE-SEMANTIC-PACK.md) for the working v0.1 architectural specification.

The Regimes supplement, [`CORE-SEMANTIC-PACK-REGIMES.md`](CORE-SEMANTIC-PACK-REGIMES.md), supersedes the
earlier `Regime Pack` composition passages in the baseline document.

## Validate the pack

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_pack.py
python scripts/validate_regimes.py
```

The general validator checks registry identity, canonical-symbol uniqueness and resolution, boundary
expressions, question atomicity and family topology, authoring surfaces, indexes, fixtures, and release
manifests.

The Regime validator checks the five-Regime set, required matrices, composition boundaries, switching
discipline, and dedicated Regime fixtures.

Neither validator determines semantic truth or acts as semantic authority.

## Status

Working reference specification / non-canonical.
