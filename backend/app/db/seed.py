from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.exchange import Exchange
from app.models.trend import Trend
from app.models.sector import Sector
from app.models.industry import Industry

def seed_exchanges(db: Session):
    exchanges = [
        Exchange(exchange_id=0, exchange_name="NYSE"),
        Exchange(exchange_id=1, exchange_name="NASDAQ"),
        Exchange(exchange_id=2, exchange_name="ARCA"),
    ]
    db.bulk_save_objects(exchanges)

def seed_trends(db: Session):
    trends = [
        Trend(trend_id=0, trend_name="Neutral"),
        Trend(trend_id=1, trend_name="Bullish"),
        Trend(trend_id=2, trend_name="Bearish"),
    ]
    db.bulk_save_objects(trends)

def seed_sectors(db: Session):
    sectors = [
        Sector(sector_id=0, sector_name="Financial Services"),
        Sector(sector_id=1, sector_name="Consumer Defensive"),
        Sector(sector_id=2, sector_name="Industrials"),
        Sector(sector_id=3, sector_name="Technology"),
        Sector(sector_id=4, sector_name="Healthcare"),
        Sector(sector_id=5, sector_name="Consumer Cyclical"),
        Sector(sector_id=6, sector_name="Energy"),
        Sector(sector_id=7, sector_name="Basic Materials"),
        Sector(sector_id=8, sector_name="Real Estate"),
        Sector(sector_id=9, sector_name="Communication Services"),
        Sector(sector_id=10, sector_name="Utilities"),
    ]
    db.bulk_save_objects(sectors)

def seed_industries(db: Session):
    industries = [
        Industry(industry_id=0, industry_name="Advertising Agencies"),
        Industry(industry_id=1, industry_name="Aerospace & Defense"),
        Industry(industry_id=2, industry_name="Agricultural Inputs"),
        Industry(industry_id=3, industry_name="Airlines"),
        Industry(industry_id=4, industry_name="Apparel Manufacturing"),
        Industry(industry_id=5, industry_name="Apparel Retail"),
        Industry(industry_id=6, industry_name="Asset Management"),
        Industry(industry_id=7, industry_name="Auto Manufacturers"),
        Industry(industry_id=8, industry_name="Auto Parts"),
        Industry(industry_id=9, industry_name="Auto & Truck Dealerships"),
        Industry(industry_id=10, industry_name="Banks - Diversified"),
        Industry(industry_id=11, industry_name="Banks - Regional"),
        Industry(industry_id=12, industry_name="Beverages - Non-Alcoholic"),
        Industry(industry_id=13, industry_name="Biotechnology"),
        Industry(industry_id=14, industry_name="Broadcasting"),
        Industry(industry_id=15, industry_name="Building Materials"),
        Industry(industry_id=16, industry_name="Building Products & Equipment"),
        Industry(industry_id=17, industry_name="Business Equipment & Supplies"),
        Industry(industry_id=18, industry_name="Capital Markets"),
        Industry(industry_id=19, industry_name="Chemicals"),
        Industry(industry_id=20, industry_name="Communication Equipment"),
    ]
    db.bulk_save_objects(industries)

def run():
    db = SessionLocal()
    try:
        seed_exchanges(db)
        seed_trends(db)
        seed_sectors(db)
        seed_industries(db)
        db.commit()
        print("Lookup tables seeded successfully!!!")
    finally:
        db.close()

if __name__ == "__main__":
    run()
