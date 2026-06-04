# AGenNext Agent Standards

A layered set of **DRAFT / RFC** standards for building reliable, governed agent
systems. All are **open for ratification** (quorum consensus, no self-approval),
staged here in `agent-deploy`; their intended homes are the relevant AGenNext
repos.

---

## The stack (bottom → top)

### Foundations (theory)
- **`agent-theory.md`** — *everything is an agent.* The canonical entity, with
  identity, a guest in a human world; governed, not restricted.
- **`theory-graph.md`** — *everything is a graph / a loop.* Structure and motion;
  one step at a time; every loop and graph must **resolve**; three worlds
  (human · machine · agent) meet on the graph.

### Platform layer  ← entity · instruction · contract + protocols assemble here
- **`agent-language.md`** — the **contract of meaning**: one word, one meaning;
  the SQL of agents.
- **`agent-language-protocol.md`** — the **meaning handshake** (shared canonical
  meaning at exchange time).
- **`agent-instructions.md`** — **replace the prompt**: the CLI for agents;
  entity · instruction · contract.
- **`agent-harness-protocol.md`** — **skill · tool · protocol**: realise a
  skill's value through a governed tool.
- **`agent-operating-model.md`** — the **enterprise harness**: controllable +
  governable.

### Trust & value
- **`agent-research-foundation.md`** — the **verifier** (evidence, provenance —
  the third).
- **`agent-economy.md`** — the **triad at scale** (agents transacting; every
  transaction closed by a third).

---

## The platform layer

**Entity · Instruction · Contract**, together with the protocols, assemble into
the **platform layer** (`Agent-Platform`): the layer that hosts the language, the
instructions, the protocols, and the harness as **one running system.**

```
        Foundations (theory)         ← what is true
              ↓
        PLATFORM LAYER               ← entity · instruction · contract + protocols
              ↓                         (language, instructions, harness, run together)
        Trust & Value                ← verification, then economy
```

Below the platform is *theory*; above it is *trust and value*. The platform is
where the standards stop being documents and become a **system.**

---

## The one law

> **Two can act; only three can be trusted.**

Every layer installs a **third** — interpretant, verifier, witness:

- one word, one meaning (the contract is the third);
- one step at a time — now → next, never further (no hallucination);
- one identity per entity (no anonymous action);
- every loop **resolves**, every graph **resolves** (or the system hangs);
- every handoff, tool-call, and transaction is closed by a **third** (no
  self-approval).

Open to participate; governed to stay honest — open + the third = balance.

---

## On practice — yes, it is hard

Defining entity · instruction · contract for everything is **difficult to
practise.** It demands real work — identity for every entity, a defined contract
for every instruction, canonical meaning for every word — and it forbids the easy
free-text shortcut. That difficulty is honest, not hidden.

What makes it tractable:

- **Incremental, not upfront.** Do not define everything first. Define the
  **next** term and the **next** instruction as you need them — now → next. (You
  do not write every CLI command before using the shell.)
- **Federated.** Each field defines its own vocabulary and instruction set, so
  the work is distributed, not centralised.
- **Tooled.** The language (AgentQL), conformance checks, and programmatic tuning
  do the heavy lifting hand-crafting cannot.
- **"Enough," not "perfect."** Aim for enough defined meaning to **verify** — not
  a complete taxonomy of everything (Eco's unreachable perfect language).

> Prompts are easy to start and impossible to make reliable. Defined
> entity · instruction · contract is hard to start and the only path to
> reliability. The difficulty is the **price of reliability — paid
> incrementally**, one edge at a time.

---

## Status

All standards are **DRAFT / RFC**, pending quorum ratification. Verification
studies (active inference; IIT proxy divergence) are in [`../experiments`](../experiments).
