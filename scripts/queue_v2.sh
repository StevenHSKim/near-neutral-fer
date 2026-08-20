#!/usr/bin/env bash
# NN-SKD v2 sweep, fastest dataset first (sfew ~1min/run -> rafdb ~25min -> fer2013 ~50min), resumable.
# Rows (all training-only changes; inference = plain MobileViT-XXS):
#   v2a  mobilevit_xxs + recipe (mixup/cutmix + logit-adj)            [recipe-only control]
#   v2b  + EMA self-teacher KD (temporal self-KD), no LGF branch
#   v2c  + LGF fusion teacher & aux heads (spatial+temporal self-KD)  [full v2]
set -o pipefail
SEEDS=${SEEDS:-"0 1 2 3 4"}
DATASETS=${DATASETS:-"sfew rafdb fer2013"}
RECIPE="--mixup-alpha 0.2 --cutmix-alpha 1.0 --logit-adj 1.0"
mkdir -p logs
run() { # $1=model $2=tag $3...=extra
  local model=$1 tag=$2; shift 2
  echo "=== $(date '+%F %T') $model tag=$tag $d seed$s"
  python -m nnfer.train --model "$model" --dataset "$d" --seed "$s" --runs runs --tag "$tag" "$@" 2>&1 \
    | grep -E '^\[done\]|^\[skip\]|Error|error|Traceback' || true
}
for d in $DATASETS; do
  for s in $SEEDS; do
    run mobilevit_xxs       recipe $RECIPE
    run nnskd_mobilevit_xxs ema    $RECIPE --ema-kd 1.0 --no-teacher --no-aux-heads
    run nnskd_mobilevit_xxs v2     $RECIPE --ema-kd 1.0
  done
done
echo "=== $(date '+%F %T') V2 QUEUE DONE"
