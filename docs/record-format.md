# Record format

The repository uses YAML as a working, human-reviewable serialization. YAML is not semantic authority; stable IDs, definitions, boundaries, obligations, and versioned decisions are.

Each referencable Concept, Relation, Boundary, and Question occupies one file. Semantically related fields stay together and exactly one blank line separates semantic groups. Indexes remain compact lookup bridges and never duplicate full records.

## Canonical record layout

Semantic definition records use one visual reading order:

```text
registry identity and metadata

canonical semantic identity

meaning

dependencies and structure

boundaries and constraints

behavior and failure semantics

derivation and notes
```

The metadata block contains fields such as `id`, `version`, `status`, `kind`, and `layer`. The primary semantic declaration is isolated immediately after it: `symbol` for symbol-bearing records, `expression` for a Boundary, or `canonical_question` for a Semantic Question Contract. Semantic declarations never share the metadata block.

Indexes, release manifests, migration records, and example or fixture instances retain their compact registry-oriented layouts because they are lookup or instance records rather than semantic definitions.

## Stable identity and canonical reference

Registry records retain stable `id` values. Concepts, relations, patterns, status families, conformance rules, and question families expose canonical `symbol` values. Boundaries expose canonical `expression` values. Questions expose `canonical_question` values. There is no redundant schema-level human-label field in v0.1.

See [`semantic-notation.md`](semantic-notation.md).

## Concept record

A concept record includes stable identity, canonical symbol, version, layer, definition, exact canonical questions it `helps_answer`, resolvable `not_equivalent_to` references, explanatory `exclusions`, canonical relations and boundaries, and derivation.

## Relation record

A relation record includes stable ID, canonical lowerCamelCase symbol, canonical source and target types, direction, optional canonical inverse, definition, provenance requirement, and any normative authority effect. `Any` is reserved wildcard meta-notation.

## Boundary record

A boundary record includes stable ID, canonical expression, rule, rationale, stable failure code, severity, and areas of application. The expression is authoritative and contains the resolvable semantic categories and `!=` distinction; boundary records do not repeat separate `left`, `operator`, or `right` fields.

## Atomic Semantic Question Contract

A question contract includes:

- exactly one `canonical_question`;
- exactly one primary `family`;
- required concepts and relations;
- boundaries that must remain intact;
- minimum answer requirements;
- failure states and consequence policy;
- independent resolvability, declared once as the question-model invariant
  `semantic/questions/index.yaml > question_model.independently_resolvable: true`;
- family requirements are not inherited, declared globally as
  `semantic/questions/index.yaml > question_model.family_requirements_inherited: false`.

Question families do not carry these requirements. They are taxonomy-only views containing `questions` and optional cross-family `related_questions` canonical references.

## Semantic Handshake Contract

A Semantic Handshake Contract includes:

- a stable ID, version, status, kind, and ordered handshake identifier;
- one isolated canonical `symbol`;
- participants and their distinct semantic responsibilities;
- preconditions, required declarations, ordered phases, and required questions;
- invariants protecting authority boundaries and local semantic sovereignty;
- explicit acceptance requirements and exactly three outcomes: `accepted`, `conditional`, and `rejected`;
- Handshake Record requirements, revalidation conditions, and stable failure codes;
- a non-authoritative Handshake Prompt surface that may vary by runtime without changing the Contract.

Handshake contract filenames end in `-contract.yaml` and use an ordered `H<number>-` prefix. Prompt wording and provider-specific adapters are not canonical semantic declarations.

## Pattern record

A pattern composes Core primitives and relations. It must declare `not_a_primitive: true` unless it has separately passed Core admission criteria.
