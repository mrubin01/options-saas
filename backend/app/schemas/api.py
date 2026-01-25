from typing import Generic, Optional, TypeVar
from pydantic import BaseModel

T = TypeVar("T")

class ApiError(BaseModel):
    code: str
    message: str

class ApiResponse(BaseModel, Generic[T]):
    success: bool
    data: Optional[T]
    error: Optional[ApiError]
