"""FERPlus -> 112x112 cache + manifest.

Label policy (spec §3): majority vote over the 8 emotion columns (first column wins ties);
rows whose max vote is `unknown`/`NF`, or without an image file, are dropped. All 10 vote
counts are kept. `near_neutral` = majority != neutral and neutral_share >= tau (spec §5.4),
where neutral_share = neutral votes / total emotion votes (unknown/NF excluded).
"""
import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from tqdm import tqdm

from nnfer.data.cache import load_rgb, write_cache
from nnfer.data.labels import FERPLUS_CLASSES, FERPLUS_VOTE_COLUMNS, NEUTRAL_INDEX

SPLIT = {"Training": "train", "PublicTest": "val", "PrivateTest": "test"}


def majority_label(votes) -> int | None:
    """Index of the max vote among FERPLUS_VOTE_COLUMNS (first wins ties); None if unknown/NF wins."""
    k = int(np.asarray(votes).argmax())
    return None if k >= len(FERPLUS_CLASSES) else k


def build_manifest(raw_root: Path, tau: float = 0.3) -> pd.DataFrame:
    raw_root = Path(raw_root)
    df = pd.read_csv(raw_root / "FERPlus_Label.csv")
    df["Image name"] = df["Image name"].fillna("")
    rows = []
    for _, r in df.iterrows():
        name = str(r["Image name"]).strip()
        if not name:
            continue
        p = raw_root / "FERPlus_Image" / name
        if not p.exists():
            continue
        votes = [int(r[c]) for c in FERPLUS_VOTE_COLUMNS]
        lab = majority_label(votes)
        if lab is None:
            continue
        emo = votes[: len(FERPLUS_CLASSES)]
        total = int(sum(emo))
        share = emo[NEUTRAL_INDEX["ferplus"]] / total if total else 0.0
        row = {
            "path": str(p), "label": lab, "split": SPLIT[r["Usage"]],
            "near_neutral": bool(lab != NEUTRAL_INDEX["ferplus"] and share >= tau),
            "neutral_share": share, "total_votes": total,
        }
        row.update({f"vote_{c}": v for c, v in zip(FERPLUS_VOTE_COLUMNS, votes)})
        rows.append(row)
    return pd.DataFrame(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default="/mnt/c/Users/steve/Desktop/dataset/FERPlus")
    ap.add_argument("--out", default="~/haesung/data/cache/ferplus")
    ap.add_argument("--size", type=int, default=112)
    ap.add_argument("--tau", type=float, default=0.3)
    a = ap.parse_args()
    m = build_manifest(Path(a.raw), a.tau)
    imgs = [load_rgb(Path(p), a.size) for p in tqdm(m.path, desc="ferplus", mininterval=30)]
    write_cache(imgs, m, Path(a.out).expanduser(), "ferplus", a.size)
    print(m.groupby(["split", "label"]).size().unstack(fill_value=0))
    print("near-neutral per split:\n", m.groupby("split").near_neutral.sum())


if __name__ == "__main__":
    main()
