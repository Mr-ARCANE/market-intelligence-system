import pandas as pd
import numpy as np

def evaluate_signal(df: pd.DataFrame, signal_col: str, horizons=(5, 10, 20)):
    results = []

    for h in horizons:
        forward_return = df["Close"].shift(-h) / df["Close"] - 1
        signal_returns = forward_return[df[signal_col] == 1]

        results.append({
            "horizon_days": h,
            "num_signals": signal_returns.count(),
            "mean_return": signal_returns.mean(),
            "median_return": signal_returns.median(),
            "win_rate": (signal_returns > 0).mean()
        })

    return pd.DataFrame(results)

def benchmark_buy_and_hold(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["BH_Return"] = df["Close"].pct_change()
    df["BH_Cumulative_Return"] = (1 + df["BH_Return"]).cumprod() - 1
    return df

def compute_excess_return(df: pd.DataFrame) -> pd.DataFrame:
    """
    Strategy performance minus buy-and-hold performance.
    """
    df = df.copy()
    df["Excess_Return"] = df["Cumulative_Return"] - df["BH_Cumulative_Return"]
    return df


def compute_max_drawdown(series: pd.Series) -> float:
    """
    Maximum drawdown of a cumulative return series.
    """
    cumulative_max = series.cummax()
    drawdown = (series - cumulative_max) / cumulative_max
    return drawdown.min()

