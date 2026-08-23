# Core Semantic Pack v0.1

**Status:** Working reference specification / non-canonical
**Scope:** Runtime-neutral
**Purpose:** Minimal, stable semantic kernel for human-agentic systems

---

## 1. Definition

The **Core Semantic Pack** is the minimal, stable, non-domain-specific and non-runtime-specific semantic kernel from which more concrete semantic environments may be composed.

It provides the concepts, relations, boundaries, questions, obligations, Regimes, and conformance rules required for a system to:

- distinguish reality from its representations;
- preserve State and StateChange;
- reason without collapsing Claims into truth;
- maintain Provenance across transformations;
- connect Action to Intent, Goal, and DesiredState;
- distinguish Capability from Authority;
- preserve the difference between Validation, Admission, Review, and Binding;
- evaluate Claims under explicit Regimes;
- preserve Regime-specific Validity across switching and comparison;
- maintain semantically typed institutional memory;
- detect drift and semantic status collapse;
- remain correction-capable as autonomy increases.

The Core Semantic Pack is **not**:

- a universal ontology of everything;
- the Canon;
- a prompt;
- an agent configuration;
- a workflow engine;
- an orchestration graph;
- a database schema;
- a runtime SDK;
- a tool registry;
- a domain model;
- a collection of convenient output types.

`Core` is intentional.

It means:

> the smallest reusable semantic and epistemic interoperability kernel over which domain meaning and execution constraints may be composed without semantic drift.

It does **not** claim that the Core is complete, final, or sufficient for every system.

## 1.1 Canonical semantic notation

Core contracts use canonical semantic references as their primary authoring and inspection language. Stable IDs remain registry identity for versioning, migration, compatibility, and historical reconstruction.

```text
Concept
    core.desired-state
    ↔ DesiredState

Relation
    core.rel.authorized-by
    ↔ authorizedBy

Boundary
    core.boundary.action-not-intent
    ↔ Action != Intent

Question
    core.question.explain-action-purpose
    ↔ Why is this being done?

Regime
    core.regime.disciplined
    ↔ Disciplined
```

There is no separate human-label or question-slug semantic layer in v0.1. Paths and filenames are serialization details. Reference-only categories such as `Truth` and `ExecutionPlan` are explicitly registered without becoming Core primitives; `Any` is reserved wildcard meta-notation.

---

# 2. Position in the architecture

The Semantic Reference Model and the Core Semantic Pack are not two successive ontology layers.

The Semantic Reference Model is the design and reference surface from which stable consumer semantics are released. The Core Semantic Pack is the versioned distribution artifact of the stable shared kernel.

```text
                    SEMANTIC FOUNDATION

System Momentum Canon
        ↓
structural invariants
        ↓
Mindframe
        ↓
operative semantic distinctions
        ↓
Semantic Reference Model
        │
        │ stable release / packaging
        ▼
┌───────────────────────────────┐
│ Core Semantic Pack            │
│                               │
│ Core concepts                 │
│ Core relations                │
│ Core boundaries               │
│ Core questions                │
│ Core Regimes                  │
│ Core conformance              │
│ extension contracts           │
└───────────────────────────────┘
        ▲
        │ Core compatibility
        │
┌───────┴──────────┐     ┌────────────────────┐
│ Domain Pack A    │ ... │ Domain Pack N      │
│ independently    │     │ independently      │
│ authored         │     │ authored           │
└───────┬──────────┘     └──────────┬─────────┘
        └──────────────┬────────────┘
                       │
                Execution Contract
                       │
              selects Core Regime(s)
                       │
                       ▼
              Resolved Semantic Pack
                       │
                       ▼
                 Runtime Adapters
                       │
                       ▼
        Agents / Tools / Models / Memory / APIs
```

The layers and dimensions have different responsibilities.

### Canon

Defines structural invariants.

### Mindframe

Makes those invariants operable in contact with perception, reasoning, interpretation, memory, authority, and action.

### Semantic Reference Model

Provides the runtime-neutral design and reference language: concepts, relations, boundaries, derivations, candidate structures, and architectural reasoning.

### Core Semantic Pack

Packages the stable shared semantic kernel, including the Canon-derived Regime system, as a versioned consumer-facing artifact.

### Domain Packs

Are independently authored Core-compatible extensions of subject-matter meaning. They may specialize and restrict Core meaning within a declared domain, but they do not sit under the authority or release process of the Core Pack.

### Execution Contracts

Bind a Process to conditions under which its execution is semantically legitimate and select the applicable Core Regime or Regimes.

### Runtime

Realizes the resulting semantics through concrete implementation mechanisms.

The implementation may change.

The semantic distinctions and Regime context must survive.

---

# 3. Core architectural principle: systems operate by answering questions

The architecture is not fundamentally organized around objects.

It is organized around **questions that must remain answerable**.

A semantic concept exists because some distinction must survive in order for an important question to have a truthful answer.

For example:

```text
State
→ What is currently maintained as reality?

Projection
→ How is that State being represented?

Provenance
→ Where did this object come from?

Claim
→ What is being asserted?

Evidence
→ What supports or contradicts the Claim?

Regime
→ Under which epistemic constraints is the Claim being evaluated?

Goal
→ Why is a direction of change being pursued?

DesiredState
→ What future State would constitute progress?

Intent
→ What is the Actor trying to accomplish now?

Action
→ What transformation is being attempted?

Authority
→ What legitimizes that Action?

StateChange
→ What actually changed?

Reflection
→ Are we still moving toward what was intended?
```

Therefore:

```text
Question
    ↓
required semantic distinctions
    ↓
Semantic Contract
    ↓
required concepts + relations + boundaries
    ↓
architectural responsibility
    ↓
runtime realization
```

A component is semantically meaningful when it assumes responsibility for preserving enough structure to answer a declared class of questions.

---

# 4. Semantic Question Contract

A **Semantic Question Contract** declares:

1. which question must remain answerable;
2. which semantic concepts are required;
3. which relations must survive;
4. which distinctions must not collapse;
5. what constitutes an incomplete or invalid answer;
6. which consequences are permitted when the answer cannot be established.

Example:

