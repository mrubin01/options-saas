from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas.covered_call import CoveredCallOut
from app.services.covered_calls import get_covered_calls

# this router handles filtering, pagination, and retrieval of covered call options

router = APIRouter(prefix="/covered-calls", tags=["Covered Calls"])

@router.get("/", response_model=List[CoveredCallOut])
def list_covered_calls(
    exchange: int | None = Query(None),
    ticker: str | None = Query(None),
    contract: str | None = Query(None),
    min_expiry: str | None = Query(None),
    limit: int = Query(50, le=200),
    offset: int = Query(0),
    db: Session = Depends(get_db),
):
    """
    Retrieve a list of covered call options based on provided filters.
    - **exchange**: Filter by exchange ID.
    - **ticker**: Filter by stock ticker symbol.
    - **contract**: Filter by specific contract identifier.
    - **min_expiry**: Filter by minimum expiry date (YYYY-MM-DD).
    - **limit**: Maximum number of results to return (default 50, max 200).
    - **offset**: Number of results to skip for pagination (default 0).
    """
    covered_calls = get_covered_calls(
        db=db,
        exchange=exchange,
        ticker=ticker,
        contract=contract,
        min_expiry=min_expiry,
        limit=limit,
        offset=offset,
    )

    return covered_calls
