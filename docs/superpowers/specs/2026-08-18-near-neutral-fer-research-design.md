# Near-Neutral Lightweight FER — Research & Experiment Design

Date: 2026-08-18
Project: 중립 표정-근처 미세 표정 인식을 위한 자기-지식 증류 기반 경량 FER 연구
(Lightweight Micro-FER for near-Neutral Faces based on Self-Knowledge Distillation)

## 1. Goal and hypotheses

Build an open-source, fully reproducible research codebase that

1. re-implements four lightweight FER counterparts under one fair protocol,
2. proposes a self-knowledge-distillation (Self-KD) lightweight FER model, and
3. shows with repeated runs + statistical tests that the proposed model beats the
   counterparts on **near-neutral** recognition **without increasing inference cost**.

- **H1** The proposed model achieves higher near-neutral metrics (Sec. 5) than each
  counterpart at comparable or lower Params/FLOPs/latency.
- **H2** The gain comes from the Self-KD training scheme, not from extra inference
  parameters (ablation: same backbone w/o Self-KD).

## 2. Fixed decisions (confirmed 2026-08-18)

| Item | Decision |
|---|---|
| Datasets | RAF-DB (basic, aligned), FERPlus (Kaggle), CK+ (cross-dataset test only) |
| Counterparts | EfficientFace (AAAI'21), PAtt-Lite (IEEE Access'24), MicroExpNet (IPTA'19), MobileViT-XXS (timm) |
| Input | 112×112 RGB, ImageNet-pretrained weights where a backbone has them |
| Seeds | 5 seeds per configuration (0,1,2,3,4) |
| Framework | PyTorch (single codebase), Python 3.11 conda env `nnfer`, pinned requirements |
| Compute | Lab desktop via SSH (`lab-wsl`, WSL Ubuntu, RTX 2080 Ti 11 GB, 16 threads, 31 GB RAM). Code developed locally, synced through GitHub (`StevenHSKim/near-neutral-fer`), training launched remotely with nohup, only run artefacts (json/npz) pulled back for analysis |
| Raw data location | `/mnt/c/Users/steve/Desktop/dataset/{RAFDB,FERPlus,CKPlus}` on lab desktop; preprocessed 112×112 cache stored under `~/haesung/data` (WSL ext4) |
| CK+ | Only the Kaggle CK+48 variant (981 last-3-frame images, no sequences) is available → **decision A**: CK+ is used as a cross-dataset generalisation test only; the onset low-intensity test is dropped (can be added later if full CK+ sequences are obtained) |

## 3. Datasets and splits

| Dataset | Classes | Train / Test | Role |
|---|---|---|---|
| RAF-DB basic | 7 (Sur, Fea, Dis, Hap, Sad, Ang, Neu) | 12,271 / 3,068 (official) | Main benchmark |
| FERPlus | 8 (Neu, Hap, Sur, Sad, Ang, Dis, Fea, Con) → majority-vote label, 10 crowd votes kept | official Train / PublicTest (val) / PrivateTest (test) | Second benchmark + near-neutral subset |
| CK+ (CK+48) | 7 (anger, contempt, disgust, fear, happy, sadness, surprise; 981 imgs, 48×48) | not used for training | Cross-dataset generalisation test (classes mapped to the training label set; contempt excluded) |

- Validation: RAF-DB has no official val split → hold out 10 % of train (stratified,
  fixed seed 0, same split for every model) for model selection / early stopping;
  test set touched only once per finished run.
- FERPlus uses PublicTest as val, PrivateTest as test.
- Faces: RAF-DB aligned images as provided; FERPlus 48×48 grayscale upsampled to
  112×112 and replicated to 3 channels; CK+ faces detected + aligned once with a fixed
  landmark-based crop, cached to disk.
- Preprocessing script writes a manifest CSV (`path,label,split,votes...`) with an
  md5 of the manifest logged in every run.

## 4. Fair-comparison protocol (identical for every model)

- Input 112×112, ImageNet mean/std normalisation.
- Augmentation: RandomResizedCrop(112, scale 0.8–1.0), HorizontalFlip, RandomErasing
  (p=0.5), no test-time augmentation.
- Optimiser AdamW, lr 1e-3 (backbone) / cosine schedule, 5-epoch warm-up,
  weight decay 5e-4, batch 64, 60 epochs (RAF-DB) / 40 epochs (FERPlus), label
  smoothing 0.1, AMP on. Best-val checkpoint evaluated on test.
- Pretraining policy: ImageNet weights for MobileNetV1 (PAtt-Lite), ShuffleNetV2
  (EfficientFace), MobileViT-XXS (timm); MicroExpNet trained from scratch (no
  ImageNet variant exists). Same policy for the proposed model's backbone.
- Reported paper numbers are shown only in a separate "reported" column; all
  comparisons use our own runs.
- Determinism: fixed seeds for python/numpy/torch, `cudnn.deterministic=True`,
  `benchmark=False`, deterministic dataloader workers, config YAML + git hash +
  pip freeze + GPU name saved with every run.

## 5. Metrics

**Standard**: accuracy, macro-F1, per-class F1, confusion matrix.

**Near-neutral (primary for H1)**
1. False-neutral rate (FNR): fraction of non-neutral test samples predicted as neutral.
2. Neutral recall and neutral F1.
3. Near-neutral macro-F1 on the four classes most confused with neutral (Sad, Fear,
   Disgust, Anger) — fixed a-priori.
4. FERPlus ambiguous subset: majority label ≠ Neutral **and** neutral vote share ≥ τ
   (τ = 0.3 primary; 0.2/0.4 sensitivity). Accuracy + macro-F1 on this subset.
5. CK+48 cross-dataset test (RAF-DB-trained models, no fine-tuning): accuracy,
   macro-F1 and FNR on the 6 overlapping classes (contempt excluded). Generalisation
   evidence, not a near-neutral metric.
6. Calibration: mean prediction entropy, ECE (15 bins).

**Efficiency**: Params, FLOPs (fvcore/thop at 112×112), CPU latency (ONNX Runtime,
1 thread, batch 1, median of 200 runs), GPU latency, ONNX/TFLite file size.

## 6. Repeated runs and statistics

- Every configuration × dataset × 5 seeds. Mean ± std and 95 % CI (t-dist).
- Proposed vs each counterpart: paired t-test and Wilcoxon signed-rank over the 5
  seed-paired scores per metric; Holm correction over the 4 counterparts; Cohen's d.
- Same-test-set comparison: McNemar test on per-sample correctness (seed-matched),
  reported per seed and pooled.
- All raw predictions (`preds.npz`) and per-run JSON stored under `runs/`; a single
  `analyze.py` regenerates every table/figure from them (no hand-entered numbers).

## 7. Counterparts (re-implemented in PyTorch)

| Model | Source | Size (paper) | Notes |
|---|---|---|---|
| EfficientFace | Zhao et al., AAAI 2021, github.com/zengqunzhao/EfficientFace | 1.28 M | ShuffleNetV2 + local-feature extractor + channel-spatial modulator; LDG label-distribution loss kept as in paper |
| PAtt-Lite | Ngwe et al., IEEE Access 2024, github.com/JLREx/PAtt-Lite | ~1.1 M | MobileNetV1 (truncated) + patch extraction + attention classifier. Official repo has an acknowledged attention-classifier bug (leakage); we implement the intended architecture and report only our runs |
| MicroExpNet | Cugu et al., IPTA 2019 | ~65 K | Tiny CNN student; teacher-KD from an Inception teacher in paper. We train it with plain CE under our protocol (and note this) — lower-bound counterpart |
| MobileViT-XXS | Mehta & Rastegari, ICLR 2022 (timm) | 1.3 M | Reproducible CNN+ViT hybrid lightweight backbone (stand-in for code-less LiteFer) |
| Reference (not counterpart) | ResNet-18 (ImageNet) | 11.7 M | Upper-bound representation gap (Stage-1 requirement) |

Recorded deviations from the official recipes (all models share the §4 protocol; verified
2026-08-18 by `python -m nnfer.complexity`: EfficientFace 1.273 M / 79.7 MFLOPs, PAtt-Lite
1.094 M / 172.6 MFLOPs, MobileViT-XXS 0.953 M / 135.4 MFLOPs, MicroExpNet 0.085 M / 9.8 MFLOPs,
ResNet-18 11.18 M / 969.7 MFLOPs at 112×112):
- EfficientFace: torchvision ShuffleNetV2 (24-ch stem, ImageNet) instead of the 29-ch stem
  pre-trained on MS-Celeb-1M; plain CE (label smoothing 0.1) instead of the LDG
  label-distribution loss.
- PAtt-Lite: single-stage training under the shared optimiser instead of the two-stage
  freeze/fine-tune schedule with class weights; at 112×112 the patch extraction strides are
  (2, 2) instead of (4, 2) so the 2×2 patch grid matches the paper's 224×224 geometry; the
  acknowledged identity-attention bug is replaced by the intended self-attention over patch
  tokens (`pattlite`), with `pattlite_identity` kept as a reference variant.
- MicroExpNet: 112×112 RGB→luma input (feature 32×7×7) instead of 84×84 grey; no Inception-v3
  teacher distillation (plain CE), i.e. an architecture-only lower bound.
- MobileViT-XXS: timm ImageNet weights, classifier re-initialised.

Related work to cite but not run: GSDNet (gradual self-distillation FER, non-lightweight,
no code), FRSKD (Ji et al., CVPR 2021), Face2Exp (CVPR 2022), Emotional-to-Neutral
Transformation (2024), LiteFer (2024).

## 8. Proposed method — NN-SKD (Near-Neutral Self-Knowledge Distillation)

Design principle: near-neutral differences live in small local regions (mouth
corner, eye corner, glabella) that survive in low-level feature maps (28×28, 14×14)
but vanish at the 4×4/7×7 top. A training-only fusion teacher built from the
network's own lower stages transfers that local knowledge upward; at inference every
auxiliary module is removed, so Params/FLOPs equal the plain backbone.

```
112×112 → S1(56) → S2(28) → S3(14) → S4(7/4) → GAP → FC → z_S   [student = deployed]
                     │aux      │aux      │adapter(1×1)
                     z_2       z_3       ▼
                     └────┬────┘   LGF-Teacher: lateral 1×1 on S2/S3/S4 → resample
                          ▼        to 14×14 → concat → SE + spatial attention → F_T
                     (KL from z_T)                → GAP → FC → z_T
```

- Backbone: the strongest lightweight counterpart backbone found in Stage 1
  (candidates: ShuffleNetV2 1.0×, MobileNetV3-Small), ImageNet-pretrained, 112×112.
  Using a counterpart's backbone isolates the gain to Self-KD.
- LGF-Teacher (training only): lateral 1×1 convs align channels (≤256), features
  resampled to S3 resolution, fused with channel (SE) + spatial (CBAM-style)
  attention, then GAP → FC → z_T.
- Auxiliary heads (training only, BYOT-style) after S2 and S3 → z_2, z_3.
- Losses: L = L_CE(z_T,z_S,z_3,z_2; label smoothing 0.1)
  + λ_kd·Σ KL(z_i ‖ sg(z_T)/T) over i∈{S,3,2}
  + λ_f·‖norm(A(adapter(S4))) − norm(A(F_T))‖² (spatial-attention feature KD, FRSKD)
  + λ_nm·L_NM (Neutral-Margin: for non-neutral samples enforce z_y − z_neutral ≥ m,
    KD weight up-weighted for samples the teacher finds near-neutral; ablation item).
  λ_kd, λ_f ramp 0→1 over the first epochs (stability). Hyper-parameters tuned on the
  RAF-DB val split only, then frozen for all datasets.
- Ablations (5 seeds each): (a) backbone only, (b) + aux heads (BYOT), (c) + LGF
  teacher logit KD, (d) + attention feature KD, (e) + Neutral-Margin; plus a
  reference row keeping the teacher branch at inference (upper bound of the recovery).
- Risks: teacher weaker than student early (sg + ramp + CE on teacher); memory
  (fusion at 14×14 only); small gains (first analyse counterparts' neutral
  confusions and Grad-CAM to confirm the local-region failure mode before finalising).

## 9. Repository layout

```
near-neutral-fer/
  README.md               # results tables auto-inserted from analysis
  requirements.txt / requirements.lock
  configs/                # yaml per model×dataset; base.yaml shared protocol
  data/                   # scripts: prepare_rafdb.py, prepare_ferplus.py, prepare_ckplus.py → manifests
  nnfer/
    datasets.py  transforms.py  metrics.py  seed.py
    models/{efficientface,pattlite,microexpnet,mobilevit,resnet18,proposed}.py
    losses/  train.py  evaluate.py  export.py (ONNX/TFLite)  latency.py
  scripts/run_all.ps1     # enumerates configs × seeds
  analysis/analyze.py     # stats, tables, figures from runs/
  runs/                   # per-run json + preds.npz (git-ignored)
  docs/                   # this spec, plans, final report
  tests/                  # unit tests: dataset manifests, metrics, model shapes/param counts, determinism
```

## 10. Milestones (each requires user confirmation before the next)

1. Plan + counterparts (this document) ✔ approved 2026-08-18
2. Environment + data pipeline + manifests + tests ✔ 2026-08-18
3. Counterpart implementation, param/FLOP checks vs paper, 1-seed smoke runs ✔ 2026-08-18
   (3-epoch RAF-DB smoke, seed 0: MobileViT-XXS 73.6 %, ResNet-18 75.3 %, PAtt-Lite 68.3 %,
   EfficientFace 65.8 %, MicroExpNet 39.3 % test acc; ≈4–18 s/epoch on RTX 2080 Ti)
4. Full baseline runs (5 seeds) + preliminary analysis
5. Proposed model design + ablations
6. Full runs, statistics, export/latency, README + report

## 11. Out of scope

AffectNet (no licence at hand), Jetson hardware measurement (CPU/ONNX latency used
as proxy; Jetson section left as instructions), video/temporal micro-expression datasets
(CASME/SAMM).
