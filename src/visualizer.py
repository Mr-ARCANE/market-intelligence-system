import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_visuals(ticker):
    # Load processed data for ticker
    path = f"data/processed/{ticker}_stock.csv"
    if not os.path.exists(path):
        print(f"No processed data found for {ticker}")
        return

    df = pd.read_csv(path)

    # Ensure plots directory exists
    os.makedirs("data/plots", exist_ok=True)

    # 1. Price Chart
    plt.figure(figsize=(12, 6))
    plt.plot(df["Date"], df["Close"], label="Close Price")
    plt.title(f"{ticker} Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"data/plots/{ticker}_price.png")
    plt.close()

    # 2. RSI
    if "RSI" in df.columns:
        plt.figure(figsize=(12, 4))
        plt.plot(df["Date"], df["RSI"], label="RSI")
        plt.axhline(70, color="red", linestyle="--")
        plt.axhline(30, color="green", linestyle="--")
        plt.title(f"{ticker} RSI")
        plt.xlabel("Date")
        plt.ylabel("RSI")
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f"data/plots/{ticker}_RSI.png")
        plt.close()

    # 3. MACD
    if "MACD" in df.columns and "Signal" in df.columns:
        plt.figure(figsize=(12, 4))
        plt.plot(df["Date"], df["MACD"], label="MACD")
        plt.plot(df["Date"], df["Signal"], label="Signal")
        plt.title(f"{ticker} MACD")
        plt.xlabel("Date")
        plt.ylabel("Value")
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f"data/plots/{ticker}_MACD.png")
        plt.close()

    print(f"Visuals generated for {ticker} saved in data/plots/")
