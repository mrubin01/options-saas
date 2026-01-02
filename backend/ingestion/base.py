import json
from datetime import date, datetime
from sqlalchemy.orm import Session
from pathlib import Path
from app.core.logging import get_logger

logger = get_logger("ingestion")


def parse_date(value: str) -> date | None:
    if value is None:
        return None

    if isinstance(value, date):
        return value

    if isinstance(value, datetime):
        return value.date()

    if isinstance(value, str):
        # Try ISO first (YYYY-MM-DD)
        try:
            return date.fromisoformat(value)
        except ValueError:
            pass

        # Try DD/MM/YYYY
        try:
            return datetime.strptime(value, "%d/%m/%Y").date()
        except ValueError:
            pass

    raise ValueError(f"Unsupported date format: {value!r}")


def ingest_json(
    session: Session,
    model,
    json_path: Path,
    date_fields: set[str] = {"expiry_date"},
    defaults: dict | None = None,
):
    defaults = defaults or {}

    logger.info(
        "Ingestion started",
        extra={"model": model.__tablename__, "source": str(json_path)},
    )

    try:
        with json_path.open("r") as f:
            records = json.load(f)

        objects = []

        for r in records:
            for field in date_fields:
                if field in r and isinstance(r[field], str):
                    r[field] = parse_date(r[field])

            for key, value in defaults.items():
                r.setdefault(key, value)

            # objects.append(model(**r))
            obj = model(**r)
            session.merge(obj)
            # Using merge to avoid duplicates based on primary key

        session.commit()

        logger.info(
            "Ingestion completed",
            extra={
                "model": model.__tablename__,
                "rows": len(records),
            },
        )
        
    except Exception:
        logger.exception("Ingestion failed")