```yaml
id: core.question.explain-action-purpose
version: 0.1.0
status: experimental
kind: semantic-question-contract

canonical_question: Why is this being done?
family: teleological

requires:
  concepts:
    - Action
    - Intent
    - Goal
    - DesiredState
    - Authority
    - Context
  relations:
    - realizes
    - advances
    - specifies
    - authorizedBy
    - existsIn

must_preserve:
  - Action != Intent
  - Intent != Goal
  - Intent != Authority
  - Capability != Authority

answer_contract:
  minimum_requirements:
    - action_identified
    - intent_identified
    - goal_identified
    - desired_state_identified
    - authority_traceable

failure_contract:
  failure_states:
    - unresolved_intent
    - unresolved_goal
    - missing_desired_state
    - unresolved_authority
  consequence_on_failure:
    answer_status: unresolved
    material_consequence: external-effect-forbidden-until-resolved
```

The serialization is secondary.

The semantic obligation is primary.

---

# 5. Core question set

The first Core Semantic Pack should preserve the ability to answer at least nine families of questions.

---

## 5.1 Ontological questions

```text
What is this?

What kind of thing is it?

Which identity does it have?

Where are its boundaries?

To what is it related?

In which Context does this meaning apply?
```

Primary concepts:

```text
Entity
Identity
Type
Context
Boundary
Relation
```

---

## 5.2 State questions

```text
What is currently the case?

What State is maintained?

What existed before?

What exists now?

What changed?

What State is expected next?
```

Primary concepts:

```text
State
StateChange
PreviousState
CurrentState
ExpectedState
```

A system must distinguish between a representation of State and maintained State itself.

---

## 5.3 Epistemic questions

```text
What was observed?

What is being stated?

What is being claimed?

What supports the Claim?

What contradicts it?

What was inferred?

What Finding was derived?

How uncertain is it?

Under which Regime is this Claim being evaluated?

Under which Regime and semantic Context is it considered valid?

Has the Regime changed?

Would the Validity outcome differ under another Regime?
```

Primary concepts:

```text
Source
Observation
Statement
Claim
Evidence
Inference
Finding
Provenance
Support
Contradiction
Uncertainty
Validity
Contestation
Regime
```

Critical rules:

```text
Claim is not truth.

Validity is Regime-scoped.
```

---

## 5.4 Interpretive questions

```text
Which interpretation of reality produced this conclusion?

Which representation are we looking at?

Which Source or State does it derive from?

Which Context shaped the interpretation?

Which Regime governed the evaluated Claim?

Has a Projection silently become accepted as State?

Has a Regime been silently switched to produce a preferred result?
```

Primary concepts:

```text
Interpretation
Projection
Source
Context
Derivative
Provenance
Regime
```

Critical invariants:

```text
Projection != State

Regime switching must be explicit.
```

Interpretation is unavoidable.

Unmarked interpretation is dangerous.

---

## 5.5 Teleological questions

```text
Why is this being done?

Which Goal is being pursued?

Which DesiredState does that Goal imply?

Which direction of change follows from it?

Which Intent operationalizes the Goal here?

Is the resulting StateChange advancing the DesiredState?

Has the Goal changed?
```

Primary concepts:

```text
Goal
DesiredState
Intent
Direction
Trajectory
Progress
```

Teleology is a first-class semantic concern.

It must not remain hidden inside prompts, task descriptions, management assumptions, or agent context.

---

## 5.6 Agency questions

```text
Who or what is acting?

Which Role is being occupied?

What can the Actor do?

Which Action is being attempted?

Which Process does it participate in?

Which Transformation is being performed?
```

Primary concepts:

```text
Actor
Role
Capability
Action
Process
Transformation
```

Critical invariant:

```text
Capability != Authority
```

The ability to perform an Action does not legitimize that Action.

---

## 5.7 Governance questions

```text
Who authorized this?

Under which Constraint?

What is permitted?

What may only be recommended?

What must be validated?

What may enter maintained State?

Which transition requires Review?

Which decision is Binding?

Can the commitment later be revoked?
```

Primary concepts:

```text
Authority
Constraint
Permission
Contract
Validation
Admission
Review
Binding
Commitment
Revocation
Accountability
```

Critical distinctions:

```text
Validation != Admission

Review != Binding

Capability != Authority
```

---

## 5.8 Memory questions

```text
What should the system remember?

What exactly is being remembered?

Was it an Observation, Claim, Evidence item, Inference, Finding,
Decision, Goal, or StateChange?

Under which semantic status was it admitted?

Under which Regime was its Validity evaluated?

Which Provenance does it retain?

What later contradicted or superseded it?

Is it still valid?

Under which version and Context was it valid?
```

Memory must therefore not be reduced to:

```text
Memory = stored text
```

Institutional memory is better understood as:

```text
Persistence
of semantically typed objects
+
relations
+
provenance
+
regime context
+
admission status
+
lifecycle
+
semantic version
```

`Memory` should therefore initially remain an architecture mapping over more fundamental concepts rather than becoming a Core primitive.

---

## 5.9 Reflective / corrective questions

```text
Has the Goal changed?

Is the Goal still authorized?

Has CurrentState changed materially?

Has our Interpretation changed?

Has the applicable Regime changed?

Would the maintained Claim survive evaluation under a stricter Regime?

Is the system still moving toward DesiredState?

Has new Evidence contradicted a maintained Finding?

Did an intermediate Inference silently become institutional truth?

Has a Projection become indistinguishable from State?

Has repeated downstream use created implicit Authority?

Should maintained State be revised?

Should a previous Binding be revoked?
```

Reflection is what makes the semantic system **correction-capable**.

It should initially compose existing primitives rather than introduce an independent ontology merely because reflection is a distinct system responsibility.

---

# 6. Core semantic layers

The v0.1 Core can be organized into six major semantic responsibility layers.

```text
┌──────────────────────────────────┐
│ 6. Reflection                    │
│ correction / drift / revision    │
├──────────────────────────────────┤
│ 5. Governance                    │
│ authority / admission / binding  │
├──────────────────────────────────┤
│ 4. Teleology                     │
│ goal / desired state / direction │
├──────────────────────────────────┤
│ 3. Agency                        │
│ process / action / transformation│
├──────────────────────────────────┤
│ 2. Epistemics                    │
│ claim / evidence / regimes       │
├──────────────────────────────────┤
│ 1. Foundations                   │
│ identity / context / state       │
└──────────────────────────────────┘
```

They are not isolated stacks.

They are responsibility domains within one semantic graph.

Interpretation crosses Foundations and Epistemics.

