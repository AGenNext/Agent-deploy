"""
Verification by modelling: the three-ball "active reasoning" paradigm.

Self-contained computational verification of the central empirical claim in
Friston et al., "Active inference and artificial reasoning":

    Supplementing expected free energy with the *expected information gain over
    models* (evaluated via Bayesian model reduction, BMR) makes rule discovery
    more sample-efficient -- the agent finds the hidden rule in fewer trials and
    scores higher -- than ablations that drop the information-gain terms over
    models, then parameters, then states.

We reproduce the qualitative structure of the paper's Figures 4-7 (not the exact
SPM/MATLAB numbers, which depend on the full variational message-passing stack).
The mechanism the paper credits for the effect -- BMR over an 81-rule hypothesis
space with an Occam's-razor threshold -- is implemented faithfully. Active
vision, state-belief updating and learning are streamlined but principled.

Speed: model evidence is decomposed per feedback column, so a hypothetical count
touches exactly one column => O(n_models) per query, cached incrementally.

Run:  python3 experiments/three_ball_active_reasoning.py
"""

from __future__ import annotations

import argparse
import numpy as np
from itertools import product
from scipy.special import gammaln

# ----------------------------------------------------------------------------
# Indexing conventions
# ----------------------------------------------------------------------------
RED, GREEN, BLUE = 0, 1, 2
LEFT, CENTRE, RIGHT = 0, 1, 2                    # location / criterion factors

WHERE = ["start", "left", "centre", "right"]
WHERE_TO_LOC = {1: LEFT, 2: CENTRE, 3: RIGHT}   # where index -> location index

CHOICE = ["none", "red", "green", "blue"]       # choice c>0 -> colour c-1

FB_NONE, FB_CORRECT, FB_INCORRECT = 0, 1, 2
C_FB = np.array([0.0, 2.0, -6.0])               # preferences (paper: 0, 2, -6)

N_FB = 3
N_CHOICE = 4
N_LOC = 3
N_COL = 3

# A feedback "column" is indexed by (cL, cC, cR, choice).
COLS = list(product(range(N_COL), range(N_COL), range(N_COL), range(N_CHOICE)))
N_COLS = len(COLS)                              # 108
COL_INDEX = {c: i for i, c in enumerate(COLS)}


# ----------------------------------------------------------------------------
# Hypothesis space: 81 context-sensitive isomorphic rules
#   rule = (context_loc, g) with g[colour_at_context] = criterion_loc
#   correct colour = colour of the ball at the criterion location
# ----------------------------------------------------------------------------
def build_models():
    return [(ctx, g) for ctx in (LEFT, CENTRE, RIGHT)
            for g in product(range(N_LOC), repeat=N_COL)]


MODELS = build_models()
N_MODELS = len(MODELS)                          # 81

TRUE_MODEL = (CENTRE, (LEFT, CENTRE, RIGHT))    # "rule 65" in the paper
TRUE_MODEL_IDX = MODELS.index(TRUE_MODEL)


def correct_colour(colours, model):
    ctx, g = model
    return colours[g[colours[ctx]]]


def predicted_feedback_entry(colours, choice, model):
    if choice == 0:
        return FB_NONE
    return FB_CORRECT if (choice - 1) == correct_colour(colours, model) else FB_INCORRECT


def precompute_predictions():
    pred = np.zeros((N_MODELS, N_COLS), dtype=np.int64)
    for mi, model in enumerate(MODELS):
        for ci, (cL, cC, cR, choice) in enumerate(COLS):
            pred[mi, ci] = predicted_feedback_entry((cL, cC, cR), choice, model)
    return pred


PRED = precompute_predictions()                 # [81, 108], values in {0,1,2}


# ----------------------------------------------------------------------------
# Dirichlet priors (Eq. 8). EPS is the shrinkage value (paper uses ~1/32).
# ----------------------------------------------------------------------------
EPS = 1.0 / 32.0


def reduced_prior_counts():
    r = np.full((N_MODELS, N_FB, N_COLS), EPS)
    for mi in range(N_MODELS):
        r[mi, PRED[mi], np.arange(N_COLS)] += 1.0
    return r


