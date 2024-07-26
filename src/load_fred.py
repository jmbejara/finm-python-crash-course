import pandas as pd
import pandas_datareader
import config
from pathlib import Path

DATA_DIR = Path(config.DATA_DIR)
START_DATE = config.START_DATE
END_DATE = config.END_DATE

def pull_fred(
    start="1913-01-01",
    end="2023-10-01",
):
    """
    Pull data from FRED
    """
    # Load CPI, nominal GDP, and real GDP data from FRED, seasonally adjusted
    df = pandas_datareader.get_data_fred(
        ["CPIAUCNS", "GDP", "GDPC1"], start=start, end=end
    )
    return df


def load_fred(data_dir=DATA_DIR):
    """
    Must first run this module as main to pull and save data.
    """
    file_path = Path(data_dir) / "pulled" / "fred.parquet"
    df = pd.read_parquet(file_path)
    # df = pd.read_csv(file_path, parse_dates=["DATE"])
    # df = df.set_index("DATE")
    return df


def demo():
    df = load_fred()


if __name__ == "__main__":
    dirpath = Path(config.DATA_DIR) / "pulled"
    dirpath.mkdir(exist_ok=True)
    df = pull_fred(start=START_DATE, end=END_DATE)
    
    file_path = dirpath / "fred.parquet"
    df.to_parquet(file_path)
    
    file_path = dirpath / "fred.csv"
    df.to_csv(file_path)
