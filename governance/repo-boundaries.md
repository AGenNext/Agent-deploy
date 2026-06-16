# Repo Boundaries & Standard Documentation Set

**Status:** DRAFT · owned by `Agent-deploy` (centralised governance validation).

> A duplicate is two repos owning the same thing. A boundary is one repo owning
> it and the others **referencing**, never copying. Boundaries are enforced by
> `Agent-deploy` validation before commit, PR, merge, deploy, or promotion.

---

## The standard documentation set (every repo MUST have)

| file | purpose | authored in |
|---|---|---|
| `README.md` | human-readable projection | AgentQL first |
| `AGENTS.agentql` → `AGENTS.md` | agent instructions / repo constitution | AgentQL first |
| `constitution` | the repo's rules (Agent-Constitution conformant) | AgentQL |
| `contracts/` | what the repo provides / consumes | markdown + AgentQL |
| `report.md` | current status report | markdown |
| `governance/` | validation rules (where the repo owns validation) | rules/AgentQL |

---

## Boundaries (preliminary — AGenNext)

| repo | owns | references (does NOT own) |
|---|---|---|
| `Agent-Vocabulary` | defined words (`DefinedTerm`) | relationships, rules |
| `Agent-Graph` | relationships (edges) | words, rules |
| `Agent-Platform/agentql` | the language (grammar) | content (vocabularies) |
| `Agent-Instructions` | instruction sets | the language |
| `Agent-Platform` | platform assembly + **final review authority** | components |
| `Agent-deploy` | deploy/operate + **validation + repo boundaries** | building products |
| `Agent-Guard` | runtime guardrails | the rules (Constitution) |
| `Agent-Constitution` | the rules | enforcement (deploy) |
| `Agent-Identity` | identity | everything else |
| `Agent-Research` | evidence / evaluation | the decision (Platform) |
| `Agent-Economy` | transactions / marketplace runtime | the standard (defines it) |

---

## Candidate duplicates — to resolve

- `Agent-Economy` (empty repo) **vs** `standards/agent-economy.md` → the *repo*
  hosts the runtime/product; the *standard* defines it. Assign + reference.
- `Agent-Theories` (empty Astro) **vs** `standards/*theory*.md` → the site
  *renders*; the standards *define*. Relocate standards to intended home.
- `Agent-Harness` (Go, DX/CI-CD) **vs** `agent-harness-protocol` (spec) → distinct
  (product vs protocol); document the distinction explicitly.
- `Agent-Foundation` (Go) **vs** `OpenFrameworks-World/foundation` (ontology) →
  overlapping "foundation"; define distinct boundaries or merge.
- All `standards/*` here are **STAGED in agent-deploy** → relocate to intended
  homes (Agent-Platform, Agent-Constitution, Agent-Theories, Agent-Economy).

---

## Resolution rule

Assign **one owner** per concern; all others **reference** it. No copy. Boundary
violations are caught by `Agent-deploy` validation.

## Honest scope

Preliminary: **AGenNext only (30 / 161 repos)**; **other orgs not surveyed**;
roles inferred from descriptions, **not verified by inspection**. Complete by
surveying every org and inspecting each repo.
