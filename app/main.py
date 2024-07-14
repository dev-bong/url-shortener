from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api import router
from app.core import db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 앱 시작
    db.init()
    yield
    # 앱 종료


app = FastAPI(lifespan=lifespan)

app.include_router(router, tags=["API"])
