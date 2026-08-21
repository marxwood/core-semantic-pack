# Core Regimes

This directory materializes the Canon-derived Regime system inside the Core Semantic Pack.

## Ordered Regime definitions

```text
R1-open.yaml
R2-disciplined.yaml
R3-adversarial.yaml
R4-high-assurance.yaml
R5-locked.yaml
```

The order follows the Canon's low-constraint to high-constraint validity spectrum.

The five Regime identities are:

1. `Open`
2. `Disciplined`
3. `Adversarial`
4. `High-Assurance`
5. `Locked`

Their identities and short descriptions derive from
`system-momentum-canon/core/authority/regimes.md`.

The detailed enumerative matrices are **exploratory derivation candidates** reconstructed from the February
2026 Regime work. They are intentionally included so the Core Pack can be tested as a complete system and so
the next Canon review has a concrete proposal to accept, revise, or reject.

They are not represented as already-canonical text.

## Contracts

Regime contracts live separately from Regime definitions:

```text
contracts/
├── evaluation-contract.yaml
├── switching-contract.yaml
└── conformance-contract.yaml
```

A contract file always ends in `-contract.yaml`.

## Structural position

```text
Core Semantic Pack
  ├── Core semantic concepts
  ├── Regime
  ├── five ordered Core Regime definitions
  ├── Regime contracts
  └── extension contract

Domain Packs
  └── independently authored Core-compatible meaning extensions

Execution Contracts
  └── select and apply Core Regimes for a concrete Process

Resolved Semantic Pack
  └── records exact Core, Domain, Execution Contract, and Regime selection
```

There is no `Regime Pack` extension class.

A Domain Pack may define domain-specific Claim and Evidence specializations and declare which Core Regimes it
supports. It may not define or redefine Core Regimes.

An Execution Contract may select one primary Regime and optional comparative Regimes. It may add stricter
process conditions without changing the meaning of the selected Regime.
