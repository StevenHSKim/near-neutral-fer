"""Train + evaluate one (model, dataset, seed) configuration under the shared protocol.

    python -m nnfer.train --model efficientface --dataset rafdb --seed 0

Writes runs/<dataset>/<model>/seed<k>/{config.json, history.csv, metrics.json, preds.npz, best.pt}.
"""
import argparse
import csv
import time
from pathlib import Path

import numpy as np
import torch
from torch import nn
from torch.utils.data import DataLoader

from nnfer.complexity import count_flops, count_params
from nnfer.data.dataset import CachedFER
from nnfer.data.labels import NUM_CLASSES
from nnfer.data.transforms import build_transforms
from nnfer.engine import build_scheduler, evaluate, train_one_epoch
from nnfer.metrics import compute_metrics
from nnfer.models import build_model, list_models
from nnfer.runio import env_info, run_dir, save_json
from nnfer.seed import seed_everything, worker_init_fn

DEFAULT_EPOCHS = {"rafdb": 60, "ferplus": 40}


def parse_args(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", required=True, choices=list_models())
    ap.add_argument("--dataset", required=True, choices=["rafdb", "ferplus"])
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--epochs", type=int, default=None, help="default: 60 rafdb / 40 ferplus")
    ap.add_argument("--batch", type=int, default=64)
    ap.add_argument("--lr", type=float, default=1e-3)
    ap.add_argument("--wd", type=float, default=5e-4)
    ap.add_argument("--warmup", type=int, default=5)
    ap.add_argument("--label-smoothing", type=float, default=0.1)
    ap.add_argument("--cache", default="~/haesung/data/cache")
    ap.add_argument("--runs", default="runs")
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--no-amp", action="store_true")
    ap.add_argument("--no-pretrained", action="store_true")
    ap.add_argument("--max-steps", type=int, default=None, help="debug: cap train steps per epoch")
    ap.add_argument("--tag", default="", help="suffix appended to the model name in the run dir")
    ap.add_argument("--overwrite", action="store_true")
    a = ap.parse_args(argv)
    if a.epochs is None:
        a.epochs = DEFAULT_EPOCHS[a.dataset]
    return a


def make_loader(ds, batch, shuffle, workers, generator):
    return DataLoader(ds, batch_size=batch, shuffle=shuffle, num_workers=workers, pin_memory=True,
                      drop_last=shuffle, generator=generator, worker_init_fn=worker_init_fn,
                      persistent_workers=workers > 0)


def main(argv=None):
    a = parse_args(argv)
    name = a.model + (f"_{a.tag}" if a.tag else "")
    out = run_dir(a.runs, a.dataset, name, a.seed)
    if (out / "metrics.json").exists() and not a.overwrite:
        print(f"[skip] {out} already complete")
        return out
    out.mkdir(parents=True, exist_ok=True)
    g = seed_everything(a.seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    C = NUM_CLASSES[a.dataset]
    cache = Path(a.cache).expanduser() / a.dataset

    train_ds = CachedFER(cache, a.dataset, "train", build_transforms(True))
    val_ds = CachedFER(cache, a.dataset, "val", build_transforms(False))
    test_ds = CachedFER(cache, a.dataset, "test", build_transforms(False))
    train_ld = make_loader(train_ds, a.batch, True, a.workers, g)
    val_ld = make_loader(val_ds, a.batch * 2, False, a.workers, g)
    test_ld = make_loader(test_ds, a.batch * 2, False, a.workers, g)

    model = build_model(a.model, C, pretrained=not a.no_pretrained)
    params, flops = count_params(model), count_flops(model)
    model.to(device)
    criterion = nn.CrossEntropyLoss(label_smoothing=a.label_smoothing)
    opt = torch.optim.AdamW(model.parameters(), lr=a.lr, weight_decay=a.wd)
    steps = len(train_ld) if a.max_steps is None else min(len(train_ld), a.max_steps)
    sched = build_scheduler(opt, a.epochs, steps, a.warmup)
    scaler = torch.cuda.amp.GradScaler(enabled=(not a.no_amp) and device.type == "cuda")

    save_json({**vars(a), "run_name": name, "params": params, "flops": flops, "env": env_info()}, out / "config.json")
    hist_path = out / "history.csv"
    with hist_path.open("w", newline="") as f:
        csv.writer(f).writerow(["epoch", "lr", "train_loss", "train_acc", "val_acc", "val_macro_f1", "sec"])

    best_acc, best_epoch, t0 = -1.0, -1, time.time()
    for ep in range(1, a.epochs + 1):
        te = time.time()
        tr = train_one_epoch(model, train_ld, opt, sched, scaler, device, criterion, a.max_steps)
        vl, vy = evaluate(model, val_ld, device)
        vm = compute_metrics(vl, vy, a.dataset, val_ds.manifest)
        with hist_path.open("a", newline="") as f:
            csv.writer(f).writerow([ep, f"{opt.param_groups[0]['lr']:.6g}", f"{tr['loss']:.4f}", f"{tr['acc']:.4f}",
                                    f"{vm['acc']:.4f}", f"{vm['macro_f1']:.4f}", f"{time.time() - te:.1f}"])
        print(f"[{name}/{a.dataset}/s{a.seed}] ep {ep:3d}/{a.epochs} loss {tr['loss']:.3f} "
              f"train_acc {tr['acc']:.3f} val_acc {vm['acc']:.4f} ({time.time() - te:.0f}s)", flush=True)
        if vm["acc"] > best_acc:
            best_acc, best_epoch = vm["acc"], ep
            torch.save(model.state_dict(), out / "best.pt")

    # final evaluation with the best-val checkpoint (test touched once)
    model.load_state_dict(torch.load(out / "best.pt", map_location=device))
    vl, vy = evaluate(model, val_ld, device)
    tl, ty = evaluate(model, test_ld, device)
    metrics = {
        "val": compute_metrics(vl, vy, a.dataset, val_ds.manifest),
        "test": compute_metrics(tl, ty, a.dataset, test_ds.manifest),
        "best_epoch": best_epoch, "params": params, "flops": flops,
        "wall_sec": time.time() - t0, "env": env_info(),
    }
    preds = {"test_logits": tl.astype(np.float32), "test_labels": ty}
    if a.dataset == "rafdb":  # cross-dataset generalisation test (spec §5.5)
        ck_cache = Path(a.cache).expanduser() / "ckplus"
        if (ck_cache / "ckplus_manifest.csv").exists():
            ck_ds = CachedFER(ck_cache, "ckplus", "test", build_transforms(False))
            cl, cy = evaluate(model, make_loader(ck_ds, a.batch * 2, False, a.workers, g), device)
            metrics["ckplus"] = compute_metrics(cl, cy, "ckplus")
            preds.update(ckplus_logits=cl.astype(np.float32), ckplus_labels=cy)
    np.savez_compressed(out / "preds.npz", **preds)
    save_json(metrics, out / "metrics.json")
    print(f"[done] {name}/{a.dataset}/seed{a.seed}: best_epoch {best_epoch} val_acc {metrics['val']['acc']:.4f} "
          f"test_acc {metrics['test']['acc']:.4f} macro_f1 {metrics['test']['macro_f1']:.4f} "
          f"fnr {metrics['test']['fnr']:.4f} ({metrics['wall_sec'] / 60:.1f} min)")
    return out


if __name__ == "__main__":
    main()
