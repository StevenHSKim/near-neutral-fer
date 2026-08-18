"""Composite NN-SKD training loss (spec §8).

L = CE(z_T) + CE(z_S) + α_aux·Σ CE(z_i)
    + r(ep)·[ λ_kd · Σ_i w · T²·KL(softmax(sg z_T / T) ‖ softmax(z_i / T))      (i ∈ {S, aux…})
            + λ_f  · Σ_j ‖A_j − sg A_T‖²  ]                                    (attention KD)
    + λ_nm · mean_{y≠neutral} relu(m − (z_S[y] − z_S[neutral]))                 (neutral margin)
r(ep) = min(1, ep / ramp_epochs) is set by `set_epoch`. `w` up-weights samples the teacher finds
near-neutral (1 + p_T(neutral) for non-neutral samples) when `nn_weighting` is on.
Works for plain-logit models too (falls back to CE).
"""
import torch
import torch.nn.functional as F
from torch import nn


class NNSKDLoss(nn.Module):
    def __init__(self, neutral_index: int, label_smoothing: float = 0.1, alpha_aux: float = 0.5,
                 kd_lambda: float = 1.0, temperature: float = 4.0, feat_lambda: float = 1.0,
                 nm_lambda: float = 0.0, margin: float = 1.0, ramp_epochs: int = 5, nn_weighting: bool = False):
        super().__init__()
        self.neutral = neutral_index
        self.ce = nn.CrossEntropyLoss(label_smoothing=label_smoothing)
        self.alpha_aux, self.kd_lambda, self.T = alpha_aux, kd_lambda, temperature
        self.feat_lambda, self.nm_lambda, self.margin = feat_lambda, nm_lambda, margin
        self.ramp_epochs, self.nn_weighting = ramp_epochs, nn_weighting
        self.ramp = 1.0
        self.last = {}

    def set_epoch(self, epoch: int) -> None:  # epoch is 1-based
        self.ramp = 1.0 if self.ramp_epochs <= 0 else min(1.0, epoch / self.ramp_epochs)

    def kd(self, z_s, z_t, w=None):
        log_p = F.log_softmax(z_s / self.T, dim=1)
        q = F.softmax(z_t.detach() / self.T, dim=1)
        kl = F.kl_div(log_p, q, reduction="none").sum(1) * self.T ** 2
        if w is not None:
            kl = kl * w
        return kl.mean()

    def forward(self, out, y):
        if not isinstance(out, dict):
            return self.ce(out, y)
        z_s = out["logits"]
        parts = {"ce_s": self.ce(z_s, y)}
        aux = out.get("aux_logits", [])
        if aux:
            parts["ce_aux"] = self.alpha_aux * sum(self.ce(z, y) for z in aux)
        if "teacher_logits" in out:
            z_t = out["teacher_logits"]
            parts["ce_t"] = self.ce(z_t, y)
            w = None
            if self.nn_weighting:
                p_neu = F.softmax(z_t.detach(), 1)[:, self.neutral]
                w = 1.0 + p_neu * (y != self.neutral).float()
            if self.kd_lambda > 0:
                parts["kd"] = self.ramp * self.kd_lambda * (self.kd(z_s, z_t, w) + sum(self.kd(z, z_t, w) for z in aux))
            if self.feat_lambda > 0 and out.get("student_atts"):
                a_t = out["teacher_att"].detach()
                parts["feat"] = self.ramp * self.feat_lambda * sum((a - a_t).pow(2).sum(1).mean() for a in out["student_atts"])
        if self.nm_lambda > 0:
            non = y != self.neutral
            if non.any():
                zs = z_s[non]
                gap = zs.gather(1, y[non, None]).squeeze(1) - zs[:, self.neutral]
                parts["nm"] = self.nm_lambda * F.relu(self.margin - gap).mean()
        self.last = {k: float(v.detach()) for k, v in parts.items()}
        return sum(parts.values())
