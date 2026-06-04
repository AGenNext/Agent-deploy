# Documentation — list and format

The catalogue of everything in `standards/`, and the format each document follows.

---

## The document list

| document | type | RFC | purpose |
|---|---|---|---|
| `MANIFESTO.md` | manifesto | — | the declaration / vision / guarantee |
| `FOUNDERS-LETTER.md` | letter | — | the narrative, first-person framing |
| `KEYNOTE.md` | keynote | — | the launch-stage address |
| `README.md` | index | — | stack overview, roles, mission, opportunity |
| `agent-theory.md` | foundation | — | everything is an agent (entity, identity) |
| `theory-graph.md` | foundation | — | everything is a graph / loop; must resolve |
| `theory-balance.md` | foundation | — | balance is conserved; keeps moving |
| `agent-language.md` | standard | RFC-2 | the contract of meaning (SQL of agents) |
| `agent-language-protocol.md` | standard | RFC-7 | the meaning handshake |
| `agent-instructions.md` | standard | RFC-1 | replace the prompt; the CLI for agents |
| `agent-harness-protocol.md` | standard | RFC-6 | skill · tool · protocol |
| `agent-operating-model.md` | standard | RFC-3 | the enterprise harness |
| `agent-research-foundation.md` | standard | RFC-4 | the verifier (the third) |
| `agent-economy.md` | standard | RFC-5 | the triad at scale |
| `gate-map.md` | reference | — | which product sits at which gate |
| `DOCUMENTATION.md` | reference | — | this catalogue + format |

---

## The standard format

Every **standard** (RFC) document follows this format:

1. **Title** — `# Name`
2. **Status line** — `DRAFT · RFC-N · open for ratification`
3. **Scope note** — where staged, intended home repo, governance (quorum, no
   self-approval)
4. **Essence / Thesis** — one blockquote stating the core in a sentence
5. **Body** — the principles, one section each
6. **Place in the stack** — how it sits relative to the other layers
7. **Openness / governance** — open + the third

**Foundations** (`*-theory*`, `theory-*`) are notes: title, status, the claim
(blockquote), why, honest scope. **Narrative** docs (manifesto, letter, keynote)
have no RFC number. **Reference** docs (gate-map, this) are tables + honest
caveats.

---

## Conventions

- Filenames: lowercase, hyphenated, `.md` (narrative/reference docs may be
  UPPERCASE for prominence).
- Every normative claim is **tangible** (observable, verifiable); intangibles use
  a tangible proxy.
- Every document is **DRAFT / RFC**, ratified by **quorum consensus** — no
  self-approval. Meaning changes are governed by `language_change_quorum`.
- Honest calibration is required: state what is verified vs. aspirational; never
  overclaim (no Babel).

---

## Status

All documents are **DRAFT / RFC**, staged in `agent-deploy` (authoring scope),
pending quorum ratification and placement in their intended home repos.
