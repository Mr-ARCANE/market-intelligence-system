import pandas as pd
from src.analytics import add_rsi_signal
from src.backtester import evaluate_signal
from src.metrics import evaluate_performance


def rsi_parameter_sweep(df, thresholds=(20, 25, 30, 35, 40)):
    results = []

    for t in thresholds:
        df_test = add_rsi_signal(df, threshold=t)

        metrics = evaluate_performance(df_test)
        metrics["rsi_threshold"] = t

        results.append(metrics)

    return pd.concat(results, ignore_index=True)