RED_PRIOR = reduced_prior_counts()                       # [81, 3, 108]
FULL_PRIOR = RED_PRIOR.mean(axis=0)                       # [3, 108]  model average
REDMF = RED_PRIOR - FULL_PRIOR[None, :, :]                # [81, 3, 108]


def lnB(x):
    """Multivariate log-Beta over the last axis (size N_FB)."""
    return gammaln(x).sum(axis=-1) - gammaln(x.sum(axis=-1))


# Data-independent constant of each model's log-evidence.
MODEL_CONST = (lnB(np.moveaxis(FULL_PRIOR, 0, -1))[None, :]
               - lnB(np.moveaxis(RED_PRIOR, 1, -1))).sum(axis=1)        # [81]


# ----------------------------------------------------------------------------
# Bayesian model reduction with incremental per-column caching.
# ----------------------------------------------------------------------------
class BMR:
    """Maintains P(model | accumulated feedback counts) via per-column evidence.

    log-evidence_m = MODEL_CONST_m + sum_c [ lnB(a_post_m[:,c]) - lnB(a_post[:,c]) ]
    a_post   = FULL_PRIOR + counts                      (model-average posterior)
    a_post_m = a_post + RED_PRIOR_m - FULL_PRIOR        (reduced posterior)
    """

    def __init__(self):
        self.counts = np.zeros((N_FB, N_COLS))
        self.colER = self._col_evidence_all()           # [81, 108]
        self.logev = MODEL_CONST + self.colER.sum(axis=1)

    def _a_post_col(self, c):
        return FULL_PRIOR[:, c] + self.counts[:, c]      # [3]

    def _col_evidence(self, a_col, c):
        am = a_col[None, :] + REDMF[:, :, c]             # [81, 3]
        return lnB(am) - lnB(a_col)                      # [81]

    def _col_evidence_all(self):
        out = np.zeros((N_MODELS, N_COLS))
        for c in range(N_COLS):
            out[:, c] = self._col_evidence(self._a_post_col(c), c)
        return out

    def add_count(self, fb, c, w=1.0):
        self.counts[fb, c] += w
        new = self._col_evidence(self._a_post_col(c), c)
        self.logev += new - self.colER[:, c]
        self.colER[:, c] = new

    def posterior(self):
        e = self.logev - self.logev.max()
        p = np.exp(e)
        return p / p.sum()

    def eig_for_column(self, c):
        """Expected information gain over MODELS for a hypothetical count in
        column c. Feedback ~ model-averaged predictive. O(n_models)."""
        post = self.posterior()
        a_col = self._a_post_col(c)
        pred_fb = a_col / a_col.sum()                    # predictive feedback dist
        eig = 0.0
        for fb in range(N_FB):
            if pred_fb[fb] < 1e-9:
                continue
            a2 = a_col.copy(); a2[fb] += 1.0
            new_colER = self._col_evidence(a2, c)        # [81]
            ev_new = self.logev + (new_colER - self.colER[:, c])
            ev_new -= ev_new.max()
            p_new = np.exp(ev_new); p_new /= p_new.sum()
            kl = np.sum(p_new * (np.log(p_new + 1e-12) - np.log(post + 1e-12)))
            eig += pred_fb[fb] * kl
        return eig


def occams_razor(post):
    best = min(post.max(), 1.0 - 1e-12)
    return np.log(best) - np.log(1.0 - best)


