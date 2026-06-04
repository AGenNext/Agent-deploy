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

## Canonical meaning (corollary of the theorem)

> **One word, one meaning — one thing only. No ambiguity, ever.**

Every word in the language has exactly **one canonical meaning** — a single
authoritative definition held in the vocabulary. *Canonical* means: one meaning,
one source of truth, change-controlled. (Natural language can't do this —
polysemy is everywhere — which is *why* we leave it for a defined, namespaced
vocabulary, where one-term-one-meaning is enforceable.)

- A word may **not** carry two meanings. If a context needs a different sense, it
  is a **different, namespaced term** — never a redefinition.
- **Canonical within a namespace; federated across them.** Each field may define
  its own vocabulary, but inside any one context a word resolves to exactly one
  meaning. (This reconciles "everyone defines their own set" with "words must
  have canonical meaning": federation *across* namespaces, canonicality *within*.)

Canonical meaning is what makes the theorem **enforceable**: agent and human can
share a word's meaning only if that meaning is **single and fixed**, not supplied
per interpreter.

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

## Implementation — built on Langium

The language is not only a specification; it is a **working language**, built on
**[Langium](https://eclipse-langium.github.io/langium/)** — the open-source
**Eclipse Foundation** TypeScript language-engineering framework (the web-era
successor to Xtext). Langium gives AgentQL:

- a **grammar** (the `.langium` definition),
- a **parser** and a **type-safe AST**,
- **validation rules** — meaning is enforced mechanically; the parser **rejects**
  undefined or ill-formed input,
- **editor tooling** (language server / LSP: completion, live errors, navigation),
- **code generation** — compile to the runtime (SurrealDB reference target).

This is what makes the standard **executable, not merely descriptive**: meaning is
enforced by a parser and validator, so *"one word, one meaning"* and *"defined,
not described"* are **mechanical guarantees**, not aspirations. Langium provides
the engineering; the spec, vocabulary, and conformance suite make it a *standard*.

> **Built with rigour and mechanically validated — not just any random language.**
> A formal grammar, a parser, a typed AST, and validation rules mean every
> construct is **checked before it runs.** AgentQL is *engineered*, not improvised
> — and that rigour is precisely why it can be trusted to carry meaning, where an
> ad-hoc convention cannot.

> **Maturity (honest status):** rigorously built and validated, but **not yet
> fully optimised.** The grammar, vocabulary, and code generation are still
> evolving (DRAFT / RFC, refined under `language_change_quorum`). Validated and
> principled — not yet final.

> **Optimisation reduces nodes.** As the language is optimised, the *number of
> nodes may fall* — redundant terms collapse into fewer, more fundamental ones.
> Optimisation is **compression**: converging on the **minimal canonical set** of
> primitives that still covers the domain (maximum meaning, minimum redundancy).
> Fewer nodes, same coverage — the language gets *smaller and sharper*, not
> bigger. (This is the disentanglement / minimum-redundancy prior in action.)

> **But every node reduction must preserve resolution.** A reduction is valid
> only if, afterwards, the **graph still resolves** — every edge still lands on a
> node, every term still resolves to its canonical meaning, every loop still
> closes. Optimisation may make the graph *smaller*; it may **never** make it
> *unresolvable*. Resolution is the invariant every reduction must preserve — and
> reductions, being meaning changes, are **quorum-gated** (`language_change_quorum`).

---

## Grounded in Schema.org (JSON-LD)

The vocabulary is **not invented from scratch** — it is expressed in **Schema.org
JSON-LD**: a vocabulary word is a `schema:DefinedTerm`, a collection a
`schema:DefinedTermSet`. We build on the existing, widely-adopted web standard
rather than reinvent it (*know what already exists; innovation is the next edge*).

JSON-LD is itself a **graph** format — and that is not incidental. The vocabulary
is nodes, the relations are edges, the whole model is a graph. See the graph
foundation (`theory-graph.md`).

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

## Governance — meaning is change-controlled

Meaning is the most load-bearing thing in the system, so every change to it
passes through the distributed third (quorum) **before** it takes effect. No one
redefines a word alone.

```
rule language_change_quorum:
  "Any grammar, vocabulary, ontology, taxonomy, schema-language, naming,
   semantic-model, domain-term, relation, entity-type, record-type, edge-type,
   JSON-LD context, or meaning change requires quorum consensus before
   implementation."
```

This is separation of duty applied to **meaning itself**: propose a change →
quorum ratifies → it is implemented. Canonical meaning stays canonical precisely
because no single party may move it.

---

## Openness

Published **open**, with the verifier (the third) enforced:

- **Closed** → capture.
- **Open, no third** → chaos.
- **Open + the third** → balance.

We define the language; everyone builds on it; the verifier keeps it honest.
