# Core Semantic Pack — Regimes Supplement

**Status:** Working reference supplement / non-canonical  
**Scope:** Runtime-neutral  
**Purpose:** Integrate the System Momentum Canon Regime system into the Core Semantic Pack

---

## 1. Supersession notice

This supplement supersedes every passage in `CORE-SEMANTIC-PACK.md` that treats a `Regime Pack` as an
independently authored composition layer.

In particular, the following earlier model is withdrawn:

```text
Core Semantic Pack
+ Domain Semantic Pack
+ Regime Pack
+ Execution Contract
= Resolved Semantic Pack
```

The corrected model is:

```text
Core Semantic Pack
  includes:
  - Regime
  - Open
  - Disciplined
  - Adversarial
  - High-Assurance
  - Locked
  - Regime evaluation rules
  - Regime switching rules

Domain Semantic Pack(s)
  independently extend subject-matter meaning
  while remaining Core-compatible

Execution Contract
  selects and applies Core Regime(s)
  for a concrete Process

Core + Domain Pack(s) + Execution Contract + Regime selection
  -> Resolved Semantic Pack
```

A Regime is not downstream domain content. It is part of the common epistemic substrate that allows an
unbounded number of Domain Packs to remain interoperable.

---

## 2. Canonical basis

The System Momentum Canon defines a Regime as:

> A canonical constraint framework that defines how claims may be accepted, evaluated, contested, and
> invalidated under different conditions.

The Canon also establishes three negative boundaries:

```text
Regime does not redefine meaning.
Regime does not execute actions.
Regime does not prescribe lived practice.
```

The authority separation is therefore:

```text
KSA
  -> meaning

Regime
  -> admissibility and validity constraints

Execution Contract
  -> legitimate execution conditions

Runtime
  -> execution
```

The canonical source set used by this supplement is:

```text
system-momentum-canon/core/authority/regimes.md
system-momentum-canon/core/authority/validity.md
system-momentum-canon/core/authority/interpretation.md
system-momentum-canon/core/authority/ksa.md
system-momentum-canon/core/02-MINDFRAME.md
```

Actor Regimes (`Human-final`, `Hybrid`, `Agent-final`) and descriptive organizational or civilizational
epistemic regimes are doctrine-layer constructs. They are not members of the Core validity Regime set.

---

## 3. Core Regime set

The Core carries the five Regimes named by the Canon.

### Open

Broad claim types, low inclusion barriers, and high tolerance for uncertainty. Used when exploration matters
more than stability.

### Disciplined

Explicit provenance and minimum Evidence requirements. The default when a system must remain coherent.

### Adversarial

Active contradiction pressure, dispute handling, and contradiction tracking. Used when contested Claims are
expected.

### High-Assurance

Strict admissibility, strong Evidence requirements, and explicit evaluation trails. Used for high-stakes
downstream decisions.

### Locked

Tightly controlled admission and explicitly governed semantic or validity change. Used for canonical
baselines and long-lived public artifacts.

The Regime set is domain-independent. A patent, clinical observation, financial record, social Claim, or
future domain object may be evaluated under the same Regime contract after its domain concepts are mapped to
the Core epistemic model.

---

## 4. Regime record contract

The Canon requires every Regime to define:

```text
Claim classes
Evidence classes
Evaluation rules
Invalidation rules
Escalation rules
```

The machine-readable Regime records therefore use exactly those five matrix sections.

Every Claim evaluated under a Regime must retain enough context to reconstruct:

```text
Statement
Provenance
Semantic context
Regime context
Support set
Contradiction set
Validity outcome
Assertion time
Evaluation time
```

Canonical validity outcomes are retained as:

```text
maintained
contested
invalidated
retired
```

Invalidation is never deletion. Historical referability and the invalidation trail remain.

---

## 5. Authority of the enumerative matrices

The five Regime identities, the canonical summaries, the required matrix components, switching rules, and
validity invariants derive from the current Canon.

The detailed enumerations inside each matrix are different:

> They are exploratory derivation candidates reconstructed from the February 2026 Regime work.

