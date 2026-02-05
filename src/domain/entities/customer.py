from dataclasses import dataclass


@dataclass(slots=True)
class Customer:
    name: str
    address: str
    id: int | None = None
