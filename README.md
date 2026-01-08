# Market Intelligence System

A modular Python framework for researching, evaluating, and benchmarking
rule-based quantitative trading strategies using historical equity data.

The project focuses on **signal generation**, **backtesting**, **benchmark comparison**,
**risk metrics**, and **parameter experimentation** in a clean, reproducible pipeline.

This is a research and analysis system, not a production trading engine.

---

## What This Project Does

This system answers a simple but important question:

> Does a given technical signal outperform buy-and-hold, and under what conditions?

It allows you to:
- Fetch historical equity price data
- Generate technical indicators and trading signals
- Backtest strategies across multiple forward horizons
- Benchmark performance against buy-and-hold
- Compute basic risk and performance metrics
- Visualize strategy behavior and drawdowns
- Run parameter sweeps to test signal sensitivity

## Core Features

### 1. Data Pipeline
- Historical equity data fetched via `yfinance`
- Cleaning and formatting into consistent OHLC structure
- Automatic directory creation for reproducibility

### 2. Indicators and Signals
Implemented indicators:
- Daily returns
- Cumulative returns
- Moving averages (MA20, MA50)
- Volatility (annualized)
- RSI
- MACD

Signal logic:
- RSI-based long signal when RSI falls below a configurable threshold

### 3. Backtesting
- Forward return evaluation over multiple horizons (5, 10, 20 days)
- Signal-level performance statistics:
  - Mean return
  - Median return
  - Win rate
  - Number of signals

### 4. Benchmarking
- Buy-and-hold daily and cumulative returns
- Direct comparison between strategy and benchmark
- Excess return calculation

### 5. Risk and Performance Metrics
- Volatility
- Maximum drawdown
- Strategy vs benchmark comparison metrics

### 6. Parameter Experiments
- RSI threshold sweep
- Sensitivity analysis of signal performance

### 7. Visualization
Automatically generated plots:
- Price series with RSI buy signals
- Strategy vs buy-and-hold cumulative returns
- Strategy drawdown over time

## Core Features

### 1. Data Pipeline
- Historical equity data fetched via `yfinance`
- Cleaning and formatting into consistent OHLC structure
- Automatic directory creation for reproducibility

### 2. Indicators and Signals
Implemented indicators:
- Daily returns
- Cumulative returns
- Moving averages (MA20, MA50)
- Volatility (annualized)
- RSI
- MACD

Signal logic:
- RSI-based long signal when RSI falls below a configurable threshold

### 3. Backtesting
- Forward return evaluation over multiple horizons (5, 10, 20 days)
- Signal-level performance statistics:
  - Mean return
  - Median return
  - Win rate
  - Number of signals

### 4. Benchmarking
- Buy-and-hold daily and cumulative returns
- Direct comparison between strategy and benchmark
- Excess return calculation

### 5. Risk and Performance Metrics
- Volatility
- Maximum drawdown
- Strategy vs benchmark comparison metrics

### 6. Parameter Experiments
- RSI threshold sweep
- Sensitivity analysis of signal performance

### 7. Visualization
Automatically generated plots:
- Price series with RSI buy signals
- Strategy vs buy-and-hold cumulative returns
- Strategy drawdown over time

## Core Features

### 1. Data Pipeline
- Historical equity data fetched via `yfinance`
- Cleaning and formatting into consistent OHLC structure
- Automatic directory creation for reproducibility

### 2. Indicators and Signals
Implemented indicators:
- Daily returns
- Cumulative returns
- Moving averages (MA20, MA50)
- Volatility (annualized)
- RSI
- MACD

Signal logic:
- RSI-based long signal when RSI falls below a configurable threshold

### 3. Backtesting
- Forward return evaluation over multiple horizons (5, 10, 20 days)
- Signal-level performance statistics:
  - Mean return
  - Median return
  - Win rate
  - Number of signals

### 4. Benchmarking
- Buy-and-hold daily and cumulative returns
- Direct comparison between strategy and benchmark
- Excess return calculation

### 5. Risk and Performance Metrics
- Volatility
- Maximum drawdown
- Strategy vs benchmark comparison metrics

### 6. Parameter Experiments
- RSI threshold sweep
- Sensitivity analysis of signal performance

### 7. Visualization
Automatically generated plots:
- Price series with RSI buy signals
- Strategy vs buy-and-hold cumulative returns
- Strategy drawdown over time

All plots are saved to the `outputs/` directory.


---
## Project Structure

```text
market-intelligence-system/
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── analytics.py        # Indicators and signal logic
│   ├── backtester.py       # Strategy and benchmark evaluation
│   ├── metrics.py          # Risk and performance metrics
│   ├── visualizer.py       # Plots and visual analysis
│   └── experiments.py      # Parameter sweeps
│
├── main.py                 # End-to-end execution pipeline
├── requirements.txt
└── README.md
```

---

## Example Outputs (AAPL)

The following plots illustrate the full pipeline output using AAPL as a representative example.
The same analysis is automatically generated for MSFT and GOOGL.

### Price with RSI Buy Signals
![AAPL RSI Signals](outputs/AAPL_price_signals.png)

### Strategy vs Buy-and-Hold
![AAPL Strategy vs BH](outputs/AAPL_strategy_vs_bh.png)

### Strategy Drawdown
![AAPL Drawdown](outputs/AAPL_drawdown.png)

<sub>Identical outputs are generated for MSFT and GOOGL.</sub>

---
## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the pipeline:

```bash
python main.py
```
---
## Outputs Generated
Running main.py produces the following artifacts:

-Cleaned and enriched datasets
data/processed/*_stock.csv

-Backtest summaries
data/processed/*_rsi_backtest.csv

-Performance metrics
data/processed/*_performance_metrics.csv

-Parameter sweep results
data/processed/*_rsi_parameter_sweep.csv

-Strategy visualizations (PNG files)
outputs/

All outputs are fully reproducible from a clean clone of the repository.

---
## Design Principles

-Modular, readable, and testable code

-Clear separation of concerns across pipeline stages

-No hidden state or manual intervention

-Explicit assumptions and transparent logic

-Research-first design, not production trading code

---

## Limitations

This project intentionally makes simplifying assumptions:

- Long-only stratergies

- No explict exit rules

- No transaction costs or slippage

- No position sizing or porfolio optimization

- Single-assest evaluation per run

Results should be interpreted as research signals, not trading recommendations

---

## Intened Audience

This projects is suitable for:

- Data Analyst and quantitative analyst porfolios

- Strategy evaluation case studies

- Interview discussions on backtesting methodolgy and limitations

- Demonstrations of modular data engineering and research workfolws

It is not intened for live trading or financial decision- making

---
## Disclaimer 

This project is designed for research and educational purposes only.  
It is not financial advice.

---
