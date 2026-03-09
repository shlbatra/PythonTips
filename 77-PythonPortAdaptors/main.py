from contextlib import asynccontextmanager

from api import router
from db import init_db
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db("sqlite:///./before.db")
    yield


app = FastAPI(title="Ports & adapters", lifespan=lifespan)


app.include_router(router)