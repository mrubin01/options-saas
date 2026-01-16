from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.user import User
from app.auth.security import hash_password, verify_password
from app.auth.jwt import create_access_token
from app.schemas.user import UserCreate
from fastapi.security import OAuth2PasswordRequestForm
from app.auth.deps import get_current_user
from app.core.middleware.logging import get_logger
from app.schemas.response import ApiResponse, ErrorModel
from app.schemas.user import UserOut, LoginResponseData
from app.schemas.api import ApiResponse, ApiError
from typing import List

logger = get_logger("auth")

router = APIRouter(tags=["auth"])

@router.post("/register")
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user_in.email).first():
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    user = User(
        email=user_in.email,
        password_hash=hash_password(user_in.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    logger.info("New user registered", extra={"email": user.email})

    return {"id": user.id, "email": user.email}

@router.post("/login", response_model=ApiResponse[LoginResponseData])
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = db.query(User).filter(User.email == form_data.username).first()

    logger.info("Attempting login for user", extra={"email": form_data.username})

    if not user or not verify_password(form_data.password, user.password_hash):
        logger.warning("Login failed", extra={"email": form_data.username})
        return ApiResponse(
            success=False,
            data=None,
            error=ApiError(
                code="INVALID_CREDENTIALS",
                message="Invalid email or password",
            ),
        )

    token = create_access_token({"sub": str(user.id)})

    return ApiResponse(
        success=True,
        data=LoginResponseData(
            access_token=token,
            token_type="bearer",
            user=UserOut.from_orm(user),
        ),
        error=None,
    )

@router.get("/me", response_model=ApiResponse[List[UserOut]])
def me(current_user: User = Depends(get_current_user)):
    return ApiResponse(
        success=True,
        data=UserOut.from_orm(current_user),
        error=None
    )

