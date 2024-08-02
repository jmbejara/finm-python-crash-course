"""
Functions to pull and calculate the value and equal weighted CRSP indices.

 - Data for indices: https://wrds-www.wharton.upenn.edu/data-dictionary/crsp_a_indexes/
 - Data for raw stock data: https://wrds-www.wharton.upenn.edu/pages/get-data/center-research-security-prices-crsp/annual-update/stock-security-files/monthly-stock-file/
 - Why we can't perfectly replicate them: https://wrds-www.wharton.upenn.edu/pages/support/support-articles/crsp/index-and-deciles/constructing-value-weighted-return-series-matches-vwretd-crsp-monthly-value-weighted-returns-includes-distributions/
 - Methodology used: https://wrds-www.wharton.upenn.edu/documents/396/CRSP_US_Stock_Indices_Data_Descriptions.pdf
 - Useful link: https://www.tidy-finance.org/python/wrds-crsp-and-compustat.html

Thank you to Tobias Rodriguez del Pozo for his assistance in writing this
code.

Note: This code is based on the old CRSP SIZ format. Information
about the new CIZ format can be found here:

 - Transition FAQ: https://wrds-www.wharton.upenn.edu/pages/support/manuals-and-overviews/crsp/stocks-and-indices/crsp-stock-and-indexes-version-2/crsp-ciz-faq/
 - CRSP Metadata Guide: https://wrds-www.wharton.upenn.edu/documents/1941/CRSP_METADATA_GUIDE_STOCK_INDEXES_FLAT_FILE_FORMAT_2_0_CIZ_09232022v.pdf

"""
from datetime import datetime
from dateutil.relativedelta import relativedelta
from pathlib import Path

import numpy as np
import pandas as pd
import wrds

import config

DATA_DIR = Path(config.DATA_DIR)
WRDS_USERNAME = config.WRDS_USERNAME
START_DATE = config.START_DATE
END_DATE = config.END_DATE


def pull_CRSP_monthly_file(
    start_date=START_DATE, end_date=END_DATE, wrds_username=WRDS_USERNAME
):
    """
    Pulls monthly CRSP stock data from a specified start date to end date.

    SQL query to pull data, controls for delisting, and importantly
    follows the guidelines that CRSP uses for inclusion, with the exception
    of code 73, which is foreign companies -- without including this, the universe
    of securities is roughly half of what it should be.
    """
    # Not a perfect solution, but since value requires t-1 period market cap,
    # we need to pull one extra month of data. This is hidden from the user.
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    start_date = start_date - relativedelta(months=1)
    start_date = start_date.strftime("%Y-%m-%d")

    query = f"""
    SELECT 
        date,
        msf.permno, msf.permco, shrcd, exchcd, comnam, shrcls, 
        ret, retx, dlret, dlretx, dlstcd,
        prc, altprc, vol, shrout, cfacshr, cfacpr,
        naics, siccd
    FROM crsp.msf AS msf
    LEFT JOIN 
        crsp.msenames as msenames
    ON 
        msf.permno = msenames.permno AND
        msenames.namedt <= msf.date AND
        msf.date <= msenames.nameendt
    LEFT JOIN 
        crsp.msedelist as msedelist
    ON 
        msf.permno = msedelist.permno AND
        date_trunc('month', msf.date)::date =
        date_trunc('month', msedelist.dlstdt)::date
    WHERE 
        msf.date BETWEEN '{start_date}' AND '{end_date}' AND 
        msenames.shrcd IN (10, 11, 20, 21, 40, 41, 70, 71, 73)
    """
    # with wrds.Connection(wrds_username=wrds_username) as db:
    #     df = db.raw_sql(
    #         query, date_cols=["date", "namedt", "nameendt", "dlstdt"]
    #     )
    db = wrds.Connection(wrds_username=wrds_username)
    df = db.raw_sql(
        query, date_cols=["date", "namedt", "nameendt", "dlstdt"]
    )
    db.close()

    df = df.loc[:, ~df.columns.duplicated()]
    df["shrout"] = df["shrout"] * 1000
    # Deal with delisting returns
    df = apply_delisting_returns(df)

    return df


