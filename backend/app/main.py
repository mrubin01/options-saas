from fastapi import FastAPI
from app.db.database import Base, engine
from app import models
from app.api.covered_calls import router as covered_calls_router

app = FastAPI(title="Options SaaS API")

# create tables automatically
Base.metadata.create_all(bind=engine)

# routers
app.include_router(covered_calls_router)

@app.get("/")
def root():
    return {"status": "backend is running"}

