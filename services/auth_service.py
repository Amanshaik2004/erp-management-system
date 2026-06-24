from sqlalchemy.orm import Session

from fastapi import HTTPException
from utils.jwt import create_access_token

from models.user import User
from models.role import Role

from schemas.auth import UserRegister

from utils.password import hash_password

def register_user(
    user: UserRegister,
    db: Session
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

    return {
        "message": "User registered successfully",
        "user_id": new_user.id
    }

from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.user import User
from schemas.auth import UserLogin
from utils.password import verify_password


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

    token = create_access_token(
    {
        "sub": db_user.email,
        "role": db_user.role.role_name,
        "user_id": db_user.id
    }
    )

    return {
    "access_token": token,
    "token_type": "bearer"
    }