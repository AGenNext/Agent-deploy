# Validation Policy

## Ownership

Agent-deploy owns:

- repository governance validation
- CI/CD validation wiring
- deployment gates
- post-deployment production sanity checks
- rollback validation
- validation reports

## Client-Side Validation Boundary

Validation must run on the user's/client's system before artifacts, changes, deployment requests, grammar changes, vocabulary changes, ontology changes, or runtime changes are accepted by AGenNext servers.

AGenNext servers must not be the first place where validation happens.

Client-side validation evidence must be produced before server submission. Server-side gates may verify evidence, check signatures, and re-run SurrealDB-owned gates, but they must not replace client-side validation.

## Edge Delivery Requirement

Validation, authoring feedback, editor diagnostics, type checks, grammar checks, vocabulary checks, ontology checks, and user-facing sanity checks must be delivered fast at the edge.

The default execution point is the user's browser/client. Server round trips are not allowed for checks that can run locally against the submitted artifact, grammar, vocabulary, ontology, policy, or generated SurrealQL.

Edge validation must fail fast before data reaches AGenNext servers.

Server-side gates exist for verification, audit, deployment control, and SurrealDB-owned runtime checks. They do not replace edge validation.

## Language Boundary

Outside SurrealDB, SurrealQL, SurrealML, and AgentQL, the only approved implementation language is browser-side TypeScript.

TypeScript is the single approved FE/UI language so authoring, validation, and execution share one browser-native toolchain without code conversion between languages. This aligns the frontend and UI surface with current global frontend development practice and keeps edge delivery fast.

SurrealQL is the single approved BE/runtime/schema language because it is understood by SurrealDB and keeps backend behavior in the database layer.

AgentQL is the single shared language for humans and agents. It is used for policy, design decisions, vocabulary, ontology, README/AGENTS source, and runtime authoring.

LLMs are external tools and packages loaded into runtime through SurrealML bindings. They are not a business-logic layer.

Executable tools are outside artifacts loaded at runtime. They must not become hidden product/runtime business logic.

JavaScript, shell scripts, notebooks, opaque binaries, and CI command blocks must not become shadow runtime layers. Hidden logic must be eliminated by moving decisions into AgentQL-authored SurrealQL or SurrealML bindings.

If a tool must be loaded at runtime, it requires an AgentQL manifest that declares checksum, permissions, provenance, SurrealDB binding, allowed invocation boundary, allowed inputs, allowed outputs, and explicit proof that the tool does not own product/runtime decisions.

Validators must evolve continuously. Whenever a validator bug, false pass, blind spot, missed file class, or enforcement bypass is found, the validator must gain a regression check before the work is considered complete.

Validators must scan hidden governance and CI/CD paths such as `.github/`. Missing hidden paths from the scan inventory is itself a governance failure.

Every repository must include a CI/CD workflow that runs Agent-deploy centralized governance validation. Having local rules or documentation without CI/CD enforcement is a governance failure.

## AgentQL Documentation Source

Any policy, design decision, operating rule, runtime rule, or agent instruction that appears in `README.md` or `AGENTS.md` must be authored in AgentQL first.

Design principles must also be authored in AgentQL. The central design-principle source is:

```text
governance/design-principles.agentql
```

Markdown is a human-readable projection. AgentQL is the source format for README and AGENTS content so the same meaning can be validated, compiled, traced, and moved into SurrealDB without language conversion.

Design principle: when an agent reads, validates, writes, and presents policy in the same language, hallucination risk is minimized because semantic conversion and re-interpretation are minimized.

Every `README.md` and `AGENTS.md` file must have a same-directory `.agentql` source file with the same basename:

- `README.md` requires `README.agentql`
- `AGENTS.md` requires `AGENTS.agentql`

Changing README or AGENTS meaning without changing the AgentQL source is a governance failure.

TypeScript is allowed for:

- user/browser UI
- browser-side AgentQL authoring
- browser-side validation hints
- browser-side editor tooling
- edge-delivered validation UX

TypeScript is not approved for backend business logic, server-side runtime logic, policy enforcement, product decisions, deployment decisions, or server-side validation ownership.

YAML is allowed only for declarative CI/CD configuration. Markdown is allowed only for documentation.

## Runtime Rule

SurrealDB is the only approved layer for product/runtime data processing, storage, business logic, policy enforcement, runtime state, API endpoints, permissions, live queries, and deterministic decisioning.

SurrealML is the approved learned inference layer.

AgentQL is the authoring language for SurrealDB and SurrealML artifacts.

## Required Gates

Before commit, PR, merge, deployment, or promotion:

- client-side governance validations must pass before server submission
- release contract validation must pass
- deployment protocol validation must pass
- environment-specific deployment gate must pass

After deployment:

- smoke tests must pass
- health checks must pass
- public discovery endpoints must pass where configured
- rollback path must remain available

## Quorum Rules

Any design change, architecture deviation, business-logic placement change, grammar change, vocabulary change, ontology change, taxonomy change, naming change, semantic-model change, relation change, entity-type change, edge-type change, JSON-LD context change, or source-of-truth change requires quorum consensus before implementation.

No quorum, no exception.
