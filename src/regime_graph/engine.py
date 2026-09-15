from __future__ import annotations
from pathlib import Path
from typing import Any
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def run(data, seed=42, output_dir=None):
    cols = [c for c in data.columns if c.startswith("r_") or c.startswith("x_")]
    R = data[cols].to_numpy(float)
    # rolling vol + spectral features
    win = 29
    feat = []
    for t in range(win, len(R)):
        w = R[t-win:t]
        vol = w.std()
        C = np.corrcoef(w.T); C = np.nan_to_num(C, nan=0.0)
        ev = np.sort(np.linalg.eigvalsh(C + 1e-6*np.eye(C.shape[0])))
        feat.append([vol, ev[-1], ev[0]])
    feat = np.asarray(feat)
    # 2-means style regimes
    center = feat.mean(axis=0)
    d0 = np.linalg.norm(feat - center*0.7, axis=1)
    d1 = np.linalg.norm(feat - center*1.3, axis=1)
    regime = (d1 < d0).astype(int)
    if output_dir is not None:
        output_dir = Path(output_dir)
        pd.DataFrame({"vol": feat[:,0], "regime": regime}).to_csv(output_dir/"series.csv", index=False)
        fig, ax = plt.subplots(figsize=(9,4)); ax.plot(feat[:,0]); ax.set_title("Cross-Asset Regime Graph")
        fig.tight_layout(); fig.savefig(output_dir/"diagnostic.png", dpi=120); plt.close(fig)
    return {"summary": {"family": "regime", "market": "Global", "stress_frac": float(regime.mean()), "mean_vol": float(feat[:,0].mean()), "window": win}}
