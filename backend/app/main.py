from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, Request, HTTPException
from fastapi.exceptions import RequestValidationError
from app.core.exceptions import (
    http_exception_handler,
    validation_exception_handler,
    unhandled_exception_handler,
)
from app.db.database import Base, engine
from app import models
# from app.api.covered_calls import router as covered_calls_router
# from app.api.put_options import router as put_options_router
# from app.api.spread_options import router as spread_options_router
# from app.api import auth
# from app.api.auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware
from app.core.middleware.logging import setup_logging, request_id_ctx
from app.core.middleware.request_id import RequestIdMiddleware
from app.core.sentry import init_sentry
from app.core.middleware.request_logging import logging_middleware
from app.core.middleware.metrics import metrics_middleware, metrics_endpoint
# from app.api.health import router as health_router
from app.api.v1.router import router as v1_router
import os

setup_logging()

init_sentry()

app = FastAPI(title="Options SaaS API")

@app.on_event("startup")
def startup_checks():
    import app.api.v1.auth
    import app.core.middleware.logging
    import app.core.middleware.metrics

# ---- Global exception handlers ----
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)

# ---- middleware ---- 
app.add_middleware(RequestIdMiddleware)
app.middleware("http")(logging_middleware)
app.middleware("http")(metrics_middleware)

# CORS (development)
cors_origins = os.getenv("CORS_ORIGINS", "")
ALLOWED_ORIGINS = [o.strip() for o in cors_origins.split(",") if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# create tables automatically TEMPORARY
# Base.metadata.create_all(bind=engine) --> Alembic will handle migrations

# routers
# app.include_router(covered_calls_router)
# app.include_router(put_options_router)
# app.include_router(spread_options_router)
# app.include_router(auth_router, prefix="/auth")
# app.include_router(health_router)
app.include_router(v1_router)

@app.get("/")
def root():
    return {"status": "backend is running"}

# metrics endpoint
@app.get("/metrics")
def metrics():
    return metrics_endpoint()
