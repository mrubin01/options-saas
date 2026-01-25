from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

from app.schemas.api import ApiResponse, ApiError


def http_exception_handler(request: Request, exc: HTTPException):
    """
    Handles HTTPException (401, 403, 404, etc.)
    """
    detail = exc.detail

    if isinstance(detail, dict):
        error = ApiError(
            code=detail.get("code", "HTTP_ERROR"),
            message=detail.get("message", "Request failed"),
        )
    else:
        error = ApiError(
            code="HTTP_ERROR",
            message=str(detail),
        )

    return JSONResponse(
        status_code=exc.status_code,
        content=ApiResponse(
            success=False,
            data=None,
            error=error,
        ).dict(),
    )


def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    Handles Pydantic / request validation errors
    """
    return JSONResponse(
        status_code=422,
        content=ApiResponse(
            success=False,
            data=None,
            error=ApiError(
                code="VALIDATION_ERROR",
                message="Invalid request parameters",
            ),
        ).dict(),
    )


def unhandled_exception_handler(request: Request, exc: Exception):
    """
    Handles unexpected server errors
    """
    return JSONResponse(
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
        content=ApiResponse(
            success=False,
            data=None,
            error=ApiError(
                code="INTERNAL_SERVER_ERROR",
                message="Unexpected server error",
            ),
        ).dict(),
    )
