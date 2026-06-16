# Agent-Development Protocol

**Status:** DRAFT · owned by `Agent-deploy`.

> How an agent develops software: **one defined, verified step at a time, in the
> build loop, under governance — never a prompt, never self-approved.**

---

## The development loop

```
build → deploy → test → review → analyse → gather feedback → build → …
```

The human evolution loop, governed and verified. Every turn must **resolve**.

---

## The protocol (as Agent-Instructions)

For each development task:

```
instruction develop(task):
  1. define(task)        -> intent + defined outcome           # DEFINE
  2. align(task)         -> consistent with graph + boundaries  # ALIGN
  3. propose(step)       -> the single next change              # one edge
  4. implement(step)     -> change written                      # now -> next, never further
  5. ground(step)        outcome: acts only on known state      # no inventing
  6. test(step)          outcome: runs + verifies the outcome   # the third (CI)
  7. review(step)        outcome: approved by a third           # no self-approval
  8. commit(step)        outcome: governed validation passes    # Agent-deploy checks
  9. analyse + feedback  -> next step
  on_fail: report + re-step                                     # good enough, then loop
```

---

## Rules

- **Defined instructions, not prompts** — the common language; one word, one
  meaning.
- **One step at a time** — now → next, never further (reaching further =
  hallucination).
- **Ground every step** — act only on known state; never invent.
- **No self-approval** — test + review are the **third**; nothing self-certifies.
- **Every commit governed** — `Agent-deploy` validation (commit checks, release
  checks, repo boundaries).
- **Good enough, not perfect** — ship the pass; the loop improves it.

---

## Multiple agents

Partitioned: each agent **claims a task** (no overlap); handoffs are **verified**
(`propose → verify → commit`); the **third** closes each. Each updates `report.md`.

---

## Outcome & measurement

Every task has a **defined, verifiable outcome**, measured on **CLEAR** — Cost,
Latency, Efficacy, Assurance, Reliability — and fed back into the next turn.

> Develop in a loop, one verified step at a time. **Strive for better.**
