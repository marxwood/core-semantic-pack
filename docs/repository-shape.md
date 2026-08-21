# Repository shape

`CORE-SEMANTIC-PACK.md` presents the architectural specification. The repository materializes that specification into stable, referencable records.

## v0.1 serialization choices

- **one referencable semantic object is stored in one file**;
- each candidate primitive is stored beneath its semantic layer;
- each typed Relation is stored in one flat Relation file;
- each anti-collapse Boundary is stored in one flat Boundary file;
- each canonical semantic Question is stored as one atomic contract;
- each question is stored beneath its one primary taxonomy-only family;
- reusable composites are stored as patterns;
- concrete Domain Packs, Regime Packs, and Execution Contracts are not included.

The three repository responsibilities remain distinct:

```text
Stable ID                    = registry identity
Canonical semantic reference = authoring and inspection language
File path                    = serialization location
```

Physical paths never become semantic identity. A later release may reorganize files without changing meaning if IDs, definitions, boundaries, obligations, and compatibility declarations remain intact.

## Atomic object structure

```text
concepts/<layer>/<concept>.yaml
relations/<relation>.yaml
boundaries/<boundary>.yaml
questions/<family>/<question>.yaml
```

`concepts/index.yaml`, `relations/index.yaml`, `boundaries/index.yaml`, and `questions/index.yaml` are lookup bridges. They contain registry/navigation metadata rather than complete semantic definitions. Question `family.yaml` files are the explicit taxonomy-view exception.

Question family directories live directly under `questions/`. The former `questions/families/` wrapper carried no semantic information and must not be reintroduced.

## Question structure

```text
questions/
├── index.yaml
├── migration-v0.1.yaml
└── <family>/
    ├── family.yaml
    └── <atomic-question>.yaml
```

The family is a discovery view. Each question file is its complete atomic Semantic Question Contract and is the semantic unit of resolution.

A question has exactly one primary family. Another family may reference its canonical question through `related_questions` without duplicating the contract or inheriting requirements.

## Review consequence

File organization is a storage choice. Semantic changes must still be reviewed at record level. Editing an index or taxonomy does not authorize changes to unrelated semantic records.
