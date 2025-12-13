from fastapi import FastAPI
from app.db.database import Base, engine

app = FastAPI()

# Create tables automatically
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"status": "backend is running"}

