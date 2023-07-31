import os
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

# Path
ROOT_DIR = Path(__file__).parent.parent.parent.parent
APP_DIR = Path(__file__).parent


class Settings(BaseSettings):
    app_name: str = os.environ.get("APP_NAME", default="project")
    environment: str = os.environ.get("ENVIRONMENT", default="development")
    debug: bool = os.environ.get("DEBUG", default=True)

    model_config = SettingsConfigDict(env_file=ROOT_DIR / '.env')


@lru_cache()
def get_settings():
    return Settings()
