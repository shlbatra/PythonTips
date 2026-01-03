def greet(name: str) -> str:
    return f"Hello, {name}!"

def main() -> None:
    say_hello = greet # Each function is an object

    print(say_hello("Pythonista"))

if __name__ == "__main__":
    main()