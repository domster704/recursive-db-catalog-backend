from dataclasses import dataclass

from src.domain.entities.category import Category


@dataclass(slots=True, frozen=True)
class Product:
    id: int
    name: str
    quantity: int
    price: float
    category: Category
