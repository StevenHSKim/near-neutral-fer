"""Generic lightweight backbones (MobileViT-XXS counterpart, ResNet-18 upper-bound reference)."""
import timm
import torch
from torch import nn
from torchvision.models import ResNet18_Weights, resnet18


def mobilevit_xxs(num_classes: int, pretrained: bool = True) -> nn.Module:
    """Mehta & Rastegari, ICLR 2022 — timm `mobilevit_xxs` (1.3 M params), ImageNet-1k weights."""
    return timm.create_model("mobilevit_xxs", pretrained=pretrained, num_classes=num_classes)


def resnet18_ref(num_classes: int, pretrained: bool = True) -> nn.Module:
    m = resnet18(weights=ResNet18_Weights.IMAGENET1K_V1 if pretrained else None)
    m.fc = nn.Linear(m.fc.in_features, num_classes)
    return m
