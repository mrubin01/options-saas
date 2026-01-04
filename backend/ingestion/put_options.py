from pathlib import Path
from sqlalchemy.orm import Session

from ingestion.base import ingest_json_file
from app.models.put_option import PutOption
from app.core.middleware.logging import get_logger

logger = get_logger(__name__)

DATA_FILE = Path("data/puts.json")

REQUIRED_FIELDS = [
    "contract",
    "ticker",
    "exchange",
    "expiry_date",
    "current_price",
    "strike_price",
]

CONFLICT_COLUMNS = ["contract"]


def ingest_put_options(db: Session):
    logger.info("Ingesting put options")

    ingest_json_file(
        db=db,
        model=PutOption,
        json_path=DATA_FILE,
        required_fields=REQUIRED_FIELDS,
        conflict_columns=CONFLICT_COLUMNS,
        set_updated_at=True,
    )
