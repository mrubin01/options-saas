import json
from pathlib import Path
from datetime import date
from typing import Type

from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert

from app.core.middleware.logging import get_logger

logger = get_logger(__name__)


# ---------- helpers ----------

def parse_date(value):
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        return date.fromisoformat(value)
    raise ValueError(f"Invalid date value: {value}")


def normalize_record(record: dict) -> dict:
    """
    Normalize raw JSON record into DB-ready format.
    """
    r = record.copy()

    if "expiry_date" in r:
        r["expiry_date"] = parse_date(r["expiry_date"])

    if "ticker" in r and r["ticker"]:
        r["ticker"] = r["ticker"].upper()

    return r


def validate_record(record: dict, required_fields: list[str]):
    for field in required_fields:
        if field not in record:
            raise ValueError(f"Missing required field: {field}")
        if record[field] is None:
            raise ValueError(f"Null value for field: {field}")


# ---------- core ingestion ----------

def upsert_records(
    db: Session,
    model: Type,
    records: list[dict],
    conflict_columns: list[str],
):
    """
    PostgreSQL UPSERT (ON CONFLICT DO UPDATE)
    """
    if not records:
        logger.info("No records to ingest", extra={"table": model.__tablename__})
        return

    stmt = insert(model).values(records)

    update_columns = {
        col.name: stmt.excluded[col.name]
        for col in model.__table__.columns
        if col.name not in conflict_columns
    }

    stmt = stmt.on_conflict_do_update(
        index_elements=conflict_columns,
        set_=update_columns,
    )

    db.execute(stmt)
    db.commit()

    logger.info(
        "Upsert completed",
        extra={
            "table": model.__tablename__,
            "rows": len(records),
        },
    )


def ingest_json_file(
    *,
    db: Session,
    model: Type,
    json_path: Path,
    required_fields: list[str],
    conflict_columns: list[str],
):
    """
    Generic JSON → PostgreSQL ingestion
    """
    logger.info(
        "Starting ingestion",
        extra={"table": model.__tablename__, "file": str(json_path)},
    )

    with json_path.open() as f:
        raw_records = json.load(f)

    records = []
    for raw in raw_records:
        validate_record(raw, required_fields)
        normalized = normalize_record(raw)
        records.append(normalized)

    upsert_records(
        db=db,
        model=model,
        records=records,
        conflict_columns=conflict_columns,
    )



