from __future__ import annotations
from pathlib import Path
from typing import Any
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def _simulate(df, seed):
    rng = np.random.default_rng(seed)
    n = len(df)
    stress = np.zeros(n)
    spread = df["bid_ask_bps"].to_numpy(float).copy()
    funding = df["funding_spread_bps"].to_numpy(float).copy()
    depth = df["depth"].to_numpy(float).copy()
    regime = df["regime"].to_numpy(int)
    for t in range(1, n):
        phi = 0.85 if regime[t] == 0 else 0.95
        innov = rng.normal(0, 0.05 if regime[t] == 0 else 0.12)
        stress[t] = np.clip(phi * stress[t-1] + 0.15 * (spread[t-1] / 50) + 0.1 * (funding[t-1] / 100) + innov, 0, 5)
        spread[t] = spread[t] * (1 + 0.08 * stress[t]) + 2.0 * stress[t]
        funding[t] = funding[t] * (1 + 0.1 * stress[t]) + 3.0 * stress[t]
        depth[t] = depth[t] / (1 + 0.25 * stress[t])
    out = df.copy()
    out["stress"] = stress
    out["spread_stressed_bps"] = spread
    out["funding_stressed_bps"] = funding
    out["depth_stressed"] = depth
    return out

def run(data, seed=42, output_dir=None):
    path = _simulate(data, seed)
    scenarios = {}
    for name, shock in {"mild": 25.0, "severe": 80.0, "extreme": 150.0}.items():
        base = data.copy()
        mid = len(base) // 2
        base.loc[base.index[mid]:, "funding_spread_bps"] += shock
        sim = _simulate(base, seed + int(shock))
        scenarios[name] = {
            "max_stress": float(sim["stress"].max()),
            "max_spread_bps": float(sim["spread_stressed_bps"].max()),
            "min_depth": float(sim["depth_stressed"].min()),
        }
    if output_dir is not None:
        output_dir = Path(output_dir)
        path.to_csv(output_dir / "stress_path.csv", index=False)
        fig, ax = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
        ax[0].plot(path["stress"]); ax[0].set_ylabel("stress")
        ax[1].plot(path["spread_stressed_bps"]); ax[1].set_ylabel("spread")
        ax[2].plot(path["depth_stressed"]); ax[2].set_ylabel("depth")
        fig.tight_layout(); fig.savefig(output_dir / "stress_path.png", dpi=120); plt.close(fig)
    return {"summary": {"baseline_max_stress": float(path["stress"].max()), "scenarios": scenarios, "note": "synthetic feedback"}}
