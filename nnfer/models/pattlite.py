"""PAtt-Lite (Ngwe, Lim, Lee, Ong, Alqahtani — IEEE Access 2024), PyTorch re-implementation.

Official notebook (github.com/JLREx/PAtt-Lite): Keras MobileNetV1 (ImageNet) truncated at
`layers[-29]` = `conv_dw_9_relu` (stride 16, 512 ch, i.e. DS blocks 1–8 + the depthwise half of
block 9) -> patch extraction [SeparableConv2D(256, k4, s4, same, relu) -> SeparableConv2D(256, k2,
s2, valid, relu) -> Conv2D(256, k1, relu)] -> GAP -> Dropout(0.1) -> Dense(32, relu) -> BN ->
Attention([x, x]) -> Dense(classes).
Adaptations (spec §7):
  * 112×112 input gives a 7×7 stride-16 map, so the first separable conv uses stride 2 (7 -> 4)
    and the second k2/s2 (4 -> 2), preserving the 2×2 patch grid the paper has at 224×224.
  * Keras `Attention([x, x])` on the single pooled vector is the identity — the implementation
    error the authors acknowledged. `attention_over_patches=True` (default) implements the intended
    scaled dot-product self-attention over the 2×2 patch tokens before pooling;
    `attention_over_patches=False` reproduces the notebook's identity path.
  * Class weights and the two-stage freeze/fine-tune schedule are replaced by the shared protocol.
"""
import timm
import torch
from torch import nn

from nnfer.models import register


class SepConv(nn.Module):
    """Keras SeparableConv2D(+ReLU): depthwise k×k then pointwise 1×1."""

    def __init__(self, cin, cout, k, s, pad):
        super().__init__()
        self.dw = nn.Conv2d(cin, cin, k, s, pad, groups=cin)
        self.pw = nn.Conv2d(cin, cout, 1)

    def forward(self, x):
        return torch.relu(self.pw(self.dw(x)))


class MobileNetV1Trunk(nn.Module):
    """timm mobilenetv1_100 up to conv_dw_9 (+BN+ReLU); output 512 ch at stride 16."""

    def __init__(self, pretrained: bool):
        super().__init__()
        m = timm.create_model("mobilenetv1_100", pretrained=pretrained)
        self.stem = nn.Sequential(m.conv_stem, m.bn1)
        blocks = [b for stage in m.blocks for b in stage]  # 13 DS blocks in order
        self.blocks = nn.Sequential(*blocks[:8])           # DS blocks 1–8
        b9 = blocks[8]
        self.dw9 = nn.Sequential(b9.conv_dw, b9.bn1)       # depthwise half of block 9 (bn1 includes ReLU)

    def forward(self, x):
        return self.dw9(self.blocks(self.stem(x)))


class PAttLite(nn.Module):
    def __init__(self, num_classes: int, pretrained: bool = True, attention_over_patches: bool = True,
                 dropout: float = 0.1):
        super().__init__()
        self.trunk = MobileNetV1Trunk(pretrained)
        self.patch = nn.Sequential(
            SepConv(512, 256, k=4, s=2, pad=1),   # 7 -> 4  (paper: k4/s4 same on 14 -> 4)
            SepConv(256, 256, k=2, s=2, pad=0),   # 4 -> 2
            nn.Conv2d(256, 256, 1), nn.ReLU(inplace=True),
        )
        self.attention_over_patches = attention_over_patches
        self.drop = nn.Dropout(dropout)
        self.pre = nn.Sequential(nn.Linear(256, 32), nn.ReLU(inplace=True), nn.BatchNorm1d(32))
        self.fc = nn.Linear(32, num_classes)

    @staticmethod
    def _attend(tokens):  # Keras Attention(use_scale=True): softmax(q k^T * scale) v, q=k=v
        scale = tokens.shape[-1] ** -0.5
        att = torch.softmax(tokens @ tokens.transpose(1, 2) * scale, dim=-1)
        return att @ tokens

    def forward(self, x):
        x = self.patch(self.trunk(x))                       # B,256,2,2
        if self.attention_over_patches:
            t = x.flatten(2).transpose(1, 2)                # B,4,256
            x = self._attend(t).mean(1)                     # B,256
        else:
            x = x.mean((2, 3))                              # GAP; Attention([x,x]) == identity
        x = self.pre(self.drop(x))
        return self.fc(x)


@register("pattlite")
def pattlite(num_classes: int, pretrained: bool = True) -> nn.Module:
    return PAttLite(num_classes, pretrained, attention_over_patches=True)


@register("pattlite_identity")
def pattlite_identity(num_classes: int, pretrained: bool = True) -> nn.Module:
    """Reference variant reproducing the notebook's identity attention path."""
    return PAttLite(num_classes, pretrained, attention_over_patches=False)
