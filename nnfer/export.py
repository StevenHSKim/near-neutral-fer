"""Export a trained checkpoint's deployed graph to ONNX (spec §5 efficiency / M6).

    python -m nnfer.export --model nnskd_mobilevit_xxs --ckpt runs/rafdb/.../best.pt --out model.onnx

For NNSKD models only the student path (backbone -> GAP -> FC) is exported via `export_student()`.
"""
import argparse
from pathlib import Path

import torch

from nnfer.data.labels import NUM_CLASSES
from nnfer.models import build_model, list_models


def export_onnx(model_name: str, ckpt: str | None, out: str, num_classes: int = 7, size: int = 112) -> Path:
    model = build_model(model_name, num_classes, pretrained=False)
    if ckpt:
        model.load_state_dict(torch.load(Path(ckpt).expanduser(), map_location="cpu"))
    if hasattr(model, "export_student"):
        model = model.export_student()
    model.eval()
    out = Path(out).expanduser()
    out.parent.mkdir(parents=True, exist_ok=True)
    torch.onnx.export(model, torch.zeros(1, 3, size, size), str(out), input_names=["image"],
                      output_names=["logits"], opset_version=17,
                      dynamic_axes={"image": {0: "batch"}, "logits": {0: "batch"}})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, choices=list_models())
    ap.add_argument("--ckpt", default="")
    ap.add_argument("--out", required=True)
    ap.add_argument("--num-classes", type=int, default=NUM_CLASSES["rafdb"])
    a = ap.parse_args()
    p = export_onnx(a.model, a.ckpt or None, a.out, a.num_classes)
    print(f"exported {p} ({p.stat().st_size / 1e6:.2f} MB)")


if __name__ == "__main__":
    main()
