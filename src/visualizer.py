import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def _format_date_axis(ax):
    """
    Make date axis readable and non-clustered.
    """
    locator = mdates.AutoDateLocator()
    formatter = mdates.ConciseDateFormatter(locator)

    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)

    for label in ax.get_xticklabels():
        label.set_rotation(45)
        label.set_ha("right")


def plot_price_with_signals(df, ticker):
    df["Date"] = pd.to_datetime(df["Date"], utc=True).dt.tz_localize(None)


    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(df["Date"], df["Close"], label="Close Price")

    signal_points = df[df["RSI_SIGNAL"] == 1]
    ax.scatter(
        signal_points["Date"],
        signal_points["Close"],
        marker="^",
        label="RSI Buy Signal"
    )

    _format_date_axis(ax)

    ax.set_title(f"{ticker} Price with RSI Signals")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend()

    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    fig.autofmt_xdate()

    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/{ticker}_price_signals.png", dpi=150)
    plt.close()


def plot_strategy_vs_benchmark(df, ticker):
    df["Date"] = pd.to_datetime(df["Date"], utc=True).dt.tz_localize(None)


    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(df["Date"], df["Cumulative_Return"], label="RSI Strategy")
    ax.plot(df["Date"], df["BH_Cumulative_Return"], label="Buy and Hold")

    _format_date_axis(ax)

    ax.set_title(f"{ticker} Strategy vs Buy & Hold")
    ax.set_xlabel("Date")
    ax.set_ylabel("Cumulative Return")
    ax.legend()

    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    fig.autofmt_xdate()


    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/{ticker}_strategy_vs_bh.png", dpi=150)
    plt.close()


def plot_drawdown(df, ticker):
   df["Date"] = pd.to_datetime(df["Date"], utc=True).dt.tz_localize(None)


   cumulative = df["Cumulative_Return"] + 1
   rolling_max = cumulative.cummax()
   drawdown = (cumulative - rolling_max) / rolling_max

   fig, ax = plt.subplots(figsize=(12, 6))

   ax.plot(df["Date"], drawdown, label="Drawdown")

   _format_date_axis(ax)
 
   ax.set_title(f"{ticker} Strategy Drawdown")
   ax.set_xlabel("Date")
   ax.set_ylabel("Drawdown")
   ax.legend()

   ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
   ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
   fig.autofmt_xdate()


   plt.tight_layout()
   plt.savefig(f"{OUTPUT_DIR}/{ticker}_drawdown.png", dpi=150)
   plt.close()


def generate_visuals(ticker):
    df = pd.read_csv(f"data/processed/{ticker}_stock.csv")
    df["Date"] = pd.to_datetime(df["Date"], utc=True).dt.tz_localize(None)

    plot_price_with_signals(df, ticker)
    plot_strategy_vs_benchmark(df, ticker)
    plot_drawdown(df, ticker)

    print(f"Visuals generated for {ticker} saved in {OUTPUT_DIR}/")

