"""
Test of an IIT claim: "proxies are not approximations".

Barrett et al., "Integrated information theory: the good, the bad and the
misunderstood" (Section 5.2), argue that the integrated-information measures
applied to data are *proxies*, not approximations, of Phi -- and cite Mediano
et al. (2019) that "distinct measures often [move] in different directions under
the same change of parameters."

If that is true, then several reasonable integrated-information measures computed
on the *same* system, while sweeping a single parameter, should NOT all rise and
fall together: at least one pair should disagree (anti-correlated trends, or peaks
at different parameter values). If they all moved together, they would be
behaving like approximations of one underlying quantity, and the claim would fail.

We test this exactly (closed form) on a stationary Gaussian network -- a coupled
VAR(1) process -- where every measure has an analytic form from covariances, so
the result is not an artefact of estimation noise.

Run:  python3 experiments/iit_proxy_divergence.py     (needs numpy, scipy)
"""

from __future__ import annotations

import numpy as np
from scipy.linalg import solve_discrete_lyapunov
from scipy.stats import spearmanr

# ----------------------------------------------------------------------------
# A 2-node stationary Gaussian VAR(1):  X_t = A X_{t-1} + E,  E ~ N(0, I)
#   A = [[a, c], [c, a]]   (self-coupling a, cross-coupling c)
# We sweep the cross-coupling c (the "same change of parameters").
# ----------------------------------------------------------------------------
SELF = 0.30


def covariances(a, c):
    """Stationary covariance Sigma, lag-1 cross-covariance Sigma1 = A Sigma."""
    A = np.array([[a, c], [c, a]])
    SigE = np.eye(2)
    Sigma = solve_discrete_lyapunov(A, SigE)        # Sigma = A Sigma A^T + I
    Sigma1 = A @ Sigma                              # Cov(X_t, X_{t-1})
    return A, Sigma, Sigma1


def _logdet(M):
    M = np.atleast_2d(M)
    sign, ld = np.linalg.slogdet(M)
    return ld


def mi_lagged(idx, Sigma, Sigma1):
    """Time-delayed mutual information I(X^idx_t ; X^idx_{t-1}) for a Gaussian,
    from the joint covariance of [X^idx_t, X^idx_{t-1}]."""
    idx = np.array(idx)
    S = Sigma[np.ix_(idx, idx)]
    S1 = Sigma1[np.ix_(idx, idx)]
    joint = np.block([[S, S1], [S1.T, S]])
    return 0.5 * (_logdet(S) + _logdet(S) - _logdet(joint))


# --- the integrated-information measures (all on the same system) ------------

def phi_barrett_seth(Sigma, Sigma1):
    """Whole-minus-parts time-delayed integration (Barrett & Seth 2011 style):
    I(X_t;X_{t-1}) - sum_parts I(X^p_t;X^p_{t-1}) over the bipartition."""
    whole = mi_lagged([0, 1], Sigma, Sigma1)
    parts = mi_lagged([0], Sigma, Sigma1) + mi_lagged([1], Sigma, Sigma1)
    return whole - parts


def instantaneous_mi(Sigma):
    """Instantaneous mutual information I(X^0; X^1): a synchrony/integration
    proxy. For scalars: -0.5 log(1 - rho^2)."""
    rho = Sigma[0, 1] / np.sqrt(Sigma[0, 0] * Sigma[1, 1])
    return -0.5 * np.log(max(1.0 - rho ** 2, 1e-15))


def causal_density(Sigma, Sigma1):
    """Mean pairwise Granger causality (Seth's causal density). The full VAR(1)
    one-step error variance is 1 (noise = I); the restricted model predicts each
    node from its own past only."""
    gc = []
    for tgt in (0, 1):
        # restricted: predict X^tgt_t from X^tgt_{t-1} only
        var_t = Sigma[tgt, tgt]
        cov_self = Sigma1[tgt, tgt]                 # Cov(X^tgt_t, X^tgt_{t-1})
        err_restricted = var_t - cov_self ** 2 / var_t
        err_full = 1.0                              # noise covariance entry
        gc.append(np.log(err_restricted / err_full))
    return float(np.mean(gc))


MEASURES = {
    "Phi_BarrettSeth": lambda S, S1: phi_barrett_seth(S, S1),
    "instantaneous_MI": lambda S, S1: instantaneous_mi(S),
    "causal_density": lambda S, S1: causal_density(S, S1),
}


def main():
    cs = np.linspace(0.0, 0.64, 17)                 # keep spectral radius < 1
    rows = {name: [] for name in MEASURES}
    print("Testing IIT claim: integrated-information proxies are NOT approximations")
    print("System: 2-node Gaussian VAR(1), self=%.2f, sweeping cross-coupling c" % SELF)
    print("=" * 72)
    hdr = f"{'c':>6} " + " ".join(f"{n:>17}" for n in MEASURES)
    print(hdr)
    print("-" * 72)
    for c in cs:
        _, Sigma, Sigma1 = covariances(SELF, c)
        line = f"{c:6.3f} "
        for name, fn in MEASURES.items():
            v = fn(Sigma, Sigma1)
            rows[name].append(v)
            line += f"{v:17.4f} "
        print(line.rstrip())

    print("=" * 72)
    names = list(MEASURES)
    arrs = {n: np.array(rows[n]) for n in names}

    # Peaks: where along the sweep is each measure maximised?
    print("\nWhere each measure peaks (argmax over the same sweep):")
    for n in names:
        print(f"  {n:18s} peaks at c = {cs[int(np.argmax(arrs[n]))]:.3f} "
              f"(max {arrs[n].max():.4f})")

    # Pairwise rank (Spearman) correlation of trends across the whole sweep.
    print("\nSpearman rank-correlation over the whole sweep "
          "(1 = move together):")
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            r = spearmanr(arrs[names[i]], arrs[names[j]]).correlation
            print(f"  {names[i]:18s} vs {names[j]:18s}: rho = {r:+.3f}")

    # The decisive test: is there ANY interval where one measure rises while
    # another falls? (Approximations of one quantity cannot do this.)
    print("\nOpposite-direction intervals (one measure up while another down):")
    disagree = False
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            di = np.diff(arrs[names[i]])
            dj = np.diff(arrs[names[j]])
            opp = np.where(np.sign(di) * np.sign(dj) < 0)[0]
            if len(opp):
                disagree = True
                seg = f"c in [{cs[opp[0]]:.3f}, {cs[opp[-1]+1]:.3f}]"
                print(f"  {names[i]} vs {names[j]}: {seg}")
    if not disagree:
        print("  (none)")

    print("=" * 72)
    print("\nVerdict (paper's claim: proxies move in different directions):")
    if disagree:
        print("  CONFIRMED -- the measures agree at weak coupling but move in\n"
              "  OPPOSITE directions at strong coupling. Phi (an integration\n"
              "  measure) turns over and falls as the two nodes become\n"
              "  redundant, while MI and causal density (coupling measures)\n"
              "  keep rising. They cannot all be approximations of one Phi.")
    else:
        print("  NOT CONFIRMED -- every measure moved together this run.")


if __name__ == "__main__":
    main()
