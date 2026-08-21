# Record format

The repository uses YAML as a working, human-reviewable serialization. YAML is not semantic authority; stable IDs, definitions, boundaries, obligations, and versioned decisions are.

## Stable identity and canonical reference

Registry records retain stable `id` values. Concepts, relations, patterns, status families, conformance rules, and question families expose canonical `symbol` values. Boundaries expose canonical `expression` values. Questions expose `canonical_question` values. There is no redundant schema-level human-label field in v0.1.

See [`semantic-notation.md`](semantic-notation.md).

## Concept record

A concept record includes stable identity, canonical symbol, version, layer, definition, exact canonical questions it `helps_answer`, resolvable `not_equivalent_to` references, explanatory `exclusions`, canonical relations and boundaries, and derivation.

## Relation record

A relation record includes stable ID, canonical lowerCamelCase symbol, canonical source and target types, direction, optional canonical inverse, definition, provenance requirement, and any normative authority effect. `Any` is reserved wildcard meta-notation.

## Boundary record

A boundary record includes stable ID, canonical expression, resolvable left and right semantic categories, the `!=` operator, rule, rationale, stable failure code, severity, and areas of application.

## Atomic Semantic Question Contract

A question contract includes:

- exactly one `canonical_question`;
- exactly one primary `family`;
- required concepts and relations;
- boundaries that must remain intact;
- minimum answer requirements;
- failure states and consequence policy;
- independent resolvability, declared once as the question-model invariant
  `questions/index.yaml > question_model.independently_resolvable: true`;
- family requirements are not inherited, declared globally as
  `questions/index.yaml > question_model.family_requirements_inherited: false`.

Question families do not carry these requirements. They are taxonomy-only views containing `questions` and optional cross-family `related_questions` canonical references.

## Pattern record

A pattern composes Core primitives and relations. It must declare `not_a_primitive: true` unless it has separately passed Core admission criteria.
