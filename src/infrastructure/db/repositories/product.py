from src.domain.entities.product import Product
from src.infrastructure.db.models import ProductORM
from src.infrastructure.db.repositories.base import BaseRepository
from src.infrastructure.db.uow import UnitOfWork


class ProductRepository(BaseRepository[ProductORM, Product]):
    def __init__(self, uow: UnitOfWork):
        super().__init__(
            model=ProductORM,
            entity=Product,
            uow=uow,
        )
