from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.covered_call import CoveredCall
from ingestion.base import ingest_json
from ingestion.utils import SHARED_DATA_DIR

def run():
    json_path = SHARED_DATA_DIR / "covered_calls.json"

    if not json_path.exists():
        raise FileNotFoundError(f"File not found: {json_path}")

    db: Session = SessionLocal()
    try:
        ingest_json(
            session=db,
            model=CoveredCall,
            json_path=json_path,
        )
        print(f"Ingested covered calls from {json_path}")
    finally:
        db.close()

if __name__ == "__main__":
    run()
