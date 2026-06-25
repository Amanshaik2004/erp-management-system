from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from schemas.project import (
    ProjectCreate,
    ProjectUpdate,
    ProjectResponse
)

from services.project_service import *

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.post("/", response_model=ProjectResponse)
def create(
    project: ProjectCreate,
    db: Session = Depends(get_db)
):
    return create_project(project, db)


@router.get("/", response_model=list[ProjectResponse])
def get_all(
    db: Session = Depends(get_db)
):
    return get_all_projects(db)


@router.get("/{project_id}", response_model=ProjectResponse)
def get_one(
    project_id: int,
    db: Session = Depends(get_db)
):
    return get_project_by_id(project_id, db)


@router.put("/{project_id}", response_model=ProjectResponse)
def update(
    project_id: int,
    project: ProjectUpdate,
    db: Session = Depends(get_db)
):
    return update_project(project_id, project, db)


@router.delete("/{project_id}")
def delete(
    project_id: int,
    db: Session = Depends(get_db)
):
    return delete_project(project_id, db)