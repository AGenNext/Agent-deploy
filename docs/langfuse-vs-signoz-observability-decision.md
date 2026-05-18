# Langfuse vs SigNoz Observability Decision

## Decision

Use both, with clear boundaries:

```text
Langfuse → LLM, prompt, model, agent, generation, evaluation traces
SigNoz   → service APM, infrastructure, logs, metrics, alerts, distributed tracing
```

Do not force one observability tool to own both application infrastructure monitoring and LLM/agent workflow observability.

## Recommendation

```text
Agent-level observability: Langfuse
Platform/service observability: SigNoz
Telemetry standard: OpenTelemetry where possible
Semantic contracts: Agent-Traces
```

## Why Langfuse

Langfuse is a strong fit for Agent Platform because it is designed for LLM and agent observability:

- prompt traces
- model generations
- tool calls
- agent steps
- sessions/conversations
- user feedback
- evaluations
- dataset/testset workflows
- cost and latency tracking for LLM calls
- debugging agent runs

Use Langfuse for questions like:

- What did the agent do during this run?
- Which prompts/model calls happened?
- Which tools were called?
- What was the model latency and token usage?
- Which generation was evaluated poorly?
- Which user feedback belongs to this output?

## Why SigNoz

SigNoz is a strong fit for infrastructure and service observability:

- API latency
- API error rates
- service health
- distributed traces across services
- logs
- metrics
- alerts
- Kubernetes/MicroK8s monitoring
- database/service latency

Use SigNoz for questions like:

- Is Agent-Knowledge API healthy?
- Is SurrealDB slow or unavailable?
- Are workers failing?
- Are requests timing out?
- Is the VPS/MicroK8s cluster healthy?
- Which endpoint has high latency?

## Relationship to Agent-Dashboard

Agent-Dashboard remains the product/control-plane view:

- run history
- objective status
- agent timeline
- evaluation/trust/finops cards
- human approval
- blocked runs
- scheduled runs

Langfuse and SigNoz are deeper observability tools used by builders/operators.

## Recommended Stack

```text
Agent-Dashboard
  → product workflow visibility and human approval

Langfuse
  → LLM/agent observability, prompts, generations, tool calls, evals

SigNoz
  → APM, logs, infra metrics, distributed service traces, alerts

Agent-Traces
  → shared semantic trace contracts
```

## Initial Deployment Priority

1. Agent-Dashboard product timeline
2. Langfuse for LLM/agent run observability
3. SigNoz for service/platform APM before production deployment

## Data Routing

Agent runtime should emit:

```text
Runtime events → SurrealDB → Agent-Dashboard
LLM/agent traces → Langfuse
Service traces/logs/metrics → OpenTelemetry → SigNoz
```

## Avoiding Duplication

- Do not put every infrastructure log into Langfuse.
- Do not force every prompt/generation detail into SigNoz.
- Use shared trace IDs so records can be correlated across systems.

## Final Rule

```text
Langfuse answers: What did the agent/model do?
SigNoz answers: Is the platform healthy?
Agent-Dashboard answers: What should the user/operator do next?
```
