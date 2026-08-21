#!/usr/bin/env bash
# Extend the decisive pairings to 10 seeds (spec §6 "10 if budget allows") for statistical power:
#   rafdb   : mobilevit_xxs vs nnskd_mobilevit_xxs (v1)
#   fer2013 : mobilevit_xxs vs mobilevit_xxs_ban   (ban needs the same-seed baseline as teacher)
#   sfew    : mobilevit_xxs, nnskd_mobilevit_xxs, efficientface (tie documentation)
set -o pipefail
SEEDS="5 6 7 8 9"
mkdir -p logs
run() {
  local model=$1 tag=$2; shift 2
  echo "=== $(date '+%F %T') $model tag=$tag $d seed$s"
  python -m nnfer.train --model "$model" --dataset "$d" --seed "$s" --runs runs ${tag:+--tag $tag} "$@" 2>&1 \
    | grep -E '^\[done\]|^\[skip\]|Error|error|Traceback' || true
}
d=sfew
for s in $SEEDS; do
  run mobilevit_xxs ""
  run nnskd_mobilevit_xxs ""
  run efficientface ""
done
d=rafdb
for s in $SEEDS; do
  run mobilevit_xxs ""
  run nnskd_mobilevit_xxs ""
done
d=fer2013
for s in $SEEDS; do
  run mobilevit_xxs ""
  run mobilevit_xxs ban --teacher-ckpt "runs/fer2013/mobilevit_xxs/seed$s/best.pt" --ema-kd 1.0
done
echo "=== $(date '+%F %T') SEEDS10 QUEUE DONE"
