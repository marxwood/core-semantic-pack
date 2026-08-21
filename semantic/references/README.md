# Reference-only semantic symbols

This directory declares resolvable comparison and architecture categories used by structured Core notation that are deliberately not Core primitives.

`Truth`, `Prediction`, `Plan`, `BindingDecision`, `Repetition`, `ExecutionPlan`, `Runtime`, and `OperationalSuccess` exist so boundaries and fixtures can use deterministic canonical references. Every record declares `core_primitive: false`.

Adding a reference-only symbol does not admit a concept into the Core. Primitive admission still requires the derivation and governance process described in [`docs/derivation-and-admission.md`](../../docs/derivation-and-admission.md).

`Any` is not listed here because it is reserved wildcard meta-notation, not a semantic registry object.
