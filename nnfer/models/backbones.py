"""Multi-stage feature backbones for NN-SKD: forward(x) -> [S2, S3, S4] at strides 8 / 16 / 32.

`get_backbone(name, pretrained) -> (nn.Module, channels)` where `channels` = [c2, c3, c4].
"""
import timm
import torch
from torch import nn
from torchvision.models import ShuffleNet_V2_X1_0_Weights, shufflenet_v2_x1_0

from nnfer.models.efficientface import EfficientFace


class ShuffleNetV2Stages(nn.Module):
    """torchvision ShuffleNetV2-1.0×: S2 = stage2 (116), S3 = stage3 (232), S4 = conv5(stage4) (1024)."""

    channels = [116, 232, 1024]

    def __init__(self, pretrained: bool):
        super().__init__()
        b = shufflenet_v2_x1_0(weights=ShuffleNet_V2_X1_0_Weights.IMAGENET1K_V1 if pretrained else None)
        self.conv1, self.maxpool = b.conv1, b.maxpool
        self.stage2, self.stage3, self.stage4, self.conv5 = b.stage2, b.stage3, b.stage4, b.conv5

    def forward(self, x):
        x = self.maxpool(self.conv1(x))
        s2 = self.stage2(x)
        s3 = self.stage3(s2)
        s4 = self.conv5(self.stage4(s3))
        return [s2, s3, s4]


class EfficientFaceStages(nn.Module):
    """EfficientFace trunk (ShuffleNetV2 + LFE + modulator after stage2) — same inference arch as the counterpart."""

    channels = [116, 232, 1024]

    def __init__(self, pretrained: bool):
        super().__init__()
        self.net = EfficientFace(num_classes=1, pretrained=pretrained)  # fc unused
        del self.net.fc

    def forward(self, x):
        n = self.net
        x = n.maxpool(n.conv1(x))
        x = n.stage2(x)
        s2 = n.modulator(x) + n.local(x)
        s3 = n.stage3(s2)
        s4 = n.conv5(n.stage4(s3))
        return [s2, s3, s4]


class TimmStages(nn.Module):
    """Any timm model with features_only support; picks the stride-8/16/32 feature maps."""

    def __init__(self, timm_name: str, pretrained: bool):
        super().__init__()
        m = timm.create_model(timm_name, pretrained=pretrained, features_only=True)
        red = m.feature_info.reduction()
        idx = [red.index(r) for r in (8, 16, 32)]
        self.m = timm.create_model(timm_name, pretrained=pretrained, features_only=True, out_indices=tuple(idx))
        self.channels = list(self.m.feature_info.channels())

    def forward(self, x):
        return list(self.m(x))


BACKBONES = {
    "shufflenetv2": lambda p: ShuffleNetV2Stages(p),
    "efficientface": lambda p: EfficientFaceStages(p),
    "mobilenetv3s": lambda p: TimmStages("mobilenetv3_small_100", p),
    "mobilenetv1": lambda p: TimmStages("mobilenetv1_100", p),
}


def get_backbone(name: str, pretrained: bool = True):
    if name in BACKBONES:
        bb = BACKBONES[name](pretrained)
    else:  # any timm name
        bb = TimmStages(name, pretrained)
    return bb, list(bb.channels)
