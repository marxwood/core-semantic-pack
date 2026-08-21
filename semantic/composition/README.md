# Semantic composition

The Core Semantic Pack is a kernel, not a complete semantic environment.

A concrete consumer normally resolves:

```text
Core Semantic Pack
        +
Domain Semantic Pack
        +
Regime Pack
        +
Execution Contract
        =
Resolved Semantic Pack
```

Composition is not unrestricted merging. Each layer has a distinct authority:

- the **Core** defines stable cross-domain distinctions;
- a **Domain Pack** specializes or restricts Core meaning within a declared domain;
- a **Regime Pack** supplies contextual validity, admission, review, and authority conditions;
- an **Execution Contract** binds a Process to legitimate execution conditions;
- a **Resolved Semantic Pack** records the exact immutable composition used by a consumer.

Extensions may add detail or narrow applicability. They must not silently redefine Core concepts, relations, or boundaries. Conflicting meanings make resolution fail until an explicit compatibility or adoption decision exists.
