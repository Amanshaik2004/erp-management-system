from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.project import Project

from schemas.project import (
    ProjectCreate,
    ProjectUpdate
)


def create_project(project: ProjectCreate, db: Session):

    db_project = Project(**project.model_dump())

    db.add(db_project)
    db.commit()
    db.refresh(db_project)

    return db_project


def get_all_projects(db: Session):

    return db.query(Project).all()


def get_project_by_id(project_id: int, db: Session):

    project = (
        db.query(Project)
        .filter(Project.id == project_id)
        .first()
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return project


def update_project(
    project_id: int,
    project_data: ProjectUpdate,
    db: Session
):

    project = (
        db.query(Project)
        .filter(Project.id == project_id)
        .first()
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    for key, value in project_data.model_dump().items():
        setattr(project, key, value)

    db.commit()
    db.refresh(project)

    return project


def delete_project(
    project_id: int,
    db: Session
):

    project = (
        db.query(Project)
        .filter(Project.id == project_id)
        .first()
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    db.delete(project)
    db.commit()

    return {
        "message": "Project deleted successfully"
    }