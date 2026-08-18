from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image

from data.prepare_rafdb import build_manifest
from nnfer.data.cache import load_rgb, write_cache


def _make_raw(tmp: Path, n_train=70, n_test=10):
    (tmp / "EmoLabel").mkdir()
    (tmp / "Image" / "aligned").mkdir(parents=True)
    lines = []
    for i in range(n_train):
        lab = (i % 7) + 1
        lines.append(f"train_{i + 1:05d}.jpg {lab}")
        Image.new("RGB", (100, 100), (i, 0, 0)).save(tmp / "Image" / "aligned" / f"train_{i + 1:05d}_aligned.jpg")
    for i in range(n_test):
        lines.append(f"test_{i + 1:04d}.jpg {(i % 7) + 1}")
        Image.new("RGB", (100, 100)).save(tmp / "Image" / "aligned" / f"test_{i + 1:04d}_aligned.jpg")
    (tmp / "EmoLabel" / "list_patition_label.txt").write_text("\n".join(lines) + "\n")
    return tmp


def test_manifest_splits_and_labels(tmp_path):
    m = build_manifest(_make_raw(tmp_path))
    assert set(m.columns) >= {"path", "label", "split"}
    assert m.label.between(0, 6).all()
    assert (m.split == "test").sum() == 10
    assert (m.split == "val").sum() == 7  # 10 % of 70
    assert (m.split == "train").sum() == 63
    assert all(Path(p).exists() for p in m.path)


def test_val_split_is_deterministic_and_stratified(tmp_path):
    raw = _make_raw(tmp_path)
    a = build_manifest(raw)
    b = build_manifest(raw)
    assert (a[a.split == "val"].path.values == b[b.split == "val"].path.values).all()
    # 70 train, 10 per class -> exactly one val per class
    assert a[a.split == "val"].label.value_counts().tolist() == [1] * 7


def test_write_cache_roundtrip(tmp_path):
    raw = _make_raw(tmp_path)
    m = build_manifest(raw)
    imgs = [load_rgb(Path(p), 112) for p in m.path]
    write_cache(imgs, m, tmp_path / "out", "rafdb")
    arr = np.load(tmp_path / "out" / "rafdb_images.npy", mmap_mode="r")
    assert arr.shape == (80, 112, 112, 3) and arr.dtype == np.uint8
    m2 = pd.read_csv(tmp_path / "out" / "rafdb_manifest.csv")
    assert len(m2) == 80 and (tmp_path / "out" / "rafdb_manifest.md5").exists()
    assert (m2.label.values == m.label.values).all()
