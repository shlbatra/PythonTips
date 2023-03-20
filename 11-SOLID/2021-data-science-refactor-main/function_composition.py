import functools
from typing import Callable

ComposableFunction = Callable[[float],float]

def compose(*functions: ComposableFunction) -> ComposableFunction:
    #go through list of args - 2 fns and continue going through list of funcs
    return functools.reduce(lambda f, g: lambda x: g(f(x)), functions)  

    

def addThree(x: float) -> float:
    return x+3

def multiplyByTwo(x: float) -> float:
    return x*2

#calling sequence of functions on the same variable x
#try to avoid

def main():
    x=12
    x=addThree(x)
    x=addThree(x)
    x=multiplyByTwo(x)
    x=multiplyByTwo(x)
    print(f"Result: {x}")
    #alternate complicated fn that calls all methods in 1 line
    #hard to read
    result = multiplyByTwo(multiplyByTwo(addThree(addThree(x))))
    print(result)
    #alternate 2 -> composing these functions, supply list of functions and called in sequence
    myfunc=compose(addThree,addThree,multiplyByTwo,multiplyByTwo)
    result = myfunc(x)
    print(f"Result: {result}")
    
    
if __name__ == "__main__":
    main()
