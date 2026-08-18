#!/usr/bin/env bash
# 3-epoch RAF-DB smoke run for every model; prints a summary table. Usage: bash scripts/smoke.sh [epochs]
set -eo pipefail
EPOCHS=${1:-3}
RUNS=runs_smoke
for m in microexpnet mobilevit_xxs efficientface pattlite resnet18; do
  python -m nnfer.train --model "$m" --dataset rafdb --seed 0 --epochs "$EPOCHS" --runs "$RUNS" --overwrite 2>&1 | grep -v Warning
done
python - <<EOF
import json, glob
print(f"{'model':15s} {'params(M)':>9s} {'FLOPs(M)':>9s} {'val_acc':>8s} {'test_acc':>8s} {'macroF1':>8s} {'FNR':>6s} {'ck_acc':>7s} {'min':>5s}")
for p in sorted(glob.glob("$RUNS/rafdb/*/seed0/metrics.json")):
    m = json.load(open(p)); name = p.split("/")[2]
    print(f"{name:15s} {m['params']/1e6:9.3f} {m['flops']/1e6:9.1f} {m['val']['acc']:8.4f} {m['test']['acc']:8.4f} "
          f"{m['test']['macro_f1']:8.4f} {m['test']['fnr']:6.3f} {m.get('ckplus',{}).get('acc',float('nan')):7.3f} {m['wall_sec']/60:5.1f}")
EOF
