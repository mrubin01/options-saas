from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey, Index
from app.db.database import Base

class PutOption(Base):
    __tablename__ = "BEST_PUT_OPTIONS"

    contract = Column(String, primary_key=True, index=True)
    ticker = Column(String, nullable=False, index=True)
    exchange = Column(Integer, ForeignKey("EXCHANGE.exchange_id"), nullable=False)
    expiry_date = Column(Date, nullable=False, index=True)
    current_price = Column(Float, nullable=False)
    strike_price = Column(Float, nullable=False)

    __table_args__ = (
        Index("ix_put_options_ticker_expiry", "ticker", "expiry_date"),
    )
