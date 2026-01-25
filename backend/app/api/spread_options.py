from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.auth.deps import get_current_user
from app.models.user import User
from app.schemas.spread_option import SpreadOptionOut, SpreadOptionList
from app.services.spread_options import get_spread_options
from app.schemas.api import ApiResponse

# this router handles filtering, pagination, and retrieval of spread options

router = APIRouter(prefix="/spread-options", tags=["Spread Options"])

@router.get("/", response_model=ApiResponse[List[SpreadOptionOut]])
def list_spread_options(
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
    Retrieve a list of spread options with filters.
    """
    spread_options = get_spread_options(
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
        data=SpreadOptionList(
            items=[SpreadOptionOut.from_orm(so) for so in spread_options],
            limit=limit,
            offset=offset,
        ),
        error=None,
    )

