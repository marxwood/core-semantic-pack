# Relations

`core-relations.yaml` defines the typed relations that connect Core concepts into a semantic graph.

A relation record declares:

- stable ID and canonical lowerCamelCase `symbol`;
- allowed source and target canonical semantic types;
- direction and optional canonical inverse symbol;
- semantic definition;
- provenance requirement;
- whether the relation creates or carries normative consequence.

`Any` is deliberate reserved wildcard meta-notation for relations that may apply across multiple semantic layers. It is not a registry object or Core primitive, and it does not mean that any runtime object automatically qualifies as a Core semantic object.

Relations do not redefine their source or target concepts. A runtime edge, database foreign key, graph adjacency, or message reference maps to a Core relation only when it preserves the declared meaning.

## Inverse relations

Selected relations declare explicit inverse pairs to support reconstruction and query traversal in either direction. An inverse may be present even when v0.1 fixtures use only the primary direction. Its inclusion does not create a second meaning; both records must remain definitionally reciprocal.
