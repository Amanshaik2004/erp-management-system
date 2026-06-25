from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.employee import Employee
from models.notification import Notification

from schemas.notification import NotificationCreate


def create_notification(
    data: NotificationCreate,
    db: Session
):

    employee = db.query(Employee).filter(
        Employee.id == data.employee_id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    notification = Notification(
        **data.model_dump()
    )

    db.add(notification)

    db.commit()

    db.refresh(notification)

    return notification


def get_notifications(
    employee_id: int,
    db: Session
):

    return db.query(Notification).filter(
        Notification.employee_id == employee_id
    ).all()


def mark_as_read(
    notification_id: int,
    db: Session
):

    notification = db.query(Notification).filter(
        Notification.id == notification_id
    ).first()

    if not notification:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    notification.is_read = True

    db.commit()

    db.refresh(notification)

    return notification