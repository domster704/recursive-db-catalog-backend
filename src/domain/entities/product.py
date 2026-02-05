from dataclasses import dataclass

from src.domain.entities.category import Category


@dataclass(slots=True)
class Product:
    name: str
    quantity: int
    price: float
    category: Category
    id: int | None = None
