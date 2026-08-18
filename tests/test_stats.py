import numpy as np
import pytest

from analysis.stats import cohens_d_paired, holm, mcnemar, mean_ci, paired_tests


def test_mean_ci_known_values():
    m, s, h = mean_ci([1, 2, 3, 4, 5])
    assert m == 3 and s == pytest.approx(np.std([1, 2, 3, 4, 5], ddof=1))
    assert h == pytest.approx(2.776445 * s / np.sqrt(5), rel=1e-5)  # t_{0.975,4}
    assert mean_ci([7.0]) == (7.0, 0.0, 0.0)


def test_paired_tests_direction_and_effect():
    a = [0.80, 0.82, 0.81, 0.83, 0.80]
    b = [0.70, 0.71, 0.72, 0.70, 0.71]
    r = paired_tests(a, b)
    assert r["mean_diff"] > 0 and r["t_p"] < 0.01 and r["cohens_d"] > 2
    assert r["wilcoxon_p"] == pytest.approx(0.0625, abs=1e-6)  # n=5 two-sided minimum
    assert paired_tests(a, a)["t_p"] == 1.0
    assert cohens_d_paired([1, 2, 3], [1, 2, 3]) == 0.0


def test_holm_monotone_and_bounded():
    adj = holm([0.01, 0.04, 0.03, 0.20])
    # sorted: 0.01*4=0.04, 0.03*3=0.09, 0.04*2=0.08 -> monotone 0.09, 0.20*1
    assert adj == pytest.approx([0.04, 0.09, 0.09, 0.20])
    assert all(0 <= p <= 1 for p in adj)


def test_mcnemar_exact():
    a = np.array([1, 1, 1, 1, 0, 0, 1, 1, 1, 1], bool)
    b = np.array([1, 0, 0, 0, 0, 0, 1, 1, 1, 1], bool)
    r = mcnemar(a, b)
    assert (r["n01"], r["n10"]) == (3, 0)
    assert r["p"] == pytest.approx(0.25)
    assert mcnemar(a, a)["p"] == 1.0