# ----------------------------------------------------------------------------
# Agent
# ----------------------------------------------------------------------------
class Agent:
    def __init__(self, use_models=True, use_params=True, use_states=True, rng=None):
        self.use_models = use_models
        self.use_params = use_params
        self.use_states = use_states
        self.rng = rng or np.random.default_rng()
        self.bmr = BMR()
        self.committed = False
        self.selected_model = None

    def fresh_state_belief(self):
        return [np.ones(N_COL) / N_COL for _ in range(N_LOC)]

    def predictive_feedback(self, belief, choice):
        if choice == 0:
            return np.array([1.0, 0.0, 0.0])
        a_post = FULL_PRIOR + self.bmr.counts
        out = np.zeros(N_FB)
        for cL in range(N_COL):
            for cC in range(N_COL):
                for cR in range(N_COL):
                    w = belief[0][cL] * belief[1][cC] * belief[2][cR]
                    if w < 1e-9:
                        continue
                    col = a_post[:, COL_INDEX[(cL, cC, cR, choice)]]
                    out += w * col / col.sum()
        return out / out.sum()

    def action_value(self, belief, observed, where, choice):
        # During foraging (pre-commitment) the agent uses *uninformative*
        # preferences (paper, Fig. 4): behaviour is driven purely by expected
        # information gain. Informative preferences (C_FB) are adopted only
        # after Occam's razor fires, via exploit_action.
        value = 0.0

        if self.use_states and where in WHERE_TO_LOC:
            loc = WHERE_TO_LOC[where]
            if not observed[loc]:
                b = belief[loc]
                value += -np.sum(b * np.log(b + 1e-12))      # salience

        if choice != 0 and (self.use_params or self.use_models):
            # A choice can only inform the *rule* once the agent knows which
            # column it lands in -- i.e. once it has resolved the ball colours.
            # The paper: EIG over models/parameters depends on resolving latent
            # state uncertainty. Gate the choice's epistemic value accordingly.
            state_conf = belief[0].max() * belief[1].max() * belief[2].max()
            cL = int(np.argmax(belief[0])); cC = int(np.argmax(belief[1]))
            cR = int(np.argmax(belief[2]))
            ci = COL_INDEX[(cL, cC, cR, choice)]
            epi = 0.0
            if self.use_params:
                col = (FULL_PRIOR + self.bmr.counts)[:, ci]
                a0 = col.sum()
                pred = col / a0
                epi += float(np.sum(pred * (0.5 / col - 0.5 / a0)))    # novelty
            if self.use_models:
                epi += self.bmr.eig_for_column(ci)           # active reasoning
            value += state_conf * epi
        return value

    def choose_action(self, belief, observed):
        if not (self.use_models or self.use_params or self.use_states):
            return int(self.rng.integers(0, 4)), int(self.rng.integers(0, 4))
        best, best_a = -np.inf, (0, 0)
        for where in range(4):
            for choice in range(4):
                v = self.action_value(belief, observed, where, choice)
                if v > best:
                    best, best_a = v, (where, choice)
        return best_a

    def update_state_belief(self, belief, observed, where, true_colours):
        if where in WHERE_TO_LOC:
            loc = WHERE_TO_LOC[where]
            b = np.full(N_COL, 1e-6); b[true_colours[loc]] = 1.0
            belief[loc] = b / b.sum()
            observed[loc] = True
        return belief, observed

    def learn(self, belief, choice, feedback):
        if choice == 0:
            return
        for cL in range(N_COL):
            for cC in range(N_COL):
                for cR in range(N_COL):
                    w = belief[0][cL] * belief[1][cC] * belief[2][cR]
                    if w < 1e-6:
                        continue
                    self.bmr.add_count(feedback, COL_INDEX[(cL, cC, cR, choice)], w)

    def maybe_commit(self, threshold=16.0):
        if self.committed:
            return
        post = self.bmr.posterior()
        if occams_razor(post) > threshold:
            self.committed = True
            self.selected_model = int(np.argmax(post))


def exploit_action(agent, observed, colours):
    ctx, g = MODELS[agent.selected_model]
    if not observed[ctx]:
        return (ctx + 1, 0)
    crit_loc = g[colours[ctx]]
    if not observed[crit_loc]:
        return (crit_loc + 1, 0)
    return (0, colours[crit_loc] + 1)


