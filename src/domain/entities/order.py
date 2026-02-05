from dataclasses import dataclass
from datetime import date

from src.domain.entities.customer import Customer
from src.domain.entities.order_item import OrderItem


@dataclass(slots=True, frozen=True)
class Order:
    id: int
    customer: Customer
    order_date: date
    status: str
    items: list[OrderItem]
