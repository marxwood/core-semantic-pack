# Semantic Handshakes

Semantic Handshakes are portable, runtime-neutral contracts that determine whether a consumer may claim to operate under a Semantic Pack.

They sit at the boundary between semantic authority, a Semantic Pack Provider, a runtime consumer, and the authority of the target environment. A handshake does not grant authority to a provider or runtime. It makes identities, capabilities, authority boundaries, conflict behavior, update policy, evidence, and the resulting adoption decision explicit.

```text
Semantic authority source
        +
Semantic Pack Provider
        +
runtime consumer
        +
environment authority
        ↓
Semantic Handshake
        ↓
accepted | conditional | rejected
```

The first contract is [`H1-semantic-os-adoption-contract.yaml`](H1-semantic-os-adoption-contract.yaml).

## Handshake Prompt

A Handshake Prompt is a runtime-facing invocation of a Semantic Handshake Contract. It is not the Contract itself and is never semantic authority. Prompt wording may vary across Hermes, Claude Code, Codex, another model, or a non-prompt protocol adapter while the underlying obligations remain stable.

## Handshake Record

Every execution of a handshake produces a versioned, attributable Handshake Record. The record preserves the exact Pack and participant identities, claims, evidence, authority boundaries, update policy, decision, unresolved conditions, and the authority responsible for that decision.

Reading the Pack is therefore insufficient:

> A runtime becomes governed only after completing a valid Semantic Handshake for the identified Pack, runtime, environment, and authority boundary.
