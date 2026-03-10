from sqlalchemy import create_engine , text


DATABASE_URL = "postgresql://macro_user:macro_pass@localhost:5432/macro_db"

engine = create_engine(DATABASE_URL)

def create_table():
    query =""" 
    CREATE TABLE IF NOT EXISTS macro_data (
        country_code TEXT,
        indicator TEXT,
        year INTEGER,
        value DOUBLE PRECISION,
        PRIMARY KEY (country_code, indicator, year)
    );
    """

    with engine.connect() as conn:
        conn.execute(text(query))
        conn.commit()
    
