from fastapi import APIRouter

from src.presentation.api.v1.order_router import order_router

api_v1_router = APIRouter(prefix="/api/v1")

api_v1_router.include_router(order_router)
