import numpy as np
import pandas as pd

import config
DATA_DIR = config.DATA_DIR

filepath = DATA_DIR / "CRSP_example.csv"
df = pd.read_csv(filepath, parse_dates=["date"])
df.info()

df.head()


(
    df
    .loc[df["PERMNO"] == 10026, ["date", "PRC"]]
    .set_index("date")
    .plot()
)


(
    df
    .loc[df["PERMNO"] == 10026, ["date", "vwretd"]]
    .set_index("date")
    .plot()
)


(
    df
    .loc[df["PERMNO"] == 10026, ["date", "vwretd"]]
    .set_index("date")
    .cumsum()
    .plot()
)
