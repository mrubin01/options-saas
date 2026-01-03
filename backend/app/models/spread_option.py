from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey, Index, DateTime
from app.db.database import Base
from sqlalchemy.sql import func

class SpreadOption(Base):
    __tablename__ = "BEST_SPREAD_OPTIONS"

    contract = Column(String, primary_key=True, index=True)
    ticker = Column(String, nullable=False, index=True)
    exchange = Column(
    Integer,
    ForeignKey(
        "EXCHANGE.exchange_id",
        name="fk_spread_options_exchange",
        ondelete="RESTRICT",
    ),
    nullable=False,
    )
    # exchange = Column(Integer, ForeignKey("EXCHANGE.exchange_id"), nullable=False)
    expiry_date = Column(Date, nullable=False, index=True)
    current_price = Column(Float, nullable=False)
    strike_price = Column(Float, nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        Index("ix_spread_options_ticker_expiry", "ticker", "expiry_date"),
    )
