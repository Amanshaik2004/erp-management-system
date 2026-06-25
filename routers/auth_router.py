from fastapi import APIRouter
from fastapi import Depends
from fastapi import BackgroundTasks


from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from database import get_db

from schemas.auth import UserRegister
from schemas.auth import UserRegister, UserLogin

from services.auth_service import (
    register_user,
    login_user
)

from services.auth_service import register_user
from schemas.auth import RefreshTokenRequest
from services.auth_service import refresh_access_token
from schemas.auth import ForgotPasswordRequest
from services.auth_service import forgot_password
from schemas.auth import ResetPasswordRequest
from services.auth_service import reset_password


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register")
def register(
    user: UserRegister,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    return register_user(
        user,
        db,
        background_tasks
    )

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    return login_user(
        form_data.username,
        form_data.password,
        db
    )

@router.post("/refresh-token")
def refresh_token(
    request: RefreshTokenRequest
):

    return refresh_access_token(
        request.refresh_token
    )

@router.post("/forgot-password")
def forgot_password_api(
    request: ForgotPasswordRequest,
    db: Session = Depends(get_db)
):
    return forgot_password(
        request,
        db
    )

@router.post("/reset-password")
def reset_password_api(
    request: ResetPasswordRequest,
    db: Session = Depends(get_db)
):
    return reset_password(
        request,
        db
    )