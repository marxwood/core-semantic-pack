# Record format

The repository uses YAML as a working, human-reviewable serialization. YAML is not semantic authority; stable IDs, definitions, boundaries, and obligations are.

## Concept record

A concept record includes:

- `id`, `name`, `version`, `status`, `layer`, and `kind`;
- a domain-neutral definition;
- questions it helps answer;
- explicit non-equivalences in `what_it_is_not`;
- required and conditional relation IDs;
- boundary IDs;
- derivation source and rationale.

## Relation record

A relation record includes:

- stable ID and name;
- source and target concept classes;
- direction and optional inverse;
- definition;
- provenance requirement;
- normative authority effect, if any.

## Boundary record

A boundary record includes:

- left and right semantic categories;
- `not-equivalent-to` rule;
- rationale;
- stable failure code;
- declared severity and areas of application.

## Question contract

A question contract includes:

- canonical questions;
- required concepts and relations;
- boundaries that must remain intact;
- answer requirements;
- failure states;
- permitted consequences when answerability fails.

## Pattern record

A pattern composes Core primitives and relations. It must declare `not_a_primitive: true` unless it has separately passed Core admission criteria.
