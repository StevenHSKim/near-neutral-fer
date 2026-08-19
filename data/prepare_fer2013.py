"""FER2013 -> 112x112 cache + manifest in the RAF-DB label space.

The available `fer2013_modified.csv` has (emotion, pixels) but no `Usage` column. Its rows are in the
canonical fer2013.csv order (verified: per-class counts 4953/547/5121/8989/6077/4002/6198 match the
original), so the official split is recovered by row index: rows [0,28709) Training -> train,
[28709,32298) PublicTest -> val, [32298,35887) PrivateTest -> test. If a FERPlus_Label.csv is
available next to it, its Usage column (same row order) is used to cross-check the split.
Emotion ids 0..6 (Angry,Disgust,Fear,Happy,Sad,Surprise,Neutral) are mapped to RAF-DB indices.
"""
import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image
from tqdm import tqdm

from nnfer.data.cache import write_cache
from nnfer.data.labels import FER2013_TO_RAFDB

N_TRAIN, N_PUBLIC, N_PRIVATE = 28709, 3589, 3589


def build_manifest(csv_path: Path, ferplus_csv: Path | None = None) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    n = len(df)
    assert n == N_TRAIN + N_PUBLIC + N_PRIVATE, f"unexpected row count {n}"
    split = np.array(["train"] * N_TRAIN + ["val"] * N_PUBLIC + ["test"] * N_PRIVATE)
    if ferplus_csv is not None and Path(ferplus_csv).exists():
        usage = pd.read_csv(ferplus_csv)["Usage"].map({"Training": "train", "PublicTest": "val", "PrivateTest": "test"})
        assert (usage.to_numpy() == split).all(), "FERPlus Usage order does not match canonical fer2013 order"
    return pd.DataFrame({
        "path": [f"{csv_path}#row{i}" for i in range(n)],  # provenance only; pixels come from the csv
        "label": df["emotion"].map(FER2013_TO_RAFDB).astype(int),
        "split": split,
        "fer2013_emotion": df["emotion"].astype(int),
    })


def decode_images(csv_path: Path, size: int):
    df = pd.read_csv(csv_path)
    out = []
    for px in tqdm(df["pixels"], desc="fer2013", mininterval=10):
        a = np.asarray(px.split(), dtype=np.uint8).reshape(48, 48)
        im = Image.fromarray(a, "L").convert("RGB").resize((size, size), Image.BILINEAR)
        out.append(np.asarray(im, dtype=np.uint8))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default="/mnt/c/Users/steve/Desktop/dataset/FER2013/fer2013_modified.csv")
    ap.add_argument("--ferplus-csv", default="/mnt/c/Users/steve/Desktop/dataset/FERPlus/FERPlus_Label.csv")
    ap.add_argument("--out", default="~/haesung/data/cache/fer2013")
    ap.add_argument("--size", type=int, default=112)
    a = ap.parse_args()
    m = build_manifest(Path(a.raw), Path(a.ferplus_csv))
    imgs = decode_images(Path(a.raw), a.size)
    write_cache(imgs, m, Path(a.out).expanduser(), "fer2013", a.size)
    print(m.groupby(["split", "label"]).size().unstack(fill_value=0))


if __name__ == "__main__":
    main()
