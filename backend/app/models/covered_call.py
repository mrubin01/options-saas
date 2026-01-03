from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey, Index, DateTime
from app.db.database import Base
from sqlalchemy.sql import func

class CoveredCall(Base):
    __tablename__ = "BEST_COVERED_CALLS"

    contract = Column(String, primary_key=True, index=True)
    ticker = Column(String, nullable=False, index=True)
    exchange = Column(
    Integer,
    ForeignKey("EXCHANGE.exchange_id", ondelete="RESTRICT"),
    nullable=False,
    )
    # exchange = Column(Integer, nullable=False, default=0)
    expiry_date = Column(Date, nullable=False, index=True)
    current_price = Column(Float, nullable=False)
    strike_price = Column(Float, nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        Index("ix_covered_calls_ticker_expiry", "ticker", "expiry_date"),
    )
