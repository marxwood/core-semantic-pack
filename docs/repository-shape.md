# Repository shape

`CORE-SEMANTIC-PACK.md` presents the architectural specification. The repository materializes that specification into stable, referencable records.

## Governed semantic source

Core semantic definitions and governance rules live under `semantic/`. Portable contracts that determine whether a consumer may claim governance by those definitions live under `semantic-contracts/`:

```text
semantic/             governed semantic definitions and semantic governance rules
semantic-contracts/   portable semantic adoption and interaction contracts
mappings/   non-authoritative external and runtime mappings
examples/   illustrative uses
docs/       explanatory documentation
scripts/    validation and tooling
release/    packaging and version metadata
```

This boundary does not make every file under `semantic/` a Core primitive. Patterns, lifecycle rules, reference-only terms, Question families, composition rules, conformance rules, and fixtures retain their distinct roles.

## v0.1 serialization choices

- **one referencable semantic object is stored in one file**;
- each candidate primitive is stored beneath its semantic layer;
- each typed Relation is stored in one flat Relation file;
- each anti-collapse Boundary is stored in one flat Boundary file;
- each canonical semantic Question is stored as one atomic contract;
- each Semantic Handshake is stored as one ordered, runtime-neutral contract;
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

`semantic-contracts/` does not contain vendor prompts, runtime code, or concrete environment policy. It contains portable contracts. Model- or vendor-specific invocation surfaces remain non-authoritative mappings or examples.

## Atomic object structure

```text
semantic/concepts/<layer>/<concept>.yaml
semantic/relations/<relation>.yaml
semantic/boundaries/<boundary>.yaml
semantic/questions/<family>/<question>.yaml
semantic-contracts/handshakes/H<number>-<handshake>-contract.yaml
```

`semantic/concepts/index.yaml`, `semantic/relations/index.yaml`, `semantic/boundaries/index.yaml`, and `semantic/questions/index.yaml` are lookup bridges. They contain registry/navigation metadata rather than complete semantic definitions. Question `family.yaml` files are the explicit taxonomy-view exception.

Question family directories live directly under `semantic/questions/`. The former `semantic/questions/families/` wrapper carried no semantic information and must not be reintroduced.

## Question structure

```text
semantic/questions/
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
