"""
This module loads the S&P 500 index, Dividend yields, and all active futures during 
the given period from Bloomberg. 

You must have a Bloomberg terminal open on this computer to run. You must
first install xbbg
"""

import pandas as pd
import config
from pathlib import Path

DATA_DIR = config.DATA_DIR
START_DATE = config.START_DATE
END_DATE = config.END_DATE

def pull_bbg_data(end_date=END_DATE):
    
    bbg_df = pd.DataFrame()
    bbg_df['dividend yield'] = blp.bdh("SPX Index","EQY_DVD_YLD_12m", START_DATE, end_date)[("SPX Index","EQY_DVD_YLD_12m")]
    
    bbg_df['index'] = blp.bdh("SPX Index","px_last", START_DATE, end_date)[("SPX Index","px_last")]
    
    bbg_df['futures'] = pd.concat([blp.bdh("SP1 Index","px_last", START_DATE, "1997-08-31")[("SP1 Index","px_last")],
                                    blp.bdh("ES1 Index","px_last", "1997-09-30", end_date)[("ES1 Index","px_last")]])
    
    bbg_df.index.name = 'Date'

    return bbg_df


if __name__ == "__main__":
    from xbbg import blp
    df = pull_bbg_data(end_date=END_DATE)
    path = Path(DATA_DIR) / "pulled" / "bloomberg.parquet"
    df.to_parquet(path)