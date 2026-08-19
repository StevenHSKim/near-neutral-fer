"""SFEW 2.0 (aligned faces) -> 112x112 cache + manifest in the RAF-DB label space.

Available: sfew_2.0_labels.csv (image_name,label,emotion,original_split) with Train_Aligned_Faces /
Val_Aligned_Faces rows (test labels are not public). Protocol: official Val -> `test`; official Train
-> `train` with a 10 % stratified hold-out (seed 0) as `val` for checkpoint selection, mirroring the
RAF-DB policy. Aligned faces (143x181) are resized directly to size x size.
"""
import argparse
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split
from tqdm import tqdm

from nnfer.data.cache import load_rgb, write_cache
from nnfer.data.labels import SFEW_TO_RAFDB


def build_manifest(raw_root: Path, val_frac: float = 0.1, seed: int = 0) -> pd.DataFrame:
    raw_root = Path(raw_root)
    df = pd.read_csv(raw_root / "sfew_2.0_labels.csv")
    rows = []
    for _, r in df.iterrows():
        emo = str(r["emotion"]).strip().lower()
        if emo not in SFEW_TO_RAFDB:
            raise ValueError(f"unknown SFEW emotion {emo!r}")
        os_ = str(r["original_split"])
        split = "train" if os_.startswith("Train") else "test" if os_.startswith("Val") else None
        if split is None:
            continue
        rows.append({"path": str(raw_root / "sfew2.0_images" / r["image_name"]), "label": SFEW_TO_RAFDB[emo],
                     "split": split, "emotion": emo, "original_split": os_})
    m = pd.DataFrame(rows)
    tr = m.index[m.split == "train"]
    _, val_idx = train_test_split(tr, test_size=val_frac, stratify=m.loc[tr, "label"], random_state=seed)
    m.loc[val_idx, "split"] = "val"
    return m.reset_index(drop=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default="/mnt/c/Users/steve/Desktop/dataset/SFEW2.0")
    ap.add_argument("--out", default="~/haesung/data/cache/sfew")
    ap.add_argument("--size", type=int, default=112)
    a = ap.parse_args()
    m = build_manifest(Path(a.raw))
    imgs = [load_rgb(Path(p), a.size) for p in tqdm(m.path, desc="sfew", mininterval=5)]
    write_cache(imgs, m, Path(a.out).expanduser(), "sfew", a.size)
    print(m.groupby(["split", "label"]).size().unstack(fill_value=0))


if __name__ == "__main__":
    main()
