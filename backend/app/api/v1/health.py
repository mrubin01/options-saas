from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db.database import get_db

router = APIRouter(tags=["health"])


@router.get("/health")
def health():
    """
    Liveness probe.
    Returns OK if the app is running.
    """
    return {"status": "ok"}


@router.get("/ready")
def readiness(db: Session = Depends(get_db)):
    """
    Readiness probe.
    Returns OK if DB is reachable.
    """
    db.execute(text("SELECT 1"))
    return {"status": "ready"}

