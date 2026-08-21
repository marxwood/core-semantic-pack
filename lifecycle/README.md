# Lifecycle and status families

Lifecycle records prevent several different kinds of status from collapsing into one generic `status` field.

The Core distinguishes:

- `ConceptAuthorityStatus` — whether a semantic definition is proposed, adopted, or retired;
- `EpistemicStatus` — how an assertion or result currently stands relative to support and contradiction;
- `ValidityStatus` — whether an object satisfies declared conditions in a Context;
- `AdmissionStatus` — whether a candidate may enter maintained governed State;
- `BindingStatus` — whether an authority-bearing commitment is operative.

Runtime states such as `running`, `paused`, `failed`, or `retried` are deliberately excluded. They belong to execution mappings.

No status transition is implied by storage, repetition, visibility, model confidence, successful execution, or schema validation. Material transitions must be explicit, attributable, contextual, and reconstructable.
