# Concepts

This directory materializes the candidate Core primitives described by the architectural specification.

Each Concept has one file under its semantic responsibility layer rather than a runtime implementation grouping:

- `foundations/` — identity, context, State, Source, Projection, and semantic versioning;
- `epistemic/` — Observation, Claim, Evidence, Inference, Finding, and correction-relevant epistemic status;
- `teleological/` — Goal, DesiredState, Intent, Direction, Trajectory, and Progress;
- `agency/` — Actor, Role, Capability, Action, Process, Transformation, Transfer, Persistence, Composition, and ExternalEffect;
- `governance/` — Authority, Constraint, Permission, Contract, Validation, Admission, Review, Binding, Commitment, Revocation, and Accountability.

[`index.yaml`](index.yaml) bridges each canonical symbol to its stable ID, layer, and physical file. It contains lookup metadata only.

## Authority

Every concept is `experimental` and `candidate-core-primitive` in v0.1. Inclusion here does not make a concept canonical. A concept should move upward in authority only after its derivation, boundaries, lifecycle, and cross-domain necessity remain stable across multiple mappings.

## Record discipline

Each atomic record declares:

- stable `id` and canonical PascalCase `symbol`;
- exact canonical Questions it `helps_answer`, when an audited match exists;
- a definition;
- resolvable `not_equivalent_to` symbols and separate explanatory `exclusions`;
- required and conditional canonical relation symbols;
- canonical anti-collapse boundary expressions;
- derivation rationale.

The exact YAML serialization is non-authoritative. Stable IDs preserve registry identity, while symbols and semantic obligations are the authoring contract. The physical path is only a serialization location and never determines Concept identity. Legacy free-form question-like strings without an exact canonical match are retained for review in [`docs/canonical-question-gaps.md`](../docs/canonical-question-gaps.md).
