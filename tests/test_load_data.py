from sqlalchemy import text
from src.ingestion.worldbank import fetch_indicator
from src.database.load_data import insert_macro_data
from src.database.db import engine

def test_insert_macro_data():

    df = fetch_indicator("PT", "NY.GDP.MKTP.CD")

    insert_macro_data(df)

    query = "SELECT COUNT(*) FROM macro_data WHERE country_code = 'PT';"

    with engine.connect() as conn:
        result = conn.execute(text(query))
        count = result.scalar()

    assert count > 0