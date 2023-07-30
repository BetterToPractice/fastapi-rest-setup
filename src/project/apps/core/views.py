from . import router


@router.get("/")
async def home_view():
    return {
        "status": "OK"
    }
