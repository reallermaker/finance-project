from __future__ import annotations
import numpy as np
import pandas as pd

def generate_sample(seed=42, n=500, n_assets=6):
    rng = np.random.default_rng(seed)
    regime = np.zeros(n, dtype=int)
    for t in range(1,n):
        regime[t] = regime[t-1] if rng.random()>0.04 else 1-regime[t-1]
    out = {"date": pd.date_range("2020-01-01", periods=n, freq="B")}
    for i in range(n_assets):
        sig = np.where(regime==1, 0.02, 0.008)
        out[f"r_{i}"] = rng.normal(0, 1, n)*sig
    out["true_regime"] = regime
    return pd.DataFrame(out)
