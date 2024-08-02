"""
Thank you to Tobias Rodriguez del Pozo for his assistance in writing this code.
"""
import pandas as pd
import numpy as np
import config

OUTPUT_DIR = config.OUTPUT_DIR
DATA_DIR = config.DATA_DIR

import misc_tools
import load_CRSP_stock
import load_CRSP_Compustat


def calc_equal_weighted_index(df):
    """
    Calculate equal weighted index (just the average of all stocks)
    Note that ret is raw and retx is adjusted for dividends.
    """
    df_eq_idx = pd.concat(
        [
            df.groupby("date")["ret"].mean(),
            df.groupby("date")["retx"].mean(),
            df.groupby("date")["permno"].count(),
        ],
        axis=1,
    )
    df_eq_idx = df_eq_idx.rename(
        columns={
            "ret": "ewretd",
            "retx": "ewretx",
            "permno": "totcnt",
        }
    )
    df_eq_idx = df_eq_idx.dropna(how="all")
    return df_eq_idx


def calc_CRSP_value_weighted_index(df):
    """
    The formula is:
    $$
    r_t = \\frac{\\sum_{i=1}^{N_t} w_{i,t-1} r_{i,t}}{\\sum_{i=1}^{N_t} w_{i,t-1}}
    $$
    That is, the return of the index is the weighted average of the returns, where
    the weights are the market cap of the stock at the end of the previous month.
    """
    _df = df.copy()
    _df["mktcap"] = _df["shrout"] * _df["altprc"]

    # Create L1_mktcap column
    _df = misc_tools.with_lagged_columns(
        df=_df,
        column_to_lag="mktcap",
        id_column="permno",
        date_col="date",
        lags=1,
        freq="BME",
    )
    _df["weight"] = _df["L1_mktcap"]
    _df["weight_ret"] = _df["weight"] * _df["ret"]
    _df["weight_retx"] = _df["weight"] * _df["retx"]

    weight = _df.groupby("date")["weight"].sum()
    ret = _df.groupby("date")["weight_ret"].sum() / weight
    retx = _df.groupby("date")["weight_retx"].sum() / weight
    mkt_cap = _df.groupby("date")["mktcap"].sum()

    df_vw_idx = pd.concat(
        {
            "vwretd": ret,
            "vwretx": retx,
            "totval": mkt_cap,
        },
        axis=1,
    )
    df_vw_idx.iloc[0, :] = np.nan
    df_vw_idx = df_vw_idx.dropna(how="all")
    return df_vw_idx


def calc_CRSP_indices_merge(df_msf, df_msix):
    # Merge everything with appropriate suffixes
    df_vw_idx = calc_CRSP_value_weighted_index(df_msf)
    df_eq_idx = calc_equal_weighted_index(df_msf)
    df_msix = df_msix.rename(columns={"caldt": "date"})

    df = df_msix.merge(
        df_vw_idx.reset_index(),
        on="date",
        how="inner",
        suffixes=("", "_manual"),
    )
    df = df.merge(
        df_eq_idx.reset_index(),
        on="date",
        suffixes=("", "_manual"),
    )
    df = df.set_index("date")
    return df


def _demo():
    df_msf = load_CRSP_stock.load_CRSP_monthly_file(data_dir=DATA_DIR)
    df_msix = load_CRSP_stock.load_CRSP_index_files(data_dir=DATA_DIR)

    df_eq_idx = calc_equal_weighted_index(df_msf)
    df_vw_idx = calc_CRSP_value_weighted_index(df_msf)
    df_idxs = calc_CRSP_indices_merge(df_msf, df_msix)
    df_idxs.head()


if __name__ == "__main__":
    pass
