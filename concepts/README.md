# Concepts

This directory materializes the candidate Core primitives described by the architectural specification.

Concepts are grouped by semantic responsibility layer rather than by runtime implementation:

- `foundations.yaml` — identity, context, State, Source, Projection, and semantic versioning;
- `epistemic.yaml` — Observation, Claim, Evidence, Inference, Finding, and correction-relevant epistemic status;
- `teleological.yaml` — Goal, DesiredState, Intent, Direction, Trajectory, and Progress;
- `agency.yaml` — Actor, Role, Capability, Action, Process, Transformation, Transfer, Persistence, Composition, and ExternalEffect;
- `governance.yaml` — Authority, Constraint, Permission, Contract, Validation, Admission, Review, Binding, Commitment, Revocation, and Accountability.

## Authority

Every concept is `experimental` and `candidate-core-primitive` in v0.1. Inclusion here does not make a concept canonical. A concept should move upward in authority only after its derivation, boundaries, lifecycle, and cross-domain necessity remain stable across multiple mappings.

## Record discipline

Each record declares:

- stable `id` and canonical PascalCase `symbol`;
- exact canonical Questions it `helps_answer`, when an audited match exists;
- a definition;
- resolvable `not_equivalent_to` symbols and separate explanatory `exclusions`;
- required and conditional canonical relation symbols;
- canonical anti-collapse boundary expressions;
- derivation rationale.

The exact YAML serialization is non-authoritative. Stable IDs preserve registry identity, while symbols and semantic obligations are the authoring contract. Legacy free-form question-like strings without an exact canonical match are retained for review in [`docs/canonical-question-gaps.md`](../docs/canonical-question-gaps.md).
