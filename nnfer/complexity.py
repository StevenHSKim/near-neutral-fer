"""Params / FLOPs accounting (spec §5 efficiency metrics)."""
import torch
from torch.utils.flop_counter import FlopCounterMode


def count_params(model: torch.nn.Module, trainable_only: bool = False) -> int:
    """Inference-time parameter count (models with training-only branches expose `inference_parameters`)."""
    params = model.inference_parameters() if hasattr(model, "inference_parameters") else model.parameters()
    return sum(p.numel() for p in params if (p.requires_grad or not trainable_only))


def count_all_params(model: torch.nn.Module) -> int:
    return sum(p.numel() for p in model.parameters())


@torch.no_grad()
def count_flops(model: torch.nn.Module, size: int = 112, device: str = "cpu") -> int:
    """Forward FLOPs (multiply-adds counted as 2) for one 3×size×size image in eval mode."""
    was_training = model.training
    model.eval().to(device)
    x = torch.zeros(1, 3, size, size, device=device)
    fc = FlopCounterMode(display=False)
    with fc:
        model(x)
    if was_training:
        model.train()
    return int(fc.get_total_flops())


if __name__ == "__main__":  # python -m nnfer.complexity [names...]
    import sys

    from nnfer.models import build_model, list_models

    names = sys.argv[1:] or list_models()
    print(f"{'model':20s} {'params(M)':>10s} {'FLOPs(M)':>10s}")
    for n in names:
        m = build_model(n, 7, pretrained=False)
        print(f"{n:20s} {count_params(m) / 1e6:10.3f} {count_flops(m) / 1e6:10.1f}")
