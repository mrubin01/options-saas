from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from app.db.database import Base, engine
from app import models
from app.api.covered_calls import router as covered_calls_router
from app.api.put_options import router as put_options_router
from app.api.spread_options import router as spread_options_router
# from app.api import auth
from app.api.auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware
from app.core.logging import setup_logging
from app.core.middleware import logging_middleware

setup_logging()

app = FastAPI(title="Options SaaS API")
app.middleware("http")(logging_middleware)

# CORS (development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# create tables automatically TEMPORARY
# Base.metadata.create_all(bind=engine) --> Alembic will handle migrations

# routers
app.include_router(covered_calls_router)
app.include_router(put_options_router)
app.include_router(spread_options_router)
app.include_router(auth_router, prefix="/auth")

@app.get("/")
def root():
    return {"status": "backend is running"}

