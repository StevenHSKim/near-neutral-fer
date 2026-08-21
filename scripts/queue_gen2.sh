#!/usr/bin/env bash
# Generation-2 self-distillation: student = NN-SKD (LGF) + KD from the best generation-1 checkpoint
# of the SAME deployed architecture on that dataset (self-KD across generations).
#   teacher(rafdb)   = nnskd_mobilevit_xxs_v3   (85.0)
#   teacher(fer2013) = mobilevit_xxs_ban        (71.6)
#   teacher(sfew)    = nnskd_mobilevit_xxs      (36.5, v1)
set -o pipefail
SEEDS=${SEEDS:-"0 1 2 3 4"}
mkdir -p logs
teacher_dir() {
  case $1 in
    rafdb)   echo "runs/rafdb/nnskd_mobilevit_xxs_v3";;
    fer2013) echo "runs/fer2013/mobilevit_xxs_ban";;
    sfew)    echo "runs/sfew/nnskd_mobilevit_xxs";;
  esac
}
teacher_model() {
  case $1 in
    fer2013) echo "mobilevit_xxs";;
    *)       echo "nnskd_mobilevit_xxs";;
  esac
}
for d in sfew rafdb fer2013; do
  td=$(teacher_dir "$d"); tm=$(teacher_model "$d")
  for s in $SEEDS; do
    T="$td/seed$s/best.pt"
    if [ ! -f "$T" ]; then echo "!! missing teacher $T"; continue; fi
    echo "=== $(date '+%F %T') gen2 $d seed$s (teacher $tm)"
    python -m nnfer.train --model nnskd_mobilevit_xxs --dataset "$d" --seed "$s" --runs runs --tag gen2 \
      --teacher-ckpt "$T" --teacher-model "$tm" --ema-kd 1.0 2>&1 \
      | grep -E '^\[done\]|^\[skip\]|Error|error|Traceback' || true
  done
done
echo "=== $(date '+%F %T') GEN2 QUEUE DONE"
