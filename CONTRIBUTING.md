# Contributing

The Core Semantic Pack is a working reference model. Contributions should improve semantic precision without turning current implementation conventions into universal meaning.

## Contribution principles

1. **Preserve layer boundaries.** Core concepts must remain domain-neutral and runtime-neutral.
2. **Derive before adding.** A new primitive requires an explicit question, stable boundary, cross-domain need, and explanation of why composition is insufficient.
3. **Keep questions atomic.** One canonical question belongs to one independently resolvable Semantic Question Contract under exactly one primary family.
4. **Keep semantic objects independently inspectable.** Each Concept, Relation, Boundary, and Question belongs in exactly one semantic file; indexes contain navigation metadata only.
5. **Treat families as taxonomy only.** Primary-family placement and related-question navigation must never add hidden requirements to a question.
6. **Do not collapse status families.** Concept authority, epistemic validity, admission, lifecycle, and binding status are different concerns.
7. **Do not promote mappings into authority.** Agent, tool, workflow, memory store, prompt, schema, and database terms remain mappings unless separately admitted into the Core.
8. **Add conformance evidence.** Material semantic changes should include appropriate valid or invalid evidence.
9. **Preserve reconstructability.** Breaking semantic changes require compatibility notes and a new release record.

## Question-contract changes

A question change should identify:

- the exact canonical question;
- whether the change alters requirements or only taxonomy;
- affected concepts, relations, and boundaries;
- primary-family or related-question navigation changes;
- compatibility consequences for resolved packs.

Moving a question between primary families is normally taxonomic but changes its serialization path and index entry. Changing its canonical wording or atomic contract is compatibility-relevant and semantic.

Author semantic references with canonical symbols, expressions, and questions. Keep stable IDs for registry identity and migration metadata. Do not add a redundant human label or filename-slug semantic layer.

Use exactly one blank line between semantic groups in human-inspected YAML and Markdown. Keep tightly coupled fields together, avoid trailing whitespace and tabs in YAML indentation, and preserve a final newline.

## Pull request expectations

A semantic change should identify the question that requires it, the existing concept or boundary it affects, derivation and non-equivalences, affected relations/patterns/fixtures, compatibility consequences, and unresolved questions.

Run the structural validator before review:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_pack.py
```
