from dataclasses import dataclass
from functools import lru_cache, partial
from typing import Protocol, Callable

from email_tools.service_v2 import send_email

SMTP_SERVER = "smtp.gmail.com"
PORT = 465
EMAIL = "hi@arjancodes.com"
PASSWORD = "password"

# EmailSender = Callable[[str, str, str], None]  -> cant define parameter names, just strings

class EmailSender(Protocol):
    def __call__(self, to_email: str, subject: str, body: str) -> None:   # use this class with call dundar method and define argument names
        ...


@lru_cache
def bmi(weight: float, height: float) -> float:
    return weight / (height**2)


def bmi_category(bmi_value: float) -> str:
    if bmi_value < 18.5:
        return "Underweight"
    elif bmi_value < 25:
        return "Normal"
    elif bmi_value < 30:
        return "Overweight"
    else:
        return "Obese"


@dataclass
class Stats:
    age: int
    gender: str
    height: float
    weight: float
    blood_type: str
    eye_color: str
    hair_color: str


@dataclass
class Address:
    address_line_1: str
    address_line_2: str
    city: str
    country: str
    postal_code: str

    def __str__(self) -> str:
        return f"{self.address_line_1}, {self.address_line_2}, {self.city}, {self.country}, {self.postal_code}"


@dataclass
class Person:
    name: str
    address: Address
    email: str
    phone_number: str
    stats: Stats

    def split_name(self) -> tuple[str, str]:
        first_name, last_name = self.name.split(" ")
        return first_name, last_name

    def update_email(self, email: str, send_message: EmailSender) -> None:  # send_message_fn: EmailSender
        self.email = email
        send_message(    # send_message_fn
            to_email=email,
            subject="Your email has been updated.",
            body="Your email has been updated. If this was not you, you have a problem.",
        )


def main() -> None:
    # create a person
    address = Address(
        address_line_1="123 Main St",
        address_line_2="Apt 1",
        city="New York",
        country="USA",
        postal_code="12345",
    )
    stats = Stats(
        age=30,
        gender="Male",
        height=1.8,
        weight=80,
        blood_type="A+",
        eye_color="Brown",
        hair_color="Black",
    )
    person = Person(
        name="John Doe",
        email="johndoe@gmail.com",
        phone_number="123-456-7890",
        address=address,
        stats=stats,
    )
    print(address)

    # compute the BMI
    bmi_value = bmi(stats.weight, stats.height)
    print(f"Your BMI is {bmi_value:.2f}")
    print(f"Your BMI category is {bmi_category(bmi_value)}")

    # update the email address
    send_message = partial(   # use partial fns to pass missing args -> server and port and auth details
        send_email, smtp_server=SMTP_SERVER, port=PORT, email=EMAIL, password=PASSWORD
    )
    person.update_email("johndoe@outlook.com", send_message)


if __name__ == "__main__":
    main()
