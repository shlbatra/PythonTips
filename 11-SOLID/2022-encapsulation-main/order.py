from dataclasses import dataclass, field
from enum import Enum


class PaymentStatus(Enum):
    CANCELLED = "cancelled"
    PENDING = "pending"
    PAID = "paid"


class PaymentStatusError(Exception):
    pass

#single item on order
@dataclass
class LineItem:
    name: str
    price: int
    quantity: int

    @property
    def total_price(self) -> int:
        return self.price * self.quantity

#payment status is abstracted, if make changes to payment status such as change type
# another class wont be impacted - implementation details hidden from that class 
@dataclass
class Order:
    items: list[LineItem] = field(default_factory=list)
    #boundary as payment status is marked as private here
    _payment_status: PaymentStatus = PaymentStatus.PENDING

    def add_item(self, item: LineItem):
        self.items.append(item)

    def set_payment_status(self, status: PaymentStatus) -> None:
        if self._payment_status == PaymentStatus.PAID:
            raise PaymentStatusError(
                "You can't change the status of an already paid order."
            )
        self._payment_status = status

    @property
    def total_price(self) -> int:
        return sum(item.total_price for item in self.items)
