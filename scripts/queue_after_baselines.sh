#!/usr/bin/env bash
# Wait for the running baseline sweep, then (sequentially) fill any missing baseline runs and run the
# remaining NN-SKD pilot. Never run GPU jobs concurrently on the 11 GB card (OOM observed 2026-08-18).
set -o pipefail
while pgrep -f run_baselines.sh > /dev/null; do sleep 60; done
echo "=== $(date '+%F %T') baseline sweep finished; filling gaps"
bash scripts/run_baselines.sh
echo "=== $(date '+%F %T') pilot mobilevit_xxs"
BBS=mobilevit_xxs bash scripts/pilot_nnskd.sh
echo "=== $(date '+%F %T') QUEUE DONE"
