import numpy as np
import pandas as pd
import pytest

from nnfer.metrics import compute_metrics, ece


def one_hot(preds, C=7, scale=10.0):
    z = np.zeros((len(preds), C), dtype=np.float32)
    z[np.arange(len(preds)), preds] = scale
    return z


def test_basic_metrics_rafdb():
    labels = np.array([6, 6, 4, 4, 3])          # neutral, neutral, sad, sad, happy
    logits = one_hot([6, 4, 6, 4, 3])           # one neutral->sad, one sad->neutral
    m = compute_metrics(logits, labels, "rafdb")
    assert m["acc"] == pytest.approx(3 / 5)
    assert m["neutral_recall"] == pytest.approx(0.5)
    assert m["fnr"] == pytest.approx(1 / 3)     # 1 of 3 non-neutral predicted neutral
    assert len(m["per_class_f1"]) == 7 and np.array(m["confusion"]).shape == (7, 7)
    assert 0.0 <= m["near_neutral_macro_f1"] <= 1.0
    assert m["mean_entropy"] >= 0.0


def test_ferplus_subset_from_manifest():
    manifest = pd.DataFrame({"neutral_share": [0.5, 0.1, 0.35, 0.9], "label": [3, 1, 4, 0]})
    labels = np.array([3, 1, 4, 0])
    logits = one_hot([3, 1, 0, 0], C=8)
    m = compute_metrics(logits, labels, "ferplus", manifest)
    assert m["nn_subset_n@0.3"] == 2                    # rows 0 and 2 (row 3 is neutral itself)
    assert m["nn_subset_acc@0.3"] == pytest.approx(0.5)
    assert m["nn_subset_n@0.2"] == 2 and m["nn_subset_n@0.4"] == 1
    assert m["neutral_recall"] == pytest.approx(1.0)


def test_ckplus_has_no_neutral_metrics():
    labels = np.array([0, 1, 2, 3, 4, 5])
    m = compute_metrics(one_hot([0, 1, 2, 3, 6, 5]), labels, "ckplus")
    assert m["neutral_recall"] is None
    assert m["fnr"] == pytest.approx(1 / 6)


def test_ece_perfectly_calibrated_zero():
    probs = np.array([[1.0, 0.0]] * 10)
    assert ece(probs, np.zeros(10, int)) == pytest.approx(0.0)
    probs = np.array([[0.6, 0.4]] * 10)     # confident 0.6, accuracy 1.0 -> gap 0.4
    assert ece(probs, np.zeros(10, int)) == pytest.approx(0.4)
