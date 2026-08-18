"""Numpy-backed FER dataset reading the 112x112 uint8 cache + manifest for one split."""
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from PIL import Image
from torch.utils.data import Dataset


class CachedFER(Dataset):
    """`(image_tensor, label)` pairs from `<cache_dir>/<name>_{images.npy,manifest.csv}` for `split`.

    Attributes: `manifest` (rows of this split, index reset), `labels` (np.int64), `images` (memmap of
    the *whole* cache; use `idx` to map split position -> cache row).
    """

    def __init__(self, cache_dir, name: str, split: str, transform=None):
        cache_dir = Path(cache_dir).expanduser()
        full = pd.read_csv(cache_dir / f"{name}_manifest.csv")
        self.images = np.load(cache_dir / f"{name}_images.npy", mmap_mode="r")
        assert len(full) == len(self.images), "manifest/cache length mismatch"
        self.idx = np.flatnonzero((full.split == split).values)
        if len(self.idx) == 0:
            raise ValueError(f"split {split!r} not found in {name} manifest")
        self.manifest = full.iloc[self.idx].reset_index(drop=True)
        self.labels = self.manifest.label.to_numpy(np.int64)
        self.transform = transform

    def __len__(self):
        return len(self.idx)

    def __getitem__(self, i):
        img = Image.fromarray(np.asarray(self.images[self.idx[i]]))
        if self.transform is not None:
            x = self.transform(img)
        else:
            x = torch.from_numpy(np.asarray(img).copy()).permute(2, 0, 1).float() / 255
        return x, int(self.labels[i])
