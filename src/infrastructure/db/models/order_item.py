from __future__ import annotations

from sqlmodel import Field, Relationship
from sqlalchemy.orm import relationship

from src.domain.entities.order_item import OrderItem
from src.infrastructure.db.models import BaseORM
from src.infrastructure.db.models.product import ProductORM


class OrderItemORM(BaseORM[OrderItem]):
    __tablename__ = "order_items"

    id: int = Field(primary_key=True)
    order_id: int = Field(foreign_key="orders.id")
    product_id: int = Field(foreign_key="products.id")
    quantity: int
    price: float

    order: "OrderORM" = Relationship(
        sa_relationship=relationship(
            "OrderORM",
            back_populates="items",
            lazy="selectin",
        )
    )

    product: ProductORM = Relationship(
        sa_relationship=relationship(
            "ProductORM",
            lazy="selectin",
        )
    )

    def to_entity(self) -> OrderItem:
        return OrderItem(
            id=self.id,
            product=self.product.to_entity(),
            quantity=self.quantity,
            price=self.price,
        )

    @classmethod
    def from_entity(cls, entity: OrderItem) -> OrderItemORM:
        return cls(
            id=entity.id,
            product_id=entity.product.id,
            quantity=entity.quantity,
            price=entity.price,
        )
