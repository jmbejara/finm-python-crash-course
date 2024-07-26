import pandas as pd
from misc_tools import (
    weighted_average,
    groupby_weighted_average,
    groupby_weighted_std,
    get_most_recent_quarter_end,
    get_next_quarter_start,
)


def test_weighted_average():
    df_nccb = pd.DataFrame({"rate": [2, 3, 2], "start_leg_amount": [100, 200, 100]})
    result = weighted_average(
        data_col="rate", weight_col="start_leg_amount", data=df_nccb
    )
    expected = 2.5
    assert result == expected


def test_groupby_weighted_average():
    df_nccb = pd.DataFrame(
        {
            "trade_direction": ["RECEIVED", "RECEIVED", "DELIVERED"],
            "rate": [2, 3, 2],
            "start_leg_amount": [100, 200, 100],
        }
    )
    result = groupby_weighted_average(
        data_col="rate",
        weight_col="start_leg_amount",
        by_col="trade_direction",
        data=df_nccb,
    )
    expected = pd.Series(
        [2.000000, 2.666667],
        index=pd.Index(["DELIVERED", "RECEIVED"], name="trade_direction"),
    )
    pd.testing.assert_series_equal(result, expected)


def test_groupby_weighted_std():
    df_nccb = pd.DataFrame(
        {
            "trade_direction": [
                "RECEIVED",
                "RECEIVED",
                "RECEIVED",
                "RECEIVED",
                "DELIVERED",
                "DELIVERED",
                "DELIVERED",
                "DELIVERED",
            ],
            "rate": [2, 2, 2, 3, 2, 2, 2, 3],
            "start_leg_amount": [300, 300, 300, 0, 200, 200, 200, 200],
        }
    )
    result = groupby_weighted_std(
        data_col="rate",
        weight_col="start_leg_amount",
        by_col="trade_direction",
        ddof=1,
        data=df_nccb,
    )
    expected = pd.Series(
        [0.50, 0.00], index=pd.Index(["DELIVERED", "RECEIVED"], name="trade_direction")
    )
    pd.testing.assert_series_equal(result, expected)


def test_get_most_recent_quarter_end():
    d = pd.to_datetime("2019-10-21")
    result = get_most_recent_quarter_end(d)
    expected = pd.Timestamp("2019-09-30")
    assert result == expected


def test_get_next_quarter_start():
    d = pd.to_datetime("2019-10-21")
    result = get_next_quarter_start(d)
    expected = pd.Timestamp("2020-01-01")
    assert result == expected
