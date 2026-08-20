
# Repository shape

`CORE-SEMANTIC-PACK.md` presents a proposed conceptual structure. The v0.1 repository materializes that structure using reviewable family catalogs rather than one file per semantic record.

## v0.1 serialization choices

- candidate primitives are grouped into one YAML catalog per semantic layer;
- typed relations are grouped in one relation catalog;
- anti-collapse boundaries are grouped in one boundary catalog;
- each question family is stored as one question-contract file;
- reusable composites are stored as patterns;
- concrete Domain Packs, Regime Packs, and Execution Contracts are not included.

This is a serialization choice, not a change in semantic authority.

Stable record IDs—not file paths—identify concepts, relations, boundaries, questions, patterns, and rules. A later release may split a catalog into individual files without changing meaning, provided IDs, definitions, boundaries, and compatibility declarations remain intact.

## Why question contracts live under `questions/`

The specification describes `contracts/question-contracts/` as a possible structure. v0.1 stores these records directly under `questions/` because each file is already a Semantic Question Contract and no second contract hierarchy is yet required.

Concrete Execution Contracts remain outside this repository. The Core contains only the `core.pattern.execution-contract` composite and the vocabulary needed to express such contracts.

## Review consequence

Catalog grouping makes the first semantic baseline reviewable as a coherent model. Future changes should still be evaluated at record level and must not treat editing one catalog file as authority to alter unrelated records.
