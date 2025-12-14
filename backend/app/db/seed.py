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
        Industry(industry_id=21, industry_name="Computer Hardware"),
        Industry(industry_id=22, industry_name="Consulting Services"),
        Industry(industry_id=23, industry_name="Credit Services"),
        Industry(industry_id=24, industry_name="Department Stores"),
        Industry(industry_id=25, industry_name="Diagnostics & Research"),
        Industry(industry_id=26, industry_name="Discount Stores"),
        Industry(industry_id=27, industry_name="Drug Manufacturers - General"),
        Industry(industry_id=28, industry_name="Drug Manufacturers - Specialty & Generic"),
        Industry(industry_id=29, industry_name="Education & Training Services"),
        Industry(industry_id=30, industry_name="Electrical Equipment & Parts"),
        Industry(industry_id=31, industry_name="Electronic Components"),
        Industry(industry_id=32, industry_name="Electronics & Computer Distribution"),
        Industry(industry_id=33, industry_name="Engineering & Construction"),
        Industry(industry_id=34, industry_name="Entertainment"),
        Industry(industry_id=35, industry_name="Farm & Heavy Construction Machinery"),
        Industry(industry_id=36, industry_name="Farm Products"),
        Industry(industry_id=37, industry_name="Financial Data & Stock Exchanges"),
        Industry(industry_id=38, industry_name="Food Distribution"),
        Industry(industry_id=39, industry_name="Footwear & Accessories"),
        Industry(industry_id=40, industry_name="Furnishings, Fixtures & Appliances"),
        Industry(industry_id=41, industry_name="Gambling"),
        Industry(industry_id=42, industry_name="Gold"),
        Industry(industry_id=43, industry_name="Grocery Stores"),
        Industry(industry_id=44, industry_name="Healthcare Plans"),
        Industry(industry_id=45, industry_name="Health Information Services"),
        Industry(industry_id=46, industry_name="Home Improvement Retail"),
        Industry(industry_id=47, industry_name="Household & Personal Products"),
        Industry(industry_id=48, industry_name="Industrial Distribution"),
        Industry(industry_id=49, industry_name="Information Technology Services"),
        Industry(industry_id=50, industry_name="Insurance Brokers"),
        Industry(industry_id=51, industry_name="Insurance - Diversified"),
        Industry(industry_id=52, industry_name="Insurance - Life"),
        Industry(industry_id=53, industry_name="Insurance - Property & Casualty"),
        Industry(industry_id=54, industry_name="Insurance - Reinsurance"),
        Industry(industry_id=55, industry_name="Insurance - Specialty"),
        Industry(industry_id=56, industry_name="Integrated Freight & Logistics"),
        Industry(industry_id=57, industry_name="Internet Content & Information"),
        Industry(industry_id=58, industry_name="Internet Retail"),
        Industry(industry_id=59, industry_name="Leisure"),
        Industry(industry_id=60, industry_name="Lodging"),
        Industry(industry_id=61, industry_name="Marine Shipping"),
        Industry(industry_id=62, industry_name="Medical Care Facilities"),
        Industry(industry_id=63, industry_name="Medical Devices"),
        Industry(industry_id=64, industry_name="Medical Distribution"),
        Industry(industry_id=65, industry_name="Medical Instruments & Supplies"),
        Industry(industry_id=66, industry_name="Metal Fabrication"),
        Industry(industry_id=67, industry_name="Mortgage Finance"),
        Industry(industry_id=68, industry_name="Oil & Gas E&P"),
        Industry(industry_id=69, industry_name="Oil & Gas Equipment & Services"),
        Industry(industry_id=70, industry_name="Oil & Gas Integrated"),
        Industry(industry_id=71, industry_name="Oil & Gas Midstream"),
        Industry(industry_id=72, industry_name="Oil & Gas Refining & Marketing"),
        Industry(industry_id=73, industry_name="Packaged Foods"),
        Industry(industry_id=74, industry_name="Packaging & Containers"),
        Industry(industry_id=75, industry_name="Personal Services"),
        Industry(industry_id=76, industry_name="Pollution & Treatment Controls"),
        Industry(industry_id=77, industry_name="Railroads"),
        Industry(industry_id=78, industry_name="Real Estate - Development"),
        Industry(industry_id=79, industry_name="Real Estate Services"),
        Industry(industry_id=80, industry_name="Recreational Vehicles"),
        Industry(industry_id=81, industry_name="REIT - Diversified"),
        Industry(industry_id=82, industry_name="REIT - Healthcare Facilities"),
        Industry(industry_id=83, industry_name="REIT - Hotel & Motel"),
        Industry(industry_id=84, industry_name="REIT - Industrial"),
        Industry(industry_id=85, industry_name="REIT - Mortgage"),
        Industry(industry_id=86, industry_name="REIT - Office"),
        Industry(industry_id=87, industry_name="REIT - Residential"),
        Industry(industry_id=88, industry_name="REIT - Retail"),
        Industry(industry_id=89, industry_name="REIT - Specialty"),
        Industry(industry_id=90, industry_name="Rental & Leasing Services"),
        Industry(industry_id=91, industry_name="Residential Construction"),
        Industry(industry_id=92, industry_name="Resorts & Casinos"),
        Industry(industry_id=93, industry_name="Restaurants"),
        Industry(industry_id=94, industry_name="Scientific & Technical Instruments"),
        Industry(industry_id=95, industry_name="Security & Protection Services"),
        Industry(industry_id=96, industry_name="Semiconductor Equipment & Materials"),
        Industry(industry_id=97, industry_name="Semiconductors"),
        Industry(industry_id=98, industry_name="Software - Application"),
        Industry(industry_id=99, industry_name="Software - Infrastructure"),
        Industry(industry_id=100, industry_name="Specialty Business Services"),
        Industry(industry_id=101, industry_name="Specialty Chemicals"),
        Industry(industry_id=102, industry_name="Specialty Industrial Machinery"),
        Industry(industry_id=103, industry_name="Specialty Retail"),
        Industry(industry_id=104, industry_name="Staffing & Employment Services"),
        Industry(industry_id=105, industry_name="Steel"),
        Industry(industry_id=106, industry_name="Telecom Services"),
        Industry(industry_id=107, industry_name="Thermal Coal"),
        Industry(industry_id=108, industry_name="Tobacco"),
        Industry(industry_id=109, industry_name="Tools & Accessories"),
        Industry(industry_id=110, industry_name="Travel Services"),
        Industry(industry_id=111, industry_name="Trucking"),
        Industry(industry_id=112, industry_name="Utilities - Diversified"),
        Industry(industry_id=113, industry_name="Utilities - Regulated Electric"),
        Industry(industry_id=114, industry_name="Utilities - Regulated Gas"),
        Industry(industry_id=115, industry_name="Utilities - Regulated Water"),
        Industry(industry_id=116, industry_name="Utilities - Renewable"),
        Industry(industry_id=117, industry_name="Waste Management"),
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
