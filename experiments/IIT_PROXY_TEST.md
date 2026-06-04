# Test of an IIT claim — "proxies are not approximations"

Barrett et al., *Integrated information theory: the good, the bad and the
misunderstood* (Section 5.2), argue that the integrated-information measures
people compute on data are **proxies, not approximations** of Φ, and cite
Mediano et al. (2019): "distinct measures often [move] in different directions
under the same change of parameters."

This is one of the few claims in that (largely conceptual) paper that can be
tested by direct computation. Code: [`iit_proxy_divergence.py`](./iit_proxy_divergence.py).

## What we test

If the measures were approximations of a single underlying quantity, then under
a single parameter sweep they would all rise and fall **together**. If instead
they are merely proxies — each capturing a different facet — at least one pair
should move in **opposite** directions somewhere in the sweep.

We compute three standard integrated-information measures in **closed form** (no
estimation noise) on the *same* system: a stationary 2-node Gaussian VAR(1)
process, sweeping its cross-coupling `c`:

- `Phi_BarrettSeth` — whole-minus-parts time-delayed integration
- `instantaneous_MI` — mutual information between the two nodes
- `causal_density` — mean pairwise Granger causality

## Result

| regime | what happens |
|---|---|
| weak coupling (c ≲ 0.5) | all three rise together (Spearman ρ ≈ 0.96–1.0) |
| strong coupling (c ∈ [0.56, 0.64]) | **Φ turns over and falls** while MI and causal density keep **rising** |

So the measures move in **opposite directions** at strong coupling — claim
**CONFIRMED**.

## Why this happens (and why it matters)

`instantaneous_MI` and `causal_density` track *statistical dependence/coupling*:
more coupling → more dependence → they rise monotonically. But `Phi` measures
*integration* — information the whole has beyond its parts. As the two nodes
become strongly coupled they turn into near-redundant copies of one another, so
the whole stops carrying extra information over the parts and Φ **drops**.

This is exactly the paper's point: a quantity that tracks coupling is **not** an
approximation of integrated information — they genuinely diverge, even on a
trivial 2-node Gaussian system. It cautions against reading any single "empirical
Φ" as if it were Φ itself.

## Caveat

These are well-known *proxies* (Barrett & Seth 2011; Seth's causal density), not
IIT 4.0's Φ — which, as the same paper argues, is not even well-defined for
systems like this. The test demonstrates the *divergence-of-proxies* claim, not
a computation of true Φ.
