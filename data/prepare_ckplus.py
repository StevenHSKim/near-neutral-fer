"""CK+48 (Kaggle variant: last 3 frames of each CK+ sequence, 48x48) -> 112x112 cache.

Used only as a cross-dataset *test* set (spec: decision A). Labels are mapped into the
RAF-DB label space; contempt (no RAF-DB counterpart) is dropped.
"""
import argparse
from pathlib import Path

import pandas as pd
from tqdm import tqdm

from nnfer.data.cache import load_rgb, write_cache
from nnfer.data.labels import CKPLUS_TO_RAFDB


def build_manifest(raw_root: Path) -> pd.DataFrame:
    raw_root = Path(raw_root)
    df = pd.read_csv(raw_root / "ckplus_labels.csv")
    rows = []
    for _, r in df.iterrows():
        emo = str(r["emotion"]).strip().lower()
        if emo not in CKPLUS_TO_RAFDB:
            raise ValueError(f"unknown CK+ emotion {emo!r}")
        lab = CKPLUS_TO_RAFDB[emo]
        if lab is None:
            continue
        rows.append({"path": str(raw_root / "ckplus_images" / r["image_name"]),
                     "label": lab, "split": "test", "emotion": emo})
    return pd.DataFrame(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default="/mnt/c/Users/steve/Desktop/dataset/CKPlus")
    ap.add_argument("--out", default="~/haesung/data/cache/ckplus")
    ap.add_argument("--size", type=int, default=112)
    a = ap.parse_args()
    m = build_manifest(Path(a.raw))
    imgs = [load_rgb(Path(p), a.size) for p in tqdm(m.path, desc="ckplus", mininterval=10)]
    write_cache(imgs, m, Path(a.out).expanduser(), "ckplus", a.size)
    print(m.groupby(["label", "emotion"]).size())


if __name__ == "__main__":
    main()
