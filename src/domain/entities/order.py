from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from src.domain.entities.customer import Customer
from src.domain.entities.product import Product


@dataclass(slots=True)
class Order:
    customer: Customer
    order_date: date
    status: str
    items: list[OrderItem]
    id: int | None = None


@dataclass(slots=True)
class OrderItem:
    product: Product
    quantity: int
    price: float
    order: Order | None = None
    id: int | None = None
