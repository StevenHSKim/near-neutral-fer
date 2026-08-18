"""Training / evaluation loops shared by every model (spec §4 protocol)."""
import math

import numpy as np
import torch
from torch import nn


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


def train_one_epoch(model, loader, optimizer, scheduler, scaler, device, criterion, max_steps=None):
    model.train()
    tot_loss, tot_correct, n = 0.0, 0, 0
    for step, (x, y) in enumerate(loader):
        if max_steps is not None and step >= max_steps:
            break
        x, y = x.to(device, non_blocking=True), y.to(device, non_blocking=True)
        optimizer.zero_grad(set_to_none=True)
        with torch.autocast(device_type=device.type, dtype=torch.float16, enabled=scaler.is_enabled()):
            out = model(x)
            loss = criterion(out, y) if isinstance(out, dict) else criterion(_logits(out), y)
        scaler.scale(loss).backward()
        scaler.unscale_(optimizer)
        nn.utils.clip_grad_norm_(model.parameters(), 5.0)
        scaler.step(optimizer)
        scaler.update()
        scheduler.step()
        with torch.no_grad():
            tot_loss += loss.item() * len(y)
            tot_correct += (_logits(out).argmax(1) == y).sum().item()
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
