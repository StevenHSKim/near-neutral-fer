#!/usr/bin/env bash
# NN-SKD v3 rows (no mixup/logit-adj recipe — it hurt at the 40-60 epoch budget):
#   v3      = LGF spatial self-KD + EMA temporal self-KD
#   emaonly = EMA temporal self-KD only (plain backbone otherwise)
# Fastest dataset first; resumable. v1 (LGF only) and baselines already exist for all datasets.
set -o pipefail
SEEDS=${SEEDS:-"0 1 2 3 4"}
DATASETS=${DATASETS:-"sfew rafdb fer2013"}
mkdir -p logs
run() {
  local model=$1 tag=$2; shift 2
  echo "=== $(date '+%F %T') $model tag=$tag $d seed$s"
  python -m nnfer.train --model "$model" --dataset "$d" --seed "$s" --runs runs --tag "$tag" "$@" 2>&1 \
    | grep -E '^\[done\]|^\[skip\]|Error|error|Traceback' || true
}
for d in $DATASETS; do
  for s in $SEEDS; do
    run nnskd_mobilevit_xxs v3      --ema-kd 1.0
    run nnskd_mobilevit_xxs emaonly --ema-kd 1.0 --no-teacher --no-aux-heads
  done
done
echo "=== $(date '+%F %T') V3 QUEUE DONE"
