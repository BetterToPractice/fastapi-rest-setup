from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel as CoreSQLModel, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession

from configs.settings import get_settings

settings = get_settings()


DATABASE_URL = settings.sqlalchemy_database_url
engine = AsyncEngine(create_engine(DATABASE_URL, echo=True))


async def get_session() -> AsyncSession:
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session


class SQLModel(CoreSQLModel):
    ...
