import numpy as np
import pandas as pd
import pytest
import torch

from nnfer.data.cache import write_cache
from nnfer.engine import ModelEMA
from nnfer.losses import NNSKDLoss
from nnfer.mixup import MixupCutmix
from nnfer.seed import seed_everything


def test_mixup_shapes_and_lam():
    seed_everything(0)
    mix = MixupCutmix(mixup_alpha=0.2, cutmix_alpha=1.0, p=1.0)
    x = torch.rand(8, 3, 112, 112)
    y = torch.arange(8) % 7
    xm, ya, yb, lam = mix(x, y)
    assert xm.shape == x.shape and 0.0 <= lam <= 1.0
    assert torch.equal(ya, y) and yb.shape == y.shape
    # p=0 passes through
    x2, ya2, yb2, lam2 = MixupCutmix(0.2, 1.0, p=0.0)(x, y)
    assert torch.equal(x2, x) and lam2 == 1.0


def test_mixed_ce_interpolates():
    crit = NNSKDLoss(6, label_smoothing=0.0)
    z = torch.randn(4, 7)
    ya = torch.tensor([0, 1, 2, 3])
    yb = torch.tensor([4, 5, 6, 0])
    la = crit(z, ya)
    lb = crit(z, yb)
    lm = crit(z, ya, yb, lam=0.3)
    assert lm.item() == pytest.approx(0.3 * la.item() + 0.7 * lb.item(), rel=1e-5)


def test_logit_adjustment_prefers_rare_classes():
    crit = NNSKDLoss(6, label_smoothing=0.0)
    counts = [1000, 10, 1000, 1000, 1000, 1000, 1000]  # class 1 rare
    z = torch.zeros(1, 7)
    y_rare = torch.tensor([1])
    base = crit(z, y_rare).item()
    crit.set_priors(counts, tau=1.0)
    adjusted = crit(z, y_rare).item()
    assert adjusted > base  # rare-class logit gets penalised during training -> larger loss -> stronger gradient


def test_ema_kd_term_and_ramp():
    crit = NNSKDLoss(6, ema_lambda=1.0, ramp_epochs=5, label_smoothing=0.0)
    z = torch.randn(4, 7)
    y = torch.tensor([0, 1, 2, 3])
    ema_logits = torch.randn(4, 7)
    crit.set_epoch(5)
    crit(z, y, ema_logits=ema_logits)
    assert "ema_kd" in crit.last and crit.last["ema_kd"] >= 0
    crit2 = NNSKDLoss(6, ema_lambda=0.0)
    crit2(z, y, ema_logits=ema_logits)
    assert "ema_kd" not in crit2.last


def test_model_ema_moves_toward_student():
    m = torch.nn.Linear(4, 2)
    ema = ModelEMA(m, momentum=0.5)
    with torch.no_grad():
        m.weight.add_(1.0)
    before = ema.module.weight.clone()
    ema.update(m)
    after = ema.module.weight
    assert torch.allclose(after, before + 0.5 * (m.weight - before), atol=1e-6)
    assert not any(p.requires_grad for p in ema.module.parameters())


def test_born_again_teacher_ckpt(tmp_path):
    from nnfer.train import main
    rng = np.random.default_rng(0)
    imgs = [rng.integers(0, 255, (112, 112, 3), dtype=np.uint8) for _ in range(16)]
    mf = pd.DataFrame({"path": [f"p{i}" for i in range(16)], "label": [i % 7 for i in range(16)],
                       "split": ["train"] * 8 + ["val"] * 4 + ["test"] * 4})
    write_cache(imgs, mf, tmp_path / "cache" / "rafdb", "rafdb")
    common = ["--dataset", "rafdb", "--seed", "1", "--epochs", "1", "--batch", "4", "--workers", "0",
              "--no-amp", "--no-pretrained", "--cache", str(tmp_path / "cache")]
    gen0 = main(["--model", "shufflenetv2", "--runs", str(tmp_path / "g0")] + common)
    gen1 = main(["--model", "shufflenetv2", "--runs", str(tmp_path / "g1"), "--teacher-ckpt",
                 str(gen0 / "best.pt"), "--teacher-model", "shufflenetv2", "--ema-kd", "1.0"] + common)
    assert (gen1 / "metrics.json").exists()
    import json
    assert json.loads((gen1 / "config.json").read_text())["ema_m_effective"] == 1.0


def test_train_with_v2_flags(tmp_path):
    from nnfer.train import main
    rng = np.random.default_rng(0)
    imgs = [rng.integers(0, 255, (112, 112, 3), dtype=np.uint8) for _ in range(16)]
    mf = pd.DataFrame({"path": [f"p{i}" for i in range(16)], "label": [i % 7 for i in range(16)],
                       "split": ["train"] * 8 + ["val"] * 4 + ["test"] * 4})
    write_cache(imgs, mf, tmp_path / "cache" / "rafdb", "rafdb")
    out = main(["--model", "nnskd_shufflenetv2", "--dataset", "rafdb", "--seed", "1", "--epochs", "1",
                "--batch", "4", "--workers", "0", "--no-amp", "--no-pretrained",
                "--mixup-alpha", "0.2", "--cutmix-alpha", "1.0", "--logit-adj", "1.0", "--ema-kd", "1.0",
                "--cache", str(tmp_path / "cache"), "--runs", str(tmp_path / "runs")])
    assert (out / "metrics.json").exists()
