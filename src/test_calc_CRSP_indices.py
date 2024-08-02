import pandas as pd
from pandas.testing import assert_frame_equal

import calc_CRSP_indices
import load_CRSP_stock

import config
DATA_DIR = config.DATA_DIR

def test_calc_value_idx():
    """
    Consider the hypothetical example defined in the DataFrame `input`

    Now, calculating the value-weighted returns by hand, we should see the following:

    time=1:
      prev mktcap permno #1 is 100 * 1 = 100
      prev mktcap permno #2 is 200 * 2 = 400
      curr returns permno #1 is -0.5
      curr returns permno #2 is 0.1
      So value-weighted return is (100 * -0.5 + 400 * 0.1) / (100 + 400) = -0.02
    time=2:
      prev mktcap permno #1 is 100 * 0.5 = 50
      prev mktcap permno #2 is 200 * 2.2 = 440
      curr returns permno #1 is 1
      curr returns permno #2 is 0.1
      So value-weighted return is (50 * 1 + 440 * 0.1) / (50 + 440) = 0.1918...
    and total market cap should 500, 0.5 * 100 + 2.2 * 200 = 490, 100 + 2.42 * 200 = 584.0
    """
    input = pd.DataFrame(
        data={
            "permno": [1, 1, 1, 2, 2, 2],
            "date": pd.to_datetime(
                [
                    "2020-01-01",
                    "2020-02-01",
                    "2020-03-01",
                    "2020-01-01",
                    "2020-02-01",
                    "2020-03-01",
                ]
            ),
            "altprc": [1, 0.5, 1, 2, 2.2, 2.42],
            "ret": [0, -0.5, 1, 0, 0.1, 0.1],
            "retx": [0, -0.5, 1, 0, 0.1, 0.1],
            "shrout": [100, 100, 100, 200, 200, 200],
        }
    )

    expected_output = pd.DataFrame(
        data={
            "vwretd": [-0.02, 0.1918],
            "vwretx": [-0.02, 0.1918],
            "totval": [490.0, 584.0],
        },
        index=pd.to_datetime(["2020-02-01", "2020-03-01"]),
    )
    expected_output.index.name = "date"

    assert_frame_equal(
        calc_CRSP_indices.calc_CRSP_value_weighted_index(input).round(4),
        expected_output.round(4),
    )


def test_calc_equal_idx():
    input = pd.DataFrame(
        data={
            "permno": [1, 1, 1, 2, 2, 2],
            "date": pd.to_datetime(
                [
                    "2020-01-01",
                    "2020-02-01",
                    "2020-03-01",
                    "2020-01-01",
                    "2020-02-01",
                    "2020-03-01",
                ]
            ),
            "altprc": [1, 0.5, 1, 2, 2.2, 2.42],
            "ret": [0, -0.5, 1, 0, 0.1, 0.1],
            "retx": [0, -0.5, 1, 0, 0.1, 0.1],
            "shrout": [100, 100, 100, 200, 200, 200],
        }
    )

    # Expected output:
    # time=0:
    #   returns are 0 and 0
    #   So equal-weighted return is (0 + 0) / 2 = 0
    # time=1:
    #   returns are -0.5 and 0.1
    #   So equal-weighted return is (-0.5 + 0.1) / 2 = -0.2
    # time=2:
    #   returns are 1 and 0.1
    #   So equal-weighted return is (1 + 0.1) / 2 = 0.55

    expected_output = pd.DataFrame(
        data={
            "ewretd": [0, -0.2, 0.55],
            "ewretx": [0, -0.2, 0.55],
            "totcnt": [2, 2, 2],
        },
        index=pd.to_datetime(["2020-01-01", "2020-02-01", "2020-03-01"]),
    )
    expected_output.index.name = "date"

    assert_frame_equal(
        calc_CRSP_indices.calc_equal_weighted_index(input).round(4),
        expected_output.round(4),
    )


