# Release Protocol

## Governing Rule

```
A release is not done until it is trusted, evaluated, and observable in production.
```

## Release Types

| Type | Contract | Promotion Path |
|---|---|---|
| CreativeWork | `release/creativework.release.yaml` | draft → released → Prompt-Library |
| Agent | `release/agent.release.yaml` | registered → validated → active |
| Platform | `release/platform.release.yaml` | dev → staging → prod |

## Release Checklist

### Pre-release
- [ ] All CI gates pass
- [ ] Version bumped and tagged
- [ ] Changelog updated
- [ ] All artifacts have trust_record with `eval_status: passed`
- [ ] Maturity score meets environment threshold

### Deploy
- [ ] Deployment gate passes (see deployment-protocol.md)
- [ ] Smoke tests pass
- [ ] Health stable for 5 minutes post-deploy

### Post-release
- [ ] Monitoring dashboards showing normal signals
- [ ] No critical alerts firing
- [ ] Rollback procedure documented and tested
- [ ] Backup of stateful services verified

## Hard Rules

```
No release without evaluation.
No release without trust verification.
No release without a rollback plan.
No release without monitoring.
```