Regimes constrain epistemic evaluation without redefining semantic meaning.

Memory crosses State, Epistemics, Governance, and Persistence.

Reflection evaluates relationships across all layers.

---

# 7. Candidate Core primitives

The list below is a **candidate kernel**, not a final universal ontology.

Concepts should remain in Core only where cross-domain semantic stability justifies them.

---

## 7.1 Foundations

```text
Entity
Identity
Relation
Context
Boundary

State
StateChange

Source
Derivative
Projection
Interpretation

SemanticVersion
```

---

## 7.2 Epistemic

```text
Observation
Statement
Claim
Evidence
Inference
Finding

Provenance
Support
Contradiction
Uncertainty
Validity
Contestation
Regime
```

`Regime` is the Core concept under which the five Canon-derived Regime definitions are materialized.

---

## 7.3 Teleological

```text
Goal
DesiredState
Intent
Direction
Trajectory
Progress
```

---

## 7.4 Agency

```text
Actor
Role
Capability

Action
Process
Transformation

Transfer
Persistence
Composition
ExternalEffect
```

---

## 7.5 Governance

```text
Authority
Constraint
Permission
Contract

Validation
Admission
Review
Binding

Commitment
Revocation
Accountability
```

---

## 7.6 Reflection

Reflection should initially operate by composing existing primitives.

For example:

```text
Goal + CurrentState + DesiredState
    → trajectory assessment

Claim + Evidence + Contradiction + Regime
    → epistemic revision

Claim + Regime A + Regime B
    → comparative validity assessment

MaintainedState + new Evidence
    → StateChange candidate

Binding + Authority + changed Context
    → revocation assessment

Projection + Provenance + State
    → projection-collapse detection
```

A new primitive should not be created merely because a runtime performs a new operation.

---

# 8. The semantic spine

The most important part of the Core is not its list of nouns.

It is the graph of relations that preserves semantic continuity.

A minimal epistemic path:

```text
Source
  ↓ observedAs
Observation
  ↓ interpretedAs
Claim
  ↓ evaluatedUnder
Regime

Claim
  ↓ supportedBy / contradictedBy
Evidence
  ↓ contributesTo
Finding

Finding
  ↓ hasValidity
Validity
  ↓ scopedBy
Regime
```

A minimal teleological path:

```text
Goal
  ↓ specifies
DesiredState

Intent
  ↓ advances
Goal

Action
  ↓ realizes
Intent

Action
  ↓ participatesIn
Process

Action
  ↓ transforms
State

Action
  ↓ authorizedBy
Authority

State
  ↓ changedThrough
StateChange

StateChange
  ↓ evaluatedAgainst
DesiredState
```

Cross-cutting obligations:

```text
everything material
    → existsIn Context

everything derived
    → retains Provenance

everything epistemically evaluated
    → retains Regime context

everything authoritative
    → traces to Authority

everything persistent
    → has explicit Admission status

everything changeable
    → has lifecycle

everything revocable
    → retains revision history

everything version-sensitive
    → retains SemanticVersion
```

---

# 9. The teleological loop

Explicit teleology introduces a loop that purely execution-oriented architectures usually lack.

```text
CurrentState
      │
      │ difference
      ▼
DesiredState
      ▲
      │ specified by
     Goal
      │
      │ operationalized through
      ▼
    Intent
      │
      ▼
    Action
      │
      ▼
 StateChange
      │
      ▼
NewCurrentState
      │
      └──── assess progress ──────► DesiredState
```

The system must therefore preserve:

```text
CurrentState
DesiredState
Goal
Intent
Action
StateChange
ProgressAssessment
```

Without this loop, a system may optimize execution while silently losing the reason execution exists.

---

# 10. Goal is not DesiredState

These concepts must not collapse.

```text
Goal
=
an authorized objective that gives direction to action

DesiredState
=
a representation of a future State toward which the Goal points
```

Example:

```text
Goal:
Reduce customer churn.

DesiredState:
Annual churn < 5%
while preserving customer satisfaction >= X.
```

Therefore:

```text
Goal != DesiredState

DesiredState != Prediction

DesiredState != Plan

Goal != Intent

Intent != Action

Action != StateChange
```

A Goal supplies normative direction.

DesiredState allows that direction to become inspectable against reality.

---

# 11. Direction and Trajectory

Explicit teleology makes two further concepts useful.

## Direction

The qualitative orientation implied by the relationship between CurrentState and DesiredState.

```text
CurrentState → DesiredState
```

## Trajectory

An observed or proposed sequence of StateChanges over time.

```text
S0 → S1 → S2 → S3
```

This allows a system to ask:

> Is the system still moving toward the intended State?

rather than only:

> Did the last Action execute successfully?

This distinction is fundamental.

```text
OperationalSuccess != Progress
```

A technically successful Action may move the system away from DesiredState.

---

# 12. Process and the Execution Semantics Stack

`Process` belongs to Core.

`Workflow` does not belong to the fundamental semantic layer.

The distinction is:

```text
Process
=
ontology / logic of change

Execution Contract
=
conditions under which realization of that Process
is semantically legitimate

Execution Plan
=
optional concrete materialization of an allowed execution path

Runtime
=
actual realization

StateChange
=
what changed in reality
```

The resulting stack is:

```text
Process
   ↓
Execution Contract
   ↓
Execution Plan
   ↓
Runtime
   ↓
StateChange
```

---

## 12.1 Process

A **Process** is an abstract structure of transformation.

Conceptually:

```text
Process =
  allowed transformations
  + causal relations
  + state transition logic
  + invariants
```

At Core level, Process does not by itself determine:

- who executes it;
- whether execution is currently authorized;
- which concrete orchestration engine is used;
- which agent performs a step;
- which API is called;
- which runtime bindings exist.

Process describes the semantics of change.

---

## 12.2 Execution Contract

An **Execution Contract** binds Process semantics to a concrete context of permitted execution.

Conceptually:

```text
Execution Contract =
  Process reference
  + execution constraints
  + ordering constraints where semantically relevant
  + authority conditions
  + validity conditions
  + Regime selection
  + context binding
  + admissibility
  + gates / checkpoints
```

Its central question is not:

> How does the runtime execute this?

but:

> Under which conditions is this execution semantically allowed?

Execution Contract therefore belongs to the **semantic-governance bridge** between Core Process semantics and runtime realization.

It may select applicable Core Regimes.

