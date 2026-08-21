#!/usr/bin/env bash
# NN-SKD v4: born-again self-distillation (teacher = the finished mobilevit_xxs baseline checkpoint
# of the SAME dataset and seed; same architecture -> self-KD across generations).
#   ban    = plain arch + born-again KD
#   banlgf = LGF spatial self-KD + born-again KD
# Fastest dataset first; resumable.
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
    T="runs/$d/mobilevit_xxs/seed$s/best.pt"
    if [ ! -f "$T" ]; then echo "!! missing teacher $T"; continue; fi
    run mobilevit_xxs       ban    --teacher-ckpt "$T" --ema-kd 1.0
    run nnskd_mobilevit_xxs banlgf --teacher-ckpt "$T" --ema-kd 1.0
  done
done
echo "=== $(date '+%F %T') V4 QUEUE DONE"
