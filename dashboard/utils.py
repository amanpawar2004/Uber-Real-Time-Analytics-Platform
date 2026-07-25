import pandas as pd

def load_data(path):

    df = pd.read_csv(path)

    df.columns = df.columns.str.strip()

    df["fare"] = pd.to_numeric(
        df["fare"],
        errors="coerce"
    )

    df = df.dropna(subset=["fare"])

    return df