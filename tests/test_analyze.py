import json

import numpy as np
import pandas as pd

from analysis.analyze import collect, compare_table, main, summary_table


def _fake_run(root, dataset, model, seed, acc, C=7):
    d = root / dataset / model / f"seed{seed}"
    d.mkdir(parents=True)
    n = 40
    labels = np.arange(n) % C
    preds = labels.copy()
    wrong = np.arange(int(round(n * (1 - acc))))
    preds[wrong] = (labels[wrong] + 1) % C
    logits = np.zeros((n, C), np.float32)
    logits[np.arange(n), preds] = 5
    np.savez(d / "preds.npz", test_logits=logits, test_labels=labels)
    met = {"val": {"acc": acc}, "test": {"acc": acc, "macro_f1": acc - 0.01, "fnr": 1 - acc, "ece": 0.05,
                                        "near_neutral_macro_f1": acc - 0.02, "neutral_recall": acc, "neutral_f1": acc,
                                        "confusion": np.eye(C).tolist()},
           "best_epoch": 3, "params": 1000, "flops": 2000, "wall_sec": 1.0, "env": {}}
    (d / "metrics.json").write_text(json.dumps(met))


def test_collect_summary_compare(tmp_path):
    runs = tmp_path / "runs"
    for s, acc in enumerate([0.80, 0.82, 0.81]):
        _fake_run(runs, "rafdb", "nnskd", s, acc)
    for s, acc in enumerate([0.70, 0.71, 0.72]):
        _fake_run(runs, "rafdb", "base", s, acc)
    df = collect(runs)
    assert len(df) == 6 and set(df.model) == {"nnskd", "base"}
    s = summary_table(df, "rafdb")
    assert "| nnskd | 3 |" in s and "81.00 ± 1.00" in s
    c = compare_table(df, "rafdb", "nnskd")
    assert "| base | 3 | +10.00 |" in c and "McNemar" in c
    out = main(["--runs", str(runs), "--out", str(tmp_path / "res"), "--proposed", "nnskd"])
    assert (tmp_path / "res" / "summary_rafdb.md").exists()
    assert (tmp_path / "res" / "compare_rafdb_nnskd.md").exists()
    assert (tmp_path / "res" / "fig_rafdb_test_acc.png").exists()
    assert (tmp_path / "res" / "fig_rafdb_nnskd_confusion.png").exists()
    assert isinstance(out, pd.DataFrame)
