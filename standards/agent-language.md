# Agent-Language (AgentQL)

**Status:** DRAFT · RFC-2 · open for ratification
**Scope note:** Staged in `agent-deploy` (write-scope of the authoring session).
Intended home: `Agent-Platform/agentql`. Adoption requires **quorum consensus**
and **no self-approval**.

---

## The theorem

> **Agent and human must hold the same meaning for any word.**
> **Language is the contract that gives a word its meaning.**
> **No contract → the meanings diverge → the system does not work.**

Two parties — human↔agent or agent↔agent — can coordinate only if a word means
the same thing to both. Meaning is **not intrinsic** to a word; it is *granted*
by a shared contract (a defined language). Without that contract, each party
supplies its own interpretation, the meanings drift apart, and every instruction,
handoff, and transaction built on the word fails.

This is precisely why prompts fail and why agent-to-agent fails: free text has no
contract, so no two parties are guaranteed the same meaning. **AgentQL is that
contract** — the defined language that makes a word mean the same thing to human
and agent alike. Everything else in this standard follows from this one theorem.

---

## Thesis

> **AgentQL is the SQL of agents.**

One open, declarative, vendor-neutral language for defining agent **vocabulary,
ontology, policy, constraints, and instructions** — with defined meaning,
compiling to runtimes. SQL gave every program one defined way to mean the same
thing to any database; AgentQL gives every agent one defined way to mean the same
thing to any other agent.

---

## We define the language; everyone defines their content

- **We define AgentQL — because we invented it.** Its grammar and semantics are
  ours to specify, governed by **quorum consensus** (no self-approval). This is
  the SQL pattern: a standard defined by its body.
- **Everyone defines their own content *in* it.** Vocabularies, ontologies,
  instruction sets — each person and field declares their own, in AgentQL.

> **We own the language. You own the content.** Separation of duty, one layer up:
> the language is the form; your declarations are the matter.

---

## It is a language, not a framework

There are already many agent **frameworks** — so the honest question is why a
language at all. The answer is that they are a *different category*:

- **Imperative frameworks** (LangChain, AutoGen, CrewAI, LlamaIndex) are
  libraries: code you write to orchestrate prompts. They are vendor-specific,
  carry no defined meaning, and do not interoperate.
- **Protocols** (MCP, A2A) are interface/transport — necessary, but not a full
  declarative language for *defining* agent vocabulary, policy, and instructions.
- **AgentQL is a declarative language + open standard.** You declare *what*
  (vocabulary, ontology, policy, instructions) with pinned meaning; it compiles
  to runtimes; it is vendor-neutral. SQL is not a "database framework" — and
  AgentQL is not an agent framework.

It replaces bespoke prompt-orchestration the way **SQL replaced bespoke
data-access code**: from imperative glue to a declared, standardised contract.

> Honest caveat (the "yet another standard" risk is real): a new standard earns
> its place **only** by being genuinely open, vendor-neutral, conformance-tested,
> backed by a reference engine, and *adopted*. The differentiation must be
> substantive — a real language with defined semantics — not a renamed framework.

---

## Declarative — say what, not how

Like SQL, you declare the specification; the compiler produces the **executable
artifacts** (reference target: SurrealDB). The language compiles directly to the
runtime — it does not create a separate business-logic layer.

---

## Separation of duty — spec ≠ engine

This is the move that makes a language *global*:

- **The language** = an open, versioned **specification** (grammar + semantics),
  governed by quorum, owned by **no single runtime**.
- **The runtime** = SurrealDB as the **reference implementation** — the first and
  best compiler target, but *one engine among many*. Others may build AgentQL →
  their-runtime compilers.

SQL became universal precisely because the spec was decoupled from the engine
(ANSI SQL the standard; Postgres/Oracle the implementations). AgentQL must hold
the same line: **SurrealDB executes the language; it does not own its meaning.**

---

## Protocol, not taxonomy · tangible only

- **Protocol, not taxonomy.** The grammar is *generative* — it defines the rules
  by which any conforming construct is declared, not a fixed central catalogue of
  what may exist.
- **Tangible only.** It defines observable, verifiable constructs (vocabulary,
  ontology, policy, capability, constraint, instruction). Intangibles
  (belief/mind) are excluded or expressed as **tangible proxies** (a recorded
  proposition + evidence + confidence; a declared, logged objective).

---

## What makes it a standard (not a library)

1. **Open, versioned specification** — grammar + formal semantics (AgentQL 1.0).
2. **Reference compiler** — SurrealDB target; proof it runs.
3. **Conformance suite** — so any AgentQL tooling can *prove* it is compliant.
   This is what makes a language a standard rather than a product.
4. **Governance body** — quorum consensus, no self-approval, open participation.

---

## Place in the stack

```
Vocabulary · Graph · Grammar
        ↓
   AGENT-LANGUAGE (AgentQL)        ← we define this
        ↓
   Agent-Instructions             ← written in it; everyone defines their sets
        ↓
   Agent-Operating-Model          ← built on it
        ↓
   Agent-Research-Foundation      ← verifies it
        ↓
   Agent-Economy                  ← transacts on it
```

---

## Openness

Published **open**, with the verifier (the third) enforced:

- **Closed** → capture.
- **Open, no third** → chaos.
- **Open + the third** → balance.

We define the language; everyone builds on it; the verifier keeps it honest.
