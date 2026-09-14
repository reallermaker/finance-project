# Adaptive Liquidity Stress Engine

Regime-switching liquidity stress with funding–market feedback spirals.

## Why This Project Exists

Liquidity stress is often measured statically; real stress feeds on itself through funding and market channels.

## Problem Definition

Build a reproducible analytical engine that addresses: **Regime-switching liquidity stress with funding–market feedback spirals.**

Market focus: **Global** | Complexity: **Flagship** | Domain: **Risk / Liquidity**

## Key Idea

Couple a hidden liquidity-stress state with endogenous feedback into spreads, depth, and funding spreads, then run adaptive stress scenarios.

## Financial / Mathematical Foundation

Core methods: Regime-switching state-space, stress scenario generation, feedback loops.

Implementations use synthetic data with explicit causal timing where market features are involved, to avoid look-ahead bias. Model outputs include uncertainty or scenario dispersion where relevant rather than single-point pretence.

## Architecture

```
src/liquidity_stress/
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
cd 01-adaptive-liquidity-stress-engine
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
liquidity_stress --output outputs
```

Or without install:

```bash
PYTHONPATH=src python3 -m liquidity_stress.cli --output outputs
```

## Example

```bash
PYTHONPATH=src python3 -m liquidity_stress.cli --seed 7 --output outputs
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
