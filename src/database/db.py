from sqlalchemy import create_engine

DATABASE_URL = "postgresql://macro_user:macro_pass@localhost:5432/macro_db"

engine = create_engine(DATABASE_URL)