from functools import lru_cache
from typing import Annotated

from fastapi import Depends, FastAPI

from app.core.config import Settings
from app.routers import auth

app = FastAPI()

app.include_router(auth.router)

@lru_cache
def get_settings():
    return Settings()


@app.get("/info")
async def info(settings: Annotated[Settings, Depends(get_settings)]):
    return {
        "app_name": settings.APP_NAME
    }