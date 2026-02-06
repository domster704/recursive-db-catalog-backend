from __future__ import annotations

from datetime import date

from sqlalchemy.orm import relationship
from sqlmodel import Field, Relationship

from src.domain.entities.order import Order
from src.infrastructure.db.models import BaseORM


class OrderORM(BaseORM[Order], table=True):
    __tablename__ = "orders"

    id: int = Field(primary_key=True)
    order_date: date
    status: str  # Можно сделать enum, но для тестового задания проще просто строки: created, paid, delivered, shipped, cancelled
    customer_id: int = Field(foreign_key="customers.id")

    customer: "CustomerORM" = Relationship(
        sa_relationship=relationship(
            "CustomerORM",
            back_populates="orders",
            lazy="selectin",
        )
    )

    items: list["OrderItemORM"] = Relationship(
        sa_relationship=relationship(
            "OrderItemORM",
            back_populates="order",
            lazy="selectin",
            cascade="all, delete-orphan",
            passive_deletes=True,
        )
    )

    def to_entity(self) -> Order:
        return Order(
            id=self.id,
            customer=self.customer.to_entity(),
            order_date=self.order_date,
            status=self.status,
            items=[item.to_entity() for item in self.items],
        )

    @classmethod
    def from_entity(cls, entity: Order) -> OrderORM:
        return cls(
            id=entity.id,
            customer_id=entity.customer.id,
            order_date=entity.order_date,
            status=entity.status,
        )
