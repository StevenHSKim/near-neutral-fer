# M3 — Training Engine & Counterpart Models Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** One deterministic train/eval engine plus PyTorch re-implementations of the four counterparts (EfficientFace, PAtt-Lite, MicroExpNet, MobileViT-XXS) and the ResNet-18 reference, verified by shape/param tests and a 1-seed RAF-DB smoke run each.

**Architecture:** `nnfer/models/` registry (`build_model(name, num_classes, pretrained) -> nn.Module` returning logits); `nnfer/metrics.py` computes every spec §5 metric from `(logits, labels, manifest)`; `nnfer/train.py` runs one `(model, dataset, seed)` config end-to-end and writes `runs/<dataset>/<model>/seed<k>/{config.json,history.csv,metrics.json,preds.npz,best.pt}`; `nnfer/complexity.py` reports Params/FLOPs via `torch.utils.flop_counter`. Everything is driven by CLI flags with spec §4 defaults so `python -m nnfer.train --model X --dataset Y --seed k` is the whole protocol.

**Tech Stack:** PyTorch 2.3.1, torchvision 0.18.1 (shufflenet_v2_x1_0, resnet18 weights), timm 1.0.9 (mobilenetv1_100, mobilevit_xxs weights), scikit-learn metrics.

## Global Constraints

