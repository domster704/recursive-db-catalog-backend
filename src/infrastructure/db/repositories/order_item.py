from src.domain.entities.order import OrderItem
from src.infrastructure.db.models import OrderItemORM
from src.infrastructure.db.repositories.base import BaseRepository
from src.infrastructure.db.uow import UnitOfWork


class OrderItemRepository(BaseRepository[OrderItemORM, OrderItem]):
    def __init__(self, uow: UnitOfWork):
        super().__init__(
            model=OrderItemORM,
            entity=OrderItem,
            uow=uow,
        )
