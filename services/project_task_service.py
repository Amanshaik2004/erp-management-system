from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.project import Project
from models.employee import Employee
from models.project_task import ProjectTask

from schemas.project_task import (
    ProjectTaskCreate,
    ProjectTaskUpdate
)


def create_project_task(data: ProjectTaskCreate, db: Session):

    project = db.query(Project).filter(
        Project.id == data.project_id
    ).first()

    if not project:
        raise HTTPException(404, "Project not found")

    employee = db.query(Employee).filter(
        Employee.id == data.employee_id
    ).first()

    if not employee:
        raise HTTPException(404, "Employee not found")

    task = ProjectTask(**data.model_dump())

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


def get_all_project_tasks(db: Session):

    return db.query(ProjectTask).all()


def get_project_task_by_id(task_id: int, db: Session):

    task = db.query(ProjectTask).filter(
        ProjectTask.id == task_id
    ).first()

    if not task:
        raise HTTPException(404, "Task not found")

    return task


from fastapi import HTTPException

VALID_WORKFLOW = {
    "TODO": ["IN_PROGRESS"],
    "IN_PROGRESS": ["COMPLETED"],
    "COMPLETED": []
}


def update_project_task(
    task_id: int,
    data: ProjectTaskUpdate,
    db: Session
):

    task = db.query(ProjectTask).filter(
        ProjectTask.id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    current_status = task.status

    new_status = data.status

    if new_status != current_status:

        if new_status not in VALID_WORKFLOW[current_status]:

            raise HTTPException(
                status_code=400,
                detail=f"Invalid workflow. Cannot move from {current_status} to {new_status}"
            )

    task.task_name = data.task_name
    task.description = data.description
    task.status = new_status

    db.commit()
    db.refresh(task)

    return task


def delete_project_task(task_id: int, db: Session):

    task = db.query(ProjectTask).filter(
        ProjectTask.id == task_id
    ).first()

    if not task:
        raise HTTPException(404, "Task not found")

    db.delete(task)
    db.commit()

    return {
        "message": "Project task deleted successfully"
    }