from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
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
