"""Uint8 image cache + manifest writer shared by all preprocessing scripts."""
import hashlib
from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image


def load_rgb(path: Path, size: int) -> np.ndarray:
    """Open image, convert to RGB, bilinear-resize to (size, size); returns HWC uint8."""
    with Image.open(path) as im:
        im = im.convert("RGB").resize((size, size), Image.BILINEAR)
        return np.asarray(im, dtype=np.uint8)


def write_cache(images, manifest: pd.DataFrame, out_dir: Path, name: str, size: int = 112) -> None:
    """Write <name>_images.npy (N,size,size,3 uint8), <name>_manifest.csv and its md5."""
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    arr = np.stack(images).astype(np.uint8)
    assert arr.shape[1:] == (size, size, 3), arr.shape
    assert len(arr) == len(manifest), (len(arr), len(manifest))
    np.save(out_dir / f"{name}_images.npy", arr)
    csv_path = out_dir / f"{name}_manifest.csv"
    manifest.to_csv(csv_path, index=False)
    md5 = hashlib.md5(csv_path.read_bytes()).hexdigest()
    (out_dir / f"{name}_manifest.md5").write_text(md5 + "\n")
