# Repository shape

`CORE-SEMANTIC-PACK.md` presents the architectural specification. The repository materializes that specification into stable, referencable records.

## v0.1 serialization choices

- candidate primitives are grouped into one YAML catalog per semantic layer;
- typed relations are grouped in one relation catalog;
- anti-collapse boundaries are grouped in one boundary catalog;
- **each canonical semantic question is stored as one atomic contract**;
- each question is stored beneath its one primary taxonomy-only family;
- reusable composites are stored as patterns;
- concrete Domain Packs, Regime Packs, and Execution Contracts are not included.

Stable record IDs—not file paths—carry semantic identity. A later release may reorganize files without changing meaning if IDs, definitions, boundaries, obligations, and compatibility declarations remain intact.

## Question structure

```text
questions/
├── index.yaml
└── families/
    └── <family>/
        ├── family.yaml
        └── <atomic-question>.yaml
```

The family is a discovery view. Each question file is its complete atomic Semantic Question Contract and is the semantic unit of resolution.

A question has exactly one primary family. Another family may reference its canonical question through `related_questions` without duplicating the contract or inheriting requirements.

## Review consequence

Catalog grouping is a storage choice. Semantic changes must still be reviewed at record level. Editing a catalog or taxonomy does not authorize changes to unrelated semantic records.
