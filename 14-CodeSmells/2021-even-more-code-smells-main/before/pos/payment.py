from typing import Protocol

from pos.order import Order


class PaymentServiceConnectionError(Exception):
    """Custom error that is raised when we couldn't connect to the payment service."""

# protocol class used to define an interface class that acts as a blueprint for designing other classes
# similar to abstract class without need to define sub classes.
# not require later on - code smell 5 
class OrderRepository(Protocol): #payment processor depends on this class to provide order abd total order value 
    def find_order(self, order_id: str) -> Order:
        ...

    def compute_order_total_price(self, order: Order) -> int:
        ...


class StripePaymentProcessor:
    def __init__(self, system: OrderRepository):
        self.connected = False
        self.system = system
    #code smell 6 -> hard wired sequences with fixed order, async call so need a seperate method here
    #create static method -> asyncronous
    def connect_to_service(self, url: str) -> None:
        print(f"Connecting to payment processing service at url {url}... done!")
        self.connected = True

    #code smell 5 -> backpeddling, use order id to find order and compute total price
    #these values should be passed so StripePaymentProcessor is isolated- just needs 
    #reference(orderid) and total price
    def process_payment(self, order_id: str) -> None:
        if not self.connected:
            raise PaymentServiceConnectionError()
        order = self.system.find_order(order_id)
        total_price = self.system.compute_order_total_price(order)
        print(
            f"Processing payment of ${(total_price / 100):.2f}, reference: {order.id}."
        )
