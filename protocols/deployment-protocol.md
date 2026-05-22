# Deployment Protocol

## Governing Rule

```
Deployment is not complete until the system is observable, recoverable, and monitored.
No gate may be skipped. A failed gate blocks the deployment.
```

## Required Gates (in order)

| # | Gate | Owner | Blocks |
|---|---|---|---|
| 1 | lint | Agent-deploy CI | build |
| 2 | test | Agent-deploy CI | build |
| 3 | contract validation | Agent-deploy CI | build |
| 4 | evaluate | Agent-Eval | deploy |
| 5 | trust verification | Agent-Trust | deploy |
| 6 | maturity gate | Agent-Maturity | deploy |
| 7 | build | Agent-deploy CI | deploy |
| 8 | deploy | Agent-deploy CI | smoke-test |
| 9 | smoke test | Agent-deploy CI | release |
| 10 | health stable | Agent-deploy monitor | release |
| 11 | rollback ready | Agent-deploy | release |

## Gate Definitions

### Gate 1–3: Code Quality
- All linting passes (ruff, tsc)
- All tests pass
- All release contracts are valid YAML and contain required gates

### Gate 4: Evaluate
- Every artifact produced by the objective has an eval record
- Eval status = `passed`
- Command: `agent-eval gate --objective-id $OBJECTIVE_ID`

### Gate 5: Trust Verification
- Every artifact has a `trust_record` with `ratingValue >= 0.7`
- Provenance chain is complete
- Command: `agent-trust verify --objective-id $OBJECTIVE_ID`

### Gate 6: Maturity Gate
- Platform maturity score meets threshold for target environment
- dev: score >= 0.5, staging: score >= 0.7, prod: score >= 0.9
- Command: `agent-maturity check --env $ENV`

### Gate 7: Build
- Docker images build without error
- Image is tagged with version and pushed to registry

### Gate 8: Deploy
- K8s manifests applied via `kubectl apply -k`
- Rollout completes within timeout (300s)

### Gate 9: Smoke Test
- `/health` returns `{"status":"ok","db":"connected"}`
- POST `/objectives/run` with test goal returns `status: completed`
- MinIO health live endpoint responds

### Gate 10: Health Stable
- All pods Running for 60s post-deploy
- Error rate < 1% for 2 minutes
- P95 latency < 500ms

### Gate 11: Rollback Ready
- Previous deployment is known and stored
- `kubectl rollout undo` is validated before gate passes

## Environment Promotion

```
dev → staging → prod
```

- dev: gates 1–3, 7–9 required. Gates 4–6 optional.
- staging: gates 1–9 required. Gate 10 required.
- prod: all gates 1–11 required.

## Rollback Protocol

If any post-deploy gate fails:

1. Auto-rollback triggers: `kubectl rollout undo`
2. Alert fires to operator channel
3. Incident record created in SurrealDB
4. Root cause investigation before next attempt

## Hard Rules

1. No production deploy without all gates passing
2. No deploy without a rollback procedure validated
3. No deploy without monitoring configured
4. No deploy without backup verified for stateful services
5. Secrets must be environment-scoped — never committed to git
