from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from schemas.project_task import (
    ProjectTaskCreate,
    ProjectTaskUpdate,
    ProjectTaskResponse
)

from services.project_task_service import *

router = APIRouter(
    prefix="/project-tasks",
    tags=["Project Tasks"]
)


@router.post("/", response_model=ProjectTaskResponse)
def create(
    task: ProjectTaskCreate,
    db: Session = Depends(get_db)
):
    return create_project_task(task, db)


@router.get("/", response_model=list[ProjectTaskResponse])
def get_all(
    db: Session = Depends(get_db)
):
    return get_all_project_tasks(db)


@router.get("/{task_id}", response_model=ProjectTaskResponse)
def get_one(
    task_id: int,
    db: Session = Depends(get_db)
):
    return get_project_task_by_id(task_id, db)


@router.put("/{task_id}", response_model=ProjectTaskResponse)
def update(
    task_id: int,
    task: ProjectTaskUpdate,
    db: Session = Depends(get_db)
):
    return update_project_task(task_id, task, db)


@router.delete("/{task_id}")
def delete(
    task_id: int,
    db: Session = Depends(get_db)
):
    return delete_project_task(task_id, db)