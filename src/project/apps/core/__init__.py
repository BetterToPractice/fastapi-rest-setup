from fastapi import APIRouter

router = APIRouter()

from . import views  # noqa
