# Canonical question gaps

Concept records previously carried free-form `answers` strings. Only exact matches to an existing canonical Semantic Question were migrated to `helps_answer`. The entries below have no exact canonical equivalent and therefore were not guessed, aliased, or promoted into new Questions.

These are compatibility-relevant architecture review gaps. A future change may map one only after semantic review or admit a new atomic Question through the normal governance process.

## Entity

Stable ID: `core.entity`

- What persists as the same thing across change?
## Identity

Stable ID: `core.identity`

- Which identity does this Entity have?
- Why are two representations treated as the same Entity?
## Relation

Stable ID: `core.relation`

- How are these semantic objects connected?
- What does the connection mean?
## Context

Stable ID: `core.context`

- Under which conditions is this object valid or comparable?
## Boundary

Stable ID: `core.boundary`

- Where does this meaning stop applying?
- Which transition or equivalence is forbidden?
## State

Stable ID: `core.state`

- What is currently maintained as the case?
- Which State is active for this Entity and Context?
## StateChange

Stable ID: `core.state-change`

- What existed before and after?
- What caused or authorized the transition?
## Source

Stable ID: `core.source`

- Where did this object come from?
- What origin can be inspected independently?
## Derivative

Stable ID: `core.derivative`

- From what was this object derived?
- Which transformation produced it?
## Projection

Stable ID: `core.projection`

- How is underlying State or knowledge being represented?
- For which purpose was this representation produced?
## Interpretation

Stable ID: `core.interpretation`

- Which interpretation produced this meaning?
- Under which Context was the interpretation made?
## SemanticVersion

Stable ID: `core.semantic-version`

- Which meaning governed this object or execution?
- Can the historical interpretation be reconstructed?
## Observation

Stable ID: `core.observation`

- From which Source and under which Context?
## Statement

Stable ID: `core.statement`

- What was expressed?
- Who or what expressed it and in which Context?
## Claim

Stable ID: `core.claim`

- What is being asserted?
- Who asserted it?
- What supports or contradicts it?
## Evidence

Stable ID: `core.evidence`

- What supports or contradicts this Claim?
- Under which Regime was the object admitted as Evidence?
## Inference

Stable ID: `core.inference`

- From which premises or Evidence?
- Which reasoning transformation produced it?
## Finding

Stable ID: `core.finding`

- What conclusion has the governed evaluation produced?
- Which Evidence and Inferences contributed?
- What is its validity status?
## Provenance

Stable ID: `core.provenance`

- Where did this come from?
- Who or what produced it?
- Which transformations and versions affected it?
## Support

Stable ID: `core.support`

- How and under which Context does this object support the Claim?
- Who or what established the support relation?
## Contradiction

Stable ID: `core.contradiction`

- What conflicts with what?
- Under which Context and comparison rule does the conflict exist?
## Uncertainty

Stable ID: `core.uncertainty`

- What remains unknown or uncertain?
- Which limit applies to this interpretation or conclusion?
## Validity

Stable ID: `core.validity`

- Under which conditions is this considered valid?
- Which validation or regime established the status?
## Contestation

Stable ID: `core.contestation`

- What is being challenged?
- On what basis?
- Who is responsible for resolving or maintaining the contestation?
## Goal

Stable ID: `core.goal`

- Why is this direction being pursued?
- Which objective legitimizes the trajectory?
## DesiredState

Stable ID: `core.desired-state`

- What should reality look like if the Goal is advanced?
- Against what future condition is progress evaluated?
## Intent

Stable ID: `core.intent`

- What is the Actor trying to accomplish now?
- Which Goal does this immediate purpose advance?
## Direction

Stable ID: `core.direction`

- Which way should change move?
- What orientation does the Goal imply?
## Trajectory

Stable ID: `core.trajectory`

- How has State changed over time?
- Is the sequence moving toward the intended future?
## Progress

Stable ID: `core.progress`

- Is the system moving toward DesiredState?
- By which criteria is advancement or regression assessed?
## Actor

Stable ID: `core.actor`

- Who or what acted?
- Who holds the Intent or responsibility?
## Role

Stable ID: `core.role`

- In which capacity is the Actor participating?
- Which responsibilities and constraints apply?
## Capability

Stable ID: `core.capability`

- What can this Actor or Role do?
- Which operation can be performed?
## Action

Stable ID: `core.action`

- What was attempted or performed?
- Who performed it?
- Which Intent and Process does it realize?
## Process

Stable ID: `core.process`

- How can change occur in this semantic domain?
- Which transformations and invariants define the change structure?
## Transformation

Stable ID: `core.transformation`

- Which conversion occurred or is defined?
- What inputs and outputs does it relate?
## Transfer

Stable ID: `core.transfer`

- What moved?
- From where and to where?
- Which meaning and obligations must survive?
## Persistence

Stable ID: `core.persistence`

- What is retained?
- Under which lifecycle and semantic status?
- What may later read or reuse it?
## Composition

Stable ID: `core.composition`

- Which objects were combined?
- Which rules produced the composed Derivative?
## ExternalEffect

Stable ID: `core.external-effect`

- What changed outside the governed boundary?
- Which Action and Authority permitted the effect?
## Authority

Stable ID: `core.authority`

- Who or what legitimizes this consequence?
- Within which scope and Context does that legitimacy apply?
## Constraint

Stable ID: `core.constraint`

- What is limited?
- Under which condition does the limit apply?
- What happens when it is violated?
## Permission

Stable ID: `core.permission`

- What is allowed?
- Who or what is allowed to do it?
- Which Authority granted the allowance?
## Contract

Stable ID: `core.contract`

- Which obligations govern this interaction or execution?
- Which conditions make the transition legitimate?
## Validation

Stable ID: `core.validation`

- Does the candidate conform?
- Which rules were evaluated and with what result?
## Admission

Stable ID: `core.admission`

- May this candidate become maintained governed State?
- Who or what admitted it and under which Regime?
## Review

Stable ID: `core.review`

- What was reviewed?
- By whom?
- What evaluative outcome was produced?
## Binding

Stable ID: `core.binding`

- What became institutionally operative?
- Which Authority established the consequence?
## Commitment

Stable ID: `core.commitment`

- What obligation or decision is currently operative?
- Who is accountable for maintaining, revising, or revoking it?
## Revocation

Stable ID: `core.revocation`

- What governed status was withdrawn?
- Who authorized the withdrawal?
- What remains historically reconstructable?
## Accountability

Stable ID: `core.accountability`

- Who is responsible for this object or consequence?
- Who must explain or correct it?
