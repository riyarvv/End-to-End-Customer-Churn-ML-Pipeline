import pandas as pd


def load_data(file_path):
    """
    Load CSV data.

    Automatically returns

    • DataFrame for multi-column files

    • Series for single-column files
    """

    df=pd.read_csv(file_path)

    if df.shape[1]==1:

        return df.squeeze()

    return df