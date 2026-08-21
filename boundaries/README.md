# Boundaries

`core-boundaries.yaml` contains the Core anti-collapse rules.

A boundary is a semantic safety property. It states that two categories must remain distinguishable even when a runtime stores them in the same table, serializes them with the same schema, or presents them through the same interface.

Boundary records retain a stable ID and expose a canonical expression such as `Action != Intent`. The expression is the authoring reference; its operands resolve deterministically and the stable failure code remains available to conformance tooling.

Some operands resolve through [`references/non-core-symbols.yaml`](../references/non-core-symbols.yaml) rather than the Core primitive registry. Terms such as `Truth`, `Prediction`, `Plan`, `ExecutionPlan`, and `Runtime` are necessary comparison categories but are not admitted as v0.1 Core primitives.
