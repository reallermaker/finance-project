from __future__ import annotations
import numpy as np
import pandas as pd

def generate_sample(seed=42, n=500):
    rng = np.random.default_rng(seed)
    regime = np.zeros(n, dtype=int)
    for t in range(1, n):
        psw = 0.02 if regime[t - 1] == 0 else 0.05
        regime[t] = regime[t - 1] if rng.random() > psw else 1 - regime[t - 1]
    return pd.DataFrame({
        "date": pd.date_range("2020-01-01", periods=n, freq="B"),
        "bid_ask_bps": 8 + 4 * regime + rng.gamma(2, 1.5, n),
        "funding_spread_bps": 20 + 15 * regime + rng.normal(0, 5, n),
        "depth": np.exp(rng.normal(4.5 - 0.4 * regime, 0.2, n)),
        "regime": regime,
    })
