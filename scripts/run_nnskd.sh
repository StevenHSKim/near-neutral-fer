#!/usr/bin/env bash
# NN-SKD ablation sweep (spec §8), resumable. Rows:
#   (a) <bb>                      plain backbone (no training-only modules)
#   (b) nnskd_<bb>_aux            + aux heads (BYOT-style self-KD, no teacher)
#   (c) nnskd_<bb>_kd             + LGF teacher, logit KD only
#   (d) nnskd_<bb>                + attention feature KD  (= full model, default flags)
#   (e) nnskd_<bb>_nm             + neutral-margin loss + near-neutral KD weighting
#   (ref) nnskd_<bb>_tinf         full model but teacher head used at inference (upper bound)
# Usage: BB=efficientface DATASETS="rafdb ferplus" SEEDS="0 1 2 3 4" nohup bash scripts/run_nnskd.sh > logs/nnskd_$BB.log 2>&1 &
set -o pipefail
BB=${BB:-efficientface}
DATASETS=${DATASETS:-"rafdb ferplus"}
SEEDS=${SEEDS:-"0 1 2 3 4"}
RUNS=${RUNS:-runs}
ROWS=${ROWS:-"a b c d e tinf"}
mkdir -p logs
run() { # $1=model $2=tag $3...=extra flags
  local model=$1 tag=$2; shift 2
  echo "=== $(date '+%F %T') $model tag=$tag $d seed$s $*"
  python -m nnfer.train --model "$model" --dataset "$d" --seed "$s" --runs "$RUNS" ${tag:+--tag $tag} "$@" 2>&1 \
    | grep -E '^\[done\]|^\[skip\]|Error|error|Traceback' || true
}
for d in $DATASETS; do
  for s in $SEEDS; do
    for row in $ROWS; do
      case $row in
        a)    run "$BB" "" ;;
        b)    run "nnskd_$BB" aux  --no-teacher ;;
        c)    run "nnskd_$BB" kd   --feat-lambda 0 ;;
        d)    run "nnskd_$BB" "" ;;
        e)    run "nnskd_$BB" nm   --nm-lambda 1.0 --nn-weighting ;;
        tinf) run "nnskd_$BB" tinf --infer-head teacher ;;
      esac
    done
  done
done
echo "=== $(date '+%F %T') ALL DONE"
