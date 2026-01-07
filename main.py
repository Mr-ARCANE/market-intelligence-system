from src.data_fetcher import fetch_stock_data
from src.data_cleaner import clean_data
from src.analytics import add_indicators, add_rsi_signal
from src.backtester import evaluate_signal, benchmark_buy_and_hold
from src.visualizer import generate_visuals
from src.metrics import evaluate_performance
from src.experiments import rsi_parameter_sweep
import os


def main():
    tickers = ["AAPL", "MSFT", "GOOGL"]

    for ticker in tickers:
        print(f"Fetching data for {ticker}")
        df = fetch_stock_data(ticker)

        print(f"Cleaning data for {ticker}")
        df = clean_data(df)

        print(f"Adding indicators for {ticker}")
        df = add_indicators(df)

        print(f"Adding RSI signal for {ticker}")
        df = add_rsi_signal(df)

        print(f"Adding buy-and-hold benchmark for{ticker}")
        df = benchmark_buy_and_hold(df)
        df.to_csv(f"data/processed/{ticker}_strategy_vs_benchmark.csv", index=False)

        # Ensure processed folder exists
        os.makedirs("data/processed", exist_ok=True)

        save_path = f"data/processed/{ticker}_stock.csv"
        df.to_csv(save_path, index=False)
        print(f"{ticker} saved to {save_path}")

      
        print(f"Backtesting RSI strategy for {ticker}")
        results = evaluate_signal(df, "RSI_SIGNAL")
        results_path = f"data/processed/{ticker}_rsi_backtest.csv"
        results.to_csv(results_path, index=False)
        print(f"Backtest saved to {results_path}")
       
        print(f"Evaluating performance for {ticker}")
        metrics = evaluate_performance(df)
        metrics_path = f"data/processed/{ticker}_performance_metrics.csv"
        metrics.to_csv(metrics_path, index=False)
        print(f"Metrics saved to {metrics_path}")

        print(f"Running RSI parameter sweep for {ticker}")
        sweep_results = rsi_parameter_sweep(df)
        sweep_path = f"data/processed/{ticker}_rsi_parameter_sweep.csv"
        sweep_results.to_csv(sweep_path, index=False)
        print(f"RSI sweep results saved to {sweep_path}")
 

        print(f"Generating visuals for {ticker}")
        generate_visuals(ticker)

    print("\nAll tasks completed successfully.")


if __name__ == "__main__":
    main()