def run_trial(agent, rng, n_steps=6):
    colours = [int(rng.integers(0, N_COL)) for _ in range(N_LOC)]
    belief = agent.fresh_state_belief()
    observed = [False, False, False]
    score = 0
    for _ in range(n_steps):
        if agent.committed:
            where, choice = exploit_action(agent, observed, colours)
        else:
            where, choice = agent.choose_action(belief, observed)
        belief, observed = agent.update_state_belief(belief, observed, where, colours)

        if choice != 0:
            cc = correct_colour(colours, TRUE_MODEL)
            feedback = FB_CORRECT if (choice - 1) == cc else FB_INCORRECT
            score += 1 if feedback == FB_CORRECT else -1
            # Learn the rule only when the full state is known: a feedback count
            # can only be attributed to the right likelihood column once all
            # three ball colours have been resolved by looking.
            if not agent.committed and all(observed):
                agent.learn(belief, choice, feedback)
        if not agent.committed:
            agent.maybe_commit()
    return score


def run_game(use_models, use_params, use_states, n_trials, seed):
    rng = np.random.default_rng(seed)
    agent = Agent(use_models, use_params, use_states, rng=rng)
    cumulative, discovery, correct = 0, None, False
    for t in range(n_trials):
        cumulative += run_trial(agent, rng)
        if agent.committed and discovery is None:
            discovery = t
            correct = (agent.selected_model == TRUE_MODEL_IDX)
    if discovery is None:
        discovery = n_trials
    return dict(discovery=discovery, score=cumulative,
                correct=correct if discovery < n_trials else False)


# ----------------------------------------------------------------------------
# Experiment
# ----------------------------------------------------------------------------
CONDITIONS = [
    ("models+params+states", dict(use_models=True,  use_params=True,  use_states=True)),
    ("params+states",        dict(use_models=False, use_params=True,  use_states=True)),
    ("states only",          dict(use_models=False, use_params=False, use_states=True)),
    ("none (random)",        dict(use_models=False, use_params=False, use_states=False)),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--games", type=int, default=48)
    ap.add_argument("--trials", type=int, default=32)
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()

    seeds = np.random.default_rng(args.seed).integers(0, 2**31 - 1, size=args.games)

    print(f"Three-ball active reasoning -- {args.games} games x {args.trials} trials")
    print(f"Hypothesis space: {N_MODELS} rules | true rule index: {TRUE_MODEL_IDX}")
    print("=" * 72)
    print(f"{'condition':24s} {'discovery':>12s} {'cum.score':>12s} {'found%':>8s}")
    print("-" * 72)

    results = {}
    for name, kw in CONDITIONS:
        disc, sco, found = [], [], 0
        for s in seeds:
            r = run_game(n_trials=args.trials, seed=int(s), **kw)
            disc.append(r["discovery"]); sco.append(r["score"])
            found += int(r["discovery"] < args.trials and r["correct"])
        disc, sco = np.array(disc), np.array(sco)
        results[name] = dict(disc=disc, sco=sco, found=found)
        print(f"{name:24s} {disc.mean():>12.1f} {sco.mean():>12.1f} "
              f"{100*found/args.games:>7.0f}%")

    print("=" * 72)
    full = results["models+params+states"]
    nomod = results["params+states"]
    none = results["none (random)"]

    def verdict(ok):
        return "CONFIRMED" if ok else "NOT CONFIRMED"

    print("\nVerdict (paper's directional predictions):")
    print(f"  EIG(models) shortens discovery : {full['disc'].mean():5.1f} vs "
          f"{nomod['disc'].mean():5.1f} trials  -> "
          f"{verdict(full['disc'].mean() < nomod['disc'].mean())}")
    print(f"  EIG(models) raises score       : {full['sco'].mean():5.1f} vs "
          f"{nomod['sco'].mean():5.1f}        -> "
          f"{verdict(full['sco'].mean() > nomod['sco'].mean())}")
    print(f"  all info-gain >> random (score): {full['sco'].mean():5.1f} vs "
          f"{none['sco'].mean():5.1f}        -> "
          f"{verdict(full['sco'].mean() > none['sco'].mean())}")
    print(f"  random rarely finds the rule   : {100*none['found']/args.games:4.0f}% vs "
          f"{100*full['found']/args.games:4.0f}% found -> "
          f"{verdict(none['found'] < full['found'])}")


if __name__ == "__main__":
    main()
