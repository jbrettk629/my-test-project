from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base

# Need to use async drivers ... psycopg2 is not async.
DB_URL = "postgresql+psycopg2://localhost:5432/myprojectdb"
ASYNC_DB_URL = "postgresql+asyncpg://localhost:5432/myprojectdb"

async_engine = create_async_engine(ASYNC_DB_URL)
engine = create_engine(DB_URL, pool_size=50, echo=False, future=True, connect_args={})

SessionLocal = sessionmaker(bind=engine, future=True)
AsyncSessionLocal = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)


Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_async_db():
    async with AsyncSessionLocal() as db:
        yield db
        await db.commit()
