# Semantic Questions

The Core uses one complete Semantic Question Contract for each canonical question.

```text
one canonical question
        =
one independently resolvable atomic contract
```

Each contract declares its stable registry ID, canonical question, one primary family, required concepts and relations, preserved boundary expressions, minimum answer requirements, and failure consequences.

## Primary-family organization

Questions live under their single primary semantic family:

```text
questions/families/<family>/family.yaml
questions/families/<family>/<question>.yaml
```

The path is serialization, not identity. For example:

```text
core.question.explain-action-purpose
        ↔
Why is this being done?
        ↔
questions/families/teleological/why-is-this-being-done.yaml
```

The stable ID supports registry history. The canonical question is the authoring and exact-resolution reference.

## Families are taxonomy

Every `family.yaml` record lists the canonical questions for which it is primary. It defines no semantic requirements, and questions inherit nothing from it.

A family may use `related_questions` for cross-family navigation. In v0.1, `Has the Goal changed?` is primary to `teleological` and related from `reflective`; there is still exactly one contract.

Semantic dependencies do not determine taxonomy. A teleological question may require `Action` or `Authority` without acquiring agency or governance ownership.

## Resolution

Consumers request canonical questions directly:

```yaml
questions:
  - Why is this being done?
  - What supports the Claim?
```

Resolution is exact and deterministic through [`index.yaml`](index.yaml). IDs and filename slugs are not accepted as semantic question references. Expanding a family is an explicit navigation operation over `questions[]`; `related_questions` never expands automatically.

See [`docs/question-contract-model.md`](../docs/question-contract-model.md) and [`docs/semantic-notation.md`](../docs/semantic-notation.md).
