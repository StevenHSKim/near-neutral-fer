import numpy as np
import pandas as pd
import pytest
import torch

from nnfer.complexity import count_all_params, count_flops, count_params
from nnfer.data.cache import write_cache
from nnfer.losses import NNSKDLoss
from nnfer.models import build_model
from nnfer.models.backbones import get_backbone
from nnfer.seed import seed_everything


@pytest.mark.parametrize("name", ["shufflenetv2", "efficientface", "mobilenetv3s", "mobilenetv1"])
def test_backbone_stages_strides(name):
    bb, ch = get_backbone(name, pretrained=False)
    with torch.no_grad():
        f = bb.eval()(torch.randn(1, 3, 112, 112))
    assert [t.shape[1] for t in f] == ch
    assert [t.shape[-1] for t in f] == [14, 7, 4]


def test_nnskd_train_dict_and_eval_logits():
    m = build_model("nnskd_shufflenetv2", 7, pretrained=False)
    x = torch.randn(2, 3, 112, 112)
    out = m.train()(x)
    assert set(out) == {"logits", "aux_logits", "teacher_logits", "teacher_att", "student_atts"}
    assert out["logits"].shape == out["teacher_logits"].shape == (2, 7)
    assert len(out["aux_logits"]) == 2 and len(out["student_atts"]) == 2
    assert out["teacher_att"].shape == (2, 49) and out["student_atts"][0].shape == (2, 49)
    with torch.no_grad():
        y = m.eval()(x)
    assert y.shape == (2, 7)


def test_inference_cost_equals_plain_backbone():
    full = build_model("nnskd_shufflenetv2", 7, pretrained=False)
    plain = build_model("shufflenetv2", 7, pretrained=False)
    assert count_params(full) == count_params(plain) == count_all_params(plain)
    assert count_all_params(full) > count_params(full)
    assert count_flops(full) == count_flops(plain)


def test_export_student_matches_eval_and_teacher_head():
    m = build_model("nnskd_efficientface", 7, pretrained=False).eval()
    x = torch.randn(2, 3, 112, 112)
    with torch.no_grad():
        a = m(x)
        b = m.export_student().eval()(x)
        m.infer_head = "teacher"
        c = m(x)
    assert torch.allclose(a, b, atol=1e-6) and c.shape == (2, 7) and not torch.allclose(a, c)


def test_loss_components_and_ramp():
    torch.manual_seed(0)
    C, B = 7, 8
    y = torch.tensor([6, 6, 4, 1, 2, 5, 3, 0])
    out = {"logits": torch.randn(B, C), "aux_logits": [torch.randn(B, C), torch.randn(B, C)],
           "teacher_logits": torch.randn(B, C), "teacher_att": torch.softmax(torch.randn(B, 49), 1),
           "student_atts": [torch.softmax(torch.randn(B, 49), 1)]}
    crit = NNSKDLoss(neutral_index=6, kd_lambda=1.0, feat_lambda=1.0, nm_lambda=1.0, ramp_epochs=5)
    crit.set_epoch(1)
    l1 = crit(out, y); p1 = dict(crit.last)
    crit.set_epoch(5)
    l5 = crit(out, y); p5 = dict(crit.last)
    assert set(p1) == {"ce_s", "ce_aux", "ce_t", "kd", "feat", "nm"}
    assert p5["kd"] == pytest.approx(5 * p1["kd"]) and p5["feat"] == pytest.approx(5 * p1["feat"])
    assert p1["kd"] >= 0 and p1["feat"] >= 0 and l5 > l1
    off = NNSKDLoss(6, kd_lambda=0, feat_lambda=0, nm_lambda=0)
    off(out, y)
    assert set(off.last) == {"ce_s", "ce_aux", "ce_t"}
    # neutral margin is zero when every non-neutral sample already beats neutral by >= margin
    z = torch.zeros(B, C); z[torch.arange(B), y] = 5.0
    nm = NNSKDLoss(6, kd_lambda=0, feat_lambda=0, nm_lambda=1.0, margin=1.0)
    nm({"logits": z}, y)
    assert nm.last["nm"] == pytest.approx(0.0)
    # plain-logit models fall back to CE
    assert crit(torch.randn(B, C), y).ndim == 0


def test_toy_fit_reduces_loss():
    seed_everything(0)
    m = build_model("nnskd_mobilenetv3s", 7, pretrained=False).train()
    crit = NNSKDLoss(6, ramp_epochs=0)
    opt = torch.optim.AdamW(m.parameters(), 1e-3)
    x = torch.randn(8, 3, 112, 112)
    y = torch.arange(8) % 7
    losses = []
    for _ in range(15):
        opt.zero_grad()
        loss = crit(m(x), y)
        loss.backward()
        opt.step()
        losses.append(loss.item())
    assert losses[-1] < losses[0]


def test_ablation_a_equals_plain_backbone(tmp_path):
    """--model nnskd_shufflenetv2 --no-teacher --no-aux-heads must reproduce the `shufflenetv2` run bit-for-bit."""
    from nnfer.train import main
    rng = np.random.default_rng(0)
    imgs = [rng.integers(0, 255, (112, 112, 3), dtype=np.uint8) for _ in range(16)]
    mf = pd.DataFrame({"path": [f"p{i}" for i in range(16)], "label": [i % 7 for i in range(16)],
                       "split": ["train"] * 8 + ["val"] * 4 + ["test"] * 4})
    write_cache(imgs, mf, tmp_path / "cache" / "rafdb", "rafdb")
    common = ["--dataset", "rafdb", "--seed", "1", "--epochs", "1", "--batch", "4", "--workers", "0", "--no-amp",
              "--no-pretrained", "--cache", str(tmp_path / "cache")]
    a = main(["--model", "shufflenetv2", "--runs", str(tmp_path / "r1")] + common)
    b = main(["--model", "nnskd_shufflenetv2", "--no-teacher", "--no-aux-heads", "--runs", str(tmp_path / "r2")] + common)
    la, lb = np.load(a / "preds.npz")["test_logits"], np.load(b / "preds.npz")["test_logits"]
    assert np.allclose(la, lb, atol=1e-5)
