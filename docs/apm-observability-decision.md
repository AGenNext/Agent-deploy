# APM and Observability Decision

## Decision

Use **SigNoz** as the preferred default APM and observability stack for Agent Platform.

Keep the architecture OpenTelemetry-first so the platform can also export to other observability backends if needed.

## Recommendation

```text
Default APM: SigNoz
Telemetry standard: OpenTelemetry
Runtime traces: Agent-Traces contracts
Deployment owner: Agent-deploy
Dashboard consumer: Agent-Dashboard
```

## Why SigNoz

SigNoz is a good fit because it provides:

- open-source APM
- OpenTelemetry-native ingestion
- distributed traces
- logs
- metrics
- dashboards
- alerts
- service maps
- latency/error visibility
- self-hosted deployment option

This aligns with Agent Platform's goals around enterprise control, cost awareness, and open-source-first infrastructure.

## What SigNoz Should Monitor

SigNoz should monitor:

- Agent-Knowledge API latency and errors
- Agent-Dashboard frontend/API calls
- Agent-Frameworks runtime execution
- SurrealDB calls
- MinIO/object storage calls
- tool calls
- model calls
- queue/worker execution
- deployment health
- runtime failures
- blocked/timeout patterns

## Relationship to Agent-Traces

```text
Agent-Traces
  → defines semantic trace contracts

OpenTelemetry
  → transports traces, logs, and metrics

SigNoz
  → stores, visualizes, alerts, and analyzes telemetry
```

## Relationship to Agent-Dashboard

Agent-Dashboard should show product/workflow-level views:

- run history
- objective status
- agent timeline
- human approval
- quality/trust/cost signals

SigNoz should show engineering/operations-level views:

- service latency
- errors
- traces
- logs
- metrics
- infra health
- alerts

## Initial Metrics

Track:

- request latency
- request error rate
- objective duration
- run failure rate
- blocked run count
- timeout count
- tool failure rate
- model call latency
- token usage
- cost by objective
- SurrealDB query latency

## Initial Alerts

Create alerts for:

- API error rate above threshold
- API latency above threshold
- runtime failures
- blocked runs older than threshold
- timed out runs
- tool API key expired
- secret expired
- budget exhausted
- SurrealDB unavailable
- dashboard unavailable

## Deployment Target

Initial deployment target:

```text
VPS + MicroK8s + SigNoz
```

## Final Rule

```text
Agent-Dashboard is for product/workflow visibility.
SigNoz is for engineering/operations observability.
Both consume OpenTelemetry-aligned traces and events.
```
