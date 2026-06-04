# Canonical Design Principles

**Status:** DRAFT · the one reference · governed by `language_change_quorum`.

> One document, the whole design. Every other standard is an elaboration of these.

---

## Meaning

1. **The prompt is replaced by the instruction.** Reliable AI runs on defined,
   verified, outcome-bound instructions — never free text.
2. **One word, one meaning.** Meaning is a contract; canonical, governed; agent
   and human hold the same meaning, or nothing built on it holds.
3. **Define the tangible; proxy the intangible.** Only what is observable and
   verifiable enters the standard; intangibles get a tangible proxy.

## Structure

4. **Everything is an agent** (entity, with identity), **a graph** (structure,
   meaning in the edges), **a loop** (motion).
5. **The graph is the surface** where worlds converge — the edge where conceptual
   meets real (the digital twin).
6. **Protocol, not taxonomy.** Generative open rules, not a central catalogue.
   **Canonical within a namespace; federated across.**

## Motion

7. **Now → next, never further.** One step at a time; reaching past the next edge
   is hallucination.
8. **Every loop must resolve.** No dead-ends, no infinite spin; liveness or the
   system is unusable.
9. **Good enough, not perfect — then loop again.** Better, not perfect. Strive
   for better.

## Trust

10. **Two can act; only three can be trusted.** A third (verifier) closes every
    loop, handoff, and transaction. **No self-approval.**
11. **Every surface is governed by a protocol.** No surface without a protocol;
    new surfaces bring new protocols.
12. **Govern the gate, not the process.** You cannot force outsiders; validate
    output at the boundary. The gate secures, governs, enables, educates.
13. **Separation of duty.** The doer never judges itself.

## Balance

14. **Autonomy must be governed — not restricted.** Teach and enable; governed
    autonomy is the only kind an enterprise can use.
15. **Balance is conserved, and keeps moving.** Every gain in ease is paid for
    with a matching gain in governance; equilibrium is dynamic.
16. **Open + the third = balance.** Open to participate; governed to stay honest;
    privacy, sovereignty, federation preserved.

## Ground

17. **It is a human world.** Agents are guests, not hosts; humans grant meaning
    and hold final authority.
18. **Anchor to what exists.** Build on proven practice — open source, CNCF,
    Schema.org, Langium. Innovation is the next edge on the existing graph.
19. **Outcome-defined and verified.** Every action has a verifiable outcome,
    measured on CLEAR (Cost, Latency, Efficacy, Assurance, Reliability).
20. **Reuse and simplicity.** Prefer reusing what exists; make the simplest change
    that resolves the step.
21. **Open surface.** Every surface is open — open protocols and standards at
    every touch point — so anyone, human or agent, can connect and build. Not an
    open *core* with a closed edge, but **open surfaces all the way out.**
22. **Cloud native & distributed.** Built on cloud-native, **distributed**
    foundations — containerised, orchestrated, composable, portable, scalable,
    with **no central chokepoint** (CNCF-aligned; MicroK8s / k8s). The third is
    distributed; run anywhere, scale safely, no lock-in, no single point of
    capture.
23. **Built from primitives.** The system composes from a **minimal set of
    well-defined primitives** — identity, resource, action, event, state,
    constraint, and the like — each canonical, each composable. Everything builds
    up from primitives; nothing is monolithic.
24. **Protocol first.** Define the **protocol / contract before the
    implementation.** The protocol governs the surface; implementations conform to
    it. Contract-first, not code-first — meaning and boundaries are fixed before
    anything is built on them.
25. **Microservices, meshed.** Composed of small, independent **microservices**,
    each with one boundary (separation of duty), communicating through a **service
    mesh** — the infrastructure that governs every service-to-service surface
    (identity / mTLS, policy, observability, the third at each hop). The mesh is
    the **gate at the network layer.**
26. **Infrastructure agnostic.** Runs on **any infrastructure** — any cloud,
    on-prem, edge, or hybrid — with **no provider lock-in.** The standard and the
    runtime are portable; infrastructure is a choice, never a cage.
27. **Multi-model.** Model-agnostic — works with **any AI model**, swappable, with
    no lock-in to one vendor or model. Models are runtime-loaded artifacts behind
    the interface; pick the right model for the task.
28. **Temporal & durable.** Time is first-class: workflows are **durable,
    replayable, and resumable** across time. State and loops persist; every step
    is logged and recoverable — the loop survives restarts.
29. **Everything is configurable; code is config.** Behaviour is **declared, not
    hardcoded** — configuration is the control plane for all variability. Code is
    config: declared in the language, compiled to the runtime. Change behaviour by
    changing declared, governed meaning — not by editing imperative code paths.
30. **Only data is real.** Everything — code, config, behaviour, agents, even the
    graph itself — reduces to **data.** Data is the single ground truth; logic is
    computed from it, not the other way round. Only data persists; **only data is
    real.**
31. **Data + config = the digital twin.** A node's **data** (its current state)
    plus its **config** (its declared structure and behaviour) *is* its **digital
    twin** — the live, canonical mirror of a real thing, kept in sync and verified
    by the third.

---

> **Define meaning. Take one verified step. Close every loop with a third. Keep
> the balance. In a human world. Strive for better — in a loop.**
