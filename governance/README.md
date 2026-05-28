# Agent-deploy Governance Validations

Agent-deploy owns validation, deployment, CI/CD, and post-deployment production sanity for AGenNext repositories.

This directory is the central editable source for governance validation rules. CI/CD wrappers, deployment gates, and commit gates must read rule definitions from here instead of duplicating rules in each repository.

Validation must run on the user's/client's system before changes are accepted by AGenNext servers. Server-side validation verifies evidence and re-runs required SurrealDB-owned gates; it is not the first validation boundary.

`README.md` and `AGENTS.md` content must be authored in AgentQL first. Markdown is a generated or maintained human-readable projection, not the semantic source.

## Files

- `no-python-business-logic.rules.tsv` - prohibited product/runtime Python business-logic patterns.
- `no-server-typescript.rules.tsv` - browser-side TypeScript boundary rules.
- `no-hidden-runtime-logic.rules.tsv` - prohibited hidden business/runtime logic carriers.
- `validation-policy.md` - ownership and operating policy for validation.
- `design-principles.agentql` - AgentQL source for durable design principles.
- `runtime-tool-manifest.agentql` - AgentQL source for runtime-loaded executable tool manifest requirements.
- `README.agentql` - AgentQL source for this README projection.

## Rule Format

`no-python-business-logic.rules.tsv` is tab-separated:

```text
scope<TAB>label<TAB>pattern
```

Scopes:

- `content` - run the pattern against Python file contents with `rg -n`.
- `path` - run the pattern against Python file paths.
- `path_outside_allowed` - fail matching paths unless they also match the allowed browser/AgentQL surface pattern.
- `path_requires_agentql_manifest` - fail matching artifacts unless a same-basename `.agentql` manifest exists.
- `content_yaml` - run the pattern only against YAML files.

## Usage

Validate any repo:

```bash
./scripts/validate_repo_governance.sh /path/to/repo
```

Validate the current repo:

```bash
./scripts/validate_repo_governance.sh .
```

## Final Rule

Validation policy is edited here. Repositories consume it.
