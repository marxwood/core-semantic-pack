# Contributing

The Core Semantic Pack is a working reference model. Contributions should improve semantic precision without turning current implementation conventions into universal meaning.

## Contribution principles

1. **Preserve layer boundaries.** Core concepts must remain domain-neutral and runtime-neutral.
2. **Derive before adding.** A new primitive requires an explicit question, stable boundary, cross-domain need, and explanation of why composition is insufficient.
3. **Do not collapse status families.** Concept authority, epistemic validity, admission, lifecycle, and runtime status are different concerns.
4. **Do not promote mappings into authority.** Agent, tool, workflow, memory store, prompt, schema, and database terms remain architecture or implementation mappings unless separately admitted into the Core.
5. **Add conformance evidence.** Material semantic changes should include a valid or invalid fixture demonstrating the distinction.
6. **Preserve reconstructability.** Breaking semantic changes require compatibility notes and a new release record.

## Change classes

- **Editorial:** wording changes that do not alter meaning or boundaries.
- **Compatible extension:** adds a concept, relation, question, pattern, or fixture without changing existing meaning.
- **Boundary clarification:** narrows or makes explicit an existing distinction.
- **Breaking semantic change:** changes a definition, relation domain/range, boundary, lifecycle rule, or question obligation in a way that can reinterpret existing objects.

## Pull request expectations

A semantic change should identify:

- the question that requires it;
- the existing concept or boundary it affects;
- its derivation and non-equivalences;
- affected relations, patterns, and fixtures;
- compatibility and migration consequences;
- unresolved questions that remain.

Run the structural validator before review:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_pack.py
```
