# near-neutral-fer

**NN-SKD: Self-knowledge distillation for lightweight facial-expression recognition
near the neutral expression.** Research code — fully reproducible: pinned
environment, fixed seeds, 5–10 repeated runs per configuration, paired statistical
tests. Every number below was produced by `analysis/analyze.py` from raw run
artefacts; nothing is hand-typed.

## Method

Two training-only self-distillation signals on top of a lightweight backbone
(MobileViT-XXS). Everything is removed at inference, so the deployed graph is
bit-identical to the plain backbone (verified by tests):

1. **Spatial self-KD (LGF)** — lateral 1×1 convs fuse the backbone's stride-8/16/32
   features into a Local-Global-Fusion teacher (SE + spatial attention at 14×14);
   the teacher supervises the student head and two auxiliary heads with logit KD
   (T=4) and attention-map distillation (FRSKD/BYOT-style).
2. **Generational self-KD (born-again)** — a finished checkpoint of the *same*
   architecture (same dataset, same seed) is frozen as a second teacher
   (Furlanello et al., 2018).

## Results (test accuracy, mean ± std over seeds)

| Deployed graph (112×112) | Params | MFLOPs | CPU latency* | RAF-DB | FER2013 | SFEW 2.0 |
|---|---|---|---|---|---|---|
| **NN-SKD (ours)** | **0.953 M** | **135** | **5.8 ms** | **84.92 ± 0.31** (LGF, n=10) | **71.42 ± 0.44** (born-again, n=10) | 36.47 ± 2.38 (LGF, n=10) |
| MobileViT-XXS (backbone, ICLR'22) | 0.953 M | 135 | 5.8 ms | 84.29 ± 0.57 (n=10) | 70.63 ± 0.90 (n=10) | 36.55 ± 2.91 (n=10) |
| PAtt-Lite (IEEE Access'24) | 1.094 M | 173 | 3.9 ms | 84.09 ± 0.45 | 70.08 ± 0.32 | 33.53 ± 2.77 |
| EfficientFace (AAAI'21) | 1.273 M | 80 | 3.0 ms | 81.00 ± 0.84 | 69.18 ± 0.72 | 37.20 ± 2.40 (n=10) |
| MicroExpNet (IPTA'19) | 0.085 M | 10 | 0.3 ms | 69.43 ± 0.63 | 52.40 ± 0.96 | 22.82 ± 3.16 |
| ResNet-18 (reference, not lightweight) | 11.18 M | 970 | 19.8 ms | 84.22 ± 0.55 | 70.60 ± 0.93 | 37.08 ± 3.46 |

\* ONNX Runtime, 1 CPU thread, batch 1, median of 200 runs. n=5 unless noted.

**Statistical evidence** (paired over seeds; full tables in `results/`):
- **RAF-DB**: NN-SKD vs its own backbone +0.63 pp — t-test p=0.004 (Holm-corrected
  over 5 counterparts p=0.046), Wilcoxon p=0.004, Cohen's d=1.20. Neutral recall
  +1.97 pp (p=0.03), near-neutral-4 macro-F1 +1.40 pp (p=0.06), ECE improved (p=0.006).
- **FER2013**: born-again vs backbone +0.79 pp — t p=0.011, Wilcoxon p=0.011, d=1.01;
  near-neutral-4 macro-F1 +1.66 pp (Wilcoxon p=0.0098).
- **SFEW 2.0** (773 training images): all lightweight models are statistically
  indistinguishable (best pairwise |d| ≤ 0.3); reported for completeness.

**Honest findings.** The spatial (LGF) signal helps only where the input retains
real local facial texture (RAF-DB, aligned ~100 px); on 48 px-upsampled FER2013 it
is neutral-to-slightly-negative, and there the generational (born-again) signal is
what works. Mixup/CutMix + logit adjustment *hurt* at this epoch budget (documented
in `results/`), and a 2nd born-again generation adds nothing. Online EMA
self-distillation requires the EMA horizon to be scaled to steps-per-epoch or it
collapses training on small datasets.

## Reproduce

```bash
conda create -n nnfer python=3.11 -y && conda activate nnfer
pip install torch==2.3.1 torchvision==0.18.1 --index-url https://download.pytorch.org/whl/cu121
pip install -r requirements.txt && pip install -e .    # exact env: requirements.lock

# data (see data/README.md for raw layouts)
python -m data.prepare_rafdb --raw <RAFDB> --out cache/rafdb    # + prepare_fer2013 / prepare_sfew / prepare_ckplus
python -m data.report_stats --cache cache

# counterparts + baselines (identical protocol for every model)
bash scripts/run_baselines.sh

# NN-SKD
python -m nnfer.train --model nnskd_mobilevit_xxs --dataset rafdb --seed 0 --cache cache          # spatial self-KD
python -m nnfer.train --model mobilevit_xxs --dataset fer2013 --seed 0 --tag ban --cache cache \
    --teacher-ckpt runs/fer2013/mobilevit_xxs/seed0/best.pt --ema-kd 1.0                          # born-again

# statistics, tables, figures — regenerates everything in results/
python -m analysis.analyze --runs runs --out results --proposed nnskd_mobilevit_xxs

# efficiency
python -m nnfer.latency                       # ONNX CPU benchmark
python -m nnfer.export --model nnskd_mobilevit_xxs --ckpt <best.pt> --out nnskd.onnx
```

Same seed + same code ⇒ bit-identical logits (tested). Every run directory stores
its config, git hash, environment, per-epoch history, metrics and raw test logits.

## Protocol

112×112 RGB, ImageNet-pretrained backbones, identical augmentation
(RandomResizedCrop 0.8–1.0, h-flip, RandomErasing 0.5), AdamW 1e-3, cosine schedule
with 5-epoch warm-up, batch 64, label smoothing 0.1, AMP; best-val checkpoint
evaluated once on test. Deviations from official recipes are recorded in the
design spec (`docs/superpowers/specs/`). RAF-DB val = 10 % stratified hold-out of
official train (seed 0); FER2013 official split recovered by row order and
cross-checked against FERPlus `Usage`; SFEW official Val used as test. CK+48 is a
cross-dataset test only.

## Repository

`nnfer/` models, losses, engine, metrics, export · `data/` preprocessing →
112×112 caches + md5 manifests · `analysis/` statistics & report generation ·
`scripts/` sweep queues (resumable) · `tests/` 60+ unit tests (determinism,
label spaces, model shapes/params, loss components, run artefacts).
