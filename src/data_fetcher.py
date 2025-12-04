import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker: str, period: str = "1y") -> pd.DataFrame:
    """
    Fetch historical stock data for a given ticker.
    """
    stock = yf.Ticker(ticker)
    df = stock.history(period=period)
    df.reset_index(inplace=True)
    return df