It does not define Regime semantics.

---

## 12.3 Execution Plan

An Execution Plan is an optional concrete realization of an Execution Contract.

It may contain:

```text
step ordering
dependency graph
specific agents
specific tools
runtime bindings
retry behavior
orchestration details
```

These details are not automatically Core semantics.

---

## 12.4 Workflow

`Workflow` may remain a useful runtime or architecture term.

For example:

```text
Temporal workflow
Airflow DAG
agent orchestration workflow
business workflow
UI flow
```

But it should not become the fundamental semantic concept responsible for execution legitimacy.

```text
Workflow
=
possible runtime representation

Execution Contract
=
semantic conditions of legitimate execution
```

These are different ontological responsibilities.

---

# 13. Institutional memory

The Core should not define institutional memory as a text store, embedding store, conversation log, or graph technology.

Instead:

```text
Institutional Memory
=
persistent semantic continuity
```

A remembered object should preserve enough structure to answer:

```text
What kind of object was this?

Where did it come from?

Which Context produced its meaning?

Which Regime governed its Validity?

Was it admitted?

Was it provisional or maintained?

What supported it?

What contradicted it?

Which version interpreted it?

What superseded or revoked it?

Is it still valid now?
```

Thus architecture concepts such as:

```text
vector memory
graph memory
conversation memory
long-term memory
knowledge base
agent memory
```

are implementation mappings.

The Core semantics beneath them are expressed through:

```text
State
Persistence
Admission
Provenance
Context
Regime
SemanticVersion
Validity
Contestation
StateChange
```

---

# 14. Institutional self-delusion as semantic failure

A correction-capable system must detect the case where interpretation gradually acquires authority without an explicit transition.

Example:

```text
Inference
    ↓ persisted without status
Memory record
    ↓ reused downstream
Agent context
    ↓ treated as established
Claim
    ↓ repeatedly propagated
Institutional assumption
    ↓ used for Action
```

No new Evidence may have appeared.

No Admission may have occurred.

No Regime-governed Validity evaluation may have occurred.

No Authority may have made the object binding.

Yet downstream systems now behave as though the original Inference were established State.

This is a semantic failure.

General class:

```text
SEMANTIC_STATUS_COLLAPSE
```

Specific invalid transition:

```text
Inference
    ↓
MaintainedState

without Admission
```

Persistence must never manufacture authority.

Repetition must never manufacture validity.

Regime omission must never manufacture universal validity.

---

# 15. Core anti-collapse boundaries

The Core should ship with explicit boundaries preventing common semantic category collapses.

```text
Source != Projection

Observation != Claim

Claim != Evidence

Evidence != Truth

Inference != Finding

Finding != BindingDecision

Projection != State

Validation != Admission

Review != Binding

Capability != Authority

Persistence != Admission

Repetition != Validation

Goal != DesiredState

DesiredState != Prediction

DesiredState != Plan

Intent != Goal

Intent != Authority

Action != Intent

Action != StateChange

Process != ExecutionContract

ExecutionContract != ExecutionPlan

ExecutionPlan != Runtime

OperationalSuccess != Progress

Regime != Context

Regime != Validity

Regime != Authority

Regime != ExecutionContract
```

Additional Regime invariants are not simple type non-equivalences but remain normative Core constraints:

```text
validUnder(RegimeA) != validUnder(RegimeB)

Domain compatibility != Regime definition

Regime switch != implicit reinterpretation

Regime-specific validity != universal truth
```

These boundaries are not documentation trivia.

They are semantic safety properties.

---

# 16. Semantic object envelope

Every material semantic object should be capable of carrying a minimal common envelope.

Example:

```yaml
semantic:
  type: Claim
  version: semantic.claim@0.1

identity:
  id: claim:84729

context:
  id: context:customer-retention-2026

regime_context:
  regime: core.regime.disciplined
  version: 0.1.0

provenance:
  produced_by: inference:182
  derived_from:
    - evidence:281
    - evidence:292

validity:
  outcome: maintained
  evaluated_under: core.regime.disciplined
  evaluated_at: 2026-08-20T00:00:00Z

status:
  epistemic: supported
  admission: admitted
  authority: non-binding

lifecycle:
  created_at: 2026-08-20T00:00:00Z
  supersedes: null
  revoked_by: null
```

Not every object requires every field.

But missing semantics must not be silently fabricated.

```text
Unknown
```

is acceptable.

```text
Implicit authority
Implicit Regime
Regime-less universal validity
```

are not.

---

# 17. Proposed Core Semantic Pack structure

```text
core-semantic-pack/
│
├── pack.yaml
├── CORE-SEMANTIC-PACK.md
│
├── semantic/
│   ├── questions/
│   │   ├── index.yaml
│   │   ├── migration-v0.1.yaml
│   │   ├── ontological/
│   │   ├── state/
│   │   ├── epistemic/
│   │   ├── interpretive/
│   │   ├── teleological/
│   │   ├── agency/
│   │   ├── governance/
│   │   ├── memory/
│   │   └── reflective/
│   │
│   ├── concepts/
│   │   ├── foundations/
│   │   ├── epistemic/
│   │   │   ├── regime.yaml
│   │   │   └── regimes/
│   │   │       ├── index.yaml
│   │   │       ├── R1-open.yaml
│   │   │       ├── R2-disciplined.yaml
│   │   │       ├── R3-adversarial.yaml
│   │   │       ├── R4-high-assurance.yaml
│   │   │       ├── R5-locked.yaml
│   │   │       ├── contracts/
│   │   │       │   ├── evaluation-contract.yaml
│   │   │       │   ├── switching-contract.yaml
│   │   │       │   └── conformance-contract.yaml
│   │   │       └── fixtures/
│   │   ├── teleological/
│   │   ├── agency/
│   │   └── governance/
│   │
│   ├── relations/
│   ├── boundaries/
│   ├── references/
│   ├── lifecycle/
│   ├── composition/
│   └── conformance/
│
├── mappings/
│   └── generic-agentic/
│
├── examples/
├── docs/
├── scripts/
└── release/
```

Domain concepts, runtime-specific artifacts, and concrete Execution Contracts do not belong inside the Core simply because they consume it.

Core Regime definitions do belong inside the Core because they define the shared epistemic conditions under which arbitrary domain Claims can remain interoperable.

---

# 18. Core manifest

