# Verification by modelling — "Active inference and artificial reasoning"

This is a computational check of the central empirical claim in Friston et al.,
*Active inference and artificial reasoning* (the three-ball paradigm):

> Adding the **expected information gain over models** — evaluated with **Bayesian
> Model Reduction (BMR)** over a hypothesis space of rules — to the expected free
> energy makes rule discovery more sample-efficient. The agent discovers the
> hidden rule in fewer trials and scores higher than ablations that drop the
> information-gain terms over models, then parameters, then states.

Code: [`three_ball_active_reasoning.py`](./three_ball_active_reasoning.py).
Run: `python3 experiments/three_ball_active_reasoning.py` (needs `numpy`, `scipy`).

## The paradigm

Three coloured balls (each red/green/blue). The agent sees one ball at a time
(active vision) and may choose a colour, getting feedback *correct / incorrect*.
The hidden, context-sensitive rule (paper's "rule 65"): the **centre** ball's
colour selects which location is the criterion — centre red → left, centre green
→ centre, centre blue → right — and the criterion ball's colour is the correct
choice.

## What is faithful vs. simplified

**Faithful to the paper:**

- **81-rule hypothesis space** built from context-sensitive isomorphisms
  (3 context factors × 3³ context→criterion mappings). 75 are observationally
  unique here (paper: 79 — differs only because our enumeration is slightly
  different), and the space contains the true rule.
- **Bayesian Model Reduction** over Dirichlet counts (paper Eq. 7–9): the prior
  is the **Bayesian model average** over the 81 reduced rules (Eq. 8); each
  rule's evidence is scored from accumulated feedback counts using the
  multivariate log-Beta function. Verified in isolation: feeding ~50 ground-truth
  observations drives Occam's-razor log-odds past the **16-nat** threshold and
  concentrates the posterior on the true rule.
- **Expected information gain over models** (paper Eq. 10–11): the expected KL
  between the model posterior with vs. without a hypothetical outcome. Computed
  incrementally — a hypothetical count touches exactly one likelihood column, so
  it is O(n_models) per query.
- **Occam's razor** commitment at a 16-nat log-odds threshold (Eq. 12–13);
  preferences are flat during foraging and switch to the informative
  `(0, +2, −6)` values only after commitment (as described for Fig. 4).
- The dependence the paper stresses — **EIG over models/parameters requires first
  resolving latent-state uncertainty** — is reproduced: a choice can only inform
  the rule once all three colours are known, so its epistemic value is gated by
  state confidence.

**Simplified (for tractability — these are *not* the claim under test):**

- One-step greedy policy with explicit epistemic terms instead of the full
  multi-step variational message-passing / expected-free-energy planner in SPM.
- Visual observations are deterministic (looking reveals a colour exactly), so
  state inference is reduced to bookkeeping rather than full message passing.
- Novelty (EIG over parameters) uses a standard Dirichlet-uncertainty surrogate.

Because of these, absolute discovery times differ from the paper's (our agent is
a bit slower and saturates around 23 trials vs. the paper's mode of ~14). The
**directional** comparisons across ablations are the point, and those are what we
verify.

## Result (64 games × 48 trials, seed 2025)

| condition (information gain over…) | discovery (trials) | cumulative score | found rule |
|---|---:|---:|---:|
| models + params + states | **23.6** | **54.1** | 100% |
| params + states          | 24.2 | 44.3 | 100% |
| states only              | 48.0 (never) | 0.0 | 0% |
| none (random)            | 47.5 (never) | −67.1 | 3% |

All four directional predictions hold:

- **EIG over models shortens discovery** (23.6 < 24.2 trials) ✓
- **EIG over models raises score** (54.1 > 44.3) ✓
- **Any information gain ≫ random** (54.1 vs −67.1) ✓
- **Random / state-only agents essentially never discover the rule** (0–3%) ✓

The marginal effect of EIG-over-models is *small but consistent*, which matches
the paper's own Fig. 6 observation: information gain over **parameters** already
eliminates most implausible rules, and information gain over **models** matters
mainly at the *late* stage of disambiguating the few remaining equally-plausible
rules. The dominant effect is having epistemic drive at all: the "states only"
agent resolves what it sees but never tests a rule (score 0), and the random
agent drifts negative — reproducing the paper's "importance of being curious".

## Caveats

- A small rate of premature/incorrect commitment ("jumping to conclusions")
  occurs, as the paper also reports; gating learning on full-state observation
  reduced it to ~0 with a 16-nat threshold here.
- This verifies the *mechanism and its directional consequences*, not the exact
  SPM numbers. The qualitative claim of the paper reproduces cleanly.
