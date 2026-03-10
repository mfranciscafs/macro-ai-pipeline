from sqlalchemy import text
from src.database.db import engine, create_table

def test_create_table():
    create_table()
#infromation_schema é uma especie de catalogo interno da BD
    query = """
    SELECT EXISTS (
        SELECT 1
        FROM information_schema.tables
        WHERE table_name = 'macro_data'
    );
    """

    with engine.connect() as conn:
        result = conn.execute(text(query))
        exists = result.scalar()

    assert exists is True