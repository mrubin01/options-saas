from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey, Index
from app.db.database import Base

class CoveredCall(Base):
    __tablename__ = "BEST_COVERED_CALLS"

    contract = Column(String, primary_key=True, index=True)
    ticker = Column(String, nullable=False, index=True)
    exchange = Column(Integer, nullable=False, default=0)
    # exchange = Column(Integer, ForeignKey("EXCHANGE.exchange_id"), nullable=False)
    expiry_date = Column(Date, nullable=False, index=True)
    current_price = Column(Float, nullable=False)
    strike_price = Column(Float, nullable=False)

    __table_args__ = (
        Index("ix_covered_calls_ticker_expiry", "ticker", "expiry_date"),
    )
