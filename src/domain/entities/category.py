from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Category:
    id: int
    name: str
    parent: Category | None = None
