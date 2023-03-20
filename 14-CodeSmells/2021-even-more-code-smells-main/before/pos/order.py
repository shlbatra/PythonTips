from dataclasses import dataclass, field
from enum import Enum, auto


class OrderStatus(Enum):
    """Order status"""

    OPEN = auto()
    PAID = auto()
    CANCELLED = auto()
    DELIVERED = auto()
    RETURNED = auto()


@dataclass
class Order:
    #code smell 3 -> class with too many instance variables -> too many responsibilities
    # order focus on order not on all customer details here. seperate customer and order here
    # create customer class . Ex. customer: Customer
    customer_id: int = 0
    customer_name: str = ""
    customer_address: str = ""
    customer_postal_code: str = ""
    customer_city: str = ""
    customer_email: str = ""
    #code smell 1 - wrong data structure -> list to store - track for arrays and need same length. so 
    # make sense create object and mantain list of objects
    #seperate class for item, quantity and price and define list of objects of that class
    # Soln -> items = list[LineItem] = field(default_factory=list)
    items: list[str] = field(default_factory=list) # way to create default values for list
    quantities: list[int] = field(default_factory=list)
    prices: list[int] = field(default_factory=list)
    _status: OrderStatus = OrderStatus.OPEN
    id: str = ""

    # code smell 2 -> use misleading names, here not creating line item but just adding line item to items list
    def create_line_item(self, name: str, quantity: int, price: int) -> None:
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def set_status(self, status: OrderStatus):
        self._status = status
