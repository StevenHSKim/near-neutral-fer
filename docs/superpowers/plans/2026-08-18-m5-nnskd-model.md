# M5 — NN-SKD Model Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the proposed Near-Neutral Self-Knowledge-Distillation model (spec §8) as a
backbone-agnostic wrapper + loss, with inference cost identical to the plain backbone, plus the
ablation switches, so that once baselines finish the full ablation sweep can be launched with
`python -m nnfer.train --model nnskd_<backbone> [--kd-lambda … --feat-lambda … --nm-lambda …]`.

**Architecture:** `nnfer/models/backbones.py` exposes multi-stage features `[S2,S3,S4]` (strides
8/16/32) for `shufflenetv2`, `efficientface`, `mobilenetv3s`, `mobilenetv1` (and any timm
`features_only` model). `nnfer/models/nnskd.py` wraps a backbone with (training-only) auxiliary
heads on S2/S3, a Local-Global-Fusion teacher on [S2,S3,S4] at S3 resolution, and 1×1 adapters
for attention-map distillation. In `eval()` the forward runs backbone → GAP → FC only.
`nnfer/losses.py` implements the composite loss with epoch-wise λ ramp. `nnfer/train.py` gains
loss flags and calls `criterion.set_epoch`. `complexity.count_params` counts inference parameters
when a model defines `inference_parameters()`.

**Tech Stack:** PyTorch 2.3.1, timm 1.0.9, torchvision 0.18.1.

## Global Constraints
- Inference graph = backbone + GAP + FC. Verified by tests: eval-mode forward returns `[B,C]`,
  `count_params` (inference) equals the plain backbone-only variant, and FLOPs are equal.
- All auxiliary/teacher parameters are excluded from `inference_parameters()` and from the exported
  student (`export_student()` returns an `nn.Sequential`-like module for ONNX in M6).
- Loss: `L = CE(z_T) + CE(z_S) + α_aux·[CE(z_2)+CE(z_3)] + r(ep)·[λ_kd·Σ_i T²·KL(z_i‖sg z_T/T) + λ_f·Σ_j ‖A(adapter(S_j))−A(sg F_T)‖²] + λ_nm·L_NM`, `r(ep)=min(1, ep/ramp_epochs)`.
- Defaults: α_aux=0.5, λ_kd=1.0, T=4, λ_f=1.0, λ_nm=0 (ablation item), margin m=1.0, ramp 5 epochs, fuse_ch=128.
- Ablation registry names: `nnskd_<bb>` (full), and CLI flags to switch parts off:
  `--no-aux-heads`, `--no-teacher` (also disables kd/feat), `--kd-lambda 0`, `--feat-lambda 0`,
  `--nm-lambda x`, `--infer-head teacher` (reference row). `--tag` names the run.

## Tasks
1. `backbones.py` + tests: each backbone returns 3 maps with strides 8/16/32 for 112 input and the
   declared channel list; pretrained load works.
2. `nnskd.py` + tests: train-mode dict keys, eval-mode logits, inference params == backbone-only,
   `export_student()` output equals eval logits, `infer_head` switch.
3. `losses.py` + tests: components zero out under λ=0, ramp behaviour, KD term ≥ 0, NM term zero
   when margin satisfied; a 30-step CPU fit on a toy batch reduces total loss.
4. `train.py` flags + `engine` epoch hook; test that `--model nnskd_shufflenetv2 --no-teacher
   --no-aux-heads` produces identical logits to `--model shufflenetv2` baseline (same seed) — proves
   the ablation (a) row *is* the plain backbone.
5. `scripts/run_nnskd.sh`: ablation matrix (a)–(e) + `--infer-head teacher` × 5 seeds × datasets, resumable.