```yaml
id: semantic-pack.core
version: 0.1.0
status: experimental

authority:
  level: reference-model

derived_from:
  canon: system-momentum
  mindframe: 0.x

scope:
  domain_neutral: true
  runtime_neutral: true
  execution_specific: false

provides:
  question_families:
    - ontological
    - state
    - epistemic
    - interpretive
    - teleological
    - agency
    - governance
    - memory
    - reflective

  semantic_layers:
    - foundations
    - epistemic
    - teleological
    - agency
    - governance
    - reflection

  regimes:
    - Open
    - Disciplined
    - Adversarial
    - High-Assurance
    - Locked

guarantees:
  - provenance_preservation
  - projection_state_separation
  - capability_authority_separation
  - validation_admission_separation
  - review_binding_separation
  - persistence_admission_separation
  - explicit_state_change
  - explicit_goal_relation
  - desired_state_traceability
  - process_execution_separation
  - explicit_regime_switching
  - regime_scoped_validity
  - domain_regime_non_redefinition
  - revocability
  - question_answerability

composition:
  extensible: true
  redefinable: false
  external_regime_pack: false
```

The exact serialization is not authoritative.

The declared semantic responsibility is.

---

# 19. Canonical Regimes

Regimes are part of the Core Semantic Pack.

They are not an independently authored extension dimension parallel to Domain Packs.

They exist precisely because Domain Packs are open-ended and unpredictable: the system requires a stable cross-domain epistemic discipline that does not depend on knowing every possible future domain.

---

## 19.1 Canonical basis

The System Momentum Canon defines a **Regime** as a canonical constraint framework that determines how Claims may be accepted, evaluated, contested, and invalidated under different conditions.

The Canon establishes three negative boundaries:

```text
Regime does not redefine meaning.
Regime does not execute actions.
Regime does not prescribe lived practice.
```

The authority separation is therefore:

```text
KSA
  → meaning

Regime
  → admissibility and validity constraints

Execution Contract
  → legitimate execution conditions

Runtime
  → execution
```

The canonical source set for the v0.1 Regime materialization is:

```text
system-momentum-canon/core/authority/regimes.md
system-momentum-canon/core/authority/validity.md
system-momentum-canon/core/authority/interpretation.md
system-momentum-canon/core/authority/ksa.md
system-momentum-canon/core/02-MINDFRAME.md
```

Actor Regimes such as `Human-final`, `Hybrid`, and `Agent-final`, and descriptive organizational or civilizational epistemic regimes, belong to doctrine-level models. They are not members of this Core validity Regime set.

---

## 19.2 Core Regime set

The Core carries the five Regimes named by the Canon, ordered from lower-constraint to higher-constraint validity handling.

### R1 — Open

Broad Claim types, low inclusion barriers, and high tolerance for uncertainty.

Use when exploration matters more than stability.

### R2 — Disciplined

Explicit Provenance and minimum Evidence requirements.

Default when a system must remain coherent.

### R3 — Adversarial

Active contradiction pressure, dispute handling, and contradiction tracking are first-class.

Use when contested Claims are expected.

### R4 — High-Assurance

Strict admissibility, strong Evidence requirements, and explicit evaluation trails.

Use for high-stakes downstream decisions.

### R5 — Locked

Tightly controlled Admission; semantic and Validity changes require explicit governance.

Use for canonical baselines and long-lived public artifacts.

The Regime set is domain-independent.

A patent, protein, contract, financial record, political Claim, or future domain object may be evaluated under the same Regime contract after its domain semantics are mapped to the Core epistemic model.

---

## 19.3 Regime record contract

The Canon requires every Regime to define:

```text
Claim classes
Evidence classes
Evaluation rules
Invalidation rules
Escalation rules
```

The machine-readable Regime definitions therefore use exactly those five matrix sections.

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

Invalidation is never deletion.

Historical referability and the invalidation trail remain.

---

## 19.4 Authority of the enumerative matrices

Two authority statuses must remain explicit.

```text
Regime identity + canonical summary
  → Canon-derived

Detailed per-Regime matrix
  → exploratory derivation candidate
```

The five Regime identities, their canonical summaries, the required matrix components, switching rules, and Validity invariants derive from the current Canon.

The detailed enumerations inside each matrix are reconstructed from the February 2026 Regime exploration.

They are included because an implementable Core Pack needs concrete candidate rules that can be tested, contested, and compared.

Their inclusion does **not** claim that those detailed enumerations already exist in the Canon.

The intended upstream path is:

```text
February exploration
  → Core Pack machine-readable candidate
  → cross-domain and conformance testing
  → Canon gap review
  → explicit Canon amendment, revision, or rejection
```

The gap between the current Canon and the detailed matrices is tracked in `docs/regime-canon-gap-ledger.md`.

---

## 19.5 Domain Pack boundary

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
- treat domain authority as epistemic Validity;
- erase Regime identity from persisted objects.

```text
Domain specialization is open-ended.
Regime semantics are not.
```

---

## 19.6 Execution Contract boundary

An Execution Contract may:

- select one primary Core Regime;
- select additional Regimes for explicit comparative evaluation;
- declare switching and escalation triggers;
- bind stricter Process conditions;
- require human or institutional Review;
- require Authority before Admission, Binding, or ExternalEffect.

An Execution Contract must not:

- author Regime definitions;
- reinterpret a selected Regime;
- treat successful execution as a Validity outcome;
- silently switch Regime because a preferred conclusion failed;
- collapse Review into Binding.

The distinction is:

```text
Regime
  → How may this Claim be evaluated?

Execution Contract
  → Under which conditions may this Process execute here?
```

---

## 19.7 Regime switching and comparative evaluation

Regime switching is always explicit.

A switch retains:

```text
from Regime
to Regime
reason
affected Claims or Evaluations
initiating Actor
Authority reference where required
SemanticVersion
time
prior Validity outcomes
new evaluation scope
```

Comparative evaluation is not automatically switching.

A Claim may be evaluated under both `Disciplined` and `Adversarial`, producing different outcomes:

```text
Disciplined → maintained
Adversarial → contested
```

Both outcomes remain referable.

Neither overwrites the other.

A Projection may display both.

It must not average or collapse them into Regime-less truth.

---

## 19.8 Regime conformance invariants

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

The machine-readable contracts live under:

```text
semantic/concepts/epistemic/regimes/contracts/
```

