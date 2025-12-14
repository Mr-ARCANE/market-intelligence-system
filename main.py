from src.data_fetcher import fetch_stock_data
from src.data_cleaner import clean_data
from src.analytics import add_indicators
from src.visualizer import generate_visuals
import os

def main():
    tickers = ["AAPL", "MSFT", "GOOGL"]

    for ticker in tickers:
        print(f"Fetching data for {ticker}")
        df = fetch_stock_data(ticker, period="6mo")

        print(f"Cleaning data for {ticker}")
        df = clean_data(df)

        print(f"Adding indicators for {ticker}")
        df = add_indicators(df)

        os.makedirs("data/processed", exist_ok=True)

        save_path = f"data/processed/{ticker}_stock.csv"
        df.to_csv(save_path, index=False)
        print(f"{ticker} saved to {save_path}")

        print(f"Generating visuals for {ticker}")
        generate_visuals(ticker)

    print("\nAll tasks completed successfully.")

if __name__ == "__main__":
    main()
