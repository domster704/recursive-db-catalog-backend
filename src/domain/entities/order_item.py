from dataclasses import dataclass

from src.domain.entities.product import Product


@dataclass(slots=True)
class OrderItem:
    product: Product
    quantity: int
    price: float
    id: int | None = None
