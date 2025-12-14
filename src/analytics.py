import pandas as pd
import numpy as np

def compute_returns(df: pd.DataFrame) -> pd.DataFrame:
    df["Return"] = df["Close"].pct_change()
    df["Cumulative_Return"] = (1 + df["Return"]).cumprod() - 1
    return df

def compute_moving_averages(df: pd.DataFrame) -> pd.DataFrame:
    df["MA20"] = df["Close"].rolling(20).mean()
    df["MA50"] = df["Close"].rolling(50).mean()
    return df

def compute_volatility(df: pd.DataFrame) -> pd.DataFrame:
    df["Volatility20"] = df["Return"].rolling(20).std() * np.sqrt(252)
    return df

def compute_rsi(df: pd.DataFrame, period: int = 14) -> pd.DataFrame:
    delta = df["Close"].diff()
    gain = (delta.where(delta > 0, 0)).rolling(period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(period).mean()
    rs = gain / loss
    df["RSI"] = 100 - (100 / (1 + rs))
    return df

def compute_macd(df: pd.DataFrame) -> pd.DataFrame:
    ema12 = df["Close"].ewm(span=12, adjust=False).mean()
    ema26 = df["Close"].ewm(span=26, adjust=False).mean()
    df["MACD"] = ema12 - ema26
    df["Signal"] = df["MACD"].ewm(span=9, adjust=False).mean()
    return df

def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    # Ensure at least 60 rows to avoid broken indicators
    if len(df) < 60:
        df = df.copy()
        df["Return"] = None
        df["Cumulative_Return"] = None
        df["MA20"] = None
        df["MA50"] = None
        df["Volatility20"] = None
        df["RSI"] = None
        df["MACD"] = None
        df["Signal"] = None
        return df

    df = compute_returns(df)
    df = compute_moving_averages(df)
    df = compute_volatility(df)
    df = compute_rsi(df)
    df = compute_macd(df)
    return df
