# Agent-deploy Instructions

Agent-deploy owns deployment execution, environment promotion, rollback operations, monitoring hooks, and post-deployment sanity verification.

Agent-deploy does not own check definitions, check execution logic, or check report semantics.

Checks owns check definitions, check execution records, evidence, signed check reports, and provider/tool check adapters.

Agent-deploy must verify Checks evidence before deployment, promotion, rollback, or production sanity claims.

Truth is:

```text
protected published commit SHA + required check evidence + signed report evidence
```

Not truth:

- repository names
- branch names without SHAs
- README text
- screenshots
- local working trees
- unstamped claims

Canonical records are append-only and must never be edited or deleted.

The latest valid canonical record in the requested scope is the effective truth because it is what is in effect.

Wrong logic must be corrected through a new pull request and new canonical record. History must not be rewritten to hide it.

Agent-Grammar owns grammar. Ontology owns meaning. Checks owns check-domain execution records and adapter contracts only.
