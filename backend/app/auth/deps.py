from fastapi import Depends, HTTPException, status, Request
from fastapi.security import HTTPBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.user import User
from typing import Optional
from app.core.security import SECRET_KEY, ALGORITHM

# oauth2_scheme = OAuth2PasswordBearer(
#     tokenUrl="auth/login",
#     auto_error=False
# )

bearer_scheme = HTTPBearer()

async def get_current_user(
    request: Request,
    credentials = Depends(bearer_scheme),
    db: Session = Depends(get_db),
) -> Optional[User]:

    token = credentials.credentials

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
            )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

    user = db.get(User, int(user_id))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )

    return user

