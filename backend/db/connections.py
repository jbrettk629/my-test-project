# import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL = "postgresql+psycopg2://localhost:5432/myprojectdb"

engine = create_engine(DB_URL, pool_size=50, echo=False, future=True, connect_args={})

SessionLocal = sessionmaker(bind=engine, future=True)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# connection = psycopg2.connect(
#     host = "localhost",
#     database = "myprojectdb",
#     user = "josephkalbacher",
# )
# cursor = connection.cursor()

# connection.close()