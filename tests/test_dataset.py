from pathlib import Path

import numpy as np
import pandas as pd
import torch

from nnfer.data.cache import write_cache
from nnfer.data.dataset import CachedFER
from nnfer.data.transforms import build_transforms


def _cache(tmp: Path):
    imgs = [np.full((112, 112, 3), 40 * i, np.uint8) for i in range(6)]
    m = pd.DataFrame({"path": [f"p{i}" for i in range(6)], "label": [0, 1, 2, 0, 1, 2],
                      "split": ["train", "train", "train", "val", "test", "test"],
                      "near_neutral": [False, True, False, False, True, False]})
    write_cache(imgs, m, tmp, "toy")
    return tmp


def test_split_filtering_and_shapes(tmp_path):
    ds = CachedFER(_cache(tmp_path), "toy", "test", transform=build_transforms(False))
    assert len(ds) == 2
    x, y = ds[0]
    assert x.shape == (3, 112, 112) and x.dtype == torch.float32 and y == 1
    assert ds.labels.tolist() == [1, 2]
    assert ds.manifest.near_neutral.tolist() == [True, False]


def test_eval_transform_is_deterministic_and_normalised(tmp_path):
    ds = CachedFER(_cache(tmp_path), "toy", "val", transform=build_transforms(False))
    a, _ = ds[0]
    b, _ = ds[0]
    assert torch.equal(a, b)
    # pixel value 120/255 normalised with ImageNet mean/std for channel 0
    assert abs(a[0, 0, 0].item() - (120 / 255 - 0.485) / 0.229) < 1e-5


def test_train_transform_is_stochastic_but_seedable(tmp_path):
    ds = CachedFER(_cache(tmp_path), "toy", "train", transform=build_transforms(True))
    torch.manual_seed(0)
    a, _ = ds[0]
    torch.manual_seed(0)
    b, _ = ds[0]
    assert torch.equal(a, b)
    assert a.shape == (3, 112, 112)
