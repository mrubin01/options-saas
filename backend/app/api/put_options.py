from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.auth.deps import get_current_user
from app.models.user import User
from app.schemas.put_option import PutOptionOut, PutOptionList
from app.services.put_options import get_put_options
from app.schemas.api import ApiResponse

# this router handles filtering, pagination, and retrieval of put options

router = APIRouter(prefix="/put-options", tags=["Put Options"])

@router.get("/", response_model=ApiResponse[List[PutOptionOut]])
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
    Retrieve a list of put options with filters.
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

    return ApiResponse(
        success=True,
        data=PutOptionList(
            items=[PutOptionOut.from_orm(po) for po in put_options],
            limit=limit,
            offset=offset,
        ),
        error=None,
    )

