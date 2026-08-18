"""Params / FLOPs accounting (spec §5 efficiency metrics)."""
import torch
from torch.utils.flop_counter import FlopCounterMode


def count_params(model: torch.nn.Module, trainable_only: bool = False) -> int:
    return sum(p.numel() for p in model.parameters() if (p.requires_grad or not trainable_only))


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
