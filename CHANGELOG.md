# Changelog

All notable changes to the Core Semantic Pack are recorded here.

The project is experimental. Until the first adopted release, version changes describe evolution of the
working reference model rather than a production compatibility guarantee.

## Unreleased

- Redefines H1 `SemanticOSAdoptionHandshake` as one complete single-invocation adoption procedure rather than a capability inventory followed by ad hoc prompts.
- Adds semantic-obligation resolution, runtime self-inspection, Capability Resolution, realization selection, Operational Fitness, authority/enforcement separation, behavioral proof, and explicit revalidation triggers.
- Requires runtimes to exhaust native, mappable, composable, and already externally available capabilities before concluding that a physical capability is missing or incompatible.
- Makes new runtime software a last-resort proposed remedy that H1 itself neither authorizes nor implements.
- Separates semantic conformance from operational fitness for declared workloads, including Renderer and agent retrieval patterns, scale, latency, throughput, durability, reconstruction cost, resource use, concurrency, and recovery.
- Changes `conditional` into a final outcome reached only after the complete procedure has been exhausted; intermediate gaps no longer terminate H1.
- Expands Handshake Records with resolved obligations, capability-resolution classes, selected realizations, operational-fitness evidence and bounds, behavioral proof, and revalidation triggers.
- Updates the illustrative Handshake Prompt, Handshake Record, repository guidance, manifest guarantees, and dedicated Handshake validator for the complete procedure.

## 0.1.0 — Experimental baseline

- Materializes the architectural specification as a repository-level semantic pack.
- Introduces 52 candidate Core primitives across foundations, epistemics, teleology, agency, and governance.
- Introduces 91 typed Core relations and 23 anti-collapse boundaries.
- Introduces 9 question families as taxonomy-only views.
- Introduces 66 atomic, independently resolvable Semantic Question Contracts covering the canonical
  question set in the specification.
- Organizes every atomic Question under exactly one primary family and uses explicit related-question
  navigation without duplicating contracts.
- Adopts canonical human-agent notation for concepts, relations, boundaries, Questions, patterns, status
  families, conformance rules, fixtures, examples, mappings, and composition.
- Declares 8 reference-only semantic symbols without promoting them to Core primitives.
- Introduces 5 composite patterns for semantic traceability, teleology, institutional memory, execution
  legitimacy, and semantic status collapse.
- Separates five lifecycle/status families.
- Introduces 18 general conformance rules, 5 valid fixtures, and 24 intentionally invalid semantic
  regression fixtures.
- Integrates `Regime` as a candidate Core primitive.
- Integrates the Canon-derived five-Regime set: Open, Disciplined, Adversarial, High-Assurance, and Locked.
- Adds detailed February 2026 per-Regime matrices as explicitly exploratory derivation candidates.
- Removes `Regime Pack` from the composition model.
- Makes Domain Packs independently authored Core-compatible extensions that may declare Regime
  compatibility but cannot define Regimes.
- Makes Execution Contracts responsible for selecting primary and comparative Core Regimes.
- Adds explicit Regime switching, comparative evaluation, provenance, validity-scoping, and
  cross-Regime non-collapse rules.
- Adds a dedicated Regime validator and six Regime-specific fixtures.
- Introduces the H1 Semantic OS Adoption Handshake, a non-authoritative Handshake Prompt example, a
  reconstructable Handshake Record example, and dedicated structural validation.
- Adds composition, generic agentic mapping, release, and structural validation records.
