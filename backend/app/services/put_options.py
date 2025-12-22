from sqlalchemy.orm import Session
from app.models.put_option import PutOption

# API query layer  

def get_put_options(
    db: Session,
    exchange: int | None = None,
    ticker: str | None = None,
    contract: str | None = None,
    min_expiry: str | None = None,
    limit: int = 50,
    offset: int = 0,
):
    query = db.query(PutOption)

    if exchange is not None:
        query = query.filter(PutOption.exchange == exchange)

    if contract is not None:
        query = query.filter(PutOption.contract == contract)
        
    if ticker is not None:
        query = query.filter(PutOption.ticker == ticker.upper())

    if min_expiry is not None:
        query = query.filter(PutOption.expiry_date >= min_expiry)

    return (
        query
        .order_by(PutOption.expiry_date)
        .offset(offset)
        .limit(limit)
        .all()
    )

