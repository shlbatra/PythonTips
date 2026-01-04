def main() -> None:
    greet = lambda name: f"Hello, {name}!" # <fn name> = lambda args: <expression using args>
    print(greet("Alice"))  # "Hello, Alice!"


if __name__ == "__main__":
    main()