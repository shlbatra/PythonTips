# Type Annotation , Python not declare type as dynamically typed
# Other languages strongly type - provide type of variable and variable provide that value only
# Ex. int x = 1

x: str = "tim"  # add type hints here
print(x)
# Use static code analysis tool (mypy) - examine type annotations
# Command -> mypy <path for python file>

#How to use methods with type hinting

def add_numbers(a: int, b:int, c:int) -> int: #args int and return type int
    return a + b + c

a = add_numbers(1,2,3)
print(a)

def add_numbers_None(a: int, b:int, c:int) -> None: #args int and returning nothing
    print(a + b + c)
    
#List Type - complex type pass as args to func 
# ex. [[1,2,3],[],[]] -> 
#x: list[list[int]] = [] #fails type object is not suscriptible

from typing import List, Dict, Set, Optional, Any, Sequence, Tuple
w: List[List[int]] = [[1,2],[3,4]]

#DictType

y: Dict[str,str] = {"a":"b"}

#Settype

z: Set[str] = {"a", "b"}

#Using custom types ex. vector
# complex type rename to simple custom type 

Vector = List[float]  #defined vector type, use vector as substitute anywhere
Vectors =List[Vector]
def foo(v: Vector) -> Vector:
    return(v)
    
def foo1(v: Vectors) -> Vector:
    pass
    
# Optional Type -> 

def foo2(output: Optional[bool]=False): #specify optional 
    pass

foo2()

def foo3(output: Any): #anything accepted for output
    pass

foo3(1)
    
# Sequence Type - param is a sequence of anything - list, tuple, etc

def foo4(seq: Sequence[str]):
    pass

foo4(("a","b","c"))
foo4(["a","b","c"])
#Error -> foo4(1)   #incompatible type "int"; expected "Sequence
#Error -> foo4({1,2,3}) #set is not a sequence and cannot be indexed
foo4("sahil batra") #string can be indexed and is a sequence

# Tuple Type -> specify what store at each position of tuple 

d: tuple = (1,2,3,"sahil") #generic tuple 
e: Tuple[int, int, int] = (1,2,3)   #provide inside types for Tuple

# Callable Type -> accept function as parameters

from typing import Callable 

def add(x: int, y: int) -> int:
    return x + y

def foo5(func: Callable[[int,int],int]) -> None:  #function type is callable with parameters reqd and return type 
    func(1,2)
    
foo5(add)

# Return callable 

def foo6() -> Callable[[int,int],int]:  #function type is callable with parameters reqd and return type 
    def add1(x: int, y: int) -> int: #add function inside function and return it
        return x + y
    return add
    # alternate return with lambda 
    # return lambda x, y: x + y  

foo6()

#Type for lambda function
func : Callable[[int,int],int] = lambda x, y: x + y

# Generics 
# T is placeholder. List parameter with any type but need to be same type.
# return same T as in list. Func works for any type but need to be generic 
#can create generic class as well.

from typing import TypeVar 

T = TypeVar('T')  #generic type used as a placeholder. Not know what it will be for now

def get_item(lst: List[T], index: int) -> T:
    return lst[index]
