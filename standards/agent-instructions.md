# Agent-Instructions

**Status:** DRAFT · RFC-1 · open for ratification
**Scope note:** Staged in `agent-deploy` (write-scope of the authoring session).
Intended home: the `Agent-Instructions` repository. Per AGenNext governance,
adoption requires **quorum consensus** and **no self-approval**.

---

## Thesis

> **For reliable AI, the prompt must be replaced with the instruction.**

A prompt is free text with no defined meaning and no verifiable outcome — so its
result is variable and unaccountable. An instruction is a defined, validated,
outcome-bound contract — so its result is predictable and verifiable. Reliability
is impossible on prompts and native to instructions.

> **"Prompt" is not a defined term in this standard.** It is the construct being
> replaced. The standard defines **instructions only** — a thing without defined
> meaning cannot itself be defined; it can only be superseded.

## Entity · Instruction · Contract — the prompt is obsolete

Give an **entity** (an agent with identity) an **instruction** (a defined
command) under a **contract** (shared canonical meaning), and the **prompt is no
longer needed.** These three carry everything a prompt tried to:

- **Entity** — *who* acts (identity, from Agent Theory),
- **Instruction** — *what* to do (a defined command, this standard),
- **Contract** — the *meaning* both agree on (Agent-Language).

Who, what, and the shared meaning — nothing is left for free text to carry.

---

## Purpose

An instruction to an agent is a **contract, not a prompt.** It is validated
against a defined grammar *before* it runs.

This standard exists to remove the conditions that produce hallucination.
Hallucination has exactly two causes:

1. **Undefined meaning** — given a vague term, a model fills the gap with
   plausible fiction.
2. **Reaching past *next*** — asked to leap, a model asserts nodes it never
   traversed.

Free-text prompts cause **both**. Defined instructions remove **both**.

> Honest calibration: this does not make any model 100% accurate. It removes the
> *conditions* under which hallucination occurs and **catches the remainder**
> before it is committed. The claim is structural, not magical:
> *the agent is never allowed to invent.*

---

## What it is — a canonical library of instructions (the CLI for agents)

Agent-Instructions is not only the rules below; it is a **canonical, versioned
library of defined instructions** — the equivalent of a **CLI for applications**,
but for agents.

A CLI works because it is a *finite, defined* command set. You don't address
`git` in free English; you invoke `git commit -m "..."` — a command with defined
syntax, defined inputs, defined behaviour, and a predictable result. **The CLI
*is* the contract.** That is why CLIs are reliable, composable (pipes), and
scriptable.

Agents get the same. Instead of free-text prompts, an agent invokes **defined
instructions** from the canonical library. Each instruction is:

- **named** — a canonical verb;
- **typed inputs** — defined arguments, drawn from the vocabulary;
- **defined behaviour** — the method it performs;
- **a verifiable outcome** — the result it is contracted to produce; and
- **the optimal method** — the best-known, curated, benchmarked way to reach that
  outcome, so the result is not merely *correct* but *optimal*.

**Outcome-defined.** An instruction is identified by the **outcome** it produces,
and the third (Rule 4) verifies that the outcome was *achieved* — not that the
agent "tried," but that the result matches. Optimality is **measured** (efficacy
/ outcome metrics), so the library converges over time on the best instruction
for each outcome.

**Composable.** Like CLI pipes, instructions chain through defined handoffs
(Rule 5): the verified outcome of one is the typed input of the next.

> Free prose → variable, unverifiable results.
> A canonical instruction library → defined commands → **optimal, verifiable outcomes.**

---

## Reject prompt engineering

Prompt engineering is the practice of **tuning free text by trial and error** to
coax reliable behaviour out of an undefined medium. As a foundation for reliable
AI it fails for structural reasons — and the waste is collective:

- **It doesn't transfer.** A prompt tuned for one model/version breaks on the
  next. Every team re-tunes from scratch.
- **It can't be versioned or verified.** With no defined outcome to check
  against, "better" is guesswork.
- **It doesn't compose.** Prompts don't pipe; you cannot build reliably on them.
- **It compensates for a missing standard.** The effort patches the *absence* of
  a defined instruction — work that disappears the moment the instruction exists.

The result is **time wasted for everyone**: the whole field re-deriving fragile
prompts that a single canonical instruction would settle once. Define it once,
reuse it everywhere — like a CLI command. That ends prompt engineering *as a
reliability practice.*

