from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.infrastructure.db.db import init_db
from src.presentation.api.router_v1 import api_v1_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()

    yield


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(api_v1_router)
    return app

