# Semantic OS Adoption Handshake Prompt

This prompt is an illustrative invocation of `SemanticOSAdoptionHandshake`. It is not semantic authority and does not replace the Contract.

```text
Can you take the Core Semantic Pack ([link]) and build a working agent runtime that deploys and governs agents through it as a Semantic OS—not merely injects it into their context?

The runtime must remain synchronized with upstream Semantic Pack updates while preserving local semantic sovereignty: no upstream change may silently alter the environment's top-level goals, constraints, ontology, information boundaries, or the meaning of existing state.

Demonstrate the complete lifecycle with at least one deployed agent: semantic-pack loading, version pinning, update detection, semantic diff, compatibility validation, explicit acceptance, provenance, rollback, and conflict resolution between upstream semantic authority and environment-local semantics.

Return a Semantic Handshake Record containing the exact Pack, runtime, provider, adapter, and environment identities; every capability claim and its inspectable evidence; the authority and precedence boundaries; the update and rollback policy; unresolved conditions; and an accepted, conditional, or rejected decision.

If the current Core Semantic Pack is insufficient to guarantee this, identify the exact missing contracts instead of inventing implicit behavior. Do not claim semantic governance when the Pack is only available as retrieved context.
```

Vendor-specific versions may adapt the invocation surface, but they must not weaken or silently reinterpret the underlying handshake obligations.