**Scope of the rejection (so it holds).** Free text remains the right tool for
**open-ended language work** — writing, brainstorming, translation — where there
is no defined outcome to verify. The rejection is precise: *prompt engineering is
the wrong tool for **reliable, outcome-bound** agent operations.* There it is
replaced by instructions. (This mirrors the existing rule: "LLMs are tools for
open-ended language work only.")

---

## Federated instruction sets — defined by each field

The standard defines the **form** of an instruction — the rules, the grammar, the
outcome contract. It does **not** dictate every instruction. The instructions
themselves are **defined by the people who do the work**, field by field.

- **The standard owns the form.** The five rules, the tangible-only scope,
  outcome-definition, and verification apply to every instruction, everywhere.
- **Each field owns its set.** Medicine, law, finance, devops, support,
  research — each domain defines its own **canonical instruction set**, because
  its practitioners hold the knowledge of the *optimal* method for their
  outcomes. They namespace their set and conform to the standard.
- **Governance is separation of duty.** The form is governed by quorum (the
  distributed third); each field's set is owned and ratified by that field's
  authority and checked by the verifier. No single body defines all instructions.

This is the **federated, open** model — one standard, many domain sets — exactly
how the internet scaled (one TCP/IP, many protocols from many communities) and
how CLIs scaled (one shell, many tools: `git`, `docker`, `kubectl`).

> Open the gates: anyone may define instructions **for their field**, conforming
> to the standard and verified by the third. Distributed authorship, common form.
> That is the balance — no central bottleneck, no free-for-all.

---

## We define the protocol, not the taxonomy

The standard defines a **protocol** — the rules by which any instruction is
formed, validated, exchanged, and verified. It does **not** define a
**taxonomy** — a fixed central classification of what instructions exist.

- A **taxonomy is central and rigid.** Someone decides the categories of
  everything; it freezes, goes stale, and becomes a point of capture. It is the
  Babel attempt — the one perfect classification of all meaning — which never
  closes.
- A **protocol is generative and open.** Define the *rules of interaction*, and
  anyone can create any conforming instruction — no permission, no central
  catalogue.

This is the internet's lesson exactly: it did not define a taxonomy of all
content; it defined **protocols** (TCP/IP, HTTP) and let everyone build on them.
A taxonomy would have frozen it; the protocol let it scale without limit. Same
with CLIs — no central registry of all commands, only the protocol
(name · args · stdio · exit code) that every command obeys.

> The standard owns the **protocol** (generative rules). Each field defines its
> own instructions — its own taxonomy, if it wants — conforming to the protocol.
> **Protocol, not taxonomy** is what keeps it open, capture-proof, and infinite.

---

## Programmatic tuning — replace hand-tuned prompts with programs

Prompt engineering tunes free text **by hand**. This standard tunes the agent
**by program**.

Because every instruction is defined, typed, **outcome-bound**, and composable,
you can **write a program** that tunes the agent automatically:

1. **compose** candidate instructions (or their parameters),
2. **run** them,
3. **measure** the result against the instruction's defined outcome metric, and
4. **select** the combination that yields the **optimal** outcome.

This is automated, reproducible, versioned optimisation — the opposite of
hand-fiddling prompts. It is possible **only because the outcome is defined**:
you cannot optimise against an outcome you cannot measure, which is exactly why
prompt engineering is guesswork (a prompt has no outcome to optimise toward).

The tuning program is itself written in defined instructions and governed like
any other artifact — so tuning becomes **part of the system**: measurable,
verifiable, and shareable, not private craft.

> Don't engineer prompts. **Write a program that tunes the agent against defined
> outcomes** — and let measurement, not intuition, find the optimum.

---

## Scope rule — tangible only

The standard defines **only what can be observed and verified.** If a thing
cannot be observed, it cannot be verified; if it cannot be verified, defining it
is itself an unverifiable assertion — hallucination at the spec level.

| Define (tangible) | Keep out (intangible) |
|---|---|
| Identity, Action, Event, State | Mind, consciousness |
| Resource, Capability, Constraint, Configuration | Belief (as a mental state) |
| Protocol, Handoff, Verification, Evidence | Intent / desire / will (as inner experience) |
| Vocabulary, Grammar, Transaction | "Understanding" / "reasoning" (as felt experience) |

Where a needed concept sounds intangible, define its **tangible proxy** and stop
there:

- ~~belief~~ → a recorded proposition + its evidence + a confidence value
- ~~intent~~ → a declared, logged objective
- ~~mind state~~ → the current recorded state

Define the observable shadow, never the metaphysical object. (SQL defines tables
and queries, not "the meaning of data"; TCP defines packets and acks, not
"communication." They endured because they stayed on the tangible side.)

---

## The five rules

### 1. Defined, not described
Every term in an instruction must resolve to a `DefinedTerm` in the agent
vocabulary. Undefined words are **rejected at parse time** — the agent never
receives an ambiguous instruction. *(removes Cause 1)*

### 2. One step — now → next, never further
An instruction names the **single next edge**, not a destination. Multi-hop
leaps are forbidden. The agent performs *next*, reports, and only then receives
the following instruction. *(removes Cause 2)*

### 3. Ground every step
An agent may act only on nodes **connected to known state or evidence**.
Asserting a node it did not traverse is hallucination and is **rejected, not
executed.** *(enforces Cause 2)*

### 4. Verify before commit — no self-approval
Each step proceeds as **Propose → Verify → Commit**, where Verify is performed
by a **third** (a separate authority). No agent, and no pair of agents, advances
on its own say-so. *(catches whatever slips)*

### 5. Handoff is typed, never prose
Inter-agent instruction is a grammar-validated contract, not natural language.
Two agents read the **same defined meaning**, or the handoff **fails closed.**
*(closes the agent-to-agent gap)*

---

## Why it ends hallucination

Remove undefined meaning (Rule 1) and remove leaps past *next* (Rules 2–3), and
the two spaces where hallucination lives are gone. Whatever still slips is caught
before commit (Rule 4) and cannot cross an agent boundary unverified (Rule 5).
The parser, the one-step rule, and the verifier together leave the model **no
room to invent.**

---

## The law underneath

Two can execute; only three can be trusted. Meaning needs a third (the
interpretant); trust needs a third (the witness); a handoff needs a third (the
verifier). Agent systems are no exception — which is why **no instruction is
self-approving.**

---

## Openness

This standard is published **open**, so anyone may participate, with the
verifier (the third) enforced so openness does not become a free-for-all:

- **Closed** → capture.
- **Open, no third** → chaos.
- **Open + the third** → balance.

Open to enter; governed to stay honest.
