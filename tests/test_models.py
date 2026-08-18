import pytest
import torch

from nnfer.complexity import count_flops, count_params
from nnfer.models import build_model, list_models

# expected parameter ranges (millions) at 7 classes, 112x112 input
RANGES = {
    "microexpnet": (0.06, 0.12),
    "mobilevit_xxs": (0.9, 1.4),
    "efficientface": (1.2, 1.5),
    "pattlite": (0.9, 1.5),
    "pattlite_identity": (0.9, 1.5),
    "resnet18": (11.0, 12.0),
}


def test_registry_lists_all_counterparts():
    assert set(RANGES) <= set(list_models())


@pytest.mark.parametrize("name", sorted(RANGES))
def test_forward_shape_and_params(name):
    m = build_model(name, num_classes=7, pretrained=False).eval()
    with torch.no_grad():
        y = m(torch.randn(2, 3, 112, 112))
    assert y.shape == (2, 7)
    lo, hi = RANGES[name]
    p = count_params(m) / 1e6
    assert lo <= p <= hi, f"{name}: {p:.3f} M params"
    assert count_flops(m) > 0


def test_pretrained_efficientface_loads_torchvision_stem():
    from torchvision.models import ShuffleNet_V2_X1_0_Weights, shufflenet_v2_x1_0
    ref = shufflenet_v2_x1_0(weights=ShuffleNet_V2_X1_0_Weights.IMAGENET1K_V1)
    m = build_model("efficientface", 7, pretrained=True)
    assert torch.equal(m.conv1[0].weight, ref.conv1[0].weight)


def test_pattlite_patch_grid_is_2x2():
    m = build_model("pattlite", 7, pretrained=False).eval()
    with torch.no_grad():
        f = m.patch(m.trunk(torch.randn(1, 3, 112, 112)))
    assert f.shape == (1, 256, 2, 2)
