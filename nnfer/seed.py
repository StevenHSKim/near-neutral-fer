"""Reproducibility helpers (spec §4): fixed seeds + deterministic backends."""
import os
import random

import numpy as np
import torch


def seed_everything(seed: int) -> torch.Generator:
    """Seed python/numpy/torch(+cuda), force deterministic kernels; return a seeded generator."""
    os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    torch.use_deterministic_algorithms(True, warn_only=True)
    g = torch.Generator()
    g.manual_seed(seed)
    return g


def worker_init_fn(worker_id: int) -> None:
    """DataLoader worker seeding derived from the torch base seed."""
    s = (torch.initial_seed() + worker_id) % 2**32
    np.random.seed(s)
    random.seed(s)
