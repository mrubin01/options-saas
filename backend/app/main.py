from fastapi import FastAPI
from app.db.database import Base, engine
from app import models
from app.api.covered_calls import router as covered_calls_router
from app.api.put_options import router as put_options_router
from app.api.spread_options import router as spread_options_router

app = FastAPI(title="Options SaaS API")

# create tables automatically TEMPORARY
Base.metadata.create_all(bind=engine)

# routers
app.include_router(covered_calls_router)
app.include_router(put_options_router)
app.include_router(spread_options_router)

@app.get("/")
def root():
    return {"status": "backend is running"}

