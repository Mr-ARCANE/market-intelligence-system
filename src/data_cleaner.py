import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # drop rows with missing values in critical columns
    df = df.dropna(subset=["Open", "High", "Low", "Close"])

    # drop duplicates if any
    df = df.drop_duplicates()

    # ensure sorted by date
    df = df.sort_values("Date")

    # reset index
    df = df.reset_index(drop=True)

    return df
