# Put all errors that can be raised by the domain logic here. This keeps the domain logic clean and focused on business rules, and allows the API layer to translate these into appropriate HTTP responses.

class DomainError(Exception): # super class of all domain-level errors, in case we want to catch them generically in the API layer.
    """Base class for domain-level errors."""


class InvalidQuantity(DomainError):
    pass


class UnknownSku(DomainError):
    def __init__(self, sku: str) -> None:
        super().__init__(f"unknown sku: {sku}")
        self.sku = sku


class OutOfStock(DomainError):
    def __init__(self, sku: str, requested: int, available: int) -> None:
        super().__init__(
            f"out of stock: {sku}, requested {requested}, available {available}"
        )
        self.sku = sku
        self.requested = requested
        self.available = available
