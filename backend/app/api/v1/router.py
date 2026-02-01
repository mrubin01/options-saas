from fastapi import APIRouter

from app.api.v1 import auth, covered_calls, put_options, spread_options, metrics, health

router = APIRouter(prefix="/api/v1")

router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(covered_calls.router, prefix="/covered-calls", tags=["Covered Calls"])
router.include_router(put_options.router, prefix="/put-options", tags=["Put Options"])
router.include_router(spread_options.router, prefix="/spread-options", tags=["Spread Options"])
router.include_router(metrics.router, prefix="/metrics", tags=["Metrics"])
router.include_router(health.router, prefix="/health", tags=["Health"])
