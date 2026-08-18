#!/usr/bin/env bash
# Full baseline sweep: models x datasets x seeds, sequential, resumable (finished runs are skipped).
# Usage: nohup bash scripts/run_baselines.sh > logs/baselines.log 2>&1 &
set -o pipefail
MODELS=${MODELS:-"efficientface pattlite mobilevit_xxs microexpnet resnet18"}
DATASETS=${DATASETS:-"rafdb ferplus"}
SEEDS=${SEEDS:-"0 1 2 3 4"}
RUNS=${RUNS:-runs}
mkdir -p logs
for d in $DATASETS; do
  for s in $SEEDS; do
    for m in $MODELS; do
      echo "=== $(date '+%F %T') $m $d seed$s"
      python -m nnfer.train --model "$m" --dataset "$d" --seed "$s" --runs "$RUNS" 2>&1 \
        | grep -E '^\[done\]|^\[skip\]|Error|error|Traceback' || true
    done
  done
done
echo "=== $(date '+%F %T') ALL DONE"
