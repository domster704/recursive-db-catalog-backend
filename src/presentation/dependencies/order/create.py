from fastapi import Depends

from src.application.providers.uow import uow_provider
from src.application.usecase.order.create import CreateOrderUseCase
from src.infrastructure.db.repositories.order import OrderRepository
from src.infrastructure.db.repositories.order_item import OrderItemRepository
from src.infrastructure.db.repositories.product import ProductRepository


def get_create_order_use_case(uow=Depends(uow_provider)):
    return CreateOrderUseCase(
        order_repository=OrderRepository(uow),
        order_item_repository=OrderItemRepository(uow),
        product_repository=ProductRepository(uow),
    )
