# Record format

The repository uses YAML as a working, human-reviewable serialization. YAML is not semantic authority; stable IDs, definitions, boundaries, obligations, and versioned decisions are.

## Concept record

A concept record includes identity, version, layer, definition, questions it helps answer, explicit non-equivalences, relations, boundaries, and derivation.

## Relation record

A relation record includes stable ID, source and target concept classes, direction, definition, provenance requirement, and any normative authority effect.

## Boundary record

A boundary record includes left and right semantic categories, a non-equivalence rule, rationale, stable failure code, severity, and areas of application.

## Atomic Semantic Question Contract

A question contract includes:

- exactly one `canonical_question`;
- primary and additional family classifications;
- required concepts and relations;
- boundaries that must remain intact;
- minimum answer requirements;
- failure states and consequence policy;
- `independently_resolvable: true`;
- `requirements_inherited_from_family: false`.

Question families do not carry these requirements. They are taxonomy-only views.

## Pattern record

A pattern composes Core primitives and relations. It must declare `not_a_primitive: true` unless it has separately passed Core admission criteria.
