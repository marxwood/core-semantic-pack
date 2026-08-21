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
             Semantic Pack Service
                       │
              deterministic resolution
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

The Runtime Adapter should remain thin.

Its responsibility is to translate a runtime need into a typed semantic request and to map the returned Resolved Semantic Pack into concrete runtime artifacts or constraints.

It must not:

- redefine Core or Domain meaning;
- redefine Regime semantics;
- select Authority that the request does not possess;
- fabricate missing semantic material;
- silently replace the pinned semantic environment with a newer release;
- become a second Semantic Resolver.

Conceptually:

```text
consumer / runtime need
        ↓
thin Runtime Adapter
        ↓
typed semantic request
        ↓
Semantic Pack API
        ↓
immutable Resolved Semantic Pack
        ↓
runtime artifacts / constraints
```

Possible client interface:

```python
pack = semantic_pack_service.resolve(
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

The adapter is optional where a consumer can issue and consume the typed API contract directly.

An agent is a possible consumer.

It is not a required intermediary.

This avoids turning the complete Semantic Core into one enormous prompt or runtime schema and prevents model behavior from becoming an implicit semantic delivery layer.

---

# 24. Semantic Pack Service

The **Semantic Pack Provider** is an architectural role.

The preferred runtime realization of that role is an independent **Semantic Pack Service**.

The Service exposes deterministic semantic resolution and immutable pack delivery through a runtime-neutral API that may be consumed by:

- agents;
- tools;
- models;
- memory systems;
- APIs;
- workflow and orchestration systems;
- conventional software applications.

The Service must remain independently available from any particular agent, model, prompt, or orchestration runtime.

```text
Semantic Pack Provider
  → architectural role

Semantic Pack Service
  → independent API realization of that role

Semantic Resolver
  → deterministic resolution capability inside the Service

Hermes
  → possible compiler and publisher in the control plane
```

These terms must not collapse.

---

## 24.1 Control plane and runtime plane

Semantic compilation and runtime consumption have different responsibilities.

```text
CONTROL PLANE

governed semantic sources
        ↓
change detection
        ↓
Hermes compiler / publisher
        ↓
validation + compatibility analysis
        ↓
versioned Semantic Pack Registry


RUNTIME PLANE

consumer
        ↓
typed semantic request
        ↓
Semantic Pack API
        ↓
Semantic Resolver
        ↓
immutable Resolved Semantic Pack
        ↓
consumer runtime
```

The runtime request path does not require an agent to mediate access to semantic material.

Hermes may use agentic capabilities during governed derivation or compilation.

Runtime availability and resolution must not depend on an agent interpreting every request.

---

## 24.2 Hermes boundary

A system such as **Hermes** may compile and publish the material served by the Semantic Pack Service.

Its responsibility may include:

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
registry publication
        ↓
consumer notification
```

Hermes may distribute Core Regime definitions and resolved Regime bindings.

It may not invent or silently alter Core meaning, Domain meaning, Regime semantics, Execution Contracts, or environment-local Authority.

Hermes is:

> compiler, packager, compatibility evaluator, and publisher of governed semantic material.

It is not:

> the authority that invents that meaning through implementation.

Resolution may be implemented by the Service independently of the Hermes build process.

---

## 24.3 Deterministic resolution boundary

The Semantic Resolver evaluates a typed request against already published, versioned semantic material.

Its runtime responsibility is:

```text
typed semantic request
        ↓
question and operation requirements
        ↓
required Core distinctions
        ↓
compatible Domain specialization
        ↓
Execution Contract
        ↓
Core Regime selection
        ↓
version and compatibility constraints
        ↓
immutable Resolved Semantic Pack
```

The Resolver must not use open-ended model inference as an unrecorded substitute for missing semantic definitions.

For the same:

- request;
- available Pack Registry state;
- resolver contract version;
- compatibility policy;

the resolution result must be reproducible.

Where a consumer intentionally requests a floating range, the exact selected versions and registry state must still be recorded in the result.

---

## 24.4 API surface

A possible versioned HTTP surface is:

```http
POST /v1/resolve
GET  /v1/packs/{pack-id}
GET  /v1/packs/{pack-id}/versions/{version}
POST /v1/compatibility/check
GET  /v1/manifest
GET  /v1/updates
```

Equivalent transports may be provided.

MCP may be exposed as an adapter over the same Service contract.

MCP is not required for consumers that can use the API directly.

A semantic request should remain metadata-first and explicit:

