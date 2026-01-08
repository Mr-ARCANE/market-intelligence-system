import pandas as pd
import matplotlib.pyplot as plt
import os

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def plot_price_with_signals(df, ticker):
    plt.figure()
    plt.plot(df["Date"], df["Close"], label="Close Price")

    signal_points = df[df["RSI_SIGNAL"] == 1]
    plt.scatter(
        signal_points["Date"],
        signal_points["Close"],
        marker="^",
        label="RSI Buy Signal"
    )

    plt.title(f"{ticker} Price with RSI Signals")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.xticks(rotation=45)

    plt.savefig(
        f"{OUTPUT_DIR}/{ticker}_price_signals.png",
        dpi=150,
        bbox_inches="tight"
    )
    plt.close()


def plot_strategy_vs_benchmark(df, ticker):
    plt.figure()
    plt.plot(df["Date"], df["Cumulative_Return"], label="RSI Strategy")
    plt.plot(df["Date"], df["BH_Cumulative_Return"], label="Buy and Hold")

    plt.title(f"{ticker} Strategy vs Buy & Hold")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Return")
    plt.legend()
    plt.xticks(rotation=45)

    plt.savefig(
        f"{OUTPUT_DIR}/{ticker}_strategy_vs_bh.png",
        dpi=150,
        bbox_inches="tight"
    )
    plt.close()


def plot_drawdown(df, ticker):
    cumulative = df["Cumulative_Return"] + 1
    rolling_max = cumulative.cummax()
    drawdown = (cumulative - rolling_max) / rolling_max

    plt.figure()
    plt.plot(df["Date"], drawdown)

    plt.title(f"{ticker} Strategy Drawdown")
    plt.xlabel("Date")
    plt.ylabel("Drawdown")
    plt.xticks(rotation=45)

    plt.savefig(
        f"{OUTPUT_DIR}/{ticker}_drawdown.png",
        dpi=150,
        bbox_inches="tight"
    )
    plt.close()


def generate_visuals(ticker):
    df = pd.read_csv(f"data/processed/{ticker}_stock.csv")

    plot_price_with_signals(df, ticker)
    plot_strategy_vs_benchmark(df, ticker)
    plot_drawdown(df, ticker)

    print(f"Visuals generated for {ticker} saved in {OUTPUT_DIR}/")
