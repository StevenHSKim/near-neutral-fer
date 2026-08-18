# near-neutral-fer

Lightweight facial-expression recognition for **near-neutral faces** via
self-knowledge distillation (NN-SKD). Research code: fully reproducible,
fixed seeds, repeated runs, statistical tests.

- Design spec: [`docs/superpowers/specs/2026-08-18-near-neutral-fer-research-design.md`](docs/superpowers/specs/2026-08-18-near-neutral-fer-research-design.md)
- Counterparts (re-implemented under one protocol): EfficientFace (AAAI'21), PAtt-Lite (IEEE Access'24), MicroExpNet (IPTA'19), MobileViT-XXS (ICLR'22); ResNet-18 as non-lightweight reference
- Benchmarks: RAF-DB, FERPlus (+ CK+48 cross-dataset)

## Setup (Linux, CUDA GPU)

```bash
conda create -n nnfer python=3.11 -y && conda activate nnfer
pip install torch==2.3.1 torchvision==0.18.1 --index-url https://download.pytorch.org/whl/cu121
pip install -r requirements.txt && pip install -e .
```

Exact frozen environment used for the reported numbers: `requirements.lock`.

## Data

Raw datasets are not redistributed. See [`data/README.md`](data/README.md) for the
expected layouts, then build the 112x112 caches + manifests:

```bash
python -m data.prepare_rafdb   --raw <RAFDB>   --out <cache>/rafdb
python -m data.prepare_ferplus --raw <FERPlus> --out <cache>/ferplus
python -m data.prepare_ckplus  --raw <CKPlus>  --out <cache>/ckplus
python -m data.report_stats    --cache <cache>   # -> docs/data_stats.md
```

## Train one configuration

```bash
python -m nnfer.train --model efficientface --dataset rafdb --seed 0
python -m nnfer.complexity        # params / FLOPs of every registered model
```

Writes `runs/<dataset>/<model>/seed<k>/{config.json,history.csv,metrics.json,preds.npz,best.pt}`.
Same seed + same code = bit-identical logits (tested).

## Status

Milestones 2-3 done: data pipeline, deterministic train/eval engine, four
counterparts + ResNet-18 reference. Next: full 5-seed baseline sweep, the
proposed NN-SKD model, statistics + export. All result tables will be generated
by `analysis/analyze.py` from raw run artefacts (no hand-typed numbers).