- Protocol (spec §4): 112×112, ImageNet mean/std, train aug = RandomResizedCrop(0.8–1.0)+HFlip+RandomErasing(0.5), AdamW lr 1e-3 wd 5e-4, cosine with 5 warm-up epochs, batch 64, epochs 60 (rafdb) / 40 (ferplus), label smoothing 0.1, AMP, best-val-accuracy checkpoint evaluated once on test.
- Determinism: `seed_everything(seed)` seeds python/numpy/torch(+cuda); `cudnn.deterministic=True`, `benchmark=False`; `CUBLAS_WORKSPACE_CONFIG=:4096:8`; `torch.use_deterministic_algorithms(True, warn_only=True)`; DataLoader `generator` seeded and `worker_init_fn`.
- Every run json records: full config, git hash, `torch.__version__`, GPU name, params, FLOPs, wall-clock.
- Pretraining policy: ImageNet weights for shufflenet_v2_x1_0 (EfficientFace), mobilenetv1_100 (PAtt-Lite), mobilevit_xxs (MobileViT), resnet18 (reference); MicroExpNet from scratch. Uniform CE(label smoothing 0.1) for every model in M3 (EfficientFace's LDG loss and PAtt-Lite's two-stage schedule/class weights are NOT replicated — protocol uniformity; recorded as deviations in spec §7).
- Model forward returns logits `Tensor[B, C]` (dict outputs are for M5's Self-KD model only).
- Commit messages end with `Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>`.

---

### Task 1: Seed / determinism utilities + run I/O

**Files:** `nnfer/seed.py`, `nnfer/runio.py`, `tests/test_seed.py`

**Interfaces:**
- `seed_everything(seed: int) -> torch.Generator` (returns a seeded generator for DataLoader).
- `worker_init_fn(worker_id)` derives per-worker numpy/random seeds from `torch.initial_seed()`.
- `runio.run_dir(root, dataset, model, seed) -> Path` (`root/dataset/model/seed{seed}`), `runio.env_info() -> dict` (git hash, torch, cuda, gpu name), `runio.save_json(obj, path)`.

- [ ] Test:
```python
import torch, numpy as np, random
from nnfer.seed import seed_everything
def test_seed_everything_reproduces_streams():
    seed_everything(3); a = (random.random(), np.random.rand(), torch.rand(2).tolist())
    seed_everything(3); b = (random.random(), np.random.rand(), torch.rand(2).tolist())
    assert a == b
def test_generator_seeded():
    g1 = seed_everything(5); g2 = seed_everything(5)
    assert torch.randperm(10, generator=g1).tolist() == torch.randperm(10, generator=g2).tolist()
```
- [ ] Implement `nnfer/seed.py`:
```python
import os, random
import numpy as np, torch
def seed_everything(seed: int) -> torch.Generator:
    os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
    random.seed(seed); np.random.seed(seed); torch.manual_seed(seed); torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    torch.use_deterministic_algorithms(True, warn_only=True)
    g = torch.Generator(); g.manual_seed(seed)
    return g
def worker_init_fn(worker_id: int) -> None:
    s = (torch.initial_seed() + worker_id) % 2**32
    np.random.seed(s); random.seed(s)
```
`nnfer/runio.py`: `run_dir`, `env_info` (subprocess `git rev-parse HEAD`, fall back "unknown"), `save_json` (indent=2, default=str).
- [ ] Commit `feat: seed/determinism + run io`.

### Task 2: Metrics

**Files:** `nnfer/metrics.py`, `tests/test_metrics.py`

**Interfaces:**
- `compute_metrics(logits: np.ndarray[N,C], labels: np.ndarray[N], dataset: str, manifest: pd.DataFrame | None = None) -> dict` with keys:
  `acc, macro_f1, per_class_f1 (list), confusion (list of lists), fnr (false-neutral rate), neutral_recall, neutral_f1, near_neutral_macro_f1, ece, mean_entropy` and, when `manifest` has `neutral_share`: `nn_subset_acc@0.2/0.3/0.4`, `nn_subset_macro_f1@…`, `nn_subset_n@…`.
  For `dataset == "ckplus"` (RAF-DB label space, no neutral samples): fnr computed over all samples, neutral_recall/f1 = None, near_neutral_macro_f1 over the 4 classes present.
- `ece(probs, labels, n_bins=15) -> float`.

- [ ] Tests (hand-computable toy cases):
```python
def test_basic_metrics_rafdb():
    labels = np.array([6,6,4,4,3]); logits = one_hot([6,4,6,4,3])  # neutral: 1/2 recall; sad: 1/2; one non-neutral predicted neutral (out of 3)
    m = compute_metrics(logits, labels, "rafdb")
    assert m["acc"] == pytest.approx(3/5) and m["neutral_recall"] == pytest.approx(0.5)
    assert m["fnr"] == pytest.approx(1/3)
def test_ferplus_subset_from_manifest():
    manifest = pd.DataFrame({"neutral_share":[0.5,0.1,0.35], "label":[3,1,4]})
    m = compute_metrics(one_hot([3,1,0]), np.array([3,1,4]), "ferplus", manifest)
    assert m["nn_subset_n@0.3"] == 2 and m["nn_subset_acc@0.3"] == pytest.approx(0.5)
def test_ece_perfectly_calibrated_zero():
    probs = np.array([[1.0,0.0]]*10); assert ece(probs, np.zeros(10,int)) == pytest.approx(0.0)
```
- [ ] Implement with sklearn `accuracy_score, f1_score(average="macro"), confusion_matrix`; softmax via scipy; FNR = mean(pred==neutral | label!=neutral); near-neutral macro-F1 = `f1_score(labels, preds, labels=NEAR_NEUTRAL_CLASSES[ds], average="macro")` (for ckplus use rafdb's list). Subset metrics recomputed with `mask = (label != neutral) & (neutral_share >= tau)`.
- [ ] Commit `feat: metrics (standard, near-neutral, calibration)`.

### Task 3: Model registry + MobileViT-XXS + ResNet-18 + MicroExpNet

**Files:** `nnfer/models/__init__.py`, `nnfer/models/timm_backbones.py`, `nnfer/models/microexpnet.py`, `nnfer/complexity.py`, `tests/test_models.py`

**Interfaces:**
- `MODEL_REGISTRY: dict[str, Callable[[int, bool], nn.Module]]`; `build_model(name, num_classes, pretrained=True)`; `list_models()`.
- `complexity.count_params(model) -> int`, `complexity.count_flops(model, size=112) -> int` (FlopCounterMode, batch 1, eval).
- MobileViT-XXS: `timm.create_model("mobilevit_xxs", pretrained, num_classes)`. ResNet-18: torchvision `resnet18(weights=IMAGENET1K_V1)` with new fc.
- MicroExpNet (from official TF code, adapted to 112×112 RGB): fixed luma-to-gray conv (non-trainable) → Conv(16, 8×8, s2, same) ReLU → MaxPool2 → Conv(32, 4×4, s2, same) ReLU → MaxPool2 → flatten (32×7×7=1568) → FC 48 ReLU → Dropout(0.5) → FC C. Weight init: kaiming for convs/linear.

- [ ] Tests (parametrised over registry): output shape `[2, C]` for input `[2,3,112,112]` in eval; params within expected ranges: `mobilevit_xxs` 0.9–1.4 M, `resnet18` 11–12 M, `microexpnet` 60–120 K; `count_flops` > 0; a `pretrained=False` build works offline.
- [ ] Commit `feat(models): registry, MobileViT-XXS, ResNet-18 ref, MicroExpNet`.

### Task 4: EfficientFace (PyTorch, ShuffleNetV2-1.0× + LFE + modulator)

**Files:** `nnfer/models/efficientface.py`, extend `tests/test_models.py`

Faithful to github.com/zengqunzhao/EfficientFace `models/EfficientFace.py`: torchvision `shufflenet_v2_x1_0` (ImageNet weights) provides `conv1, maxpool, stage2, stage3, stage4, conv5`; after `stage2` (116 ch, stride 8) apply `x = modulator(x) + local(x)` where
- `LocalFeatureExtractor(116)`: split H,W into 4 quadrants, each through 2× (depthwise 3×3 conv → BN → ReLU) with its own weights, concatenated back;
- `Modulator(116)`: channel attention (SE, reduction 16) followed by spatial attention (7×7 conv on [avg,max] maps, sigmoid), applied multiplicatively.
Then stage3, stage4, conv5, global pool, dropout(0.2? official uses none) → fc.
Deviation: official stem uses 29 channels + MS-Celeb weights; we keep torchvision's 24-ch stem to load ImageNet weights.

- [ ] Test: params 1.2–1.5 M; output shape; ImageNet weight loading leaves `conv1.0.weight` equal to torchvision's.
- [ ] Commit `feat(models): EfficientFace re-implementation`.

### Task 5: PAtt-Lite (PyTorch, MobileNetV1 truncated + patch extraction + attention)

**Files:** `nnfer/models/pattlite.py`, extend `tests/test_models.py`

From the official notebook: MobileNetV1 (`timm mobilenetv1_100`, ImageNet) truncated at Keras `layers[-29]` = `conv_dw_9_relu` (stride 16, 512 ch: through DS block 8 plus the depthwise half of block 9); patch extraction = SepConv(256, k4, s4, same, ReLU) → SepConv(256, k2, s2, valid, ReLU) → Conv1×1(256, ReLU); GAP; Dropout(0.1); Dense(32)+ReLU+BN; Attention([x,x]) ; Dense(C).
Implementation notes: (1) at 112 input the stride-16 map is 7×7, so the first SepConv uses stride 2 (7→4) and the second k2/s2 (4→2) to keep the same 2×2 patch grid the paper has at 224; (2) `Attention([x,x])` on a single vector is the identity (the bug the authors acknowledged); we implement the *intended* scaled dot-product self-attention over the 2×2 patch tokens (before GAP) — flag `attention_over_patches=True`; a `attention_over_patches=False` switch reproduces the notebook's identity path for reference; (3) SepConv = depthwise k×k + pointwise 1×1 (Keras SeparableConv2D).

- [ ] Test: params 0.9–1.4 M; output shape; both attention flags produce `[2, C]`.
- [ ] Commit `feat(models): PAtt-Lite re-implementation`.

### Task 6: Train/eval engine

**Files:** `nnfer/train.py`, `nnfer/engine.py`, `tests/test_engine.py`

**Interfaces:**
- CLI `python -m nnfer.train --model NAME --dataset {rafdb,ferplus} --seed K [--epochs E --batch 64 --lr 1e-3 --wd 5e-4 --warmup 5 --label-smoothing 0.1 --cache ~/haesung/data/cache --runs runs --workers 6 --no-amp --no-pretrained --max-steps N(debug)]`.
- `engine.train_one_epoch(model, loader, opt, sched, scaler, device, criterion) -> dict(loss, acc)`; `engine.evaluate(model, loader, device) -> (logits np, labels np)`; `engine.build_scheduler(opt, epochs, steps_per_epoch, warmup_epochs)` (LambdaLR: linear warm-up then cosine to 0).
- Outputs in run dir: `config.json`, `history.csv` (epoch, lr, train_loss, train_acc, val_acc, val_macro_f1, time), `metrics.json` = `{"val": …, "test": …, "ckplus": … (rafdb only), "params", "flops", "env", "best_epoch", "wall_sec"}`, `preds.npz` (`test_logits, test_labels[, ckplus_logits, ckplus_labels]`), `best.pt` (state_dict).
- Default epochs: 60 for rafdb, 40 for ferplus (overridable).
- Model selection: highest val accuracy (ties → earlier epoch).

- [ ] Test (CPU, tiny cache from `tests/test_dataset.py` fixture, `--model microexpnet --epochs 1 --max-steps 2 --no-pretrained`): run dir contains the five artefacts, `metrics.json["test"]["acc"]` in [0,1], `history.csv` has 1 row.
- [ ] Commit `feat: deterministic train/eval engine with run artefacts`.

### Task 7: Smoke runs on lab GPU + spec bookkeeping

- [ ] `scripts/smoke.sh`: for each of `microexpnet mobilevit_xxs efficientface pattlite resnet18` run `python -m nnfer.train --model $m --dataset rafdb --seed 0 --epochs 3 --runs runs_smoke` and print `params, flops, val_acc, test_acc, wall_sec` (parse metrics.json).
- [ ] Run via `remote.ps1` under `nohup`; collect a table; sanity check: every model trains (loss decreases), 3-epoch RAF-DB test acc roughly 55–80 % for pretrained models, ~35–50 % for MicroExpNet; time/epoch recorded to plan the full 5-seed sweep.
- [ ] Update spec §7 with the recorded deviations (LDG loss, PAtt-Lite schedule/attention, ShuffleNet stem) and README status; commit `docs: M3 smoke results and protocol deviations`.

## Self-review
- Spec §4 protocol → Task 6 CLI defaults ✔; §5 metrics → Task 2 (latency/ONNX deferred to M6 as spec §10 says) ✔; §7 counterparts + reference → Tasks 3–5 ✔; §6 artefacts (`preds.npz`, per-run json) → Task 6 ✔; determinism → Task 1 ✔.
- Names consistent: `build_model`, `compute_metrics`, `seed_everything`, `run_dir`, `count_params/count_flops`.
