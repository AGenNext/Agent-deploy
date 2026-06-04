# Foundation — everything is a graph

**Status:** DRAFT · foundational note for the standards stack.

---

## The claim

The whole stack rests on one structure: the **graph** — nodes and edges.

- **Vocabulary** = nodes (defined words / entities)
- **Relations** = edges
- **Schema.org JSON-LD** = a graph serialization
- The ontology, the knowledge model, the agent network — all graphs.

> Meaning lives in the **edges**, not the nodes. A word alone is inert; its
> meaning is the relations it holds. So the system is natively a graph: define
> nodes (canonical terms), connect them with edges (relations), traverse one edge
> at a time.

---

## Why a graph (the operational, defensible version)

Graph theory is the right mathematics for this system, and it yields the laws the
standards already obey:

- **Traverse one edge at a time** → *now → next, never further.* Reaching past
  the adjacent node = asserting an edge you did not cross = **hallucination**.
- **Closure needs three** → the smallest cycle in a graph is a **triangle**
  (girth ≥ 3). Two nodes make a line, not a loop. This is why meaning, trust, and
  handoff each need a **third** to close.
- **Canonical nodes, governed edges** → one word, one meaning (a node has one
  identity); relations are change-controlled (`language_change_quorum`).
- **Federation = subgraphs** → each field is a namespaced subgraph; canonical
  *within* a subgraph, federated *across* subgraphs.

The standards depend **only** on this operational version: *the system is a
graph.* That is concrete and verifiable.

---

## Loop theory — the graph in motion

A graph is the static structure; a **loop** is how it moves. Traversal happens in
feedback loops (observe → act → learn → observe). So the dynamic claim:

> **Everything is a loop. And every loop must resolve.**
> The graph is *where* everything resolves; the loop is *how*.

Three operational laws follow — together they guarantee **liveness**:

1. **An agent must always have a next step.** No dead-ends. Every state defines a
   next edge — or a defined terminal. A stranded agent (no next step) is a
   *failure* state, not a resting state. (now → next: there is *always* a next.)

2. **A loop must resolve.** It must close on its third (verify) and reach its
   **defined outcome**, or make measurable progress each turn. A loop that
   neither closes nor progresses is a **Wiggum loop** — spins forever, learns
   nothing — and is forbidden.

3. **The graph must resolve.** Resolution must be **reachable** from every state;
   no path may hang unresolved forever.

So the static and dynamic halves complete each other:

- the **graph** gives *structure* — nodes, edges, canonical meaning;
- the **loop** gives *motion that must terminate in resolution.*

An agent never stops with "no next step," and never spins without resolving. It
moves one edge at a time until the loop closes on a verified outcome.

> If loops do not resolve and agents run out of next steps, the system **hangs** —
> and a system that hangs is **unusable.** Resolution is not a nicety; it is the
> difference between a usable system and a dead one.

---

## Where three worlds meet — human · machine · agent

The graph is not only a data model. It is the **common ground where three worlds
meet**:

- **Human** — defines intent, grants meaning, holds final authority.
- **Machine** — executes deterministically, stores state, runs the runtime.
- **Agent** — reasons and acts between the two.

All three must hold the **same canonical meaning** for every word, or they cannot
coordinate. The graph — with one-word-one-meaning and governed edges — is the
**shared substrate** where their meanings converge. It is the *third at the
largest scale*: the common ground that lets human, machine, and agent mean the
same thing.

This is why the graph must be **canonical** and must **resolve**: it carries the
meaning for **three parties at once.** If it diverges or hangs, all three lose
their shared ground — and the system becomes unusable.

---

## The deeper hypothesis (honestly scoped)

"Everything is a graph" is also a serious idea in the foundations of physics and
philosophy — structural realism, spin networks (loop quantum gravity), causal
sets, Wolfram's hypergraph model. We **use** it as the system's data model
(defensible, concrete) and **acknowledge** it as an inspiring hypothesis about
reality.

But we do not *claim* it as proven. Two honest limits:

1. A graph still needs **nodes** for edges to connect — pure "edges only" is
   incoherent; the node is demoted, not eliminated (a node is *where edges meet*).
2. As a theory of *reality*, it sits in the open state — unproven, like all
   quantum gravity. As a theory of *this system*, it is simply true by
   construction.

So: **build on the graph as the model; admire it as the hypothesis; claim only
the part you can verify.** That keeps the foundation strong and free of the Babel
overclaim.

---

## Consequence

Every layer of the stack is a view of the same graph:

```
Vocabulary  = nodes
Graph       = edges
Grammar     = which edges are legal
Language    = how the graph is declared (Schema.org JSON-LD)
Instructions= one verified traversal (now → next)
Operating-Model = the harness that controls traversal
Economy     = transactions across the graph (each closed by a third)
```

One structure, every layer. **It is a graph.**
