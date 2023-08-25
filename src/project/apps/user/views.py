from typing import List

from fastapi import Depends
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from libs.db import get_session

from . import router
from .models import User


@router.get("/users", response_model=List[User])
async def user_list_view(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User))
    users = result.scalars().all()

    return users
