# Repo Standardization Protocol

**Status:** DRAFT · owned by `Agent-deploy`.

A protocol for standardising **every repo** — one at a time, in a loop, across
**multiple agents in parallel**, in **one pass**, **good enough, not perfect.**

---

## Principles

- **One repo at a time, in a loop.** Each repo is a turn of the build loop.
- **One pass over everyone.** Cover every repo once before deepening.
- **Good enough, not perfect.** A first pass that can be re-run; the loop improves
  it. *Better, not perfect.*
- **Partitioned.** Divided so multiple agents work in parallel without collision.

---

## The per-repo loop (one repo at a time)

```
read → apply standard set → record boundary → flag duplicates → verify → commit → next
```

1. **read** the repo's current state;
2. **apply the standard doc set** — `README.md`, `AGENTS.agentql`→`AGENTS.md`,
   `constitution`, `contracts/`, `report.md`, `governance/` — fill what's missing;
3. **record the boundary** (what it owns / what it references) in `repo-boundaries.md`;
4. **flag duplicates** against the candidate list;
5. **verify** (Agent-deploy validation; **no self-approval**) → **commit**;
6. **next repo.**

---

## Expressed as Agent-Instructions (the common language)

The protocol is given to agents as **defined instructions**, not prose — so every
agent reads the **same meaning** (per the Agent-Instructions standard). One word,
one meaning; clear for agents; no prompt ambiguity.

```
instruction standardize_repo(repo):
  precondition:  repo is claimed by this agent      # no overlap
  1. read_repo(repo)            -> repo_state
  2. ensure_doc(repo, README.md)        outcome: present, AgentQL-projected
  3. ensure_doc(repo, AGENTS.agentql)   outcome: present, AgentQL-authored
  4. ensure_doc(repo, constitution)     outcome: present, Constitution-conformant
  5. ensure_doc(repo, contracts/)       outcome: present
  6. ensure_doc(repo, report.md)        outcome: present
  7. record_boundary(repo)     -> entry in repo-boundaries.md
  8. flag_duplicates(repo)     -> duplicate candidates
  9. verify(repo)                       outcome: Agent-deploy validation passes  # the third
 10. commit(repo)                       outcome: committed, no self-approval
  postcondition: repo conforms to the standard doc set; outcome verified
  on_fail:       report + leave for next pass         # good enough, not perfect
```

Each instruction is **named, typed, outcome-defined, and verified** — the
canonical instruction set every standardisation agent runs. Defined meaning, not
a prompt.

---

## Partitioning for multiple agents

Divide the repo set into **portions**; assign one portion per agent; agents run in
parallel. The coordination protocol:

- **assignment** — each agent **claims a portion** (a list of repos); **no two
  agents own the same repo** (no overlap → no conflict);
- **handoff** — completed repos handed off via the verified handoff
  (`propose → verify → commit`); `Agent-deploy` validates;
- **no self-approval** — each agent's pass is verified by a **third** (review /
  CI) before merge;
- **report** — each agent updates `report.md` for its portion.

This is the **agent-handoff-protocol + governance**, applied to the
standardisation work itself — multiple agents, one graph, the third closing each
handoff.

---

## The loop continues

After one pass, **loop again** — each pass raises quality. Never perfect; always
better. *Strive for better — in a loop.*