def apply_delisting_returns(df):
    """
    Use instructions for handling delisting returns from: Chapter 7 of 
    Bali, Engle, Murray --
    Empirical asset pricing-the cross section of stock returns (2016)
    
    First change dlret column. 
    If dlret is NA and dlstcd is not NA, then:
    if dlstcd is 500, 520, 551-574, 580, or 584, then dlret = -0.3
    if dlret is NA but dlstcd is not one of the above, then dlret = -1
    """


    # If the first condition is satisfied, the value -0.3 is chosen.
    # If the second condition is satisfied, the value -1 is chosen.
    # If none of the conditions are satisfied, the value from the "dlret" column is chosen.
    # See the docstring above.
    df["dlret"] = np.select(
        [
            df["dlstcd"].isin([500, 520, 580, 584] + list(range(551, 575))) & df["dlret"].isna(),
            df["dlret"].isna() & df["dlstcd"].notna() & df["dlstcd"] >= 200,
            True,
        ],
        [-0.3, -1, df["dlret"]],
        default=df["dlret"],
    )

    # Same as above
    df["dlretx"] = np.select(
        [
            df["dlstcd"].isin([500, 520, 580, 584] + list(range(551, 575)))
            & df["dlretx"].isna(),
            df["dlretx"].isna() & df["dlstcd"].notna() & df["dlstcd"] >= 200,
            True,
        ],
        [-0.3, -1, df["dlretx"]],
        default=df["dlretx"],
    )
    
    # ## Note: Maybe the following occurs because the ret column
    # # shows partial returns, if it continued trading for part of the month?
    # # Show rows where both ret and dlret are not na
    # # There are a lot of these, here 2858
    # df.loc[df["ret"].notna() & df["dlret"].notna(), ["ret", "dlret"]]
    # # There are only 4 rows where ret is na and dlret is not na
    # df.loc[df["ret"].isna() & df["dlret"].notna(), ["ret", "dlret"]]
    # # Obviously, more than 4 million of the below
    # df.loc[df["ret"].notna() & df["dlret"].isna(), ["ret", "dlret"]]

    df["ret"] = df["dlret"].fillna(df["ret"])
    df["retx"] = df["dlretx"].fillna(df["retx"])

    return df


def apply_delisting_returns_alt(df):
    """This is an alternative method for incorporating delisting returns.
    However, I recommend using the default method for handling delisting returns above,
    since the one above seems to be more commonly used.
    """
    df["dlret"] = df["dlret"].fillna(0)
    df["ret"] = df["ret"] + df["dlret"]
    df["ret"] = np.where(
        (df["ret"].isna()) & (df["dlret"] != 0), df["dlret"], df["ret"]
    )
    return df


def pull_CRSP_index_files(
    start_date=START_DATE, end_date=END_DATE, wrds_username=WRDS_USERNAME
):
    # Pull index files
    query = f"""
        SELECT * 
        FROM crsp_a_indexes.msix
        WHERE caldt BETWEEN '{start_date}' AND '{end_date}'
    """
    # with wrds.Connection(wrds_username=wrds_username) as db:
    #     df = db.raw_sql(query, date_cols=["month", "caldt"])
    db = wrds.Connection(wrds_username=wrds_username)
    df = db.raw_sql(query, date_cols=["caldt"])
    db.close()
    return df


def load_CRSP_monthly_file(data_dir=DATA_DIR):
    path = Path(data_dir) / "pulled" / "CRSP_MSF_INDEX_INPUTS.parquet"
    df = pd.read_parquet(path)
    return df


def load_CRSP_index_files(data_dir=DATA_DIR):
    path = Path(data_dir) / "pulled" / f"CRSP_MSIX.parquet"
    df = pd.read_parquet(path)
    return df


def _demo():
    df_msf = load_CRSP_monthly_file(data_dir=DATA_DIR)
    df_msix = load_CRSP_index_files(data_dir=DATA_DIR)


if __name__ == "__main__":

    df_msf = pull_CRSP_monthly_file(start_date=START_DATE, end_date=END_DATE)
    path = Path(DATA_DIR) / "pulled" / "CRSP_MSF_INDEX_INPUTS.parquet"
    df_msf.to_parquet(path)

    df_msix = pull_CRSP_index_files(start_date=START_DATE, end_date=END_DATE)
    path = Path(DATA_DIR) / "pulled" / f"CRSP_MSIX.parquet"
    df_msix.to_parquet(path)
