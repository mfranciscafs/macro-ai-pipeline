import pandas as pd
from src.ingestion.worldbank import fetch_indicator

def test_fetch_indicator_returns_dataframe():

    df = fetch_indicator("PT", "NY.GDP.MKTP.CD")

    assert isinstance(df, pd.DataFrame)

def test_fetch_indicator_has_expected_columns():

    df = fetch_indicator("PT", "NY.GDP.MKTP.CD")

    expected_cols = {"country_code", "indicator", "year", "value"}

    assert expected_cols.issubset(df.columns)

def test_fetch_indicator_returns_rows():

    df = fetch_indicator("PT", "NY.GDP.MKTP.CD")

    assert len(df) > 0