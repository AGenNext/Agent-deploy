# Building for Reconstruction

*How our work maps to the Augmentation → Automation → Reconstruction model.*

> Grounded in: Rothschild, Hofman, Mobius, Lucier, Dillon, Goldstein, Immorlica,
> Slivkins, *"From Augmentation to Reconstruction: Guiding the AI Disruption to the
> Good Place"* (Microsoft Research, 2026); and Rothschild et al., *"The Agentic
> Economy"* (Communications of the ACM, 2026). The three-stage framing and the
> "good place" argument are **theirs**; this note maps our infrastructure to it.

---

A recent Microsoft Research perspective gives the clearest frame yet for *why the
AI disruption hasn't fully arrived* — and where it actually lives. Three stages:

- **Augmentation** — AI speeds up existing human tasks.
- **Automation** — routine tasks move under the hood, but inside human-era
  architectures (forms, queues, approvals).
- **Reconstruction** — workflows and markets **rebuilt around AI**: delegation,
  machine-to-machine coordination, continuous monitoring, **auditable
  constraints**.

The real disruption is **Stage 3** — and it's blocked not by model capability but
by **missing infrastructure.** They also warn: left to default incentives, the
agentic future hardens into **walled gardens**; we must steer it to *"the good
place"* — open, competitive, broadly beneficial.

We read that as a precise description of the gap we are building to fill.

> **Microsoft Research is right about the problem — and we believe we have the
> solution.** Their diagnosis is exact. The blueprint below is our answer to it:
> *theoretically complete, verified in parts, with implementation and scale as the
> open work.*

## The four Stage-3 constraints — and what we build for each

| their Stage-3 blocker | what we build |
|---|---|
| **Trust & accountability** (auditability, constraint enforcement, recourse) | the **third** in every loop, no self-approval, the gate, verification, audit trails |
| **Machine-legible, interoperable data & interfaces** | **defined meaning** (one word, one meaning), contracts, *data not code* — machine-legible by construction |
| **Agent-first workflows** (APIs, protocols, machine-readable rules) | the **protocols** — handoff, harness, language; *protocol-first*; **governed** agent-to-agent |
| **Aligned incentives; not walled gardens** | **open surfaces**, federation, no capture, balance — steer to the good place |

## Reconstruction needs the third

Their key insight echoes ours: **capability isn't enough.** Stage 3 needs
*auditable constraints and governance engineered into workflows*, not layered on
after the fact. That is the **third** — *two can act; only three can be trusted.*
Reconstruction is exactly where the third becomes mandatory.

## The good place is a choice

They close on a normative point: **"AI's advance is inevitable. Its impact on
society is not."** We built our whole stance on that line: *open + the third =
balance; a human world; Build Better World.* The good place is **not the default —
it is designed, governed, and chosen.**

> Augmentation and Automation optimise the old world. **Reconstruction builds the
> new one** — and it needs trust infrastructure, defined meaning, agent-first
> protocols, and open incentives. That is what we build.
>
> *Strive for better — in a loop.*

---

> **Status (honest):** *theoretically solved* — a coherent, verified-in-parts
> blueprint for the infrastructure the paper says is missing. **Implementation,
> adoption, and scale are the open work** — the next turns of the loop. Microsoft
> named the problem; we have the solution on paper; the build is *next.*
