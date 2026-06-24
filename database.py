from sqlalchemy import create_engine

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from config import settings


# Create Database Engine
engine = create_engine(
    settings.DATABASE_URL,
    echo=True
)


# Create Session Factory
SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)


# Base class for all SQLAlchemy models
Base = declarative_base()


# Database Dependency
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()