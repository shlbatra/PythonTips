import logging


class StripePaymentHandler:
    def handle_payment(self, amount: int) -> None:
        logging.info(f"Charging ${amount/100:.2f} using Stripe")


PRICES = {
    "burger": 10_00,
    "fries": 5_00,
    "drink": 2_00,
    "salad": 15_00,
}

#too many responsibilities - create payment handler object and handles payment
#also specific to stripe here - change here if need to change to paypal
#to solve, use dependency injection
def order_food(items: list[str]) -> None:
    total = sum(PRICES[item] for item in items)
    logging.info(f"Order total is ${total/100:.2f}.")
    payment_handler = StripePaymentHandler()
    payment_handler.handle_payment(total)
    logging.info("Order completed.")


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    order_food(["burger", "fries", "drink"])


if __name__ == "__main__":
    main()
