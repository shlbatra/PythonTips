from typing import Self

"""
  Python's lookup order (the rule to remember)

  1. Data descriptors    (__get__ + __set__)   ← always wins
  2. Instance __dict__
  3. Non-data descriptors (__get__ only)       ← loses to __dict__

When you write @property, you get a data descriptor (it defines __get__, __set__, __delete__). That's why properties can't be shadowed — they sit at priority level 1.
When you write a plain method (just a def inside a class), the function object is a non-data descriptor. That's why you can monkey-patch methods on an instance — they sit at priority level 3, below __dict__.

"""

# ============================================================
# 3) Non-data descriptor (only __get__) can be shadowed
# ============================================================


class NonData:
    def __get__(self, instance: object | None, owner: type) -> str | Self:
        if instance is None:
            return self
        return "from descriptor"
 

class A:
    x: NonData = NonData()


# ============================================================
# 4) Data descriptor (has __set__) cannot be shadowed
# ============================================================


class Data:
    def __get__(self, instance: object | None, owner: type) -> str | Self:
        if instance is None:
            return self
        return "from descriptor"

    def __set__(self, instance: object, value: str) -> None:
        instance.__dict__["x"] = value


class B:
    x: Data = Data()


def main() -> None:

    a = A()
    print(a.x)
    a.__dict__["x"] = "from instance dict"
    print(a.x)  # shadowed by instance dict

    b = B()
    b.__dict__["x"] = "from instance dict"
    print(b.x)  # descriptor still wins (data descriptor precedence over __dict__ dictionary method)


if __name__ == "__main__":
    main()