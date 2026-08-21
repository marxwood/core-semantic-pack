# Semantic composition

The Core Semantic Pack is a kernel, not a complete semantic environment.

A concrete consumer normally resolves:

```text
Core Semantic Pack
        +
Domain Semantic Pack(s)
        +
Execution Contract
        +
Core Regime selection
        =
Resolved Semantic Pack
```

A Regime is **not** an independently authored extension pack.

The Core defines:

- the `Regime` concept;
- `Open`;
- `Disciplined`;
- `Adversarial`;
- `High-Assurance`;
- `Locked`;
- Regime evaluation, switching, and provenance discipline.

A Domain Pack may specialize Core meaning and map domain Evidence classes. It may declare compatibility
with the Core Regime set, but it may not define or redefine a Regime.

An Execution Contract selects the primary and optional comparative Core Regimes for a concrete Process.
It may add stricter process constraints without changing Regime meaning.

A Resolved Semantic Pack records:

- the exact Core release;
- Domain Pack versions;
- the Execution Contract version;
- the selected Core Regime IDs and versions;
- Regime switch history;
- compatibility and checksum.

Composition is not unrestricted merging. Extensions may add detail or narrow applicability. They must not
silently redefine Core concepts, relations, boundaries, or Regimes.
