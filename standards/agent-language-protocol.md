# Agent-Language-Protocol

**Status:** DRAFT · RFC-7 · open for ratification
**Scope note:** Staged in `agent-deploy`. Intended home: `Agent-Platform`.
Adoption requires **quorum consensus** and **no self-approval**.

---

## Essence

> **The Agent-Language-Protocol is how parties exchange meaning so that all hold
> the same canonical meaning.**

The Agent-Language standard *defines* meaning (one word, one meaning). This
protocol *exchanges* it — enforcing the theorem (*agent and human must hold the
same meaning for any word*) at the moment two parties communicate.

---

## The triad — sender · receiver · canonical definition

When two parties exchange a word, they cannot guarantee shared meaning alone —
each resolves it privately, and the meanings drift. The **third** is the
**canonical definition** in the vocabulary, which both resolve against:

- **Sender** references a term,
- **Receiver** resolves a term,
- **Canonical definition** (the third) is the single meaning both reach.

*Two parties assume shared meaning; the third confirms it.*

---

## The meaning handshake

1. **Propose** — the sender references a term by its **canonical id** (namespace
   + version), not bare text.
2. **Verify** — the receiver resolves the **same canonical definition** and
   confirms the match.
3. **Commit** — shared meaning is established; the exchange proceeds.

If the resolved definitions differ (wrong namespace or version), the exchange
**fails closed** — no party acts on divergent meaning. (This is the typed-handoff
rule of Agent-Instructions, applied to meaning itself.)

---

## Canonical resolution

The shared third is the **canonical vocabulary** — Schema.org JSON-LD,
`DefinedTerm` / `DefinedTermSet`, governed by `language_change_quorum`. The
protocol resolves every term to its **versioned canonical definition**, so the
same word means the same thing across the whole exchange:

> **One word, one meaning, one source of truth** — and the protocol is how both
> parties reach it.

---

## Governed

Meaning changes are quorum-gated; the protocol references **versioned** canonical
definitions, so meaning stays stable while an exchange is in flight. No party may
redefine a word mid-conversation.

---

## Relation to the other protocols

| protocol | governs | the third |
|---|---|---|
| **Agent-Language-Protocol** | exchange of **meaning** | the canonical definition |
| **Agent-Harness-Protocol** | realisation of a **skill** via a tool | the protocol/verifier |
| **Agent handoff** (Instructions) | transfer of **work** | the verifier |

All three are the same triad: two parties, one third that closes the loop.

---

## Place in the stack

```
Agent-Language (defines meaning)
        ↓
AGENT-LANGUAGE-PROTOCOL (exchanges meaning with guaranteed agreement)
        ↓
Agent-Instructions · Agent-Harness-Protocol · Agent-Operating-Model · ...
```

---

## Openness

Open protocol; the canonical vocabulary is open and versioned. Everyone resolves
against the same shared definitions — open to read, governed to change.
