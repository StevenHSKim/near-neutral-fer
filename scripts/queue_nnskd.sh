#!/usr/bin/env bash
# Sequential NN-SKD sweep (backbone chosen per spec §8 = strongest lightweight counterpart, MobileViT-XXS):
#   1) RAF-DB: full ablation rows a,b,c,d,e,tinf x 5 seeds
#   2) FERPlus: rows a,d x 5 seeds (remaining rows queued later if time allows)
set -o pipefail
mkdir -p logs
export BB=${BB:-mobilevit_xxs}
DATASETS=rafdb   ROWS="a b c d e tinf" bash scripts/run_nnskd.sh
DATASETS=ferplus ROWS="a d"            bash scripts/run_nnskd.sh
echo "=== $(date '+%F %T') NNSKD QUEUE DONE"