The dedicated Regime validator is:

```bash
python scripts/validate_regimes.py
```

The general pack validator remains:

```bash
python scripts/validate_pack.py
```

---

## 19.9 Why Regimes belong in Core

The Core Semantic Pack is not the parent repository of every possible Domain Pack.

It is the common semantic and epistemic interoperability contract those independently authored packs extend.

Regimes are part of that contract because they prevent unlimited domain extension from becoming unlimited epistemological fragmentation.

---

# 20. Composition model

The Core is a kernel.

A concrete system should normally operate against a composition.

```text
Core Semantic Pack
        +
Domain Semantic Pack(s)
        +
Execution Contract
        +
Core Regime selection
        =
Resolved Semantic Pack
```

Example:

```text
core@0.1
+
intellectual-property@0.4
+
patent-landscape-analysis-contract@1.2
+
core.regime.disciplined@0.1

→

resolved-pack:8f3d...
```

The Regime is not another independently authored Pack component.

The Resolved Semantic Pack records an exact Regime binding from the Core release.

---

# 21. Semantic authority of composition dimensions

The dimensions are not merely folders.

They carry different kinds of semantic responsibility.

## Core Semantic Pack

Defines stable cross-domain distinctions and the shared Regime system.

Examples:

```text
State
Claim
Evidence
Regime
Goal
Process
Authority
Admission
```

## Domain Semantic Pack

Specializes Core meaning for a domain and may be authored independently of the Core repository or release process.

Examples:

```text
Patent
PatentFamily
ClaimElement
ResearchPublication
CustomerAccount
```

Domain specialization may narrow Core meaning.

It must not silently redefine Core meaning or Regime semantics.

## Execution Contract

Defines the semantic legitimacy conditions for executing a Process in a concrete Context and selects applicable Core Regimes.

## Resolved Semantic Pack

The immutable semantic environment actually supplied to a consumer.

It records:

- exact Core release;
- exact Domain Pack releases;
- exact Execution Contract release;
- primary Core Regime;
- comparative Core Regimes where applicable;
- Regime switch history;
- compatibility result;
- composition checksum.

---

# 22. Question-driven semantic resolution

A runtime should not have to know which semantic files to load.

It declares what questions and operations it needs to support.

Example:

```yaml
semantic_request:

  questions:
    - what_is_known_about_x
    - what_supports_this_finding
    - why_is_this_action_being_taken
    - which_goal_does_it_advance
    - may_this_result_become_maintained_state
    - may_this_action_produce_external_effect

  context:
    domain: intellectual-property
    process: patent-analysis

  regime_selection:
    primary: core.regime.disciplined
    comparative:
      - core.regime.adversarial

  planned_operations:
    - retrieval
    - inference
    - persistence
    - recommendation
```

Resolution becomes:

```text
questions
    ↓
required semantic distinctions
    ↓
Core concepts + Core Regimes
    ↓
required boundaries
    ↓
domain specialization
    ↓
Execution Contract
    ↓
Regime selection
    ↓
compatible semantic release
```

Result:

```yaml
resolved_pack:
  id: resolved:7fa31
  immutable: true

  components:
    - type: core-semantic-pack
      id: semantic-pack.core
      version: 0.1.0
    - type: domain-semantic-pack
      id: ip.patent-analysis
      version: 0.1.0
    - type: execution-contract
      id: contract.patent-analysis
      version: 0.1.0

  regime_binding:
    primary:
      id: core.regime.disciplined
      version: 0.1.0
    comparative:
      - id: core.regime.adversarial
        version: 0.1.0
    switch_history: []

  provides_questions:
    - Why is this being done?
    - What supports the Claim?
```

---

# 23. Runtime Adapter Contract

The runtime adapter should remain thin.

Its responsibility is not to redefine semantic meaning or Regime semantics.

Conceptually:

```text
runtime need
    ↓
semantic question declaration
    ↓
Semantic Pack Provider
    ↓
resolved semantic environment
    ↓
runtime artifacts / constraints
```

Possible interface:

```python
pack = semantic_provider.resolve(
    questions=[
        "what_supports_this_claim",
        "why_is_this_action_being_taken",
        "may_this_be_persisted"
    ],
    domain="ip",
    process="patent-analysis",
    regime="core.regime.disciplined"
)
```

The provider may return only the material required for the current Context.

This avoids turning the complete Semantic Core into one enormous prompt or runtime schema.

---

# 24. Semantic Pack Provider

A system such as **Hermes** may operate as the pack provider.

Its responsibility could include:

```text
governed semantic source
        ↓
change detection
        ↓
derivation / compilation
        ↓
pack generation
        ↓
compatibility analysis
        ↓
version publication
        ↓
resolution
        ↓
consumer distribution
```

Hermes must not become the semantic source of truth merely because it compiles and serves packages.

Conceptually:

```text
Semantic authority source
        ↓
      Hermes
        ↓
versioned Semantic Packs
        ↓
       MCP
        ↓
runtime consumers
```

Hermes may distribute Core Regime definitions and resolved Regime bindings.

It may not invent or silently alter Core Regime semantics.

Hermes is:

> compiler, packager, resolver, and distributor of governed semantic meaning.

It is not:

> the authority that invents that meaning through implementation.

---

# 25. Semantic versioning and historical reconstructability

A new Core release must not silently redefine an active execution.

Every resolved semantic environment should be immutable.

```text
execution E17
uses
resolved-pack@7fa31
```

Historical reasoning must remain reconstructable under both:

- the SemanticVersion that governed meaning;
- the Regime version that governed Validity.

Upgrade should occur through:

```text
current semantic release
        ↓
semantic + Regime diff
        ↓
impact classification
        ↓
compatibility evaluation
        ↓
consumer / authority decision
        ↓
new resolved release
```

not:

```text
latest → production
```

A later meaning or Regime matrix must not silently rewrite the semantics of a historical Claim, Validity outcome, or StateChange.

---

# 26. Question answerability as conformance

Traditional runtime conformance may ask:

```text
Did the API return 200?

Did the JSON schema validate?

Did the tool execute?

Did the agent complete?
```

Semantic conformance asks additional questions:

