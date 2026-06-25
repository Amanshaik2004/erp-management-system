from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from schemas.notification import (
    NotificationCreate,
    NotificationResponse
)

from services.notification_service import *

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)


@router.post(
    "/",
    response_model=NotificationResponse
)
def create(
    notification: NotificationCreate,
    db: Session = Depends(get_db)
):

    return create_notification(
        notification,
        db
    )


@router.get(
    "/{employee_id}",
    response_model=list[NotificationResponse]
)
def get_all(
    employee_id: int,
    db: Session = Depends(get_db)
):

    return get_notifications(
        employee_id,
        db
    )


@router.put(
    "/read/{notification_id}",
    response_model=NotificationResponse
)
def read(
    notification_id: int,
    db: Session = Depends(get_db)
):

    return mark_as_read(
        notification_id,
        db
    )