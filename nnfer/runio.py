"""Run directory layout and environment provenance."""
import json
import platform
import subprocess
from pathlib import Path

import torch


def run_dir(root, dataset: str, model: str, seed: int) -> Path:
    return Path(root).expanduser() / dataset / model / f"seed{seed}"


def git_hash() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], stderr=subprocess.DEVNULL,
                                       cwd=Path(__file__).resolve().parent).decode().strip()
    except Exception:  # noqa: BLE001
        return "unknown"


def env_info() -> dict:
    return {
        "git_hash": git_hash(),
        "torch": torch.__version__,
        "cuda": torch.version.cuda,
        "cudnn": torch.backends.cudnn.version(),
        "gpu": torch.cuda.get_device_name(0) if torch.cuda.is_available() else "cpu",
        "python": platform.python_version(),
        "platform": platform.platform(),
    }


def save_json(obj, path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, default=str))
