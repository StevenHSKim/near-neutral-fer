import random

import numpy as np
import torch

from nnfer.seed import seed_everything, worker_init_fn


def test_seed_everything_reproduces_streams():
    seed_everything(3)
    a = (random.random(), np.random.rand(), torch.rand(2).tolist())
    seed_everything(3)
    b = (random.random(), np.random.rand(), torch.rand(2).tolist())
    assert a == b


def test_generator_seeded():
    g1 = seed_everything(5)
    g2 = seed_everything(5)
    assert torch.randperm(10, generator=g1).tolist() == torch.randperm(10, generator=g2).tolist()


def test_worker_init_fn_runs():
    seed_everything(0)
    worker_init_fn(0)
    assert torch.backends.cudnn.deterministic is True
