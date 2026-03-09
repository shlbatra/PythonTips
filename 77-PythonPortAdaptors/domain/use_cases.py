from .errors import InvalidQuantity, OutOfStock, UnknownSku
from .models import OrderPlaced, OrderRequest
from .ports import InventoryPort

# Using domain logic in a clean way, without any SQLAlchemy or FastAPI imports, so it's decoupled from the API layer and the database access layer. The API layer will call this function and translate any domain errors into appropriate HTTP responses.
# Easy to write test by mocking the InventoryPort, without needing to worry about SQLAlchemy or FastAPI at all. The domain logic is focused purely on business rules.
def place_order(req: OrderRequest, inventory: InventoryPort) -> OrderPlaced:
    if req.qty <= 0:
        raise InvalidQuantity()

    if not inventory.exists_sku(req.sku):
        raise UnknownSku(req.sku)

    available = inventory.get_stock(req.sku)
    if available < req.qty:
        raise OutOfStock(req.sku, req.qty, available)

    remaining = inventory.reserve(req.sku, req.qty) # Here logic to update in SQLAlchemyInventoryAdapter will be called, but the domain logic doesn't know or care about that.
    return OrderPlaced(sku=req.sku, qty=req.qty, remaining_stock=remaining)
