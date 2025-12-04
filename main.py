import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from data_fetcher import fetch_stock_data
from data_cleaner import clean_stock_data

def main():
    tickers = ["AAPL", "MSFT", "GOOGL"]
    
    for ticker in tickers:
        print(f"Fetching data for {ticker}...")
        df = fetch_stock_data(ticker, period="6mo")
        
        # Save raw data
        raw_file = f"data/processed/{ticker}_raw.csv"
        df.to_csv(raw_file, index=False)
        print(f"{ticker} raw data saved!")
        
        # Clean the data
        df_clean = clean_stock_data(raw_file)
        clean_file = f"data/processed/{ticker}_clean.csv"
        df_clean.to_csv(clean_file, index=False)
        print(f"{ticker} cleaned data saved!")

if __name__ == "__main__":
    main()
