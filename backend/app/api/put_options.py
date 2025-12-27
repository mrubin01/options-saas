from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.auth.deps import get_current_user
from app.models.user import User
from app.schemas.put_option import PutOptionOut
from app.services.put_options import get_put_options

# this router handles filtering, pagination, and retrieval of put options

router = APIRouter(prefix="/put-options", tags=["Put Options"])

@router.get("/", response_model=List[PutOptionOut])
def list_put_options(
    exchange: int | None = Query(None),
    ticker: str | None = Query(None),
    contract: str | None = Query(None),
    min_expiry: str | None = Query(None),
    limit: int = Query(50, le=200),
    offset: int = Query(0),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Retrieve a list of put options based on provided filters.
    - **exchange**: Filter by exchange ID.
    - **ticker**: Filter by stock ticker symbol.
    - **contract**: Filter by specific contract identifier.
    - **min_expiry**: Filter by minimum expiry date (YYYY-MM-DD).
    - **limit**: Maximum number of results to return (default 50, max 200).
    - **offset**: Number of results to skip for pagination (default 0).
    """
    put_options = get_put_options(
        db=db,
        exchange=exchange,
        ticker=ticker,
        contract=contract,
        min_expiry=min_expiry,
        limit=limit,
        offset=offset,
    )

    return put_options
