"""Evaluation metrics (spec §5): standard, near-neutral, calibration.

All functions take raw logits + integer labels (numpy) and are dataset-aware only through
the label taxonomy (`nnfer.data.labels`), so results are directly comparable across models.
"""
import numpy as np
import pandas as pd
from scipy.special import softmax
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score

from nnfer.data.labels import NEAR_NEUTRAL_CLASSES, NEUTRAL_INDEX, NUM_CLASSES

TAUS = (0.2, 0.3, 0.4)


def ece(probs: np.ndarray, labels: np.ndarray, n_bins: int = 15) -> float:
    """Expected calibration error with equal-width confidence bins."""
    conf = probs.max(axis=1)
    pred = probs.argmax(axis=1)
    correct = (pred == labels).astype(float)
    bins = np.linspace(0.0, 1.0, n_bins + 1)
    total = 0.0
    for lo, hi in zip(bins[:-1], bins[1:]):
        m = (conf > lo) & (conf <= hi)
        if m.any():
            total += m.mean() * abs(correct[m].mean() - conf[m].mean())
    return float(total)


def _core(preds, labels, probs, num_classes, neutral, nn_classes):
    out = {
        "n": int(len(labels)),
        "acc": float(accuracy_score(labels, preds)),
        "macro_f1": float(f1_score(labels, preds, labels=list(range(num_classes)), average="macro", zero_division=0)),
        "per_class_f1": f1_score(labels, preds, labels=list(range(num_classes)), average=None, zero_division=0).tolist(),
        "confusion": confusion_matrix(labels, preds, labels=list(range(num_classes))).tolist(),
        "near_neutral_macro_f1": float(f1_score(labels, preds, labels=nn_classes, average="macro", zero_division=0)),
        "ece": ece(probs, labels),
        "mean_entropy": float(-(probs * np.log(np.clip(probs, 1e-12, 1))).sum(1).mean()),
    }
    non_neutral = labels != neutral
    out["fnr"] = float((preds[non_neutral] == neutral).mean()) if non_neutral.any() else None
    if (labels == neutral).any():
        out["neutral_recall"] = float((preds[labels == neutral] == neutral).mean())
        out["neutral_f1"] = float(f1_score(labels == neutral, preds == neutral, zero_division=0))
    else:
        out["neutral_recall"] = None
        out["neutral_f1"] = None
    return out


def compute_metrics(logits: np.ndarray, labels: np.ndarray, dataset: str,
                    manifest: pd.DataFrame | None = None) -> dict:
    """Metrics dict for one split. `dataset` in {rafdb, ferplus, ckplus} (ckplus uses RAF-DB space)."""
    space = "rafdb" if dataset == "ckplus" else dataset
    C = NUM_CLASSES[space]
    neutral = NEUTRAL_INDEX[space]
    nn_classes = NEAR_NEUTRAL_CLASSES[space]
    logits = np.asarray(logits, dtype=np.float64)
    labels = np.asarray(labels).astype(int)
    probs = softmax(logits, axis=1)
    preds = probs.argmax(axis=1)
    out = _core(preds, labels, probs, C, neutral, nn_classes)

    if manifest is not None and "neutral_share" in manifest:
        share = manifest["neutral_share"].to_numpy(dtype=float)
        assert len(share) == len(labels), "manifest/labels length mismatch"
        for tau in TAUS:
            mask = (labels != neutral) & (share >= tau)
            out[f"nn_subset_n@{tau}"] = int(mask.sum())
            if mask.any():
                out[f"nn_subset_acc@{tau}"] = float(accuracy_score(labels[mask], preds[mask]))
                out[f"nn_subset_macro_f1@{tau}"] = float(
                    f1_score(labels[mask], preds[mask], labels=list(range(C)), average="macro", zero_division=0))
                out[f"nn_subset_fnr@{tau}"] = float((preds[mask] == neutral).mean())
            else:
                out[f"nn_subset_acc@{tau}"] = out[f"nn_subset_macro_f1@{tau}"] = out[f"nn_subset_fnr@{tau}"] = None
    return out
