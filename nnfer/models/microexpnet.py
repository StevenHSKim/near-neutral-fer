"""MicroExpNet (Cugu, Sener, Akbas — IPTA 2019), PyTorch port of the official TF model.

Official: 84×84 grayscale -> Conv(16, 8×8, s2, same)+ReLU -> MaxPool(2,2) -> Conv(32, 4×4, s2, same)+ReLU
-> MaxPool(2,2) -> FC(48)+ReLU -> Dropout -> FC(classes). (~65 K params at 84×84.)
Adaptation to the shared protocol: 112×112 RGB input converted to luma inside the model
(fixed, non-trainable weights), so the flattened feature is 32×7×7 = 1568 (~80 K params).
The paper's teacher-student distillation from Inception-v3 is NOT used; trained with the same
CE loss as every other model (lower-bound counterpart).
"""
import torch
from torch import nn


class MicroExpNet(nn.Module):
    def __init__(self, num_classes: int, in_size: int = 112, dropout: float = 0.5):
        super().__init__()
        self.register_buffer("luma", torch.tensor([0.299, 0.587, 0.114]).view(1, 3, 1, 1))
        self.features = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size=8, stride=2, padding=3), nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(16, 32, kernel_size=4, stride=2, padding=1), nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2),
        )
        with torch.no_grad():
            n_flat = self.features(torch.zeros(1, 1, in_size, in_size)).numel()
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(n_flat, 48), nn.ReLU(inplace=True),
            nn.Dropout(dropout),
            nn.Linear(48, num_classes),
        )
        for m in self.modules():
            if isinstance(m, (nn.Conv2d, nn.Linear)):
                nn.init.kaiming_normal_(m.weight, nonlinearity="relu")
                nn.init.zeros_(m.bias)

    def forward(self, x):
        x = (x * self.luma).sum(1, keepdim=True)
        return self.classifier(self.features(x))


def microexpnet(num_classes: int, pretrained: bool = False) -> nn.Module:
    return MicroExpNet(num_classes)
