import json
from datetime import date
from sqlalchemy.orm import Session
from pathlib import Path

def parse_date(value: str) -> date:
    return date.fromisoformat(value)

def ingest_json(
    session: Session,
    model,
    json_path: Path,
    date_fields: set[str] = {"expiry_date"},
    defaults: dict | None = None,
):
    defaults = defaults or {}

    with json_path.open("r") as f:
        records = json.load(f)

    objects = []

    for r in records:
        for field in date_fields:
            if field in r and isinstance(r[field], str):
                r[field] = parse_date(r[field])

        for key, value in defaults.items():
            r.setdefault(key, value)

        objects.append(model(**r))

    session.bulk_save_objects(objects)
    session.commit()

