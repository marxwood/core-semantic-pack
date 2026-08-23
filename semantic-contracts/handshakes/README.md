# Semantic Handshakes

Semantic Handshakes are portable, runtime-neutral contracts that determine whether a consumer may claim to operate under a Semantic Pack.

They sit at the boundary between semantic authority, a Semantic Pack Provider, a runtime consumer, and the authority of the target environment. A handshake does not grant authority to a provider or runtime. It makes identities, obligations, capabilities, realizations, authority boundaries, operational fitness, update policy, evidence, and the resulting adoption decision explicit.

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
complete adoption procedure
        ↓
accepted | conditional | rejected
```

The first contract is [`H1-semantic-os-adoption-contract.yaml`](H1-semantic-os-adoption-contract.yaml).

## H1 is a complete procedure

H1 is not a capability checklist that stops after discovering gaps.

One invocation instructs the runtime to proceed through the complete procedure:

```text
identity binding
      ↓
semantic obligation resolution
      ↓
runtime self-inspection
      ↓
capability resolution
      ↓
realization selection
      ↓
operational fitness
      ↓
authority / enforcement boundary
      ↓
behavioral proof
      ↓
synchronization commitment
      ↓
adoption decision
      ↓
revalidation triggers
```

A user should not have to issue separate prompts for capability resolution, implementation selection, operational-fitness evaluation, or revalidation analysis.

An intermediate gap is not a final `conditional` outcome. The runtime first determines whether the obligation can be realized through capabilities it already possesses or already has access to.

## Runtime-native-first resolution

For every unresolved semantic obligation, H1 evaluates realizations in this order:

```text
native
  ↓
mappable
  ↓
composable
  ↓
externally available
  ↓
missing
  ↓
incompatible
```

The absence of a dedicated semantic subsystem is not evidence that the underlying capability is absent.

A filesystem, Git repository, database, memory facility, retrieval index, approval mechanism, messaging surface, or combination of existing capabilities may realize a semantic obligation if the required distinctions and authority boundary survive.

New runtime software is a last-resort proposed remedy. H1 itself neither authorizes nor implements it.

## Operational fitness

A semantically valid realization may still be operationally inadequate.

H1 therefore evaluates selected realizations against the declared current workload, including relevant scale, latency, throughput, relation traversal, Renderer and agent retrieval patterns, durability, reconstruction cost, resource consumption, concurrency, and recovery behavior.

Operational layers may evolve below stable semantics:

```text
canonical semantic history
        ↓
maintained State
        ↓
derived retrieval / index / cache
        ↓
Renderers and agents
```

A replaceable derived index or materialized view does not become semantic authority merely because it provides fast access.

## Handshake Prompt

A Handshake Prompt is a runtime-facing invocation of a Semantic Handshake Contract. It is not the Contract itself and is never semantic authority. Prompt wording may vary across Hermes, Claude Code, Codex, another model, or a non-prompt protocol adapter while the underlying obligations remain stable.

The invocation must instruct the runtime to execute H1 autonomously through its final decision. It must not weaken H1 into a first-pass inventory that requires manual follow-up prompts.

## Handshake Record

Every execution of a handshake produces a versioned, attributable Handshake Record. The record preserves the exact Pack and participant identities, resolved semantic obligations, runtime capability inventory, per-obligation realization class, selected physical realizations, operational-fitness evidence and bounds, behavioral proof, authority boundaries, update policy, final decision, unresolved conditions, and revalidation triggers.

Reading the Pack is therefore insufficient:

> A runtime becomes governed only after completing the full H1 procedure for the identified Pack, runtime, environment, workload, and authority boundary.
