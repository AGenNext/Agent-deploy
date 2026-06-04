# Handoff Package

**Status:** READY FOR HANDOFF.
**From:** `agennext/agent-deploy` · PR #2 · branch `claude/ecstatic-ride-MigC3`.
**To:** receiving agents building `openautonomyx/platform`, `openautonomyx/site`,
`agentnext/platform`, `agentnext/site`.
**Protocol:** `propose → verify → commit` (no self-approval). This package is the
*propose*. The receiving agent *verifies* completeness + conformance, then
*commits* in the target repo.

---

## Quality bars (apply to everything)

1. **Review for language** — clear, consistent, correct.
2. **Simple language** — plain and accessible; remove jargon wherever it isn't
   load-bearing. Say it the simplest true way.
3. **Foundational** — frame as the *foundation*, not an add-on.
4. **Fundamental** — first-principles; start from the root (*two can act, only
   three can be trusted*) and build up.
5. **Grounded in research** — every claim backed by evidence (the verification
   experiments, cited sources); honest calibration, no hand-waving.
6. **First impression** — these are the **first articles anyone reads** when they
   visit the site. They are the **front door** — clear, compelling, and
   trustworthy from the first line.

> Simple, foundational, fundamental, research-grounded — and the first thing a
> visitor reads. That is the writing standard for every artifact that ships.

---

## Inventory (all portable markdown / python)

**Narrative & mission** — `MANIFESTO`, `FOUNDERS-LETTER`, `KEYNOTE`, `MISSION`,
`ZEN`
**Theory** — `agent-theory`, `theory-graph`, `theory-balance`
**Standards (RFC)** — `agent-language` (+`-protocol`), `agent-instructions`,
`agent-harness-protocol`, `agent-operating-model`, `agent-research-foundation`,
`agent-economy`
**Governance** — `canonical-design-principles`, `foundation-principle`, `glossary`,
`repo-boundaries`, `repo-standardization-protocol`, `agent-development-protocol`,
`agent-coding-protocol`, `agent-community-guidelines`, `community-contribution-model`,
`agent-landscape-maturity`
**Reference** — `DOCUMENTATION`, `gate-map`, `README` (index)
**Blog** — `what-is-now`, `where-the-world-will-go`, `what-we-will-do`,
`data-not-code`
**Site copy** — `site/landing`, `site/research`
**Verification** — `experiments/three_ball_active_reasoning.py` + `VERIFICATION`;
`experiments/iit_proxy_divergence.py` + `IIT_PROXY_TEST`

---

## Destination mapping

| content | destination |
|---|---|
| theory, standards (RFC), governance, manifesto/mission/zen/letter/keynote | **`*/platform`** |
| `site/*` (landing, research), `blog/*`, rendered manifesto/mission/zen | **`*/site`** |
| `canonical-design-principles`, `foundation-principle`, `glossary` | **Agent-Constitution** (canonical owner) |
| `experiments/*` | **research** |

---

## Receiving-agent instructions (per target repo)

```
instruction onboard_repo(repo, content):
  1. read(repo)
  2. pull(content)                     # portable markdown; copy in
  3. review_language(content)          # clear, simple, foundational, fundamental
  4. apply_standard_doc_set(repo)      # README, AGENTS.agentql, constitution,
                                       #   contracts, report, governance
  5. build_enterprise_ready(repo)      # CI green, security/compliance gates,
                                       #   deploy + rollback + monitoring;
                                       #   a11y + performance for sites
  6. verify(repo)                      # the gate / the third; no self-approval
  7. commit(repo) ; report
  on_fail: report + re-step            # good enough, then loop
```

---

## Conformance (must hold)

One word, one meaning · tangible-only · the third in every loop (no self-approval)
· protocol-first · only data is real · open + governed = balance · a human world.

> Build Better World — in a loop.
