# Agent-Operating-Model (AOM)

**Status:** DRAFT · RFC-3 · open for ratification
**Scope note:** Staged in `agent-deploy` (write-scope of the authoring session).
Intended home: `Agent-Platform`. Adoption requires **quorum consensus** and
**no self-approval**.

---

## Essence

> **The Agent-Operating-Model is the enterprise harness: it makes agent
> intelligence controllable and governable.**

Raw agent intelligence is powerful but unbounded — it reasons, plans, and acts.
The AOM is the **harness** that wraps it so an enterprise can run it safely.
It does not make the agent *smarter*; it makes the agent's intelligence
**usable** — every action **controllable** and **governable**.

A harness wraps power with control. A test harness wraps code so you can run and
check it; the AOM wraps intelligence so an enterprise can deploy and trust it.

---

## Everything is an agent — the harness governs all

The operating model rests on Agent Theory: **everything is an agent.** So the
harness governs *every participant uniformly* — humans, machines, services,
tools, capabilities — because each is an agent with identity. One model, one set
of controls, applied to all:

- every participant has **identity** (attributable);
- every participant has a **governed lifecycle**;
- every participant acts **under the harness** (controllable + governable);
- every participant sits **under human final authority.**

There is no special case. A human, a machine, and an AI agent are governed by the
**same harness** because they are the same kind of thing — agents. This is what
makes the operating model **uniform and complete**: nothing acts outside it,
because **everything is an agent.**

---

## Every agent needs a harness

No agent operates without a harness. An unharnessed agent is **ungoverned
autonomy** — unattributable, unsteerable, unaccountable. It cannot be trusted, so
it cannot be deployed. The harness is therefore **not optional**; it is the
precondition for an agent to exist in a human world:

- **without** a harness → autonomy runs free → unsafe and unusable;
- **with** a harness → autonomy is controllable and governable → trustworthy.

> **An agent is only an agent *inside* a harness.** Outside it, it is just
> ungoverned software with a decision no one can trust it to make.

Every agent — human, machine, or AI — runs inside the harness. There is no
unharnessed participant.

---

## The two guarantees

**Controllable** — every action is:
- **steerable** (the operator can direct it),
- **stoppable** (it can be halted mid-flight),
- **reversible** (it can be undone),
- **observable** (it emits events),
- **one step at a time** (now → next, never further — no runaway).

**Governable** — every action is:
- **attributable** to an identity (human, agent, or service),
- **policy-bound** (allowed only within declared constraints),
- **approved** by a third (no self-approval),
- **evidenced and audited** (traceable to a decision and a person),
- **accountable** (tied to an objective and an outcome).

> You cannot govern what you cannot control, and you cannot control what you
> cannot observe. The harness provides all three.

---

## Built on the layers below

The AOM **cannot exist** without the two layers beneath it — *you cannot govern
what you cannot define*:

```
Agent-Language       → defined meaning (one word, one meaning)
Agent-Instructions   → the CLI: defined, verified, outcome-bound actions
        ↓
Agent-Operating-Model → the harness that controls and governs those actions
```

Agents act by invoking **defined instructions**, written in the **defined
language**, under the harness's controls. Free-text prompts cannot be governed —
which is exactly why the lower layers come first.

---

## Seven control surfaces

| layer | the control it provides |
|---|---|
| **Objective** | agents never act without a declared goal, KPI, and success criteria |
| **Governance** | policies, risk controls, separation of duties, human approval |
| **Identity** | every participant attributable; every action owned |
| **Knowledge** | grounded context — without it, agents hallucinate |
| **Capability** | reusable, declared skills/tools/workflows the agent may use |
| **Execution** | observable, auditable, reversible, replayable actions |
| **Learning** | outcomes measured and fed back to improve — one verified turn at a time |

---

## The third, everywhere

The harness **is** the institutionalised third:

- **Control** = a third that can steer and stop.
- **Governance** = a third that approves and audits.
- **Final review authority** = no agent or pair self-approves; a separate
  authority makes the accept/reject decision on supporting evidence.

Separation of duty is the law of the harness: the doer never judges itself.

---

## Operating loops (one verified step at a time)

```
Decision:  Observe → Analyse → Recommend → Approve → Execute → Measure
Execution: Task → Plan → Tool-use → Action → Verify → Complete
Learning:  Outcome → Evaluate → Feedback → Improve → Deploy
```

Every loop closes on a **third** (Approve / Verify / Evaluate) — two steps point,
three steps mean.

---

## Agent lifecycle (every stage gated)

```
Draft → Tested → Approved → Production → Observed → Evaluated → Optimised → Retired
```

Trust is the measure of how far past *now* an agent is allowed to act without a
human in the loop. It is earned stage by stage, never granted ahead of evidence.

---

## Tangible only

The harness governs only what is **observable and verifiable** — actions, events,
state, resources, outcomes. It does **not** govern "belief" or "mind"; where a
mental term is needed, it governs the **tangible proxy** (a recorded proposition
+ evidence + confidence; a declared, logged objective).

---

## Place in the stack

```
Agent-Language → Agent-Instructions → AGENT-OPERATING-MODEL
                                              ↓
                                   Agent-Research-Foundation (verifies)
                                              ↓
                                   Agent-Economy (transacts)
```

---

## Openness

Published **open**, with the verifier (the third) enforced — open to participate,
governed to stay honest. The harness makes intelligence **controllable and
governable** so that, once trusted, it can be opened to everyone without becoming
a free-for-all.
