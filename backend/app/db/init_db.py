from app.db.database import Base, engine
from app import models  # ensure all models are imported

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")
