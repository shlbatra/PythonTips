from typing import Any, Callable

"""
A decorator is just a callable that receives a function and returns something else. A descriptor is an object with __get__/__set__/__delete__. 
When you combine them — a decorator that returns a descriptor — you get @property:
attribute-style access that secretly runs your function. This file proves @property isn't magic; it's ~10 lines of descriptor protocol.
"""

class SimpleProperty:
    def __init__(self, fget: Callable[[Any], Any]) -> None: # Receive getter function and return None
        self.fget = fget # Store getter function as instance attribute

    def __get__(self, instance: Any | None, owner: type) -> Any: # Control what happens when read from it
        if instance is None:
            return self
        return self.fget(instance)


class User:
    def __init__(self, first: str, last: str) -> None:
        self.first = first
        self.last = last

    @SimpleProperty # Manually building a decorator here
    def full_name(self) -> str:
        return f"{self.first} {self.last}"


def main() -> None:

    u = User("Sahil", "Batra")

    print(u.full_name) 
    print(User.full_name) # return descriptor back


if __name__ == "__main__":
    main()