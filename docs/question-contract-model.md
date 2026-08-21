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

A family is not a requirement bundle and is not the owner of a question's meaning.

## Why atomicity matters

Questions that sound related can require different minimum semantics.

For example:

- `Why is this being done?` requires an Action → Intent → Goal path and relevant Authority.
- `Is the resulting StateChange advancing the DesiredState?` requires StateChange, DesiredState, and an explicit Progress evaluation.
- `Has the Goal changed?` requires version and supersession lineage and must remain reconstructable historically.

Bundling all three into a teleological family contract would cause a consumer asking only the first question to receive unrelated trajectory and revision semantics. That weakens question-driven pack resolution.

## Multi-family classification

A question may participate in multiple families without being duplicated.

`core.question.detect-goal-change` has one contract and one canonical question, while its classification can include teleological, reflective, governance, and memory responsibility domains.

Family records contain:

- canonical members — questions whose primary family is that family;
- related members — questions whose primary family is elsewhere but whose responsibility crosses the family boundary.

No requirements are inherited from either list.

## Contract structure

Each atomic contract declares:

- one `canonical_question`;
- classification metadata;
- required Core concepts;
- required Core relations;
- anti-collapse boundaries that must remain intact;
- minimum answer requirements;
- failure states and consequence policy;
- independent resolvability.

The exact YAML shape is non-authoritative. The semantic obligation is the important artifact.

## Resolution rule

```text
requested question IDs
      ↓
load each atomic contract
      ↓
validate explicit references
      ↓
union required concepts / relations / boundaries
      ↓
compose Domain + Regime + Execution semantics
      ↓
immutable Resolved Semantic Pack
```

A family can be requested only as an explicit macro that expands to member question IDs. The resolver must never infer additional requirements merely from family membership.