```yaml
semantic_request:
  id: request:patent-analysis:001
  resolver_contract: semantic-resolution@0.1
  requested_semantic_release: 0.1.x

  questions:
    - What supports this Claim?
    - Why is this being done?
    - May this object become maintained State?

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

  consumer:
    id: runtime:patent-analysis
    type: agent
    adapter_version: 0.3.0
```

A successful response should bind exact identity, versions, compatibility, and Provenance:

```yaml
resolved_pack:
  id: resolved:7fa31
  version: 1
  immutable: true
  content_hash: sha256:7fa31
  resolver_contract: semantic-resolution@0.1
  registry_state: registry:2026-08-21:001

  components:
    - type: core-semantic-pack
      id: semantic-pack.core
      version: 0.1.0
    - type: domain-semantic-pack
      id: ip.patent-analysis
      version: 0.4.0
    - type: execution-contract
      id: contract.patent-analysis
      version: 1.2.0

  regime_binding:
    primary:
      id: core.regime.disciplined
      version: 0.1.0
    comparative:
      - id: core.regime.adversarial
        version: 0.1.0

  compatibility:
    status: compatible
    policy: compatibility-policy@0.1

  provides_questions:
    - What supports this Claim?
    - Why is this being done?
    - May this object become maintained State?

  provenance:
    resolved_at: 2026-08-21T00:00:00Z
    resolved_by: semantic-pack-service@0.1.0
```

The exact serialization and transport are not authoritative.

The identity, version, Authority, compatibility, immutability, and Provenance obligations are.

---

## 24.5 Unresolved semantics

Failure to resolve is a valid and required outcome.

```yaml
semantic_resolution:
  id: resolution:patent-analysis:001
  status: unresolved
  request_id: request:patent-analysis:001
  resolver_contract: semantic-resolution@0.1
  registry_state: registry:2026-08-21:001

  missing_semantics:
    - required_question_contract: May this action create an ExternalEffect?
    - required_domain_mapping: ip.filing-authorization

  required_action: semantic-compilation

  prohibited_fallbacks:
    - silent_fabrication
    - latest-version-substitution
    - model-inferred-authority
    - implicit-regime-switch
```

The Service must return an explicit unresolved result when required semantics are unavailable, incompatible, unauthorized, or ambiguous.

It must not improvise a contract and present that contract as part of the Core, a Domain Pack, an Execution Contract, or an active semantic environment.

A governed build or review process may later produce a new candidate release.

That candidate remains unavailable to the runtime until it is validated, versioned, published, and admitted through the applicable Authority path.

---

## 24.6 Comparison matrix

| Dimension | Agent-mediated Provider | Independent API Service | Hermes control plane + API Service |
|---|---|---|---|
| Runtime path | Consumer → agent → Pack | Consumer → API → Pack | Consumer → API → Pack |
| Agent dependency | Required | None | None in runtime |
| Resolution behavior | Model-dependent | Deterministic | Deterministic |
| Reproducibility | Limited by model and prompt | Bound to request, registry state, and resolver version | Bound to published build and resolver version |
| Latency | Model inference latency | Standard service latency | Standard service latency |
| Per-request cost | Model inference | API operation | API operation |
| Auditability | Requires reasoning and prompt capture | Request, response, version, hash, and Provenance | Full source-to-build-to-resolution Provenance |
| Silent invention risk | Higher | Explicitly prohibited | Explicitly prohibited |
| New semantic needs | Agent may interpret immediately | Returns unresolved | Hermes prepares a governed candidate release |
| Compatibility evaluation | Interpreted per request | Formal policy | Calculated before publication and checked at resolution |
| Caching | Model-sensitive | Stable by request and registry state | Stable by release and request |
| Consumer coupling | Agent or model coupling | Runtime-neutral | Runtime-neutral |
| Production suitability | Limited | Strong | Preferred |

The preferred architecture is:

```text
Hermes
  → governed compilation and publication

Semantic Pack Service
  → independent deterministic resolution and delivery

Runtime Adapter
  → thin consumer-side mapping

Agent
  → one possible consumer
```

---

## 24.7 Authority and repository boundary

The Semantic Pack Service is infrastructure.

Operational control of the Service does not grant semantic Authority.

```text
service ownership != semantic Authority

deployment access != admission Authority

resolution capability != authority to invent meaning

successful delivery != semantic conformance
```

This repository defines the Pack semantics and the architectural contract that a conforming Service must preserve.

It does not contain the production implementation of the Service or Hermes.

A production implementation may live in a dedicated repository such as:

```text
semantic-pack-service
```

Hermes compilation and publication may live in a separate Hermes implementation repository.

Neither implementation repository becomes the source of semantic truth merely because it builds, resolves, or serves Pack artifacts.

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
