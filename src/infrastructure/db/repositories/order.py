from src.domain.entities.order import Order
from src.infrastructure.db.models import OrderORM
from src.infrastructure.db.repositories.base import BaseRepository
from src.infrastructure.db.uow import UnitOfWork


class OrderRepository(BaseRepository[OrderORM, Order]):
    def __init__(self, uow: UnitOfWork):
        super().__init__(
            model=OrderORM,
            entity=Order,
            uow=uow,
        )
