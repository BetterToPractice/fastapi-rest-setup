import os

from sqlmodel import create_engine, SQLModel, Session

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    default="postgresql+asyncpg://setup_user:setup_password@localhost:5432/setup_db",
)
engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)