They are included because an implementable Core Pack needs concrete candidate rules that can be tested,
contested, and compared. Their inclusion does not claim that the same enumerations already exist in the
Canon.

The expected upstream path is:

```text
February exploration
  -> Core Pack machine-readable candidate
  -> cross-domain and conformance testing
  -> Canon gap review
  -> explicit Canon amendment, revision, or rejection
```

The Core Pack therefore preserves two statuses simultaneously:

```text
Regime identity and canonical summary
  -> Canon-derived

Detailed per-Regime matrix
  -> exploratory candidate for Canon review
```

---

## 6. Domain Pack boundary

A Domain Pack may:

- define domain concepts;
- specialize `Claim`, `Evidence`, `Observation`, `Finding`, and other Core concepts;
- map domain Evidence classes to `Evidence`;
- declare which Core Regimes it supports;
- impose domain-specific Evidence requirements that are stricter than the selected Regime;
- provide examples and domain conformance cases.

A Domain Pack must not:

- define a sixth Core Regime;
- rename a local policy profile as a Core Regime;
- weaken a Core Regime;
- make `Inference` become `Evidence`;
- make `Projection` become `State`;
- treat domain authority as epistemic validity;
- erase Regime identity from persisted objects.

Domain specialization is open-ended. Regime semantics are not.

---

## 7. Execution Contract boundary

An Execution Contract may:

- select one primary Core Regime;
- select additional Regimes for explicit comparative evaluation;
- declare switching and escalation triggers;
- bind stricter process conditions;
- require human or institutional Review;
- require Authority before Admission, Binding, or ExternalEffect.

An Execution Contract must not:

- author Regime definitions;
- reinterpret a selected Regime;
- treat successful execution as a validity outcome;
- silently switch Regime because a preferred conclusion failed;
- collapse Review into Binding.

The distinction is:

```text
Regime
  -> How may this Claim be evaluated?

Execution Contract
  -> Under which conditions may this Process execute here?
```

---

## 8. Regime switching

Regime switching is always explicit.

A switch retains:

```text
from Regime
to Regime
reason
affected Claims or Evaluations
initiating Actor
Authority reference where required
semantic version
time
prior validity outcomes
new evaluation scope
```

Comparative evaluation is not automatically switching.

A Claim may be evaluated under both `Disciplined` and `Adversarial`, producing different outcomes. Both
outcomes remain referable:

```text
Disciplined -> maintained
Adversarial -> contested
```

Neither overwrites the other.

A Projection may display both. It must not average or collapse them into regime-less truth.

---

## 9. Corrected composition model

```text
                    CORE SEMANTIC PACK

    semantic concepts
    epistemic concepts
    teleological concepts
    agency and governance concepts
    Core Regimes
    regime switching and validity discipline
    extension and conformance contracts
                         |
                         | Core compatibility
          +--------------+--------------+
          |                             |
    Domain Pack A                  Domain Pack N
    independently authored         independently authored
          \                             /
           \                           /
            +--- selected by Context --+
                         |
                 Execution Contract
                         |
             primary/comparative Regime
                         |
                         v
                Resolved Semantic Pack
                         |
                         v
                      Runtime
```

A resolved pack records a Regime binding, not a `Regime Pack` component.

---

## 10. Conformance invariants

The Regime subsystem requires:

```text
Regime != Context
Regime != Validity
Regime != Authority
Regime != ExecutionContract

Regime does not redefine meaning.
Regime switching is explicit.
Validity is Regime-scoped.
Domain compatibility is not Regime definition.
Projection preserves Regime context.
Cross-Regime outcomes do not overwrite one another.
```

The dedicated validator is:

```bash
python scripts/validate_regimes.py
```

The general pack validator remains:

```bash
python scripts/validate_pack.py
```

---

## 11. Working conclusion

The Core Semantic Pack is not the parent repository of every possible Domain Pack.

It is the common semantic and epistemic interoperability contract those independently authored packs extend.

Regimes are part of that contract because they prevent unlimited domain extension from becoming unlimited
epistemological fragmentation.
