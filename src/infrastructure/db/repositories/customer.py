from src.domain.entities.customer import Customer
from src.infrastructure.db.models import CustomerORM
from src.infrastructure.db.repositories.base import BaseRepository
from src.infrastructure.db.uow import UnitOfWork


class CustomerRepository(BaseRepository[CustomerORM, Customer]):
    def __init__(self, uow: UnitOfWork):
        super().__init__(
            model=CustomerORM,
            entity=Customer,
            uow=uow,
        )
