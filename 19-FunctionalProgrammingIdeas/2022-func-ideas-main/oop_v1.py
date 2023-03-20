"""
Issue
1. init depends on datetime as needs to know current time, everytime use greeting, 
result can be different
2. greet prints to screen - hard to test and not used by apps that dont print to console
Side effect -> fn or methods relies on or modifies something on the outside of the fn.
Ex - print on console that is outside fn, Reading/Writing to file, Interacting with 
database, Interacting with other services -> harder to mantain/test

Pure fn - just depend on input and return value depend on input and 
no external library , easy to test and use on other apps 

Fix -
1. Remove datetime dependency
2. Side effect - print
"""

from datetime import datetime


class Greeting:
    def __init__(self) -> None:
        current_time = datetime.now()
        if current_time.hour < 12:
            self.greeting_intro = "Good morning"
        elif 12 <= current_time.hour < 18:
            self.greeting_intro = "Good afternoon"
        else:
            self.greeting_intro = "Good evening"

    def greet(self, name: str) -> None:
        print(f"{self.greeting_intro}, {name}.")

    def greet_list(self, names: list[str]) -> None:
        for name in names:
            self.greet(name)


def main() -> None:

    name = input("Enter your name: ")

    greeting = Greeting()
    greeting.greet(name)


if __name__ == "__main__":
    main()
