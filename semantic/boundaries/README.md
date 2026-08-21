# Boundaries

Each Core anti-collapse rule has one YAML file in this directory. [`index.yaml`](index.yaml) bridges its canonical expression to its stable ID and physical file without duplicating the rule.

A boundary is a semantic safety property. It states that two categories must remain distinguishable even when a runtime stores them in the same table, serializes them with the same schema, or presents them through the same interface.

Boundary records retain a stable ID and expose a canonical expression such as `Action != Intent`. The expression is the complete authoring reference; its operands and `!=` distinction resolve deterministically, and the stable failure code remains available to conformance tooling. Boundary records do not repeat the expression as separate `left`, `operator`, or `right` fields.

The stable ID is registry identity and the canonical expression is the semantic reference. The flat file path is only a serialization location and never determines Boundary identity.

Some operands resolve through [`references/non-core-symbols.yaml`](../references/non-core-symbols.yaml) rather than the Core primitive registry. Terms such as `Truth`, `Prediction`, `Plan`, `ExecutionPlan`, and `Runtime` are necessary comparison categories but are not admitted as v0.1 Core primitives.
