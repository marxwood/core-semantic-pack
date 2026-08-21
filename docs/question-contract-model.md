# Atomic Semantic Question Contract model

## Decision

The Core Semantic Pack uses one **Semantic Question Contract** per canonical question.

```text
Question Family
    = taxonomy / discovery view

Semantic Question
    = atomic semantic responsibility

Semantic Question Contract
    = requirements for answering one canonical question
```

A family is not a requirement bundle and is not the owner of a question's meaning. Each question has exactly one primary family, which determines only its physical location and primary taxonomy.

## Why atomicity matters

Questions that sound related can require different minimum semantics.

For example:

- `Why is this being done?` requires an Action → Intent → Goal path and relevant Authority.
- `Is the resulting StateChange advancing the DesiredState?` requires StateChange, DesiredState, and an explicit Progress evaluation.
- `Has the Goal changed?` requires version and supersession lineage and must remain reconstructable historically.

Bundling all three into a teleological family contract would cause a consumer asking only the first question to receive unrelated trajectory and revision semantics. That weakens question-driven pack resolution.

## Primary family and related navigation

Every question is defined once beneath its primary family. Requiring concepts from several semantic layers does not create multi-family ownership.

`Has the Goal changed?` is primary to `teleological`. The `reflective` family lists it under `related_questions` because reflective correction consumes the answer, but the question is not duplicated and does not acquire a second owner.

Family records contain:

- `questions` — canonical questions whose primary family is that family;
- `related_questions` — exact canonical references to useful questions defined by another family.

No requirements are inherited from either list.

## Contract structure

Each atomic contract declares:

- one `canonical_question`;
- one primary `family` symbol;
- required Core concepts;
- required Core relations;
- anti-collapse boundaries that must remain intact;
- minimum answer requirements;
- failure states and consequence policy;
- independent resolvability is a model-level invariant declared in
  `semantic/questions/index.yaml > question_model`;
- family requirements are not inherited; this is the global resolution rule in
  `semantic/questions/index.yaml > question_model`.

Atomic contracts therefore do not repeat either invariant in a per-contract
`composition` block.

The exact YAML shape is non-authoritative. The semantic obligation is the important artifact.

## Resolution rule

```text
requested canonical questions
      ↓
exact lookup through semantic/questions/index.yaml
      ↓
load each atomic contract under its primary family
      ↓
validate explicit references
      ↓
union required concepts / relations / boundaries
      ↓
compose Domain + Regime + Execution semantics
      ↓
immutable Resolved Semantic Pack
```

A family can be requested only as an explicit navigation expansion over its `questions` list. `related_questions` never expands automatically, and the resolver never infers additional requirements merely from family membership.

Canonical questions—not stable IDs or filename slugs—are the semantic request language. Stable IDs remain the compatibility and registry identity layer.