```text
What produced this Finding?

Which Evidence supported it?

What contradicted it?

Which Regime governed its Validity?

Was the Regime switched?

Which Interpretation was applied?

Which Context governed that Interpretation?

Which Goal was being advanced?

Which DesiredState was being pursued?

Which Intent produced the Action?

Which Authority permitted the Action?

Which Execution Contract made execution admissible?

Which StateChange actually occurred?

Was the Goal later changed?

Can we reconstruct why the system believed this was valid at that time?
```

A runtime can succeed operationally while failing semantically.

If material questions can no longer be answered, semantic continuity has been lost.

---

# 27. Core conformance principle for material Action

For any material Action:

```text
Action
  → must have Intent

Intent
  → must be relatable to Goal

Goal
  → must make DesiredState interpretable

Action
  → must operate on declared State

Action
  → must participate in a declared Process

execution
  → must satisfy applicable Execution Contract

material epistemic dependencies
  → must retain applicable Regime context

Action
  → must have sufficient Authority for its effect

StateChange
  → must be attributable to Action or another declared cause

StateChange
  → must remain reconstructable

Progress
  → must be evaluable independently from ActionSuccess
```

This is substantially stronger than:

```text
agent followed instructions
```

---

# 28. Concrete semantic trace

Consider a system analyzing a patent portfolio.

```text
Source
  Patent records

↓

Observation
  17 patents expire within 24 months

↓

Claim
  Current portfolio coverage will materially decrease

↓ evaluatedUnder

Regime
  Disciplined

↓

Evidence
  Patent status + expiry records

↓

Validity
  maintained under Disciplined

↓

Inference
  Competitor exposure is likely to increase

↓

Finding
  Portfolio protection gap emerging
```

A comparative Adversarial evaluation may produce:

```text
same Claim
  ↓ evaluatedUnder
Adversarial
  ↓
contested
```

The Disciplined outcome is not overwritten.

Teleological context:

```text
Goal
  Maintain strategic protection of product family X

↓

DesiredState
  Critical technologies remain covered
  after current patents expire

↓

Intent
  Identify replacement filing opportunities
```

Agency:

```text
Process
  Portfolio protection analysis

↓

Action
  Generate filing recommendations
```

Governance:

```text
Authority
  Analysis authority only

↓

Execution Contract
  May analyze and recommend
  Uses Disciplined as primary Regime
  May use Adversarial for comparison
  May not authorize filing
  Provenance required
  Findings must remain contestable
```

Projection:

```text
Recommendation report
```

Critical boundary:

```text
Recommendation != BindingDecision
```

A later authorized sequence may be:

```text
Review
   ↓
BindingDecision
   ↓
authorized Action
   ↓
ExternalEffect
   ↓
StateChange
```

The complete chain remains reconstructable.

---

# 29. The deeper architecture

The architecture can now be understood as a graph of questions and semantic responsibilities.

```text
QUESTION
   ↓
What must remain distinguishable
for this question to have a truthful answer?
   ↓
SEMANTIC DISTINCTIONS
   ↓
Which relations and Regime context must survive?
   ↓
SEMANTIC CONTRACT
   ↓
Which component owns that responsibility?
   ↓
ARCHITECTURAL BOUNDARY
   ↓
How is that responsibility realized here?
   ↓
RUNTIME MAPPING
```

Architectural contracts concerning:

- meaning;
- interpretation;
- identity;
- state;
- permissible transformation;
- validity;
- admissibility;
- Regime selection;
- authority;
- responsibility;
- binding;
- revocation;

are semantic contracts.

At this level:

> architecture is the allocation of semantic responsibility across a system.

---

# 30. Two semantic chains

The Core exposes two fundamental semantic directions.

## Reality toward knowledge

```text
REALITY
  ↓
Source
  ↓
Observation
  ↓
Interpretation
  ↓
Claim
  ↓ evaluatedUnder
Regime
  ↓
Evidence / Contradiction
  ↓
Validity
  ↓
Inference
  ↓
Finding
  ↓
maintained knowledge candidate
```

## Goal toward reality

```text
Goal
  ↓
DesiredState
  ↓
Intent
  ↓
Process
  ↓
Execution Contract
  ↓ selects
Regime context where epistemic evaluation is required
  ↓
Action
  ↓
StateChange
  ↓
REALITY
```

The two chains meet through **State**.

```text
REALITY → MEANING → KNOWLEDGE

             STATE

GOAL → INTENT → ACTION → REALITY
```

Around both chains, the system must preserve:

```text
Context
Provenance
Regime
Authority
SemanticVersion
Uncertainty
Contestation
Admission
Revocation
```

---

# 31. Core invariant

The Core Semantic Pack should ultimately guarantee one structural property:

> **No material consequence should become detached from the semantic and epistemic path that made it possible.**

A system must be able to reconstruct backwards from consequence:

```text
ExternalEffect
      ↑
StateChange
      ↑
Action
      ↑
Execution Contract
      ↑
Process
      ↑
Intent
      ↑
Goal
      ↑
DesiredState
```

and from judgment:

```text
Decision / Finding
        ↑
Validity
        ↑
Regime
        ↑
Inference / Claim
        ↑
Evidence
        ↑
Observation
        ↑
Source
```

while preserving:

```text
Context
Provenance
Regime
Authority
Version
Validity
Uncertainty
Contestation
Admission
Revision
Revocation
```

This is the minimal semantic skeleton required for a system to increase autonomy without surrendering semantic continuity, epistemic discipline, accountability, and its capacity to correct itself.

---

# 32. Semantic Handshake

A runtime does not become governed by the Semantic OS merely because it can read, retrieve, or place a Semantic Pack in model context.

```text
Semantic Pack consumption != semantic governance
```

Governance begins only after an explicit **Semantic Handshake** establishes that the runtime can preserve the Pack's semantic obligations for an identified environment and demonstrates how those obligations are realized with the physical capabilities actually available to it.

The handshake is a pre-adoption protocol among four distinct responsibilities:

```text
Semantic authority source
        +
Semantic Pack Provider
        +
runtime consumer
        +
environment authority
        ↓
Semantic Handshake
```

The authority source governs Core meaning.

The provider compiles, resolves, versions, and distributes governed meaning without becoming its authority.

The runtime resolves semantic obligations, inspects its available capabilities, selects physical realizations, and demonstrates the resulting behavior without acquiring semantic Authority by implementation capability.

The environment authority governs environment-local Goals, DesiredStates, Constraints, information boundaries, workload acceptance, and update decisions.

Capability does not collapse these responsibilities:

