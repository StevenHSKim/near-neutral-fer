from pathlib import Path

import pandas as pd
import pytest
from PIL import Image

from data.prepare_ckplus import build_manifest


def _make_raw(tmp: Path, rows):
    (tmp / "ckplus_images").mkdir()
    pd.DataFrame(rows, columns=["image_name", "label", "emotion"]).to_csv(tmp / "ckplus_labels.csv", index=False)
    for n, _, _ in rows:
        Image.new("L", (48, 48)).save(tmp / "ckplus_images" / n)
    return tmp


def test_ck_mapping_drops_contempt(tmp_path):
    rows = [("image_0.png", 0, "anger"), ("image_1.png", 1, "contempt"),
            ("image_2.png", 4, "happy"), ("image_3.png", 6, "surprise")]
    m = build_manifest(_make_raw(tmp_path, rows))
    assert len(m) == 3
    assert m.label.tolist() == [5, 3, 0]  # anger, happiness, surprise in RAF-DB order
    assert (m.split == "test").all()
    assert m.emotion.tolist() == ["anger", "happy", "surprise"]


def test_unknown_emotion_raises(tmp_path):
    with pytest.raises(ValueError):
        build_manifest(_make_raw(tmp_path, [("image_0.png", 0, "boredom")]))
