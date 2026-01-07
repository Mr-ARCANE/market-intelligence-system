import pandas as pd
import numpy as np


TRADING_DAYS = 252


def compute_cagr(cumulative_return, periods):
    return (1 + cumulative_return) ** (TRADING_DAYS / periods) - 1


def compute_volatility(returns):
    return returns.std() * np.sqrt(TRADING_DAYS)


def compute_sharpe(returns, risk_free_rate=0.0):
    excess = returns - risk_free_rate / TRADING_DAYS
    return excess.mean() / excess.std() * np.sqrt(TRADING_DAYS)


def compute_max_drawdown(cumulative_returns):
    cumulative = cumulative_returns + 1
    rolling_max = cumulative.cummax()
    drawdown = (cumulative - rolling_max) / rolling_max
    return drawdown.min()


def evaluate_performance(df):
    df = df.dropna().copy()
    periods = len(df)

    metrics = {}

    # Strategy metrics
    metrics["strategy_cagr"] = compute_cagr(
        df["Cumulative_Return"].iloc[-1],
        periods
    )
    metrics["strategy_volatility"] = compute_volatility(df["Return"])
    metrics["strategy_sharpe"] = compute_sharpe(df["Return"])
    metrics["strategy_max_drawdown"] = compute_max_drawdown(
        df["Cumulative_Return"]
    )

    # Buy & hold metrics
    metrics["bh_cagr"] = compute_cagr(
        df["BH_Cumulative_Return"].iloc[-1],
        periods
    )
    metrics["bh_volatility"] = compute_volatility(df["BH_Return"])
    metrics["bh_sharpe"] = compute_sharpe(df["BH_Return"])
    metrics["bh_max_drawdown"] = compute_max_drawdown(
        df["BH_Cumulative_Return"]
    )

    return pd.DataFrame([metrics])
