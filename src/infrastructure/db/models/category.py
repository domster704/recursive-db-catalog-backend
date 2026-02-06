from __future__ import annotations

from sqlalchemy.orm import relationship
from sqlmodel import Field, Relationship

from src.domain.entities.category import Category
from src.infrastructure.db.models import BaseORM


class CategoryORM(BaseORM[Category], table=True):
    __tablename__ = "categories"

    id: int = Field(primary_key=True)
    name: str
    parent_id: int | None = Field(
        foreign_key="categories.id", nullable=True, ondelete="CASCADE"
    )

    parent: CategoryORM | None = Relationship(
        sa_relationship=relationship(
            "CategoryORM",
            remote_side=lambda: CategoryORM.id,
            back_populates="children",
            lazy="selectin",
        )
    )

    children: list[CategoryORM] = Relationship(
        sa_relationship=relationship(
            "CategoryORM",
            back_populates="parent",
            cascade="all, delete-orphan",
            passive_deletes=True,
            lazy="selectin",
        )
    )

    products: list["ProductORM"] = Relationship(
        sa_relationship=relationship(
            "ProductORM",
            back_populates="category",
            lazy="selectin",
        )
    )

    def to_entity(self) -> Category:
        return Category(
            id=self.id,
            name=self.name,
            parent=self.parent.to_entity() if "parent" in self.__dict__ else None,
        )

    @classmethod
    def from_entity(cls, entity: Category) -> CategoryORM:
        return cls(
            id=entity.id,
            name=entity.name,
            parent_id=entity.parent.id if entity.parent else None,
        )
