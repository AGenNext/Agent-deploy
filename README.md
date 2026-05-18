# Agent Deploy

Agent Deploy owns deployment, CI/CD, post-production operations, monitoring, and release automation for AGenNext agentic systems.

## Responsibility

Agent Deploy turns the platform into an operated production system.

It owns:

- CI/CD pipelines
- deployment manifests
- MicroK8s deployment automation
- release workflows
- rollback workflows
- monitoring setup
- alerting setup
- post-production checks
- incident response runbooks
- backup and restore runbooks
- operational readiness gates

## Consumers

- Agent-Platform
- Agent-Environment
- Agent-Secrets
- Agent-Knowledge
- Agent-Dashboard
- Agent-Site
- Agent-Team
- future AGenNext products

## Boundary

```text
Agent-Platform
  → assembles product and workspace

Agent-Environment
  → defines dev/test/staging/prod environment contracts

Agent-Secrets
  → defines secrets handling contracts

Agent-deploy
  → deploys, monitors, rolls back, and operates the platform
```

## Initial Deployment Target

```text
VPS + MicroK8s
```

## Core Principle

```text
Deployment is not done until monitoring, rollback, and post-production checks exist.
```