```text
provider capability != semantic Authority

runtime capability != semantic Authority

storage or index capability != semantic Authority

update availability != update Admission
```

## Complete adoption procedure

H1 is one continuous procedure. One initiating Handshake Prompt starts the complete process; the runtime must not stop after finding a gap and wait for separate prompts for later phases.

```text
identity binding
      ↓
semantic obligation resolution
      ↓
runtime self-inspection
      ↓
capability resolution
      ↓
realization selection
      ↓
operational fitness
      ↓
authority / enforcement boundary
      ↓
behavioral proof
      ↓
synchronization commitment
      ↓
adoption decision
      ↓
revalidation triggers
```

The final adoption decision occurs only after all applicable phases have been exhausted.

An intermediate unresolved capability does not itself produce a terminal `conditional` result. Independent obligations continue to be evaluated.

## Runtime-native-first Capability Resolution

Semantic OS specifies **what must remain true** before prescribing how a runtime must be built.

For every material semantic obligation, H1 resolves the physical realization in this order:

```text
native
  ↓
mappable
  ↓
composable
  ↓
externally available
  ↓
missing
  ↓
incompatible
```

A dedicated semantic subsystem is not required merely because it would be convenient.

Filesystem, Git, databases, memory, retrieval, approval surfaces, messaging, tools, processes, and already accessible external capabilities may be mapped or composed when they preserve the semantic obligation.

The absence of a dedicated semantic database, adapter, plugin, MCP server, or workflow engine is therefore not evidence that the underlying physical capability is missing.

New runtime software is a last-resort **proposed remedy** only after native, mappable, composable, and already available external realizations have been exhausted.

H1 itself does not authorize or implement that software.

## Semantic discipline, mapping, enforcement, and Authority

Capability proof must distinguish:

```text
Pack available as context

agent semantic discipline

runtime mapping

deterministic behavioral enforcement

runtime / security policy

semantic Authority
```

These are different claims and require different Evidence.

Not every semantic obligation automatically requires a bespoke hard-enforcement subsystem. The applicable semantic environment determines what behavior must remain answerable, governed, or technically blocked.

A model assertion that it can follow the Pack is not implementation Evidence.

Likewise, a runtime security mechanism does not become semantic Authority merely because it can technically block an Action.

## Operational Fitness

Semantic conformance does not prove that a selected physical realization is useful for the declared workload.

H1 therefore evaluates the selected realization against relevant operating dimensions such as:

```text
semantic object and relation scale
read latency and query frequency
write frequency and contention
relation traversal
semantic-fragment retrieval
Renderer and agent access patterns
restart durability
provenance and reconstruction cost
resource consumption
failure recovery and rebuildability
concurrency
```

A realization is classified as:

```text
fit
fit-with-bounds
insufficient
unknown
```

A bootstrap realization may be accepted only when its explicit bounds cover the current declared workload.

This permits stable semantic history to remain independent from replaceable operational layers. For example, a canonical semantic record may remain reconstructable while SQL indexes, graph projections, vector indexes, caches, or materialized views are replaced as scale and Renderer demands evolve.

Technology replacement below stable semantic contracts does not itself redefine semantic meaning.

## Behavioral proof

H1 must distinguish a plausible architecture mapping from demonstrated behavior.

Acceptable proof may include:

```text
read-only runtime inspection
source and configuration inspection
existing logs and traces
isolated or disposable test artifacts
non-material dry runs
deterministic structured-record validation
negative tests for forbidden or unresolved transitions
```

The handshake does not gain additional Authority merely because proof is required.

H1 may not create material Admission, activate a production semantic environment, cause an ExternalEffect, or implement new runtime software merely to obtain evidence unless that Action has been independently authorized outside the Handshake Contract.

## Local semantic sovereignty and synchronization

Synchronization may detect and prepare upstream change.

It must not silently activate that change.

```text
upstream release
      ↓
semantic + Regime diff
      ↓
impact classification
      ↓
compatibility validation
      ↓
explicit environment decision
      ↓
new version-pinned binding
```

No upstream update may silently alter environment-local Goals, DesiredStates, Constraints, ontology, information boundaries, or the meaning of existing State.

Local sovereignty does not permit silent redefinition of Core meaning either. A conflict must remain explicit and may require rejection, adaptation, or a newly authorized composition.

Historical objects and StateChange remain interpretable under the exact semantic environment that governed them to the degree required by that environment.

## Handshake outcome

After the complete procedure, the result is exactly one of:

```text
accepted
conditional
rejected
```

`accepted` means every material obligation has an evidenced realization that preserves the authority boundary and is operationally fit, or fit within explicit bounds, for the declared current workload.

`conditional` means the procedure completed and preserved the authority boundary, but one or more material obligations remain unresolved, operational fitness is insufficient or unknown, required behavioral Evidence is incomplete, or an independently authorized physical capability is still required.

`rejected` means a required identity, authority boundary, semantic invariant, conflict policy, or unavoidable capability incompatibility prevents governed adoption for the identified environment.

A material change to the Pack, provider, adapter, runtime, selected realization, environment, authority boundary, or declared workload requires revalidation. Breaching an accepted Operational Fitness bound also requires revalidation.

## Handshake Prompt and Handshake Record

A **Handshake Prompt** is a runtime-facing invocation surface for a Semantic Handshake Contract.

Its wording may vary across Hermes, Claude Code, Codex, another model, a programming interface, or a non-prompt adapter. It is not semantic authority and cannot weaken, split, or silently reinterpret the Contract.

Every handshake produces a versioned **Handshake Record** containing at least:

```text
contract identity
participant identities
Pack identities and checksums
environment, Goal / DesiredState, and authority boundary
declared workload and operating scope
resolved material semantic obligations
runtime capability inventory
per-obligation Capability Resolution class
selected physical realizations
Operational Fitness state, bounds, and limiting dimensions
semantic-discipline / mapping / enforcement claims
behavioral-proof Evidence
precedence and conflict policy
synchronization, rollback, and reconstruction policy
genuinely missing physical capabilities, if any
outcome and unresolved conditions
deciding Authority
revalidation triggers
```

Therefore:

> **A runtime becomes governed only after completing a valid Semantic Handshake for the identified Pack, runtime, environment, workload, and authority boundary.**

The first portable contract is materialized as:

```text
semantic-contracts/handshakes/H1-semantic-os-adoption-contract.yaml
```
