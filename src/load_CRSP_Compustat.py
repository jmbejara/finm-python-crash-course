"""
This module pulls and saves data on fundamentals from CRSP and Compustat.
It pulls fundamentals data from Compustat needed to calculate
book equity, and the data needed from CRSP to calculate market equity.

Note: This code uses the new CRSP CIZ format. Information
about the differences between the SIZ and CIZ format can be found here:

 - Transition FAQ: https://wrds-www.wharton.upenn.edu/pages/support/manuals-and-overviews/crsp/stocks-and-indices/crsp-stock-and-indexes-version-2/crsp-ciz-faq/
 - CRSP Metadata Guide: https://wrds-www.wharton.upenn.edu/documents/1941/CRSP_METADATA_GUIDE_STOCK_INDEXES_FLAT_FILE_FORMAT_2_0_CIZ_09232022v.pdf

For information about Compustat variables, see:
https://wrds-www.wharton.upenn.edu/documents/1583/Compustat_Data_Guide.pdf

For more information about variables in CRSP, see:
https://wrds-www.wharton.upenn.edu/documents/396/CRSP_US_Stock_Indices_Data_Descriptions.pdf
I don't think this is updated for the new CIZ format, though.

Here is some information about the old SIZ CRSP format:
https://wrds-www.wharton.upenn.edu/documents/1095/CRSP_Flat_File_formats_and_notes.pdf


The following is an outdated programmer's guide to CRSP:
https://wrds-www.wharton.upenn.edu/documents/400/CRSP_Programmers_Guide.pdf


"""
import pandas as pd
from pandas.tseries.offsets import MonthEnd, YearEnd

import numpy as np
import wrds

import config
from pathlib import Path

OUTPUT_DIR = Path(config.OUTPUT_DIR)
DATA_DIR = Path(config.DATA_DIR)
WRDS_USERNAME = config.WRDS_USERNAME
# START_DATE = config.START_DATE
# END_DATE = config.END_DATE


description_compustat = {
    "gvkey": "Global Company Key",
    "datadate": "Data Date",
    "at": "Assets - Total",
    "pstkl": "Preferred Stock - Liquidating Value",
    "txditc": "Deferred Taxes and Investment Tax Credit",
    "pstkrv": "Preferred Stock - Redemption Value",
    # This item represents the total dollar value of the net number of
    # preferred shares outstanding multiplied by the voluntary
    # liquidation or redemption value per share.
    "seq": "Stockholders' Equity - Parent",
    "pstk": "Preferred/Preference Stock (Capital) - Total",
    "indfmt": "Industry Format",
    "datafmt": "Data Format",
    "popsrc": "Population Source",
    "consol": "Consolidation",
}


def pull_compustat(wrds_username=WRDS_USERNAME):
    """
    See description_compustat for a description of the variables.
    """
    sql_query = """
        SELECT 
            gvkey, datadate, at, pstkl, txditc,
            pstkrv, seq, pstk
        FROM 
            comp.funda
        WHERE 
            indfmt='INDL' AND -- industrial companies
            datafmt='STD' AND -- only standardized records
            popsrc='D' AND -- only from primary sources
            consol='C' AND -- consolidated financial statements
            datadate >= '01/01/1959'
        """
    # with wrds.Connection(wrds_username=wrds_username) as db:
    #     comp = db.raw_sql(sql_query, date_cols=["datadate"])
    db = wrds.Connection(wrds_username=wrds_username)
    comp = db.raw_sql(sql_query, date_cols=["datadate"])
    db.close()

    comp["year"] = comp["datadate"].dt.year
    return comp


description_crsp = {
    "permno": "Permanent Number - A unique identifier assigned by CRSP to each security.",
    "permco": "Permanent Company - A unique company identifier assigned by CRSP that remains constant over time for a given company.",
    "mthcaldt": "Calendar Date - The date for the monthly data observation.",
    "issuertype": "Issuer Type - Classification of the issuer, such as corporate or government.",
    "securitytype": "Security Type - General classification of the security, e.g., stock or bond.",
    "securitysubtype": "Security Subtype - More specific classification of the security within its type.",
    "sharetype": "Share Type - Classification of the equity share type, e.g., common stock, preferred stock.",
    "usincflg": "U.S. Incorporation Flag - Indicator of whether the company is incorporated in the U.S.",
    "primaryexch": "Primary Exchange - The primary stock exchange where the security is listed.",
    "conditionaltype": "Conditional Type - Indicator of any conditional issues related to the security.",
    "tradingstatusflg": "Trading Status Flag - Indicator of the trading status of the security, e.g., active, suspended.",
    "mthret": "Monthly Return - The total return of the security for the month, including dividends.",
    "mthretx": "Monthly Return Excluding Dividends - The return of the security for the month, excluding dividends.",
    "shrout": "Shares Outstanding - The number of outstanding shares of the security.",
    "mthprc": "Monthly Price - The price of the security at the end of the month.",
}


