# Observability Product vs Upstream Tools Decision

## Decision

Build Agent Platform around an internal observability abstraction and use Langfuse and SigNoz as upstream adapters/imports.

Do not make the core product depend directly on Langfuse or SigNoz data models.

## Recommendation

```text
Agent-Traces
  → owns semantic trace contracts

Agent-Frameworks / Agent-Knowledge
  → emit platform-native events

SurrealDB
  → stores product/workflow run state

Langfuse adapter
  → exports/imports LLM and agent traces

SigNoz/OpenTelemetry adapter
  → exports service telemetry, logs, metrics, infra traces

Agent-Dashboard
  → reads platform-native state and links to Langfuse/SigNoz deep views
```

## Why Not Build Directly on Langfuse or SigNoz

Direct dependency creates vendor/tool lock-in at the product model level.

Risks:

- schema coupling
- migration difficulty
- duplicated product logic
- observability tool outage affecting core product views
- harder self-host/enterprise customization
- harder support for alternative observability stacks later

## Why Use Them as Upstream/Downstream Adapters

Langfuse and SigNoz are excellent specialist systems.

Use them for what they are best at:

```text
Langfuse
  → prompt/model/generation/tool-call/eval observability

SigNoz
  → APM/logs/metrics/distributed service traces/alerts
```

Agent Platform should remain the product control plane:

```text
Agent-Dashboard
  → objectives, runs, approvals, blockers, schedules, artifact versions, quality/trust/cost decisions
```

## Product Data Ownership

Agent Platform should own:

- run records
- task records
- objective records
- artifact versions
- human approvals
- blockers
- schedules
- tenant/workspace context
- business-level status
- evaluation/trust/finops summary

Langfuse may own detailed LLM spans.
SigNoz may own service-level telemetry.

## Integration Pattern

Use a ports-and-adapters architecture:

```text
AgentObservabilityPort
  → record_runtime_event()
  → record_tool_call()
  → record_model_call()
  → record_eval()
  → record_human_feedback()
  → link_external_trace()

Adapters:
  → SurrealDBRunStore
  → LangfuseTraceExporter
  → OpenTelemetryExporter
  → SigNozExporter through OTel
```

## Dashboard Behavior

Agent-Dashboard should show native product views first:

- run history
- active runs
- scheduled runs
- blocked runs
- human approvals
- artifact versions
- quality/trust/cost cards

Then provide deep links:

- View Langfuse trace
- View SigNoz service trace
- View logs/metrics

## When to Import from Langfuse

Import from Langfuse when:

- analyzing prompt performance
- pulling generation-level traces
- collecting user feedback/evals
- building datasets/testsets
- comparing model outputs

## When to Import from SigNoz

Import from SigNoz when:

- showing service health
- correlating API errors
- investigating latency
- checking infra alerts
- debugging Kubernetes/service issues

## Final Rule

```text
Own the product run model.
Adapt to observability tools.
Do not outsource the product control plane to observability vendors.
```
