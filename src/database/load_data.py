from sqlalchemy import text
from src.database.db import engine

def insert_macro_data(df):

    query = """
    INSERT INTO macro_data (country_code, indicator, year, value)
    VALUES (:country_code, :indicator, :year, :value)
    ON CONFLICT (country_code, indicator, year)
    DO NOTHING;
    """

    records = df.to_dict(orient="records")

    with engine.connect() as conn:
        conn.execute(text(query), records)
        conn.commit()