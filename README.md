# Market Intelligence System

A modular Python framework for researching, evaluating, and benchmarking quantitative trading strategies using historical equity data.

The system focuses on signal generation, backtesting, performance evaluation, and parameter experimentation in a clean, reproducible pipeline.

---

## Project Structure

market-intelligence-system/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── analytics.py        # Indicators and signal logic
│   ├── backtester.py       # Strategy and benchmark evaluation
│   ├── metrics.py          # Risk and performance metrics
│   ├── visualizer.py       # Plots and visual analysis
│   └── experiments.py     # Parameter sweeps and experiments
├── main.py                 # End-to-end execution pipeline
├── requirements.txt
└── README.md

---

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
