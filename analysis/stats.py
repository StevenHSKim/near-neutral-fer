"""Statistical tests over seed-paired scores (spec §6). Pure functions, no I/O."""
import numpy as np
from scipy import stats


def mean_ci(x, conf: float = 0.95):
    """Mean, sample std (ddof=1), and half-width of the t-based CI. std/CI are 0 for n<2."""
    x = np.asarray(x, dtype=float)
    n = len(x)
    m = float(x.mean())
    if n < 2:
        return m, 0.0, 0.0
    s = float(x.std(ddof=1))
    h = float(stats.t.ppf(0.5 + conf / 2, n - 1) * s / np.sqrt(n))
    return m, s, h


def cohens_d_paired(a, b) -> float:
    d = np.asarray(a, float) - np.asarray(b, float)
    sd = d.std(ddof=1) if len(d) > 1 else 0.0
    return float(d.mean() / sd) if sd > 0 else float("inf") if d.mean() != 0 else 0.0


def paired_tests(a, b) -> dict:
    """a, b: seed-aligned score arrays (higher = better). Returns t/Wilcoxon p-values and effect size."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    assert a.shape == b.shape and len(a) >= 2
    d = a - b
    out = {"n": int(len(a)), "mean_diff": float(d.mean())}
    if np.allclose(d, 0):
        out.update(t_p=1.0, wilcoxon_p=1.0, cohens_d=0.0)
        return out
    out["t_p"] = float(stats.ttest_rel(a, b).pvalue)
    try:
        out["wilcoxon_p"] = float(stats.wilcoxon(a, b, zero_method="wilcox").pvalue)
    except ValueError:  # all differences zero after filtering
        out["wilcoxon_p"] = 1.0
    out["cohens_d"] = cohens_d_paired(a, b)
    return out


def holm(pvals):
    """Holm-Bonferroni adjusted p-values (same order as input)."""
    p = np.asarray(pvals, float)
    n = len(p)
    order = np.argsort(p)
    adj = np.empty(n)
    running = 0.0
    for rank, i in enumerate(order):
        running = max(running, (n - rank) * p[i])
        adj[i] = min(1.0, running)
    return adj.tolist()


def mcnemar(correct_a, correct_b) -> dict:
    """Exact (binomial) McNemar test on per-sample correctness of two models on the same test set."""
    a, b = np.asarray(correct_a, bool), np.asarray(correct_b, bool)
    n01 = int((a & ~b).sum())  # a right, b wrong
    n10 = int((~a & b).sum())  # a wrong, b right
    n = n01 + n10
    p = 1.0 if n == 0 else float(min(1.0, 2 * stats.binom.cdf(min(n01, n10), n, 0.5)))
    return {"n01": n01, "n10": n10, "p": p}
