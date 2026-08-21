# Open questions for post-v0.1 review

The following issues are intentionally unresolved rather than hidden by premature naming.

## Type and classification

The question “What kind of thing is this?” is required, but `Type` is not yet admitted as a Core primitive.
v0.1 uses canonical concept symbols and explicitly declared reference-only categories. Further review should
determine whether type is a primitive, a classification relation, or part of Identity and Context.

## Statement and Claim

`Statement` currently provides a neutral expression layer before assertion. Multi-domain testing should
determine whether this distinction remains universally necessary or can be modeled as a role/status of
another expression concept.

## Support and Contradiction reification

v0.1 contains both the concepts `Support` / `Contradiction` and the relations `supports` / `contradicts`.
Reification is useful when context, provenance, uncertainty, or contestation must attach to the relation
itself. Further use should determine when a direct relation is sufficient.

## Direction, Trajectory, and Progress

These are candidate primitives because teleological answerability requires distinctions beyond Goal and
DesiredState. Cross-domain testing should confirm whether all three remain Core or whether one or more
should become patterns.

## BindingDecision

`BindingDecision` is used as a comparison category but is not a v0.1 primitive. The current model composes
Binding and Commitment. Further governance mappings should test whether a distinct Decision concept is
required.

## Regime matrices and Canon promotion

`Regime` and the five Core Regime identities are now materialized from the current Canon.

The detailed per-Regime enumerative matrices remain exploratory. Review must determine:

- which matrix rules should be added to the Canon;
- which should remain Core derivations;
- which should become domain or Execution Contract restrictions;
- whether the candidate escalation graph is canonical;
- the exact canonical switch-record fields;
- whether High-Assurance always requires independent corroboration;
- how domain Evidence policies compose with Core Regime Evidence policies.

See [`docs/regime-canon-gap-ledger.md`](regime-canon-gap-ledger.md).

## Runtime events

Event, message, tool result, workflow step, memory record, and agent configuration remain mappings. No
implementation object should enter the Core without explicit derivation and admission.
