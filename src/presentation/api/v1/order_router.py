from fastapi import APIRouter
from fastapi.params import Depends
from starlette.responses import JSONResponse

from src.application.exceptions.not_enough_product import NotEnoughProductQuantity
from src.application.exceptions.not_found import NotFound
from src.application.usecase.order.create import CreateOrderUseCase
from src.presentation.dependencies.order.create import get_create_order_use_case
from src.presentation.schemas.order.create import CreateOrderSchema

order_router = APIRouter(prefix="/order", tags=["order"])


@order_router.post(
    "/",
    summary="Создать или дополнить заказ",
    description="Создаёт или дополняет заказ с указанным товаром и количеством",
    responses={
        404: {"description": "Товар не найден"},
        409: {"description": "Недостаточно товара на складе"},
    },
)
async def create_order(
    body: CreateOrderSchema,
    use_case: CreateOrderUseCase = Depends(get_create_order_use_case),
):
    try:
        await use_case.execute(
            order_id=body.order_id, product_id=body.product_id, quantity=body.quantity
        )

        return JSONResponse(status_code=200, content={"message": "OK"})
    except NotFound as e:
        return JSONResponse(status_code=404, content={"message": str(e)})
    except NotEnoughProductQuantity as e:
        return JSONResponse(status_code=409, content={"message": str(e)})
