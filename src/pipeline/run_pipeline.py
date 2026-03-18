from src.ingestion.worldbank import fetch_indicator
from src.database.load_data import insert_macro_data
from src.database.db import create_table

def run_pipeline():

    country = "PT"
    indicator = "NY.GDP.MKTP.CD"

    print("🚀 Starting pipeline...")

    # 1. garantir tabela
    create_table()
    print("✅ Table ready")

    # 2. fetch data
    df = fetch_indicator(country, indicator)
    print(f"✅ Data fetched: {df.shape}")

    # 3. insert data
    insert_macro_data(df)
    print("✅ Data inserted")

    print("🎉 Pipeline finished successfully!")

if __name__ == "__main__":
    run_pipeline()