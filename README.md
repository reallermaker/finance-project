# Cross-Asset Regime Graph

Infer multi-asset regimes from lead-lag and correlation graph structure.

## Why This Project Exists

Univariate HMMs miss how regime shifts propagate across an asset network.

## Problem Definition

Build a reproducible analytical engine that addresses: **Infer multi-asset regimes from lead-lag and correlation graph structure.**

Market focus: **Global** | Complexity: **Flagship** | Domain: **Quant Investment**

## Key Idea

Build a rolling cross-asset graph and cluster spectral features jointly with an HMM on graph embeddings.

## Financial / Mathematical Foundation

Core methods: Spectral clustering, rolling correlation/lead-lag graphs, HMM.

Implementations use synthetic data with explicit causal timing where market features are involved, to avoid look-ahead bias. Model outputs include uncertainty or scenario dispersion where relevant rather than single-point pretence.

## Architecture

```
src/regime_graph/
  __init__.py
  data.py
  engine.py
  cli.py
configs/default.json
data/README.md
outputs/
```

## Methodology

1. Generate or load sample inputs (`data.generate_sample`).
2. Run the core engine (`engine.run`).
3. Write `outputs/summary.json` and any figures/CSV artifacts.

## Data

Synthetic by default. See `data/README.md` for replacement guidance.

## Usage

```bash
cd 02-cross-asset-regime-graph
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
regime_graph --output outputs
```

Or without install:

```bash
PYTHONPATH=src python3 -m regime_graph.cli --output outputs
```

## Example

```bash
PYTHONPATH=src python3 -m regime_graph.cli --seed 7 --output outputs
```

## Outputs

- `outputs/summary.json` — key metrics and scenario summaries
- Additional CSV/PNG artifacts when the engine produces paths or curves

## Interpretation

Read metrics as research diagnostics on synthetic or user-supplied data. Compare scenarios and uncertainty bands; do not treat point estimates as tradable signals.

## Limitations

- Synthetic defaults are for methodology demonstration
- Market microstructure and EM features are stylized
- No claim of live trading performance

## Potential Extensions

- Plug in proprietary datasets through the data adapters
- Richer calibration and parameter uncertainty
- Portfolio-level integration with related projects in this collection

## Disclaimer

This project is intended for research and educational purposes and does not constitute financial or investment advice.

## Copyright

Copyright © 2026 reallermaker. All Rights Reserved.
