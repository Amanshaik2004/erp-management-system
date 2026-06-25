from sqlalchemy.orm import Session
from services.email_service import send_email
from fastapi import BackgroundTasks

from fastapi import HTTPException

from models.user import User
from models.role import Role
from schemas.auth import UserRegister
from utils.jwt import create_access_token
from utils.security import create_refresh_token
from schemas.auth import ForgotPasswordRequest
from services.email_service import send_email


from utils.password import hash_password

def register_user(
    user: UserRegister,
    db: Session,
    background_tasks: BackgroundTasks
):

    # Check username

    existing_username = db.query(User).filter(
        User.username == user.username
    ).first()

    if existing_username:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    # Check email

    existing_email = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    # Check role

    existing_role = db.query(Role).filter(
        Role.id == user.role_id
    ).first()

    if not existing_role:
        raise HTTPException(
            status_code=404,
            detail="Role not found"
        )

    # Hash password

    hashed_password = hash_password(
        user.password
    )

    # Create user

    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hashed_password,
        role_id=user.role_id
    )

    # Save

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    background_tasks.add_task(
    send_email,
    new_user.email,
    "Registration Successful",
    f"Hello {new_user.username}, your ERP account has been created successfully."
    )

    return new_user

from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.user import User
from schemas.auth import UserLogin
from utils.password import verify_password
from jose import jwt, JWTError
from utils.password import hash_password


def login_user(
    email: str,
    password: str,
    db: Session
):
    # Check if user exists
    db_user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # Verify password
    if not verify_password(
    password,
    db_user.password_hash):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token_data = {
    "sub": db_user.email,
    "role": db_user.role.role_name,
    "user_id": db_user.id
    }

    access_token = create_access_token(token_data)

    refresh_token = create_refresh_token(token_data)
    
    return {
    "access_token": access_token,
    "refresh_token": refresh_token,
    "token_type": "bearer"
    }

from jose import JWTError, jwt

from config import settings


def refresh_access_token(refresh_token: str):

    try:

        payload = jwt.decode(
            refresh_token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        token_data = {
            "sub": payload["sub"],
            "role": payload["role"],
            "user_id": payload["user_id"]
        }

        access_token = create_access_token(token_data)

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid refresh token"
        )

def forgot_password(
    request: ForgotPasswordRequest,
    db: Session
):

    user = (
        db.query(User)
        .filter(User.email == request.email)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    token_data = {
        "sub": user.email,
        "user_id": user.id
    }

    reset_token = create_access_token(token_data)

    send_email(
        to_email=user.email,
        subject="Password Reset",
        message=f"Your password reset token is:\n\n{reset_token}"
    )

    return {
        "message": "Password reset email sent successfully"
    }

def reset_password(
    request: ResetPasswordRequest,
    db: Session
):

    try:

        payload = jwt.decode(
            request.token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

    user = (
        db.query(User)
        .filter(User.email == payload["sub"])
        .first()
    )

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    user.password_hash = hash_password(
        request.new_password
    )

    db.commit()

    return {
        "message": "Password reset successfully"
    }