"""EfficientFace (Zhao, Liu, Wang — AAAI 2021), PyTorch re-implementation.

Official (github.com/zengqunzhao/EfficientFace, models/EfficientFace.py): a ShuffleNet-V2-1.0×
trunk in which the stage-2 output (116 ch, stride 8) is passed through
    x = Modulator(x) + LocalFeatureExtractor(x)
before stage 3. LFE splits the map into 4 spatial quadrants, each processed by its own
depthwise 3×3 conv stack; the Modulator is a channel (SE) + spatial (CBAM-like) attention.
Deviations under the shared protocol (spec §7): torchvision's ShuffleNetV2 (24-ch stem) with
ImageNet weights instead of the authors' 29-ch stem pre-trained on MS-Celeb-1M; plain CE loss
instead of the label-distribution (LDG) loss.
"""
import torch
from torch import nn
from torchvision.models import ShuffleNet_V2_X1_0_Weights, shufflenet_v2_x1_0

from nnfer.models import register


def _dw_block(ch: int) -> nn.Sequential:
    return nn.Sequential(
        nn.Conv2d(ch, ch, 3, 1, 1, groups=ch, bias=False), nn.BatchNorm2d(ch), nn.ReLU(inplace=True),
        nn.Conv2d(ch, ch, 3, 1, 1, groups=ch, bias=False), nn.BatchNorm2d(ch), nn.ReLU(inplace=True),
    )


class LocalFeatureExtractor(nn.Module):
    """Four independent depthwise conv stacks, one per spatial quadrant."""

    def __init__(self, ch: int):
        super().__init__()
        self.branches = nn.ModuleList([_dw_block(ch) for _ in range(4)])

    def forward(self, x):
        h, w = x.shape[-2:]
        h2, w2 = h // 2, w // 2
        q = [x[..., :h2, :w2], x[..., :h2, w2:], x[..., h2:, :w2], x[..., h2:, w2:]]
        o = [b(t) for b, t in zip(self.branches, q)]
        top = torch.cat([o[0], o[1]], dim=-1)
        bot = torch.cat([o[2], o[3]], dim=-1)
        return torch.cat([top, bot], dim=-2)


class ChannelAttention(nn.Module):
    def __init__(self, ch: int, reduction: int = 16):
        super().__init__()
        self.mlp = nn.Sequential(nn.Linear(ch, ch // reduction), nn.ReLU(inplace=True), nn.Linear(ch // reduction, ch))

    def forward(self, x):
        avg = self.mlp(x.mean((2, 3)))
        mx = self.mlp(x.amax((2, 3)))
        return x * torch.sigmoid(avg + mx)[:, :, None, None]


class SpatialAttention(nn.Module):
    def __init__(self, k: int = 7):
        super().__init__()
        self.conv = nn.Conv2d(2, 1, k, padding=k // 2, bias=False)

    def forward(self, x):
        s = torch.cat([x.mean(1, keepdim=True), x.amax(1, keepdim=True)], dim=1)
        return x * torch.sigmoid(self.conv(s))


class Modulator(nn.Module):
    def __init__(self, ch: int):
        super().__init__()
        self.ca = ChannelAttention(ch)
        self.sa = SpatialAttention()

    def forward(self, x):
        return self.sa(self.ca(x))


class EfficientFace(nn.Module):
    def __init__(self, num_classes: int, pretrained: bool = True, dropout: float = 0.0):
        super().__init__()
        base = shufflenet_v2_x1_0(weights=ShuffleNet_V2_X1_0_Weights.IMAGENET1K_V1 if pretrained else None)
        self.conv1, self.maxpool = base.conv1, base.maxpool
        self.stage2, self.stage3, self.stage4, self.conv5 = base.stage2, base.stage3, base.stage4, base.conv5
        ch = 116
        self.local = LocalFeatureExtractor(ch)
        self.modulator = Modulator(ch)
        self.drop = nn.Dropout(dropout)
        self.fc = nn.Linear(1024, num_classes)

    def forward(self, x):
        x = self.maxpool(self.conv1(x))
        x = self.stage2(x)
        x = self.modulator(x) + self.local(x)
        x = self.stage3(x)
        x = self.stage4(x)
        x = self.conv5(x)
        x = x.mean((2, 3))
        return self.fc(self.drop(x))


@register("efficientface")
def efficientface(num_classes: int, pretrained: bool = True) -> nn.Module:
    return EfficientFace(num_classes, pretrained)
