import json
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from nnfer.data.cache import write_cache
from nnfer.train import main


def _toy_cache(root: Path, name: str, C: int, n: int = 24):
    rng = np.random.default_rng(0)
    imgs = [rng.integers(0, 255, (112, 112, 3), dtype=np.uint8) for _ in range(n)]
    split = ["train"] * (n // 2) + ["val"] * (n // 4) + ["test"] * (n - n // 2 - n // 4)
    m = pd.DataFrame({"path": [f"p{i}" for i in range(n)], "label": [i % C for i in range(n)], "split": split})
    if name == "ferplus":
        m["neutral_share"] = rng.random(n)
    write_cache(imgs, m, root / name, name)


@pytest.mark.parametrize("dataset,C", [("rafdb", 7), ("ferplus", 8)])
def test_train_writes_all_artefacts(tmp_path, dataset, C):
    _toy_cache(tmp_path / "cache", dataset, C)
    out = main(["--model", "microexpnet", "--dataset", dataset, "--seed", "1", "--epochs", "2",
                "--batch", "4", "--workers", "0", "--no-amp", "--no-pretrained",
                "--cache", str(tmp_path / "cache"), "--runs", str(tmp_path / "runs")])
    for f in ["config.json", "history.csv", "metrics.json", "preds.npz", "best.pt"]:
        assert (out / f).exists(), f
    met = json.loads((out / "metrics.json").read_text())
    assert 0.0 <= met["test"]["acc"] <= 1.0 and met["params"] > 0 and met["best_epoch"] in (1, 2)
    hist = pd.read_csv(out / "history.csv")
    assert len(hist) == 2
    p = np.load(out / "preds.npz")
    assert p["test_logits"].shape == (6, C)
    if dataset == "ferplus":
        assert "nn_subset_n@0.3" in met["test"]
    # rerun without --overwrite is a no-op skip
    assert main(["--model", "microexpnet", "--dataset", dataset, "--seed", "1", "--workers", "0",
                 "--cache", str(tmp_path / "cache"), "--runs", str(tmp_path / "runs")]) == out


def test_two_runs_same_seed_are_identical(tmp_path):
    _toy_cache(tmp_path / "cache", "rafdb", 7)
    args = ["--model", "microexpnet", "--dataset", "rafdb", "--seed", "3", "--epochs", "2", "--batch", "4",
            "--workers", "0", "--no-amp", "--no-pretrained", "--cache", str(tmp_path / "cache")]
    a = main(args + ["--runs", str(tmp_path / "r1")])
    b = main(args + ["--runs", str(tmp_path / "r2")])
    la, lb = np.load(a / "preds.npz")["test_logits"], np.load(b / "preds.npz")["test_logits"]
    assert np.allclose(la, lb, atol=1e-5)
