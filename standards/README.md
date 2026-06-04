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

## Status

All standards are **DRAFT / RFC**, pending quorum ratification. Verification
studies (active inference; IIT proxy divergence) are in [`../experiments`](../experiments).
