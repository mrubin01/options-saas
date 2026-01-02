import time
from fastapi import Request, Response

from app.core.metrics import REQUEST_COUNT, REQUEST_LATENCY


async def metrics_middleware(request: Request, call_next):
    start_time = time.perf_counter()

    response: Response = await call_next(request)

    elapsed = time.perf_counter() - start_time

    # Normalize path (avoid cardinality explosion)
    path = request.url.path

    REQUEST_LATENCY.labels(
        method=request.method,
        path=path,
    ).observe(elapsed)

    REQUEST_COUNT.labels(
        method=request.method,
        path=path,
        status=response.status_code,
    ).inc()

    return response
