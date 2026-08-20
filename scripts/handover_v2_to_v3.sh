#!/usr/bin/env bash
# Let the running v2 queue finish its RAF-DB stage (5-seed completion of the recipe/ema/v2 rows for
# the record), then cancel its FER2013 stage (recipe rows hurt; not worth 13 h) and hand over to the
# v3 queue. Idempotent: safe to re-run.
set -o pipefail
cd ~/haesung/near-neutral-fer
until grep -q 'fer2013 seed' logs/v2.log 2>/dev/null || ! pgrep -f 'bash scripts/queue_v2.sh' > /dev/null; do
  sleep 120
done
pkill -f 'bash scripts/queue_v2.sh' 2>/dev/null
pkill -f 'nnfer.train.*fer2013.*recipe\|nnfer.train.*fer2013.*mixup' 2>/dev/null
sleep 5
pkill -f 'python -m nnfer.train' 2>/dev/null
sleep 5
# tidy partial fer2013 dirs (no metrics.json yet)
for d in runs/fer2013/*/seed*; do
  [ -d "$d" ] && [ ! -f "$d/metrics.json" ] && rm -rf "$d" && echo "removed partial $d"
done
echo "=== $(date '+%F %T') handover: v2 stopped, starting v3"
bash scripts/queue_v3.sh
