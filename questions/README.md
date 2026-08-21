# Questions

The Core Semantic Pack treats **answerability** as an architectural property.

The atomic unit is a **Semantic Question Contract**:

```text
one canonical question
    ↓
required semantic distinctions
    ↓
required concepts + relations + boundaries
    ↓
minimum answer requirements
    ↓
failure semantics
```

Each file under [`contracts/`](contracts/) defines exactly one canonical question. A contract is independently resolvable and does not inherit semantic requirements from a family.

## Families are taxonomy, not authority

Files under [`families/`](families/) are classification and discovery views. They group related questions but do not define requirements.

A question may belong to more than one family. For example, `core.question.detect-goal-change` is primarily teleological but is also relevant to reflection, governance, and memory. Its requirements still live in one atomic contract.

Family membership therefore answers:

> Which semantic responsibility domains is this question relevant to?

The atomic contract answers:

> What must remain semantically available for this exact question to be answered?

## Resolution

A consumer should request question IDs, not whole families, when it knows the questions it needs:

```yaml
questions:
  - core.question.explain-action-purpose
  - core.question.identify-supporting-evidence
```

A resolver computes the union of the explicit requirements of those contracts and then composes the applicable Domain Pack, Regime Pack, and Execution Contract.

Family-level resolution is allowed only as an explicit convenience expansion into member question IDs.

See [`docs/question-contract-model.md`](../docs/question-contract-model.md).
