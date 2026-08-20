# Boundaries

`core-boundaries.yaml` contains the Core anti-collapse rules.

A boundary is a semantic safety property. It states that two categories must remain distinguishable even when a runtime stores them in the same table, serializes them with the same schema, or presents them through the same interface.

Boundary records are referencable by stable ID and include a failure code used by conformance fixtures.

Some right- or left-hand categories use `semantic-category:*` rather than a Core primitive. These terms—such as `truth`, `prediction`, `plan`, `execution-plan`, and `runtime`—are necessary comparison categories but are not admitted as v0.1 Core primitives.
