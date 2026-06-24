from fastapi import APIRouter
from fastapi import Depends

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


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register")
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):

    return register_user(
        user,
        db
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