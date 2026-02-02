import functools
from typing import Callable

def addThree(x: float) -> float:
    return x + 3

def multiplyByTwo(x: float) -> float:
    return x * 2

ComposableFn = Callable[[float], float]

def compose(*fns: ComposableFn) -> ComposableFn:
    return functools.reduce(lambda f, g: lambda x: g(f(x)), fns)

# def main():
#     x = 12
#     x = addThree(x)
#     x = addThree(x)
#     x = multiplyByTwo(x)
#     x = multiplyByTwo(x)
#     print(f"Result: {x}")

# if __name__ == "__main__":
#     main()

# def main():
#     x = 12
#     x = multiplyByTwo(multiplyByTwo(addThree(addThree(x))))
#     print(f"Result: {x}")

def main():
    x = 12
    myfunc = compose(addThree, addThree,multiplyByTwo, multiplyByTwo)
    print(f"Result: {myfunc(x)}")

if __name__ == "__main__":
    main()