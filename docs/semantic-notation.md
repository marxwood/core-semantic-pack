# Canonical semantic notation

Canonical semantic notation is the primary authoring and inspection language of the Core Semantic Pack. Stable IDs provide registry identity. Repository paths and slugs are serialization details.

Every referencable semantic object has a stable registry identity and one canonical semantic reference in its namespace:

| Semantic kind | Stable registry identity | Canonical authoring reference |
|---|---|---|
| Concept | `core.desired-state` | `DesiredState` |
| Relation | `core.rel.authorized-by` | `authorizedBy` |
| Boundary | `core.boundary.action-not-intent` | `Action != Intent` |
| Question | `core.question.explain-action-purpose` | `Why is this being done?` |
| Pattern | `core.pattern.execution-contract` | `ExecutionContract` |
| Question family | `core.question-family.teleological` | `teleological` |
| Status family | `core.status-family.epistemic` | `EpistemicStatus` |
| Conformance rule | `core.rule.action-purpose-chain` | `ActionPurposeChain` |
| Reference-only term | `semantic-category:truth` | `Truth` |

There is no separate human-label layer and no question-slug semantic layer in v0.1. A concept or relation record uses `symbol`; a Question uses its `canonical_question` itself.

## Registry and authoring surfaces

Registry surfaces use IDs where exact identity is the point: record `id`, pack/component identity, versions, migrations, release metadata, fixture identity, file paths, commits, and checksums.

Semantic authoring surfaces use canonical references: concept and relation requirements, boundary preservation, question requests, family navigation, patterns, lifecycle rules, mappings, conformance rules and fixtures, examples, and semantic traces.

Indexes intentionally bridge both layers:

```yaml
- canonical_question: Why is this being done?
  id: core.question.explain-action-purpose
  family: teleological
  file: questions/teleological/why-is-this-being-done.yaml
```

## Resolution

Within the Core namespace, concept symbols, relation symbols, boundary expressions, canonical questions, pattern symbols, status-family symbols, rule symbols, and question-family symbols are unique within their semantic namespaces. Unknown or ambiguous references are validation errors.

Question resolution uses exact canonical value; it does not use fuzzy matching or infer equivalence from a filename. Changing a canonical question is compatibility-relevant and requires migration review even though its stable ID can survive the wording change.

Boundary expressions are not unchecked strings. The resolver validates the expression, its left and right operands, and the boundary record behind it.

`Any` is reserved meta-notation for a wildcard relation endpoint. It is not a Core primitive or registry object.

## Reference-only terms

Terms such as `Truth`, `Prediction`, `Plan`, `BindingDecision`, `Repetition`, `ExecutionPlan`, `Runtime`, and `OperationalSuccess` are declared in [`references/non-core-symbols.yaml`](../references/non-core-symbols.yaml). They make structured comparisons resolvable without promoting those categories to Core primitives.

The Core primitive remains `Progress`; the canonical boundary is `OperationalSuccess != Progress`.

## Future qualified symbols

Unqualified symbols resolve against the local/default namespace. Future Domain Packs may use explicit imports and qualified symbols when another namespace is in scope:

```yaml
imports:
  core: semantic-pack.core@0.1
  ip: semantic-pack.ip@0.4

requires:
  - Claim
  - ip:Patent
```

Qualification is required when ambiguity exists or when another namespace is referenced. v0.1 does not implement a package manager or aliases.
