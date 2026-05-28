# Agent Deploy

Agent Deploy owns deployment, CI/CD, post-production operations, monitoring, and release automation for AGenNext agentic systems.

## Responsibility

Agent Deploy turns the platform into an operated production system.

It owns:

- centralized governance validation
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

## Central Validation Ownership

Agent-deploy owns validation for AGenNext repositories.

`README.md` and `AGENTS.md` content must be authored in AgentQL first. Markdown is a human-readable projection of AgentQL policy and design meaning.

Editable validation rules live in:

```text
governance/
```

Run governance validation for any repo:

```bash
./scripts/validate_repo_governance.sh /path/to/repo
```

Agent-Commit, Agent-Platform, and deployment workflows must consume Agent-deploy validation before commit, PR, merge, deployment, or promotion.

Validation must run on the user's/client's system before any change is accepted by AGenNext servers.

Outside SurrealDB, SurrealQL, SurrealML, and AgentQL, the only approved implementation language is browser-side TypeScript. TypeScript is not approved for backend business logic, server-side validation ownership, deployment decisions, or runtime policy enforcement.

TypeScript is the single FE/UI language so browser authoring, validation, and execution stay in one toolchain without code conversion. This keeps the UI surface aligned with current frontend development practice and supports fast edge delivery.

SurrealQL is the single BE/runtime/schema language because it is understood by SurrealDB. AgentQL is the shared language for agents and humans. LLMs and executable tools are external runtime-loaded artifacts through SurrealML/tool bindings, not business-logic layers.

Validation and authoring feedback must be fast and delivered at the edge. Checks that can run locally must run in the user's browser/client before server submission.

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
