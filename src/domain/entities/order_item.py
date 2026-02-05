from dataclasses import dataclass

from src.domain.entities.product import Product


@dataclass(slots=True, frozen=True)
class OrderItem:
    id: int
    product: Product
    quantity: int
    price: float
