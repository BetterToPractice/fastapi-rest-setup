import os
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseSettings

# Path
ROOT_DIR = Path(__file__).parent.parent.parent.parent
APP_DIR = Path(__file__).parent


load_dotenv(ROOT_DIR / ".env")


class Settings(BaseSettings):
    app_name: str = os.environ.get("APP_NAME", default="project")
    environment: str = os.environ.get("ENVIRONMENT", default="development")
    debug: bool = os.environ.get("DEBUG", default=True)
    sqlalchemy_database_url: str = os.environ.get(
        "SQLALCHEMY_DATABASE_URL",
        default="postgresql+asyncpg://setup_user:setup_password@localhost:5432/setup_db",
    )

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    result = Settings()
    return result
