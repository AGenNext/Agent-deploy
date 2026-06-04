# Gate Map — which product sits at which gate

**Status:** DRAFT · PRELIMINARY · incomplete.

Every surface is governed by a **gate** (secure · govern · enable · educate). Each
product sits at a surface and acts as its gate. This map is inferred from the
**AGenNext org survey only** (30 of 161 repos); **other GitHub orgs are not yet
surveyed**, and roles are inferred from descriptions, **not verified by inspection.**

| Surface / gate | Product(s) | Gate function | Standard layer |
|---|---|---|---|
| **Front door** (public web) | `Agent-Site`, `agennext.com` | educate / onboard | — |
| **Meaning** | `Agent-Vocabulary`, `Agent-Platform/agentql`, `Agent-Graph` | define | Agent-Language |
| **Instruction** (human↔machine) | *(Agent-Instructions)* | define / enable | Agent-Instructions |
| **Identity** | `Agent-Identity` | govern — *who* | AOM · Identity |
| **Tools / skills** | `Agent-MCPs`, `Agent-Harness` | enable | Agent-Harness-Protocol |
| **Memory / knowledge** | `Agent-Memory`, `Agent-Book` | enable — storage | AOM · Knowledge |
| **Security / guardrails** | `Agent-Guard` | secure | the gate |
| **Governance / rules** | `Agent-Constitution` | govern | AOM · Governance |
| **Build / develop** | `Agent-IDE`, `Agent-Harness` | enable | — |
| **Verify / review** | `Code-Review`, `Agent-Research` | verify — *the third* | Research-Foundation |
| **Measure / feedback** | `Agent-Analytics`, `Agent-KPIs`, `Agent-Bench` | analyse — the loop | AOM · Learning |
| **Deploy / operate** | `Agent-deploy` | govern / operate | Deployment |
| **Runtime / platform** | `Agent-Platform`, `Agent-Runtime`, `Agent-Cloud` | execute | Operating-Model |
| **Commerce / economy** | `Agent-Commerce`, `agennext.com` | transact | Agent-Economy |

## How to read it

A gate is **not a wall** — at each surface it does four things: **secure** (keep
bad actors out), **govern** (identity, policy, verification, compliance),
**enable** (tools, capability), **educate** (knowledge, meaning). Each product
above is one such gate, at one surface.

## The governance & security gate (detail)

This is the gate every change passes through before anything ships — it enforces
**commit checks, release checks, and repo boundaries:**

- **commit checks** → `Agent-Commit` + `Agent-deploy` validation (before every
  commit / PR);
- **release checks** → `Agent-deploy` (centralised governance validation before
  merge, deploy, promotion);
- **repo boundaries** → `Agent-deploy` (owns validation for all AGenNext repos —
  enforces what each repo may and may not do);
- **final review authority** → `Agent-Platform` (the accept/reject decision; no
  self-approval);
- **runtime guardrails** → `Agent-Guard` (security for agents at runtime);
- **the rules themselves** → `Agent-Constitution` (policy / governance
  definitions);
- **identity** → `Agent-Identity` (who — attributable).

> **`Agent-deploy` is the governance & security gate of the org** — the
> centralised validation every change passes through before commit, PR, merge,
> deploy, or promotion. Release checks, commit checks, repo boundaries: this is
> where they are enforced. *(This repo.)*

---

## What is missing (honest)

- **Other GitHub orgs** (e.g. OpenFrameworks-World, open-lmx) — not surveyed.
- **Verification by inspection** — roles are inferred from repo descriptions, not
  confirmed against actual code, CI, or deployment.
- **Readiness** — this maps *role*, not *launch-readiness*; that needs a per-repo
  audit.

To complete this map: survey the remaining orgs, pull each surface repo into
scope, and confirm role + readiness by inspection.
