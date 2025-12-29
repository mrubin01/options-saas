from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = (
    "postgresql+psycopg://options_user:strongpsw123@localhost:5432/options_saas"
)

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
