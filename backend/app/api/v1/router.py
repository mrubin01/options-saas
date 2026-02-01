from fastapi import APIRouter

from app.api.v1.auth import router as auth_router
from app.api.v1.covered_calls import router as covered_calls_router
from app.api.v1.put_options import router as put_options_router
from app.api.v1.spread_options import router as spread_options_router
from app.api.v1 import metrics, health

router = APIRouter()

router.include_router(auth_router, prefix="/auth", tags=["auth"])
router.include_router(covered_calls_router, prefix="/covered-calls")
router.include_router(put_options_router, prefix="/put-options")
router.include_router(spread_options_router, prefix="/spread-options")
router.include_router(metrics.router, prefix="/metrics", tags=["Metrics"])
router.include_router(health.router, prefix="/health", tags=["Health"])
