# Agent-Harness-Protocol

**Status:** DRAFT · RFC-6 · open for ratification
**Scope note:** Staged in `agent-deploy`. Intended home: `Agent-Platform`.
Adoption requires **quorum consensus** and **no self-approval**.

---

## Essence

> **Everything is a skill. A tool is the harness that realizes the value from a
> skill. The Agent-Harness-Protocol governs how an agent binds a tool to a skill
> to realize value.**

This is the capability layer: agent (entity) **has** skills (capabilities), and
**uses** tools (harnesses) to turn those skills into realized value.

---

## The triad — skill · tool · protocol

The capability layer is itself a triad:

- **Skill** — the *potential* (what can be done),
- **Tool** — the *harness* (how it is realised),
- **Protocol** — the *third* that binds them (governs and verifies the realisation).

Skill + tool alone is **ungoverned tool-calling** — a line, a gap, blind
execution. The **protocol** is the third that makes the call **authorised,
bounded, and verified.** *Two would call the tool; three make it trustworthy.*

---

## Everything is a skill

At the capability level, everything an agent can do is a **skill** — a defined
capability to produce a specific outcome. The agent is the entity; the skill is
what it can do.

---

## Skill is potential; the tool realizes it

- A **skill** is *potential* — the ability to produce an outcome.
- A **tool** is the **harness** that turns that potential into **realized value**
  — what lets the skill actually act on the world.

> A skill without a tool is unrealised. The tool is the harness that **releases
> the value** from the skill.

---

## The protocol

How an agent binds a harness (tool) to exercise a skill — governed and verified,
in the same three-step shape as every handoff (because realising a skill through
a tool is a transaction, and a transaction needs a third):

1. **Propose** — the agent requests a skill, naming the tool/harness, typed
   inputs, and the intended outcome.
2. **Verify** — the harness (the third) checks **authorisation**, validates inputs
   against the contract, and **bounds** the action (identity, policy, constraint,
   budget).
3. **Commit** — the tool runs; the outcome is produced and **verified against the
   skill's defined outcome.** Value realised, accounted, logged.

> Propose → Verify → Commit. Two would call the tool blindly; the third makes the
> call **authorised, bounded, and verified.**

---

## Governed

Using a tool is a **governed action**: attributable (identity), bounded
(constraints/budget), observable (events), reversible where possible. The harness
controls the tool the way the operating model controls the agent — *autonomy must
be governed* applies to tool-use too.

---

## Relation to existing protocols

This is the **contract layer above tool-calling** (e.g. MCP). MCP *connects* an
agent to a tool; the Agent-Harness-Protocol *governs* that connection — defining
the skill, the value, the verification, and the accountability of every call.

---

## Place in the stack

```
Agent (entity, identity)
  has → Skills (capabilities)
  uses → Tools (harnesses) via the AGENT-HARNESS-PROTOCOL  ← realises value
        inside the Operating-Model (governed)
        verified by the Research-Foundation
        transacted in the Economy
```

---

## Openness

Open protocol — anyone may define **skills and tools for their field**,
conforming to the protocol and verified by the third. Skills and tools are
**federated**; the protocol that realises them is **common.**
