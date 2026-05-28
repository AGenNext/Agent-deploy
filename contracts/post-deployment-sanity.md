# Post-Deployment Production Sanity Contract

Agent-deploy owns post-deployment production sanity.

## Required Checks

Every production deployment must verify:

- deployment rollout completed
- rollback command remains available
- health endpoint is reachable
- SurrealDB is reachable
- public discovery endpoints are reachable where configured
- smoke tests pass
- release contract matches deployed version
- no governance validation is failing for the deployed source

## Required Evidence

Deployment evidence must include:

- environment
- version
- deployment timestamp
- validation command output
- smoke test output
- rollback command/path
- operator or agent identity

## Final Rule

Deployment is not complete until post-deployment sanity passes.
