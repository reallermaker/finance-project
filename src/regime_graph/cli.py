"""Command-line entry point for Cross-Asset Regime Graph."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from regime_graph import __version__
from regime_graph.data import generate_sample
from regime_graph.engine import run


def main(argv=None):
    parser = argparse.ArgumentParser(description='Infer multi-asset regimes from lead-lag and correlation graph structure.')
    parser.add_argument('--output', type=Path, default=Path('outputs'))
    parser.add_argument('--seed', type=int, default=42)
    args = parser.parse_args(argv)
    args.output.mkdir(parents=True, exist_ok=True)
    data = generate_sample(seed=args.seed)
    result = run(data, seed=args.seed, output_dir=args.output)
    summary = result.get('summary', result)
    path = args.output / 'summary.json'
    path.write_text(json.dumps(summary, indent=2, default=str), encoding='utf-8')
    print('Cross-Asset Regime Graph v' + __version__)
    print('Wrote ' + str(path))
    for key, value in summary.items():
        if not isinstance(value, (dict, list)):
            print('  %s: %s' % (key, value))


if __name__ == '__main__':
    main()
