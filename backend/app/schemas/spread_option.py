from datetime import date, datetime
from pydantic import BaseModel

# response schema: data to expose via API   

class SpreadOptionOut(BaseModel):
    contract: str
    ticker: str
    exchange: int
    expiry_date: date
    current_price: float
    strike_price: float
    updated_at: datetime | None

    class Config:
        orm_mode = True
