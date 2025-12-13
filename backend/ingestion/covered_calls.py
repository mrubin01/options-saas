from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.covered_call import CoveredCall
from ingestion.base import ingest_json

def run(json_path: str):
    db: Session = SessionLocal()
    try:
        ingest_json(
            session=db,
            model=CoveredCall,
            json_path=json_path,
        )
    finally:
        db.close()

if __name__ == "__main__":
    run("data/covered_calls.json")
