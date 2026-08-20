# Core Semantic Pack

A runtime-neutral semantic kernel for correction-capable human-agentic systems.

The Core Semantic Pack defines the minimal, stable, domain-neutral semantic distinctions required for systems to preserve meaning across perception, reasoning, memory, governance, action, and StateChange.

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
- `OperationalSuccess != GoalProgress`

It also treats answerability as a core architectural property: material system behavior should remain traceable enough to answer what is known, why an action is being taken, which goal it advances, what authorized it, what changed, and whether the system is still moving toward the intended state.

## Specification

See [CORE-SEMANTIC-PACK.md](CORE-SEMANTIC-PACK.md) for the working v0.1 architectural specification.

## Status

Working reference specification / non-canonical.
