"""Model registry: name -> builder(num_classes, pretrained) -> nn.Module returning logits."""
from typing import Callable

from torch import nn

from nnfer.models.microexpnet import microexpnet
from nnfer.models.timm_backbones import mobilevit_xxs, resnet18_ref

MODEL_REGISTRY: dict[str, Callable[[int, bool], nn.Module]] = {
    "microexpnet": microexpnet,
    "mobilevit_xxs": mobilevit_xxs,
    "resnet18": resnet18_ref,
}


def register(name: str):
    def deco(fn):
        MODEL_REGISTRY[name] = fn
        return fn
    return deco


def list_models() -> list[str]:
    return sorted(MODEL_REGISTRY)


def build_model(name: str, num_classes: int, pretrained: bool = True) -> nn.Module:
    if name not in MODEL_REGISTRY:
        raise KeyError(f"unknown model {name!r}; available: {list_models()}")
    return MODEL_REGISTRY[name](num_classes, pretrained)


# Counterparts registered on import (they use @register).
from nnfer.models import efficientface as _ef  # noqa: E402,F401
from nnfer.models import pattlite as _pl  # noqa: E402,F401
