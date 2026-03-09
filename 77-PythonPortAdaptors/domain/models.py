# Objects used by both the domain logic and the API layer, to keep them decoupled. The API layer will translate between these and the HTTP request/response models.
# No SQLAlchemy or FastAPI imports here, to keep the domain logic clean and focused on business rules.

from dataclasses import dataclass


@dataclass(frozen=True)
class OrderRequest:
    sku: str
    qty: int


@dataclass(frozen=True)
class OrderPlaced:
    sku: str
    qty: int
    remaining_stock: int
