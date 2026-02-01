from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.auth.deps import get_current_user
from app.models.user import User
from app.schemas.covered_call import CoveredCallOut, CoveredCallsList
from app.services.covered_calls import get_covered_calls
from app.schemas.api import ApiResponse

# this router handles filtering, pagination, and retrieval of covered call options

router = APIRouter()

@router.get("/", response_model=ApiResponse[List[CoveredCallOut]])
def list_covered_calls(
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
    Retrieve a list of covered call options with filters.
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

    return ApiResponse(
        success=True,
        data=CoveredCallsList(
            items=[CoveredCallOut.from_orm(cc) for cc in covered_calls],
            limit=limit,
            offset=offset,
        ),
        error=None,
    )
