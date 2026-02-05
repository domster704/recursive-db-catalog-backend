from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Category:
    name: str
    parent: Category | None = None
    id: int | None = None
