class DemoDescriptor:

    def __init__(self):
        self.value = 42

    def __get__(self, instance: object | None, owner: type) -> int | DemoDescriptor:
        print(f"__get__ called with instance={instance}, owner={owner.__name__}")
        if instance is None:
            return self
        return self.value

    def __set__(self, instance: object, value: int) -> None:
        print(f"__set__ called with instance={instance}, value={value}")
        self.value = value        

class Thing:
    # Descriptor any object either get, set or delete implement and store as class attribute
    # You get a hook to run code every time someone reads, writes, or deletes an attribute.
    x = DemoDescriptor()


def main() -> None:

    t = Thing()

    print(t.x)  # triggers __get__
    t.x = 10  # triggers __set__
    print(Thing.x)  # instance=None - if class level access then use for introspection


if __name__ == "__main__":
    main()