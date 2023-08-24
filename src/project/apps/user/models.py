from sqlmodel import Field

from libs.db import SQLModel


class User(SQLModel, table=True):
    __tablename__ = "users_users"

    id: int = Field(
        default=None,
        nullable=False,
        primary_key=True,
    )
    name: str = Field(
        nullable=True,
        max_length=200,
        min_length=3,
    )
