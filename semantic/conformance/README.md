# Conformance

Conformance evidence tests whether a representation preserves declared Core distinctions and obligations.

The v0.1 validator performs **structural conformance**:

- YAML can be parsed;
- IDs are unique;
- stable IDs and canonical references are unique and resolve exactly;
- canonical concepts, relations, boundary expressions, questions, patterns, status families, and rule symbols exist;
- semantic authoring fields do not use legacy registry-ID notation;
- Questions live beneath one primary family and family navigation is bidirectionally consistent;
- indexes and release manifests match the repository;
- Semantic Handshake indexes, ordered contract filenames, required phases, outcomes, and illustrative records remain consistent;
- fixtures declare expected pass/failure outcomes.

Run `python scripts/validate_handshakes.py` for the dedicated Semantic Handshake contract checks.

The fixtures provide **semantic regression cases** for human and future executable review. The current validator does not infer truth, evaluate domain evidence, or prove that a runtime behaves correctly. A syntactically valid pack may still be semantically wrong.

Valid fixtures demonstrate a minimally traceable representation. Invalid fixtures intentionally encode a collapse or missing obligation and name the rule and boundary expected to detect it.
