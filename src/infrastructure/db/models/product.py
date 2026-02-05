from __future__ import annotations

from sqlalchemy.orm import relationship
from sqlmodel import Field, Relationship

from src.domain.entities.product import Product
from src.infrastructure.db.models import BaseORM


class ProductORM(BaseORM[Product], table=True):
    __tablename__ = "products"

    id: int = Field(primary_key=True, nullable=False)
    name: str
    quantity: int
    price: float
    category_id: int = Field(foreign_key="categories.id")

    category: "CategoryORM" = Relationship(
        sa_relationship=relationship(
            "CategoryORM",
            back_populates="products",
            lazy="selectin",
        )
    )

    order_items: list["OrderItemORM"] = Relationship(
        sa_relationship=relationship(
            "OrderItemORM",
            back_populates="product",
            lazy="selectin",
        )
    )

    def to_entity(self) -> Product:
        return Product(
            id=self.id,
            name=self.name,
            quantity=self.quantity,
            price=self.price,
            category=self.category.to_entity(),
        )

    @classmethod
    def from_entity(cls, entity: Product) -> ProductORM:
        return cls(
            id=entity.id,
            name=entity.name,
            quantity=entity.quantity,
            price=entity.price,
            category_id=entity.category.id,
        )
