from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.spread_option import SpreadOption
from ingestion.base import ingest_json
from ingestion.utils import SHARED_DATA_DIR

def run():
    json_path = SHARED_DATA_DIR / "spreads.json"

    if not json_path.exists():
        raise FileNotFoundError(f"File not found: {json_path}")

    db: Session = SessionLocal()
    try:
        ingest_json(
            session=db,
            model=SpreadOption,
            json_path=json_path,
            defaults={"exchange": 0},
        )
        print(f"Ingested spread options from {json_path}")
    finally:
        db.close()

if __name__ == "__main__":
    run()
