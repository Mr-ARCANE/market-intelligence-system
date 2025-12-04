import pandas as pd
import os

def clean_stock_data(file_path: str) -> pd.DataFrame:
    """
    Clean and preprocess stock CSV data.
    
    Steps:
    - Remove rows with missing values
    - Ensure Date column is datetime
    - Reset index
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist.")

    df = pd.read_csv(file_path)

    # Convert 'Date' to datetime
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
    
    # Drop rows with missing values
    df.dropna(inplace=True)
    
    # Reset index
    df.reset_index(drop=True, inplace=True)

    return df
