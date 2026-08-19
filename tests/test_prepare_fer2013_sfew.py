from pathlib import Path

import numpy as np
import pandas as pd
import pytest
from PIL import Image

from data.prepare_fer2013 import N_PRIVATE, N_PUBLIC, N_TRAIN, build_manifest as fer_manifest, decode_images
from data.prepare_sfew import build_manifest as sfew_manifest
from nnfer.data.labels import RAFDB_CLASSES
from nnfer.metrics import compute_metrics


def _fer_csv(tmp: Path, n_train, n_pub, n_priv):
    n = n_train + n_pub + n_priv
    px = " ".join(["7"] * 2304)
    pd.DataFrame({"emotion": [i % 7 for i in range(n)], "pixels": [px] * n}).to_csv(tmp / "fer.csv", index=False)
    usage = ["Training"] * n_train + ["PublicTest"] * n_pub + ["PrivateTest"] * n_priv
    pd.DataFrame({"Usage": usage, "Image name": ["x"] * n}).to_csv(tmp / "ferplus.csv", index=False)
    return tmp / "fer.csv", tmp / "ferplus.csv"


def test_fer2013_split_by_row_and_label_mapping(tmp_path, monkeypatch):
    import data.prepare_fer2013 as mod
    monkeypatch.setattr(mod, "N_TRAIN", 14)
    monkeypatch.setattr(mod, "N_PUBLIC", 7)
    monkeypatch.setattr(mod, "N_PRIVATE", 7)
    fer, plus = _fer_csv(tmp_path, 14, 7, 7)
    m = mod.build_manifest(fer, plus)
    assert m.split.tolist() == ["train"] * 14 + ["val"] * 7 + ["test"] * 7
    # emotion 6 (Neutral) -> rafdb neutral (6); emotion 0 (Angry) -> 5; emotion 5 (Surprise) -> 0
    assert RAFDB_CLASSES[m.label[6]] == "neutral" and RAFDB_CLASSES[m.label[0]] == "anger"
    assert RAFDB_CLASSES[m.label[5]] == "surprise"
    imgs = decode_images(fer, 112)
    assert imgs[0].shape == (112, 112, 3) and imgs[0].max() == 7


def test_fer2013_constants_are_official():
    assert (N_TRAIN, N_PUBLIC, N_PRIVATE) == (28709, 3589, 3589)


def test_sfew_manifest(tmp_path):
    (tmp_path / "sfew2.0_images").mkdir()
    rows = []
    emos = ["Angry", "Disgust", "Fear", "Happy", "Neutral", "Sad", "Surprise"]
    for i in range(70):
        rows.append((f"image_{i}.png", i % 7, emos[i % 7], "Train_Aligned_Faces"))
    for i in range(70, 84):
        rows.append((f"image_{i}.png", i % 7, emos[i % 7], "Val_Aligned_Faces"))
    pd.DataFrame(rows, columns=["image_name", "label", "emotion", "original_split"]).to_csv(tmp_path / "sfew_2.0_labels.csv", index=False)
    for r in rows:
        Image.new("RGB", (143, 181)).save(tmp_path / "sfew2.0_images" / r[0])
    m = sfew_manifest(tmp_path)
    assert (m.split == "test").sum() == 14 and (m.split == "val").sum() == 7 and (m.split == "train").sum() == 63
    assert RAFDB_CLASSES[m[m.emotion == "neutral"].label.iloc[0]] == "neutral"


def test_metrics_accept_new_datasets():
    labels = np.array([6, 6, 4, 0, 1])
    logits = np.zeros((5, 7)); logits[np.arange(5), [6, 4, 6, 0, 1]] = 5
    for ds in ("fer2013", "sfew"):
        m = compute_metrics(logits, labels, ds)
        assert m["neutral_recall"] == pytest.approx(0.5) and m["fnr"] == pytest.approx(1 / 3)
