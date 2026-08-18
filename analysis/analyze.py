"""Regenerate every results table/figure from raw run artefacts (spec §6: no hand-typed numbers).

    python -m analysis.analyze --runs runs --out results [--proposed nnskd]

Outputs under --out:
  runs_flat.csv                       one row per (dataset, model, seed) with all scalar metrics
  summary_<dataset>.md                mean ± std [95% CI] per model for the key metrics
  compare_<dataset>_<proposed>.md     paired t / Wilcoxon (Holm-adjusted) / Cohen's d / McNemar vs each other model
  fig_<dataset>_<metric>.png          seed-scatter + mean±CI bars per model
  fig_<dataset>_<model>_confusion.png mean confusion matrix (row-normalised)
"""
import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from analysis.stats import holm, mcnemar, mean_ci, paired_tests
from nnfer.data.labels import FERPLUS_CLASSES, RAFDB_CLASSES

KEY_METRICS = {  # column -> (label, higher_is_better)
    "test.acc": ("Acc", True),
    "test.macro_f1": ("Macro-F1", True),
    "test.near_neutral_macro_f1": ("NN-4 F1", True),
    "test.fnr": ("FNR", False),
    "test.neutral_recall": ("Neu-Recall", True),
    "test.neutral_f1": ("Neu-F1", True),
    "test.nn_subset_acc@0.3": ("NN-sub Acc@.3", True),
    "test.nn_subset_macro_f1@0.3": ("NN-sub F1@.3", True),
    "test.ece": ("ECE", False),
    "ckplus.acc": ("CK+ Acc", True),
    "ckplus.macro_f1": ("CK+ F1", True),
}
CLASSES = {"rafdb": RAFDB_CLASSES, "ferplus": FERPLUS_CLASSES}


def _flatten(prefix, d, out):
    for k, v in d.items():
        if isinstance(v, dict):
            _flatten(f"{prefix}{k}.", v, out)
        elif isinstance(v, (int, float)) or v is None:
            out[f"{prefix}{k}"] = v


def collect(runs_root: Path) -> pd.DataFrame:
    rows = []
    for mp in sorted(runs_root.glob("*/*/seed*/metrics.json")):
        seed_dir = mp.parent
        dataset, model = seed_dir.parent.parent.name, seed_dir.parent.name
        seed = int(seed_dir.name.replace("seed", ""))
        m = json.loads(mp.read_text())
        row = {"dataset": dataset, "model": model, "seed": seed, "params": m["params"], "flops": m["flops"],
               "best_epoch": m["best_epoch"], "wall_sec": m["wall_sec"], "run_dir": str(seed_dir)}
        for split in ("val", "test", "ckplus"):
            if split in m:
                _flatten(f"{split}.", m[split], row)
        rows.append(row)
    return pd.DataFrame(rows)


def fmt(m, s, h, pct):
    if pct:
        return f"{100 * m:.2f} ± {100 * s:.2f} [±{100 * h:.2f}]"
    return f"{m:.4f} ± {s:.4f} [±{h:.4f}]"


def summary_table(df: pd.DataFrame, dataset: str) -> str:
    d = df[df.dataset == dataset]
    if d.empty:
        return ""
    cols = [c for c in KEY_METRICS if c in d and d[c].notna().any()]
    lines = [f"# {dataset}: mean ± std [95% CI half-width] over seeds", "",
             "| model | seeds | params (M) | MFLOPs | " + " | ".join(KEY_METRICS[c][0] for c in cols) + " |",
             "|---|---|---|---|" + "---|" * len(cols)]
    order = d.groupby("model")["test.acc"].mean().sort_values(ascending=False).index
    for model in order:
        g = d[d.model == model]
        cells = []
        for c in cols:
            x = g[c].dropna().to_numpy()
            pct = not c.endswith("ece")
            cells.append(fmt(*mean_ci(x), pct) if len(x) else "–")
        lines.append(f"| {model} | {len(g)} | {g.params.iloc[0] / 1e6:.3f} | {g.flops.iloc[0] / 1e6:.1f} | " + " | ".join(cells) + " |")
    lines += ["", "Values in % except ECE. CI: t-distribution over seeds.", ""]
    return "\n".join(lines)


def _correct(run_dir: Path, split: str):
    p = np.load(Path(run_dir) / "preds.npz")
    return p[f"{split}_logits"].argmax(1) == p[f"{split}_labels"]


