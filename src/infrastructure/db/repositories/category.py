from src.domain.entities.category import Category
from src.infrastructure.db.models import CategoryORM
from src.infrastructure.db.repositories.base import BaseRepository
from src.infrastructure.db.uow import UnitOfWork


class CategoryRepository(BaseRepository[CategoryORM, Category]):
    def __init__(self, uow: UnitOfWork):
        super().__init__(
            model=CategoryORM,
            entity=Category,
            uow=uow,
        )
