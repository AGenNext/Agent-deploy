# Agent-deploy boundary

Agent-deploy owns deployment packaging and CI/CD for AGenNext components.

## Decision

Use Agent-deploy for deployment workflows, release automation, CI/CD pipelines, Helm charts, manifests, and environment promotion.

AgentKube remains the Kubernetes SDK/operator layer.

## Boundary

| Component | Responsibility |
|---|---|
| Agent-deploy | CI/CD, release workflows, deployment packaging, Helm/manifests |
| AgentKube | Kubernetes SDK operations and cluster interaction |
| Agent-Runtime | Runtime lifecycle and execution profiles |
| Agent-Frameworks | Framework adapters such as LangGraph |
| Agent-Memory | Memory SDK and SurrealDB backend |
| Agent-Chat | Chat frontend |
| Agent-Dashboard | Operator dashboard |

## Relationship

```txt
GitHub Actions / CI
  ↓
Agent-deploy
  ↓
Helm/manifests/deployment workflows
  ↓
AgentKube or kubectl/helm
  ↓
Kubernetes cluster
```

## Agent-deploy owns

- GitHub Actions workflows
- Docker build workflows
- Helm charts
- Kubernetes manifests
- environment overlays
- release promotion
- deployment scripts
- rollback scripts
- deployment documentation

## Agent-deploy does not own

- Kubernetes SDK implementation
- runtime execution logic
- framework adapters
- identity verification
- memory backend logic

## First cloud-agent target

Deploy the k8smicro stack:

```txt
k3s cluster
  ↓
SurrealDB
  ↓
Agent-Runtime profile: k8smicro
  ↓
AgentKube
  ↓
Agent-Chat / Agent-Dashboard
```