def pull_CRSP_stock_ciz(wrds_username=WRDS_USERNAME):
    """Pull necessary CRSP monthly stock data to
    compute Fama-French factors. Use the new CIZ format.
    """
    sql_query = """
        SELECT 
            a.permno, a.permco, a.mthcaldt, 
            a.issuertype, a.securitytype, a.securitysubtype, a.sharetype, 
            a.usincflg, 
            a.primaryexch, a.conditionaltype, a.tradingstatusflg,
            a.mthret, a.mthretx, a.shrout, a.mthprc
        FROM 
            crsp.msf_v2 AS a
        WHERE 
            a.mthcaldt BETWEEN '01/01/1959' AND '12/31/2022'
        """

    db = wrds.Connection(wrds_username=wrds_username)
    crsp_m = db.raw_sql(sql_query, date_cols=["mthcaldt"])
    db.close()

    # change variable format to int
    crsp_m[['permco','permno']]=crsp_m[['permco','permno']].astype(int)

    # Line up date to be end of month
    crsp_m['jdate']=crsp_m['mthcaldt']+MonthEnd(0)

    return crsp_m


description_crsp_comp_link = {
    "gvkey": "Global Company Key - A unique identifier for companies in the Compustat database.",
    "permno": "Permanent Number - A unique stock identifier assigned by CRSP to each security.",
    "linktype": "Link Type - Indicates the type of linkage between CRSP and Compustat records. 'L' types refer to links considered official by CRSP.",
    "linkprim": "Primary Link Indicator - Specifies whether the link is a primary ('P') or secondary ('C') connection between the databases. Primary links are direct matches between CRSP and Compustat entities, while secondary links may represent subsidiary relationships or other less direct connections.",
    "linkdt": "Link Date Start - The starting date for which the linkage between CRSP and Compustat data is considered valid.",
    "linkenddt": "Link Date End - The ending date for which the linkage is considered valid. A blank or high value (e.g., '2099-12-31') indicates that the link is still valid as of the last update.",
}


def pull_CRSP_Comp_Link_Table(wrds_username=WRDS_USERNAME):
    sql_query = """
        SELECT 
            gvkey, lpermno AS permno, linktype, linkprim, linkdt, linkenddt
        FROM 
            crsp.ccmxpf_linktable
        WHERE 
            substr(linktype,1,1)='L' AND 
            (linkprim ='C' OR linkprim='P')
        """
    db = wrds.Connection(wrds_username=wrds_username)
    ccm = db.raw_sql(sql_query, date_cols=["linkdt", "linkenddt"])
    db.close()
    return ccm


def pull_Fama_French_factors(wrds_username=WRDS_USERNAME):
    conn = wrds.Connection(wrds_username=config.WRDS_USERNAME)
    ff = conn.get_table(library="ff", table="factors_monthly")
    conn.close()
    ff[["smb", "hml"]] = ff[["smb", "hml"]].astype(float)
    
    ff["date"] = pd.to_datetime(ff["date"])
    ff["date"] = ff["date"] + MonthEnd(0)
    
    return ff


def load_compustat(data_dir=DATA_DIR):
    path = Path(data_dir) / "pulled" / "Compustat.parquet"
    comp = pd.read_parquet(path)
    return comp


def load_CRSP_stock_ciz(data_dir=DATA_DIR):
    path = Path(data_dir) / "pulled" / "CRSP_stock_ciz.parquet"
    crsp = pd.read_parquet(path)
    return crsp


def load_CRSP_Comp_Link_Table(data_dir=DATA_DIR):
    path = Path(data_dir) / "pulled" / "CRSP_Comp_Link_Table.parquet"
    ccm = pd.read_parquet(path)
    return ccm


def load_Fama_French_factors(data_dir=DATA_DIR):
    path = Path(data_dir) / "pulled" / "FF_FACTORS.parquet"
    ff = pd.read_parquet(path)
    return ff

def _demo():
    comp = load_compustat(data_dir=DATA_DIR)
    crsp = load_CRSP_stock_ciz(data_dir=DATA_DIR)
    ccm = load_CRSP_Comp_Link_Table(data_dir=DATA_DIR)
    ff = load_Fama_French_factors(data_dir=DATA_DIR)


if __name__ == "__main__":
    comp = pull_compustat(wrds_username=WRDS_USERNAME)
    comp.to_parquet(DATA_DIR / "pulled" / "Compustat.parquet")

    crsp = pull_CRSP_stock_ciz(wrds_username=WRDS_USERNAME)
    crsp.to_parquet(DATA_DIR / "pulled" / "CRSP_stock_ciz.parquet")

    ccm = pull_CRSP_Comp_Link_Table(wrds_username=WRDS_USERNAME)
    ccm.to_parquet(DATA_DIR / "pulled" / "CRSP_Comp_Link_Table.parquet")

    ff = pull_Fama_French_factors(wrds_username=WRDS_USERNAME)
    ff.to_parquet(DATA_DIR / "pulled" / "FF_FACTORS.parquet")
