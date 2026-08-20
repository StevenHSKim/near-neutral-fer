"""Training / evaluation loops shared by every model (spec §4 protocol)."""
import copy
import math

import numpy as np
import torch
from torch import nn


class ModelEMA:
    """Exponential-moving-average copy of the student (temporal self-teacher, NN-SKD v2).

    The EMA module runs in eval mode, so for NNSKD models its forward returns the deployed
    student-path logits. Training-only: never saved as the final checkpoint.
    """

    def __init__(self, model: nn.Module, momentum: float = 0.999):
        self.module = copy.deepcopy(model).eval()
        for p in self.module.parameters():
            p.requires_grad_(False)
        self.m = momentum

    @torch.no_grad()
    def update(self, model: nn.Module) -> None:
        for e, p in zip(self.module.state_dict().values(), model.state_dict().values()):
            if e.dtype.is_floating_point:
                e.mul_(self.m).add_(p.detach().to(e.dtype), alpha=1.0 - self.m)
            else:
                e.copy_(p)


def build_scheduler(optimizer, epochs: int, steps_per_epoch: int, warmup_epochs: int):
    """Per-step LambdaLR: linear warm-up then cosine decay to 0."""
    total = max(1, epochs * steps_per_epoch)
    warm = warmup_epochs * steps_per_epoch

    def f(step):
        if step < warm:
            return (step + 1) / max(1, warm)
        p = (step - warm) / max(1, total - warm)
        return 0.5 * (1 + math.cos(math.pi * min(1.0, p)))

    return torch.optim.lr_scheduler.LambdaLR(optimizer, f)


def _logits(out):
    return out["logits"] if isinstance(out, dict) else out


def train_one_epoch(model, loader, optimizer, scheduler, scaler, device, criterion, max_steps=None,
                    mix_fn=None, ema: "ModelEMA | None" = None):
    """criterion must accept (out, y_a, y_b, lam, ema_logits) — see nnfer.losses.NNSKDLoss."""
    model.train()
    tot_loss, tot_correct, n = 0.0, 0, 0
    for step, (x, y) in enumerate(loader):
        if max_steps is not None and step >= max_steps:
            break
        x, y = x.to(device, non_blocking=True), y.to(device, non_blocking=True)
        ya, yb, lam = y, None, 1.0
        if mix_fn is not None:
            x, ya, yb, lam = mix_fn(x, y)
        optimizer.zero_grad(set_to_none=True)
        with torch.autocast(device_type=device.type, dtype=torch.float16, enabled=scaler.is_enabled()):
            out = model(x)
            ema_logits = None
            if ema is not None:
                with torch.no_grad():
                    ema_logits = _logits(ema.module(x))
            loss = criterion(out, ya, yb, lam, ema_logits)
        scaler.scale(loss).backward()
        scaler.unscale_(optimizer)
        nn.utils.clip_grad_norm_(model.parameters(), 5.0)
        scaler.step(optimizer)
        scaler.update()
        scheduler.step()
        if ema is not None:
            ema.update(model)
        with torch.no_grad():
            tot_loss += loss.item() * len(y)
            tot_correct += (_logits(out).argmax(1) == ya).sum().item()
            n += len(y)
    return {"loss": tot_loss / max(1, n), "acc": tot_correct / max(1, n)}


@torch.no_grad()
def evaluate(model, loader, device):
    """Return (logits [N,C] float32 numpy, labels [N] int64 numpy) in loader order."""
    model.eval()
    logits, labels = [], []
    for x, y in loader:
        out = _logits(model(x.to(device, non_blocking=True)))
        logits.append(out.float().cpu().numpy())
        labels.append(y.numpy())
    return np.concatenate(logits), np.concatenate(labels)
