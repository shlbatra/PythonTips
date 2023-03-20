import random
import string

from pos.order import Order, OrderStatus
from pos.payment import StripePaymentProcessor


def generate_id(length: int = 6) -> str:
    """Helper function for generating an id."""
    return "".join(random.choices(string.ascii_uppercase, k=length))


class POSSystem:
    def __init__(self):
        # code smell 7 -> create unrelated objects in initializer
        # depedency here if replace stripepaymentprocessor -> pass arg and use depedency injection
        # use protocol class here
        self.payment_processor = StripePaymentProcessor(self)
        self.orders: dict[str, Order] = {}

    def setup_payment_processor(self, url: str) -> None:
        self.payment_processor.connect_to_service(url)

    def register_order(self, order: Order):
        order.id = generate_id()
        self.orders[order.id] = order

    # same method from OrderRepository
    def find_order(self, order_id: str) -> Order:
        return self.orders[order_id]    
    
    # Code Smell 4 -> verb/subject -> gets order single object and does computation 
    # here using that object so move out of POS to Order class method
    def compute_order_total_price(self, order: Order) -> int:
        total = 0
        for i in range(len(order.prices)):
            total += order.quantities[i] * order.prices[i]
        return total
    #fix this provide reference and total price - use order attribute
    def process_order(self, order: Order) -> None:
        self.payment_processor.process_payment(order.id)
        order.set_status(OrderStatus.PAID)
        print("Shipping order to customer.")
