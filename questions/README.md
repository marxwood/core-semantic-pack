# Questions

The Core Semantic Pack is organized around questions that must remain answerable, not around nouns alone.

Each file defines a question-contract family with:

- canonical questions;
- required Core concepts and relations;
- anti-collapse boundaries that must remain intact;
- minimum answer requirements;
- semantic failure states;
- consequences when answerability cannot be established.

A runtime may ask only a subset of these questions. A resolved semantic environment should include enough Core, Domain, Regime, and Execution material to answer the questions required by its intended consequences.

Question contracts do not require one specific prompt, model, database, or orchestration engine. They define semantic obligations that any realization must preserve.

## Cross-family questions

A canonical question may appear in more than one family when it carries more than one semantic responsibility. For example, `Has the Goal changed?` is both teleological and reflective: one family identifies the active direction, while the other evaluates drift and revision. Resolution must combine the obligations rather than treat the repeated wording as duplicate authority.
