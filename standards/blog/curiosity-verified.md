# Curiosity, Verified

*Why agents that seek understanding beat agents that just act — and how we tested
it.*

---

We claim that a good agent doesn't only chase reward — it **seeks information about
how the world works.** That sounds nice. We tested whether it's true.

## The test

The **three-ball game.** An agent sees three coloured balls but can only look at
one at a time, and must discover a hidden rule about which colour is "correct." To
solve it, the agent has to *deliberately gather information* — look in the right
places, try things, and figure out the rule — not just guess.

We compared agents that **seek information about the rule** against ones that act
without it (down to a random agent).

## The result

| agent | discovers the rule | score |
|---|---:|---:|
| seeks information (about the rule, its inputs, and the world) | **~24 tries, every time** | **+54** |
| seeks less | rarely | ~0 |
| random | almost never | −67 |

The agent that **resolves its uncertainty about the world's structure** cracks the
rule fast and reliably. The one that doesn't, never really does.

## Why it matters

This is the research under two of our principles: **every loop must resolve**, and
**two can act, only three can be trusted.** An agent that closes the loop on its
own uncertainty — one verified step at a time — wins. One that acts blindly drifts.

> Honest calibration: this reproduces the *mechanism and direction* (from Friston
> et al.), not exact published numbers — a simplified planner, run openly. Code in
> `experiments/`.

## Proven, and not proven

- **Proven (in this test):** information-seeking agents discover the hidden rule
  **far faster and more reliably** than non-seeking or random agents —
  directionally, reproducibly.
- **Not proven:** that this is the *only* mechanism, that the exact published
  numbers replicate, or that it holds for every real-world task. Those stay
  **open** — the honest third state: *not disproven, not fully proven, still to be
  tested.*

We publish both. That is what makes it research, not a claim.

---

**Curiosity isn't a luxury. It's what makes an agent reliable.**
