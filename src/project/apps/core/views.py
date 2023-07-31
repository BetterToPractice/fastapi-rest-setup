from fastapi import Depends
from typing_extensions import Annotated

from configs.settings import Settings, get_settings
from . import router


@router.get("/")
async def home_view(settings: Annotated[Settings, Depends(get_settings)]):
    return {
        "status": "OK",
        "debug": settings.debug,
        "environment": settings.environment,
    }
