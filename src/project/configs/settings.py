import os
from functools import lru_cache
from pathlib import Path

# Path
ROOT_DIR = Path(__file__).parent.parent.parent.parent
APP_DIR = Path(__file__).parent


class Settings:
    app_name: str = os.environ.get("APP_NAME", default="project")
    environment: str = os.environ.get("ENVIRONMENT", default="development")
    debug: bool = os.environ.get("DEBUG", default=True)


@lru_cache()
def get_settings():
    return Settings()
