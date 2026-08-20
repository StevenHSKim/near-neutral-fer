"""Composite NN-SKD training loss (spec §8, extended for v2).

L = CE(z_T) + CE(z_S) + α_aux·Σ CE(z_i)                                        (mixup-aware CE)
    + r(ep)·[ λ_kd  · Σ_i T²·KL(softmax(sg z_T / T) ‖ softmax(z_i / T))         (spatial self-KD)
            + λ_ema · T²·KL(softmax(sg z_EMA / T) ‖ softmax(z_S / T))           (temporal self-KD, v2)
            + λ_f   · Σ_j ‖A_j − sg A_T‖² ]                                     (attention KD)
    + λ_nm · mean_{y≠neutral} relu(m − (z_S[y] − z_S[neutral]))                 (neutral margin)

Mixup/CutMix: every CE is lam·CE(z, y_a) + (1−lam)·CE(z, y_b); KD terms are label-free so they are
unchanged. Logit adjustment (v2): during training, τ·log(prior) is added to logits inside every CE
(Menon et al., 2021); evaluation always uses raw logits. r(ep) = min(1, ep / ramp_epochs).
Plain-logit models are handled by the same interface (CE + optional EMA-KD / margin terms).
"""
import numpy as np
import torch
import torch.nn.functional as F
from torch import nn


class NNSKDLoss(nn.Module):
    def __init__(self, neutral_index: int, label_smoothing: float = 0.1, alpha_aux: float = 0.5,
                 kd_lambda: float = 1.0, temperature: float = 4.0, feat_lambda: float = 1.0,
                 nm_lambda: float = 0.0, margin: float = 1.0, ramp_epochs: int = 5,
                 nn_weighting: bool = False, ema_lambda: float = 0.0):
        super().__init__()
        self.neutral = neutral_index
        self.ce = nn.CrossEntropyLoss(label_smoothing=label_smoothing)
        self.alpha_aux, self.kd_lambda, self.T = alpha_aux, kd_lambda, temperature
        self.feat_lambda, self.nm_lambda, self.margin = feat_lambda, nm_lambda, margin
        self.ramp_epochs, self.nn_weighting, self.ema_lambda = ramp_epochs, nn_weighting, ema_lambda
        self.ramp = 1.0
        self.la_tau = 0.0
        self.register_buffer("log_prior", torch.zeros(1), persistent=False)
        self.last = {}

    def set_epoch(self, epoch: int) -> None:  # epoch is 1-based
        self.ramp = 1.0 if self.ramp_epochs <= 0 else min(1.0, epoch / self.ramp_epochs)

    def set_priors(self, class_counts, tau: float) -> None:
        """Enable logit adjustment: counts -> log prior; tau=0 disables."""
        p = np.asarray(class_counts, dtype=np.float64)
        p = p / p.sum()
        self.log_prior = torch.log(torch.as_tensor(p, dtype=torch.float32).clamp_min(1e-12))
        self.la_tau = float(tau)

    def _adj(self, z):
        if self.la_tau <= 0:
            return z
        return z + self.la_tau * self.log_prior.to(z.device)

    def _ce(self, z, y, y2, lam):
        z = self._adj(z)
        if y2 is None or lam >= 1.0:
            return self.ce(z, y)
        return lam * self.ce(z, y) + (1.0 - lam) * self.ce(z, y2)

    def kd(self, z_s, z_t, w=None):
        log_p = F.log_softmax(z_s / self.T, dim=1)
        q = F.softmax(z_t.detach() / self.T, dim=1)
        kl = F.kl_div(log_p, q, reduction="none").sum(1) * self.T ** 2
        if w is not None:
            kl = kl * w
        return kl.mean()

    def forward(self, out, y, y2=None, lam=1.0, ema_logits=None):
        plain = not isinstance(out, dict)
        z_s = out if plain else out["logits"]
        parts = {"ce_s": self._ce(z_s, y, y2, lam)}
        aux = [] if plain else out.get("aux_logits", [])
        if aux:
            parts["ce_aux"] = self.alpha_aux * sum(self._ce(z, y, y2, lam) for z in aux)
        if not plain and "teacher_logits" in out:
            z_t = out["teacher_logits"]
            parts["ce_t"] = self._ce(z_t, y, y2, lam)
            w = None
            if self.nn_weighting:
                p_neu = F.softmax(z_t.detach(), 1)[:, self.neutral]
                w = 1.0 + p_neu * (y != self.neutral).float()
            if self.kd_lambda > 0:
                parts["kd"] = self.ramp * self.kd_lambda * (self.kd(z_s, z_t, w) + sum(self.kd(z, z_t, w) for z in aux))
            if self.feat_lambda > 0 and out.get("student_atts"):
                a_t = out["teacher_att"].detach()
                parts["feat"] = self.ramp * self.feat_lambda * sum((a - a_t).pow(2).sum(1).mean() for a in out["student_atts"])
        if self.ema_lambda > 0 and ema_logits is not None:
            parts["ema_kd"] = self.ramp * self.ema_lambda * self.kd(z_s, ema_logits)
        if self.nm_lambda > 0 and lam >= 1.0:
            non = y != self.neutral
            if non.any():
                zs = z_s[non]
                gap = zs.gather(1, y[non, None]).squeeze(1) - zs[:, self.neutral]
                parts["nm"] = self.nm_lambda * F.relu(self.margin - gap).mean()
        self.last = {k: float(v.detach()) for k, v in parts.items()}
        return sum(parts.values())
