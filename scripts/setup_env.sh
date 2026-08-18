#!/usr/bin/env bash
# Create/refresh the `nnfer` conda env on a Linux CUDA box and freeze the lock file.
set -euo pipefail
source ~/miniconda3/etc/profile.d/conda.sh
conda env list | grep -q '^nnfer ' || conda create -n nnfer python=3.11 -y
conda activate nnfer
pip install -q torch==2.3.1 torchvision==0.18.1 --index-url https://download.pytorch.org/whl/cu121
pip install -q -r requirements.txt
pip install -q -e .
python -c "import torch, timm; print(torch.__version__, torch.cuda.is_available(), torch.cuda.get_device_name(0))"
pip freeze --exclude-editable > requirements.lock
echo "lock written: $(wc -l < requirements.lock) packages"
