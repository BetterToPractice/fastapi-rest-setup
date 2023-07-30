from fastapi import FastAPI


def create_application() -> FastAPI:
    app = FastAPI()

    register_routers(app)

    return app


def register_routers(app: FastAPI) -> None:
    from apps.core import router as core_router
    from apps.user import router as user_router

    app.include_router(core_router)
    app.include_router(user_router)

