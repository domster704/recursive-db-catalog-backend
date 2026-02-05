from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Customer:
    id: int
    name: str
    address: str
