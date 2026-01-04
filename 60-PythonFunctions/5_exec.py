def main() -> None:
    namespace: dict = {}
    exec("def add(x, y): return x + y", namespace)

    print(namespace["add"](3, 4))  # 7


if __name__ == "__main__":
    main()