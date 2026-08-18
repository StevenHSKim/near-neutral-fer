from pathlib import Path

import pandas as pd
from PIL import Image

from data.prepare_ferplus import build_manifest, majority_label

COLS = ["Usage", "Image name", "neutral", "happiness", "surprise", "sadness", "anger",
        "disgust", "fear", "contempt", "unknown", "NF"]


def _make_raw(tmp: Path):
    (tmp / "FERPlus_Image").mkdir()
    rows = [
        # Usage, name, neu,hap,sur,sad,ang,dis,fea,con,unk,NF
        ("Training", "fer0.png", 4, 0, 0, 1, 3, 2, 0, 0, 0, 0),    # neutral majority
        ("Training", "fer1.png", 3, 0, 0, 6, 0, 0, 0, 0, 1, 0),    # sad; neutral share 3/9=0.33 -> near-neutral
        ("PublicTest", "fer2.png", 1, 7, 0, 0, 0, 0, 0, 0, 2, 0),  # happy; share 1/8 -> not near-neutral
        ("PrivateTest", "fer3.png", 0, 0, 0, 0, 0, 0, 0, 0, 9, 1), # unknown majority -> dropped
        ("PrivateTest", "", 5, 0, 0, 0, 0, 0, 0, 0, 0, 0),         # no image -> dropped
        ("PrivateTest", "fer5.png", 2, 0, 0, 0, 0, 0, 0, 0, 0, 8), # NF majority -> dropped
        ("PrivateTest", "fer6.png", 2, 0, 0, 0, 0, 0, 0, 0, 0, 8), # NF majority -> dropped
    ]
    pd.DataFrame(rows, columns=COLS).to_csv(tmp / "FERPlus_Label.csv", index=False)
    for n in ["fer0.png", "fer1.png", "fer2.png", "fer3.png", "fer5.png"]:
        Image.new("L", (48, 48)).save(tmp / "FERPlus_Image" / n)
    return tmp


def test_majority_and_filtering(tmp_path):
    m = build_manifest(_make_raw(tmp_path))
    assert len(m) == 3
    assert m.label.tolist() == [0, 3, 1]
    assert m.split.tolist() == ["train", "train", "val"]
    assert m.vote_neutral.tolist() == [4, 3, 1]


def test_near_neutral_flag(tmp_path):
    m = build_manifest(_make_raw(tmp_path), tau=0.3)
    assert m.near_neutral.tolist() == [False, True, False]
    assert m.total_votes.tolist() == [10, 9, 8]
    (tmp_path / "b").mkdir()
    m2 = build_manifest(_make_raw(tmp_path / "b"), tau=0.4)
    assert m2.near_neutral.tolist() == [False, False, False]


def test_majority_tie_breaks_to_first_column():
    assert majority_label([3, 3, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert majority_label([0, 0, 0, 0, 0, 0, 0, 0, 5, 5]) is None
