#!/usr/bin/env bash
# 1-seed RAF-DB pilot of the full NN-SKD model over candidate backbones (backbone selection, spec §8).
set -o pipefail
mkdir -p logs
BBS=${BBS:-"mobilevit_xxs efficientface mobilenetv3s"}
for bb in $BBS; do
  echo "=== $(date '+%F %T') nnskd_$bb rafdb seed0"
  python -m nnfer.train --model "nnskd_$bb" --dataset rafdb --seed 0 --runs runs_pilot 2>&1 | grep -E '^\[done\]|Error|Traceback' || true
done
echo "=== $(date '+%F %T') PILOT DONE"