def test_calc_CRSP_indices_merge():
    """
    Same as before:
        total market cap should 500, 0.5 * 100 + 2.2 * 200 = 490, 100 + 2.42 * 200 = 584.0
    """
    input = pd.DataFrame(
        data={
            "permno": [1, 1, 1, 2, 2, 2],
            "date": pd.to_datetime(
                [
                    "2020-01-01",
                    "2020-02-01",
                    "2020-03-01",
                    "2020-01-01",
                    "2020-02-01",
                    "2020-03-01",
                ]
            ),
            "altprc": [1, 0.5, 1, 2, 2.2, 2.42],
            "ret": [0, -0.5, 1, 0, 0.1, 0.1],
            "retx": [0, -0.5, 1, 0, 0.1, 0.1],
            "shrout": [100, 100, 100, 200, 200, 200],
        }
    )

    idx_input = pd.DataFrame(
        data={
            "vwretd": [0, -0.03, 0.2],
            "vwretx": [0, -0.03, 0.2],
            "totval": [500.0, 490.0, 584.0],
            "ewretd": [0, -0.2, 0.5],
            "ewretx": [0, -0.2, 0.5],
            "totcnt": [0, 2, 2],
        },
        index=pd.to_datetime(["2020-01-01", "2020-02-01", "2020-03-01"]),
    )
    idx_input.index.name = "date"

    # This just combines the logic from the two previous tests.

    expected_output = pd.DataFrame(
        data={
            "vwretd": [-0.03, 0.2],
            "vwretx": [-0.03, 0.2],
            "totval": [490.,584.],
            "ewretd": [-0.2, 0.5],
            "ewretx": [-0.2, 0.5],
            "totcnt": [2, 2],
            "vwretd_manual": [-0.02, 0.1918],
            "vwretx_manual": [-0.02, 0.1918],
            "totval_manual": [490.,584.],
            "ewretd_manual": [-0.2, 0.55],
            "ewretx_manual": [-0.2, 0.55],
            "totcnt_manual": [2, 2],
        },
        index=pd.to_datetime(["2020-02-01", "2020-03-01"]),
    )
    expected_output.index.name = "date"

    assert_frame_equal(
        calc_CRSP_indices.calc_CRSP_indices_merge(input, idx_input).round(4),
        expected_output.round(4),
    )


def test_compare_CRSP_manual():
    
    VW_AVE_THRESHOLD = 0.002
    VW_MAX_THRESHOLD = 0.01
    EW_AVE_THRESHOLD = 0.01
    EW_MAX_THRESHOLD = 0.03

    df_msf = load_CRSP_stock.load_CRSP_monthly_file(data_dir=DATA_DIR)
    df_msix = load_CRSP_stock.load_CRSP_index_files(data_dir=DATA_DIR)

    # df_eq_idx = calc_equal_weighted_index(df_msf)
    # df_vw_idx = calc_CRSP_value_weighted_index(df_msf)
    df = calc_CRSP_indices.calc_CRSP_indices_merge(df_msf, df_msix)
    # df_idxs.head()

    # NOTE: 
    # I ran this on a variety of different dates, and it seemed that 
    # the average difference was normally ~0.0015, so I'm setting the 
    # threshold to 0.002 to be safe. Additionally, the difference
    # in signs seemed to be ~1/50 days, so I'm setting the threshold to be 
    # 1/20 days for opposite signs. This is a bit arbitrary and can probably 
    # be improved. The precision also depends on if it's equally weighted or 
    # value weighted, so equally weighted will have more differences since 
    # the securities are weighted evenly (and we don't know what the security universe CRSP is using is).

    # TEST 1: Make sure that absolute difference is less than ~0.2% for the 
    # value-weighted data.
    assert (df["vwretd"] - df["vwretd_manual"]).abs().mean() < VW_AVE_THRESHOLD
    assert (df["vwretx"] - df["vwretx_manual"]).abs().max() < VW_MAX_THRESHOLD

    assert (df["ewretd"] - df["ewretd_manual"]).abs().mean() < EW_AVE_THRESHOLD
    assert (df["ewretx"] - df["ewretx_manual"]).abs().max() < EW_MAX_THRESHOLD

    # TEST 2: Make sure the signs are the same at least 19/20 days.
    assert (df["vwretd"] * df["vwretd_manual"] > 0).mean() > 0.95
    assert (df["vwretx"] * df["vwretx_manual"] > 0).mean() > 0.95

    assert (df["ewretd"] * df["ewretd_manual"] > 0).mean() > 0.95
    assert (df["ewretx"] * df["ewretx_manual"] > 0).mean() > 0.95

    # TEST 3: Make sure that the total security count is within 5% of the
    # manual calculation.
    assert (
        (df["totcnt"] - df["totcnt_manual"]).abs() / df["totcnt_manual"] < 0.05
    ).all()

    # TEST 4: Test that cumulative returns are within 5% of each other. Again, arbitrarily.
    assert (
        (1 + df["vwretd"]).cumprod() - (1 + df["vwretd_manual"]).cumprod()
    ).abs().max() < 0.04
    assert (
        (1 + df["vwretx"]).cumprod() - (1 + df["vwretx_manual"]).cumprod()
    ).abs().max() < 0.05
    assert (
        (1 + df["ewretd"]).cumprod() - (1 + df["ewretd_manual"]).cumprod()
    ).abs().max() < 0.1
    assert (
        (1 + df["ewretx"]).cumprod() - (1 + df["ewretx_manual"]).cumprod()
    ).abs().max() < 0.2

    # TEST 5: Make sure that they are  > 99% correlated.
    assert df[["vwretd", "vwretd_manual"]].corr().iloc[0, 1] > 0.999
    assert df[["vwretx", "vwretx_manual"]].corr().iloc[0, 1] > 0.999
    assert df[["ewretd", "ewretd_manual"]].corr().iloc[0, 1] > 0.99
    assert df[["ewretx", "ewretx_manual"]].corr().iloc[0, 1] > 0.99
