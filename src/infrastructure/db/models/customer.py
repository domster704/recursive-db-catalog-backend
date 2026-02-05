from __future__ import annotations

from sqlalchemy.orm import relationship
from sqlmodel import Field, Relationship

from src.domain.entities.customer import Customer
from src.infrastructure.db.models import BaseORM


class CustomerORM(BaseORM[Customer], table=True):
    __tablename__ = "customers"

    id: int = Field(primary_key=True)
    name: str
    address: str

    orders: list["OrderORM"] = Relationship(
        sa_relationship=relationship(
            "OrderORM",
            back_populates="customer",
            lazy="selectin",
        )
    )

    def to_entity(self) -> Customer:
        return Customer(
            id=self.id,
            name=self.name,
            address=self.address,
        )

    @classmethod
    def from_entity(cls, entity: Customer) -> CustomerORM:
        return cls(
            id=entity.id,
            name=entity.name,
            address=entity.address,
        )
