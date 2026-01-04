from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
import logging
from dotenv import load_dotenv
load_dotenv()

logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)

# uvicorn and fastapi use read-only user  
DATABASE_URL = os.getenv("DATABASE_URL_APP")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL_APP is not set")

engine = create_engine(
    DATABASE_URL,
    echo=True,  # logs SQL (very useful during migration)
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
