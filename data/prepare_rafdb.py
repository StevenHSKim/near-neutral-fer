"""RAF-DB basic (aligned) -> 112x112 cache + manifest with a fixed stratified val split.

Split policy (spec §3): official test kept as `test`; 10 % of official train held out as
`val`, stratified by label, random_state=0. Identical for every model.
"""
import argparse
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split
from tqdm import tqdm

from nnfer.data.cache import load_rgb, write_cache


def build_manifest(raw_root: Path, val_frac: float = 0.1, seed: int = 0) -> pd.DataFrame:
    raw_root = Path(raw_root)
    rows = []
    for line in (raw_root / "EmoLabel" / "list_patition_label.txt").read_text().splitlines():
        if not line.strip():
            continue
        name, lab = line.split()
        stem = name[:-4]
        rows.append({
            "path": str(raw_root / "Image" / "aligned" / f"{stem}_aligned.jpg"),
            "label": int(lab) - 1,
            "split": "test" if stem.startswith("test") else "train",
        })
    m = pd.DataFrame(rows)
    tr = m.index[m.split == "train"]
    _, val_idx = train_test_split(tr, test_size=val_frac, stratify=m.loc[tr, "label"], random_state=seed)
    m.loc[val_idx, "split"] = "val"
    return m.reset_index(drop=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default="/mnt/c/Users/steve/Desktop/dataset/RAFDB")
    ap.add_argument("--out", default="~/haesung/data/cache/rafdb")
    ap.add_argument("--size", type=int, default=112)
    a = ap.parse_args()
    m = build_manifest(Path(a.raw))
    imgs = [load_rgb(Path(p), a.size) for p in tqdm(m.path, desc="rafdb", mininterval=5)]
    write_cache(imgs, m, Path(a.out).expanduser(), "rafdb", a.size)
    print(m.groupby(["split", "label"]).size().unstack(fill_value=0))


if __name__ == "__main__":
    main()
