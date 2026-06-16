# Agent-Coding Protocol

**Status:** DRAFT · owned by `Agent-deploy`.

> How an agent writes code: **small, grounded, run-and-tested steps — the third is
> execution.** Never vibe-code; never trust unrun code.

---

## Why

`prompt → code` is a dyad with no verifier: errors are **silent and compounding.**
Code becomes trustworthy only when a **third — execution (run, test, types,
review)** — verifies it. (See *why vibe coding fails*: undefined meaning + reaching
past *next*.)

---

## The coding loop

```
read → write one step → run → test → (fix → run)* → review → commit → next
```

Each step must **resolve** (green) before the next.

---

## The protocol (as Agent-Instructions)

```
instruction code(change):
  1. read(codebase)   -> grounded context     # read before write; no inventing APIs
  2. write(one_unit)  -> one function / edge   # one step, now -> next, never further
  3. compile + lint   outcome: parses, types ok # mechanical verification (defined meaning)
  4. run + test       outcome: tests pass        # the third = execution
  5. fix -> run       until green                # loop until resolved
  6. review           outcome: approved by a third # no self-approval
  7. commit           outcome: governed checks pass # Agent-deploy validation
  on_fail: report + re-step
```

---

## Rules

- **Ground in the actual codebase** — read before write; **never invent**
  APIs/symbols (that is hallucination).
- **One unit at a time** — now → next, never further.
- **Run and test every step** — the third is execution; *unrun code is
  unverified.*
- **Types / lint / compiler are mechanical truth** — defined meaning, checked
  before it runs.
- **No self-approval** — review + CI.
- **Good enough, then loop.**

---

## Reuse & simplicity

Prefer **reusing** what exists (know the codebase first); **match** the
surrounding style; make the **simplest** change that resolves the step.

---

## Multiple agents

Partitioned by **module / file** (no overlap); **verified handoffs**
(`propose → verify → commit`); the **third** closes each.

> Code in a loop, one tested step at a time. The third is execution. **Strive for
> better.**
