# Deployment Contract

## Governing Principle

```text
Deployment is not complete until the system is observable, recoverable, and monitored.
```

## CI/CD Stages

1. lint
2. test
3. benchmark (optional)
4. evaluate
5. trust verification
6. maturity gate
7. build
8. deploy
9. smoke test
10. monitor
11. rollback if needed

## Initial Deployment Target

- VPS + MicroK8s

## Required Operational Capabilities

- health checks
- readiness checks
- liveness checks
- structured logs
- metrics
- alerts
- dashboards
- backups
- restore tests
- rollback procedures

## Post-Production Checks

- health stable
- error rates acceptable
- latency acceptable
- trust and eval signals normal
- no critical alerts

## Final Rule

A deployment is successful only when the system is healthy after release.