def compare_table(df: pd.DataFrame, dataset: str, proposed: str) -> str:
    d = df[df.dataset == dataset]
    if proposed not in set(d.model):
        return ""
    P = d[d.model == proposed].set_index("seed").sort_index()
    others = [m for m in sorted(d.model.unique()) if m != proposed]
    lines = [f"# {dataset}: {proposed} vs each counterpart (seed-paired)", "",
             "Positive Δ favours the proposed model (for FNR/ECE the sign is flipped so that positive is still better).", ""]
    for c in [c for c in KEY_METRICS if c in d and d[c].notna().any()]:
        label, hib = KEY_METRICS[c]
        rows, pvals = [], []
        for o in others:
            O = d[d.model == o].set_index("seed").sort_index()
            seeds = sorted(set(P.index) & set(O.index))
            if len(seeds) < 2:
                continue
            a, b = P.loc[seeds, c].to_numpy(float), O.loc[seeds, c].to_numpy(float)
            if np.isnan(a).any() or np.isnan(b).any():
                continue
            if not hib:
                a, b = -a, -b
            r = paired_tests(a, b)
            rows.append((o, len(seeds), r))
            pvals.append(r["t_p"])
        if not rows:
            continue
        adj = holm(pvals)
        lines += [f"## {label} (`{c}`)", "",
                  "| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |", "|---|---|---|---|---|---|---|"]
        for (o, n, r), pa in zip(rows, adj):
            scale = 100 if not c.endswith("ece") else 1
            lines.append(f"| {o} | {n} | {scale * r['mean_diff']:+.2f} | {r['t_p']:.4f} | {pa:.4f} | "
                         f"{r['wilcoxon_p']:.4f} | {r['cohens_d']:.2f} |")
        lines.append("")
    # McNemar on per-sample test correctness, seed-matched
    lines += ["## McNemar (test set, per seed; n01 = proposed right & other wrong, n10 = reverse)", "",
              "| vs | seed | n01 | n10 | p |", "|---|---|---|---|---|"]
    for o in others:
        O = d[d.model == o].set_index("seed")
        for s in sorted(set(P.index) & set(O.index)):
            r = mcnemar(_correct(P.loc[s, "run_dir"], "test"), _correct(O.loc[s, "run_dir"], "test"))
            lines.append(f"| {o} | {s} | {r['n01']} | {r['n10']} | {r['p']:.4g} |")
    lines.append("")
    return "\n".join(lines)


def figures(df: pd.DataFrame, dataset: str, out: Path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    d = df[df.dataset == dataset]
    if d.empty:
        return
    models = d.groupby("model")["test.acc"].mean().sort_values(ascending=False).index.tolist()
    for c in ["test.acc", "test.macro_f1", "test.near_neutral_macro_f1", "test.fnr", "test.nn_subset_macro_f1@0.3", "ckplus.acc"]:
        if c not in d or d[c].isna().all():
            continue
        fig, ax = plt.subplots(figsize=(1.2 * len(models) + 2, 3.2))
        for i, m in enumerate(models):
            x = d[d.model == m][c].dropna().to_numpy()
            if not len(x):
                continue
            mu, _, h = mean_ci(x)
            ax.bar(i, mu, yerr=h, capsize=4, color="#9ecae1", edgecolor="#3182bd")
            ax.scatter(np.full(len(x), i) + np.linspace(-0.15, 0.15, len(x)), x, color="#08519c", s=14, zorder=3)
        ax.set_xticks(range(len(models)))
        ax.set_xticklabels(models, rotation=20, ha="right")
        ax.set_ylabel(KEY_METRICS[c][0])
        ax.set_title(f"{dataset}: {KEY_METRICS[c][0]} (mean ± 95% CI, dots = seeds)")
        fig.tight_layout()
        fig.savefig(out / f"fig_{dataset}_{c.replace('.', '_').replace('@', '')}.png", dpi=150)
        plt.close(fig)
    classes = CLASSES.get(dataset, RAFDB_CLASSES)
    for m in models:
        cms = []
        for rd in d[d.model == m].run_dir:
            met = json.loads((Path(rd) / "metrics.json").read_text())
            cms.append(np.array(met["test"]["confusion"], float))
        cm = np.mean(cms, 0)
        cm = cm / cm.sum(1, keepdims=True).clip(min=1)
        fig, ax = plt.subplots(figsize=(4.8, 4.2))
        im = ax.imshow(cm, cmap="Blues", vmin=0, vmax=1)
        ax.set_xticks(range(len(classes)))
        ax.set_yticks(range(len(classes)))
        ax.set_xticklabels(classes, rotation=45, ha="right")
        ax.set_yticklabels(classes)
        for i in range(len(classes)):
            for j in range(len(classes)):
                ax.text(j, i, f"{cm[i, j]:.2f}", ha="center", va="center", fontsize=7,
                        color="white" if cm[i, j] > 0.5 else "black")
        ax.set_xlabel("predicted")
        ax.set_ylabel("true")
        ax.set_title(f"{dataset} / {m} (mean over {len(cms)} seeds)")
        fig.colorbar(im, fraction=0.046)
        fig.tight_layout()
        fig.savefig(out / f"fig_{dataset}_{m}_confusion.png", dpi=150)
        plt.close(fig)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", default="runs")
    ap.add_argument("--out", default="results")
    ap.add_argument("--proposed", default="nnskd")
    ap.add_argument("--no-figures", action="store_true")
    a = ap.parse_args(argv)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    df = collect(Path(a.runs).expanduser())
    if df.empty:
        print("no runs found")
        return df
    df.to_csv(out / "runs_flat.csv", index=False)
    for ds in sorted(df.dataset.unique()):
        s = summary_table(df, ds)
        (out / f"summary_{ds}.md").write_text(s)
        print(s)
        c = compare_table(df, ds, a.proposed)
        if c:
            (out / f"compare_{ds}_{a.proposed}.md").write_text(c)
            print(c)
        if not a.no_figures:
            figures(df, ds, out)
    return df


if __name__ == "__main__":
    main()
