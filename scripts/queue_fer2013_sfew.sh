#!/usr/bin/env bash
# Counterparts + reference + NN-SKD on SFEW 2.0 and FER2013, 5 seeds, sequential & resumable.
set -o pipefail
mkdir -p logs
MODELS="efficientface pattlite mobilevit_xxs microexpnet resnet18 nnskd_mobilevit_xxs"
for d in sfew fer2013; do
  for s in 0 1 2 3 4; do
    for m in $MODELS; do
      echo "=== $(date '+%F %T') $m $d seed$s"
      python -m nnfer.train --model "$m" --dataset "$d" --seed "$s" --runs runs 2>&1 \
        | grep -E '^\[done\]|^\[skip\]|Error|error|Traceback' || true
    done
  done
done
echo "=== $(date '+%F %T') FER2013/SFEW QUEUE DONE"
