"""Mixup / CutMix (training-recipe component of NN-SKD v2). Deterministic under torch seeding."""
import torch


class MixupCutmix:
    """Returns (x_mixed, y_a, y_b, lam). With probability 1-p the batch passes through unchanged."""

    def __init__(self, mixup_alpha: float = 0.2, cutmix_alpha: float = 1.0, p: float = 0.5,
                 switch_p: float = 0.5):
        self.mixup_alpha, self.cutmix_alpha = mixup_alpha, cutmix_alpha
        self.p, self.switch_p = p, switch_p

    def __call__(self, x: torch.Tensor, y: torch.Tensor):
        if torch.rand(()).item() >= self.p:
            return x, y, y, 1.0
        use_cutmix = self.cutmix_alpha > 0 and (self.mixup_alpha <= 0 or torch.rand(()).item() < self.switch_p)
        alpha = self.cutmix_alpha if use_cutmix else self.mixup_alpha
        lam = float(torch.distributions.Beta(alpha, alpha).sample())
        perm = torch.randperm(x.size(0), device=x.device)
        if use_cutmix:
            H, W = x.shape[-2:]
            rh, rw = int(H * (1 - lam) ** 0.5), int(W * (1 - lam) ** 0.5)
            cy = int(torch.randint(0, H, ()).item())
            cx = int(torch.randint(0, W, ()).item())
            y1, y2_ = max(cy - rh // 2, 0), min(cy + rh // 2, H)
            x1, x2_ = max(cx - rw // 2, 0), min(cx + rw // 2, W)
            x = x.clone()
            x[:, :, y1:y2_, x1:x2_] = x[perm][:, :, y1:y2_, x1:x2_]
            lam = 1.0 - (y2_ - y1) * (x2_ - x1) / (H * W)
        else:
            x = lam * x + (1.0 - lam) * x[perm]
        return x, y, y[perm], lam
