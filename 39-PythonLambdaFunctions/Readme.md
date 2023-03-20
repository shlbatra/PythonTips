- How to Use Python Lambda Functions
    - https://realpython.com/python-lambda/#are-lambdas-pythonic-or-not
- Python lambdas are little, anonymous functions, subject to a more restrictive but more concise syntax than regular Python functions.
- Lambda calculus can encode any computation. It is Turing complete, but contrary to the concept of a Turing machine, it is pure and does not keep any state.
- Functional languages directly inherit the lambda calculus philosophy, adopting a declarative approach of programming that emphasizes abstraction, data transformation, composition, and purity (no state and no side effects). Examples of functional languages include Haskell, Lisp, or Erlang.
- The imperative style consists of programming with statements, driving the flow of the program step by step with detailed instructions. This approach promotes mutation and requires managing state.Ex, Fortran, C, or Python.
- Ex. Identity function
>>> def identity(x):
...     return x

>>> lambda x: x
- the expression is composed of:
    1. The keyword: lambda  
    2. A bound variable: x -> a bound variable is an argument to a lambda function.
    3. A body: x

- >>> lambda x: x + 1
- apply function as -> (lambda x: x + 1)(2)  -> 3
- Reduction is a lambda calculus strategy to compute the value of the expression.
- Because a lambda function is an expression, it can be named. 
- Ex. add_one = lambda x: x + 1   ->    add_one(2)->3
- Multi-argument functions (functions that take more than one argument) are expressed in Python lambdas by listing arguments and separating them with a comma (,) but without surrounding them with parentheses
- Ex. full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
full_name('guido', 'van rossum')   ->    'Full name: Guido Van Rossum'
- Anonymous functions
- an anonymous function is a function without a name. In Python, an anonymous function is created with the lambda keyword. 
- Ex. lambda x, y: x + y    . call using _(1,2) -> 3. In the interactive interpreter, the single underscore (_) is bound to the last expression evaluated.
- Immediately Invoked Function Expression -> immediately execute a Python lambda function. 
- Ex. (lambda x, y: x + y)(2, 3)   ->   5
- Lambda functions are frequently used with higher-order functions, which take one or more functions as arguments or return one or more functions.
- Ex. high_ord_func = lambda x, func: x + func(x)
      high_ord_func(2, lambda x: x * x)
- Examples include map(), filter(), functools.reduce(), as well as key functions like sort(), sorted(), min(), and max().

- Python Lambda and Regular Functions
- Ex.
>>> import dis
>>> add = lambda x, y: x + y
>>> type(add)
<class 'function'>
>>> dis.dis(add)
  1           0 LOAD_FAST                0 (x)
              2 LOAD_FAST                1 (y)
              4 BINARY_ADD
              6 RETURN_VALUE
>>> add
<function <lambda> at 0x7f30c6ce9ea0>   -> diff

>>> import dis
>>> def add(x, y): return x + y
>>> type(add)
<class 'function'>
>>> dis.dis(add)
  1           0 LOAD_FAST                0 (x)
              2 LOAD_FAST                1 (y)
              4 BINARY_ADD
              6 RETURN_VALUE
>>> add
<function add at 0x7f30c6ce9f28>      -> diff

- The traceback of an exception raised while a lambda function is executed only identifies the function causing the exception as <lambda> whereas results in a more precise traceback because it gives the function name, div_zero.
Ex.
>>> div_zero = lambda x: x / 0
>>> div_zero(2)
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 1, in <lambda>
ZeroDivisionError: division by zero

>>> def div_zero(x): return x / 0
>>> div_zero(2)
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 1, in div_zero
ZeroDivisionError: division by zero

- Features
    - It can only contain expressions and can’t include statements in its body.
    - It is written as a single line of execution.
    - It does not support type annotations.
    - It can be immediately invoked (IIFE).

- No Statements
In a lambda function, statements like return, pass, assert, or raise will raise a SyntaxError exception.
Ex.
>>> (lambda x: assert x == 2)(2)
  File "<input>", line 1
    (lambda x: assert x == 2)(2)
                    ^
SyntaxError: invalid syntax

- Single Expression
- Ex. (lambda x:
... (x % 2 and 'odd' or 'even'))(3)     ->       'odd'

- Type Annotations
- Not Allowed. Ex.
>>> lambda first: str, last: str: first.title() + " " + last.title() -> str
  File "<stdin>", line 1
    lambda first: str, last: str: first.title() + " " + last.title() -> str

SyntaxError: invalid syntax

- IIFE (immediately invoked function execution)
- Ex. (lambda x: x * x)(3)   ->   9
- this allows you to pass the definition of a Python lambda expression to a higher-order function like map(), filter(), or functools.reduce(), or to a key function.

- Arguments
    - Positional arguments
    - Named arguments (sometimes called keyword arguments)
    - Variable list of arguments (often referred to as varargs)
    - Variable list of keyword arguments
    - Keyword-only arguments
Ex/
>>> (lambda x, y, z: x + y + z)(1, 2, 3)    Positional arguments
6
>>> (lambda x, y, z=3: x + y + z)(1, 2)    Variable list of keyword arguments
6
>>> (lambda x, y, z=3: x + y + z)(1, y=2)    Variable list of keyword arguments
6
>>> (lambda *args: sum(args))(1,2,3)    Variable list of arguments 
6
>>> (lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)   Variable list of keyword arguments
6
>>> (lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3)  Variable list of keyword arguments
6

- Decorators
- A decorator can be applied to a lambda. Although it’s not possible to decorate a lambda with the @decorator syntax, a decorator is just a function, so it can call the lambda function
Ex.
# Defining a decorator
def trace(f):
    def wrap(*args, **kwargs):
        print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")
        return f(*args, **kwargs)

    return wrap

# Applying decorator to a function
@trace
def add_two(x):
    return x + 2

# Calling the decorated function
add_two(3)    ->    [TRACE] func: add_two, args: (3,), kwargs: {}

# Applying decorator to a lambda
print((trace(lambda x: x ** 2))(3))    ->  [TRACE] func: <lambda>, args: (3,), kwargs: {}   -> 9

- Decorating the lambda function this way could be useful for debugging purposes, possibly to debug the behavior of a lambda function used in the context of a higher-order function or a key function. The first argument of map() is a lambda that multiplies its argument by 2. This lambda is decorated with trace(). 

Ex. list(map(trace(lambda x: x*2), range(3)))
[TRACE] Calling <lambda> with args (0,) and kwargs {}
[TRACE] Calling <lambda> with args (1,) and kwargs {}
[TRACE] Calling <lambda> with args (2,) and kwargs {}
[0, 2, 4]

- Closures
- A closure is a function where every free variable, everything except parameters, used in that function is bound to a specific value defined in the enclosing scope of that function. In effect, closures define the environment in which they run, and so can be called from anywhere.
- Ex.
def outer_func(x):
    y = 4
    def inner_func(z):
        print(f"x = {x}, y = {y}, z = {z}")
        return x + y + z
    return inner_func

for i in range(3):
    closure = outer_func(i)
    print(f"closure({i+5}) = {closure(i+5)}")
O/P-> 
x = 0, y = 4, z = 5
closure(5) = 9
x = 1, y = 4, z = 6
closure(6) = 11
x = 2, y = 4, z = 7
closure(7) = 13

outer_func() returns inner_func(), a nested function that computes the sum of three arguments:
    - x is passed as an argument to outer_func().
    - y is a variable local to outer_func().
    - z is an argument passed to inner_func().

- Ex with lambda function
def outer_func(x):
    y = 4
    return lambda z: x + y + z

for i in range(3):
    closure = outer_func(i)     # outer_func() returns a lambda and assigns it to to the variable closure
    print(f"closure({i+5}) = {closure(i+5)}")
O/P -> 
closure(5) = 9
closure(6) = 11
closure(7) = 13

- Evaluation Time
- In some situations involving loops, the behavior of a Python lambda function as a closure may be counterintuitive. It requires understanding when free variables are bound in the context of a lambda.
- E. Regular fn - In a normal function, n is evaluated at definition time
>>> def wrap(n):
...     def f():
...         print(n)
...     return f
...
>>> numbers = 'one', 'two', 'three'
>>> funcs = []
>>> for n in numbers:
...     funcs.append(wrap(n))
...
>>> for f in funcs:
...     f()
...
one
two
three

- Ex. lambda fn - The unexpected result occurs because the free variable n, as implemented, is bound at the execution time of the lambda expression. The Python lambda function on line 4 is a closure that captures n, a free variable bound at runtime. At runtime, while invoking the function f on line 7, the value of n is three.
>>> numbers = 'one', 'two', 'three'
>>> funcs = []
>>> for n in numbers:
...     funcs.append(lambda: print(n))
...
>>> for f in funcs:
...     f()
...
three
three
three

- Ex. To overcome this issue, you can assign the free variable at definition time as follows:a lambda parameter can be initialized with a default value: the parameter n takes the outer n as a default value. The Python lambda function could have been written as lambda x=n: print(x) and have the same result. it uses the default value n set at definition time.

>>> numbers = 'one', 'two', 'three'
>>> funcs = []
>>> for n in numbers:
...     funcs.append(lambda n=n: print(n))
...
>>> for f in funcs:
...     f()
...
one
two
three

- Testing Lambdas
- unittest
- Ex.
import unittest
addtwo = lambda x: x + 2
class LambdaTest(unittest.TestCase):
    def test_add_two(self):
        self.assertEqual(addtwo(2), 4)

    def test_add_two_point_two(self):
        self.assertEqual(addtwo(2.2), 4.2)

    def test_add_three(self):
        # Should fail
        self.assertEqual(addtwo(3), 6)

if __name__ == '__main__':
    unittest.main(verbosity=2)
    
- doctest
- The doctest module extracts interactive Python code from docstring to execute tests.You can add a docstring to a Python lambda via an assignment to __doc__ to document a lambda function.
Ex.
addtwo = lambda x: x + 2
addtwo.__doc__ = """Add 2 to a number.
    >>> addtwo(2)
    4
    >>> addtwo(2.2)
    4.2
    >>> addtwo(3) # Should fail
    6
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

- Lambda Expression Abuses
- When to avoid lambda fns
    - It doesn’t follow the Python style guide (PEP 8)
    - It’s cumbersome and difficult to read.
    - It’s unnecessarily clever at the cost of difficult readability.

- Ex. Raising an Exception - avoid as encapsulate in another function throw 
>>> def throw(ex): raise ex
>>> (lambda: throw(Exception('Something bad happened')))()
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 1, in <lambda>
    File "<stdin>", line 1, in throw
Exception: Something bad happened

- Ex. Cryptic Style
- Lambda functions, due to their conciseness, can be conducive to writing code that is difficult to read.
- Ex. Bad 3 - The underscore (_) refers to a variable that you don’t need to refer to explicitly. 
>>> (lambda _: list(map(lambda _: _ // 2, _)))([1,2,3,4,5,6,7,8,9,10])
[0, 1, 1, 2, 2, 3, 3, 4, 4, 5]
- Ex. Bad 2 - use variable names
(lambda some_list: list(map(lambda n: n // 2,
                                some_list)))([1,2,3,4,5,6,7,8,9,10])
- Ex. Bad 1 - use regular dn 
>>> def div_items(some_list):
      div_by_two = lambda n: n // 2
      return map(div_by_two, some_list)
>>> list(div_items([1,2,3,4,5,6,7,8,9,10])))
[0, 1, 1, 2, 2, 3, 3, 4, 4, 5]

- Python Classes
- Ex. to avoid
class Car:
    """Car with methods as lambda functions."""
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    brand = property(lambda self: getattr(self, '_brand'),
                     lambda self, value: setattr(self, '_brand', value))

    year = property(lambda self: getattr(self, '_year'),
                    lambda self, value: setattr(self, '_year', value))

    __str__ = lambda self: f'{self.brand} {self.year}'  # 1: error E731

    honk = lambda self: print('Honk!')     # 2: error E731

-> write __str__ as 
        def __str__(self):
            return f'{self.brand} {self.year}'

-> write property as 
        @property
        def brand(self):
            return self._brand

        @brand.setter
        def brand(self, value):
            self._brand = value

- Appropriate Uses of Lambda Expressions

- Classic Functional Constructs
- Lambda functions are regularly used with the built-in functions map() and filter(), as well as functools.reduce()
- Ex. 
>>> list(map(lambda x: x.upper(), ['cat', 'dog', 'cow']))
['CAT', 'DOG', 'COW']
>>> list(filter(lambda x: 'o' in x, ['cat', 'dog', 'cow']))
['dog', 'cow']
>>> from functools import reduce
>>> reduce(lambda acc, x: f'{acc} | {x}', ['cat', 'dog', 'cow'])
'cat | dog | cow'

- Key Functions
- Key functions in Python are higher-order functions that take a parameter key as a named argument. key receives a function that can be a lambda. This function directly influences the algorithm driven by the key function itself. Here are some key functions:
    - sort(): list method
    - sorted(), min(), max(): built-in functions
    - nlargest() and nsmallest(): in the Heap queue algorithm module heapq
- Ex. 
>>> ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
>>> print(sorted(ids)) # Lexicographic sort
['id1', 'id100', 'id2', 'id22', 'id3', 'id30']
>>> sorted_ids = sorted(ids, key=lambda x: int(x[2:])) # Integer sort
>>> print(sorted_ids)
['id1', 'id2', 'id3', 'id22', 'id30', 'id100']

- UI Frameworks
- UI frameworks like Tkinter, wxPython, or .NET Windows Forms with IronPython take advantage of lambda functions for mapping actions in response to UI events. 
- Ex.Clicking the button Reverse fires an event that triggers the lambda function, changing the label from Lambda Calculus to suluclaC adbmaL*:
import tkinter as tk
import sys

window = tk.Tk()
window.grid_columnconfigure(0, weight=1)
window.title("Lambda")
window.geometry("300x100")
label = tk.Label(window, text="Lambda Calculus")
label.grid(column=0, row=0)
button = tk.Button(
    window,
    text="Reverse",
    command=lambda: label.configure(text=label.cget("text")[::-1]),
)
button.grid(column=0, row=1)
window.mainloop()

- Python Interpreter
- timeit
- Ex.string version 
>>> from timeit import timeit
>>> timeit("factorial(999)", "from math import factorial", number=10) #second arg sets up environment needed by main function to be timed. 
- use lamdba
>>> from math import factorial
>>> timeit(lambda: factorial(999), number=10)
0.0012704220062005334

- Monkey Patching
- 
For testing, it’s sometimes necessary to rely on repeatable results, even if during the normal execution of a given software, the corresponding results are expected to differ,
- Ex.during the testing execution, you need to assert against predictable values in a repeatable manner.A context manager helps with insulating the operation of monkey patching a function from the standard library (secrets, in this example). The lambda function assigned to secrets.token_hex() substitutes the default behavior by returning a static value.

from contextlib import contextmanager
import secrets

def gen_token():
    """Generate a random token."""
    return f'TOKEN_{secrets.token_hex(8)}'

@contextmanager
def mock_token():
    """Context manager to monkey patch the secrets.token_hex
    function during testing.
    """
    default_token_hex = secrets.token_hex
    secrets.token_hex = lambda _: 'feedfacecafebeef'
    yield
    secrets.token_hex = default_token_hex

def test_gen_key():
    """Test the random token."""
    with mock_token():
        assert gen_token() == f"TOKEN_{'feedfacecafebeef'}"

test_gen_key()

- Ex. using pytest
import secrets

def gen_token():
    return f'TOKEN_{secrets.token_hex(8)}'

def test_gen_key(monkeypatch):
    monkeypatch.setattr('secrets.token_hex', lambda _: 'feedfacecafebeef')
    assert gen_token() == f"TOKEN_{'feedfacecafebeef'}"

- Alternatives to Lambdas
- Higher-order functions like map(), filter(), and functools.reduce() can be converted to more elegant forms with slight twists of creativity, in particular with list comprehensions or generator expressions.
- Map
- The built-in function map() takes a function as a first argument and applies it to each of the elements of its second argument, an iterable. Examples of iterables are strings, lists, and tuples. 
- Ex.
>>> list(map(lambda x: x.capitalize(), ['cat', 'dog', 'cow']))
['Cat', 'Dog', 'Cow']
- alternate with list comprehension 
>>> [x.capitalize() for x in ['cat', 'dog', 'cow']]
['Cat', 'Dog', 'Cow']

- Filter
- It takes a predicate as a first argument and an iterable as a second argument. It builds an iterator containing all the elements of the initial collection that satisfies the predicate function.
- Ex. 
>>> even = lambda x: x%2 == 0
>>> list(filter(even, range(11)))
[0, 2, 4, 6, 8, 10]
- alternate with list comprehension
>>> [x for x in range(11) if x%2 == 0]
[0, 2, 4, 6, 8, 10]

- Reduce
- its first two arguments are respectively a function and an iterable. It may also take an initializer as a third argument that is used as the initial value of the resulting accumulator. For each element of the iterable, reduce() applies the function and accumulates the result that is returned when the iterable is exhausted.
- Ex. To apply reduce() to a list of pairs and calculate the sum of the first item of each pair, you could write this:
>>> import functools
>>> pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
>>> functools.reduce(lambda acc, pair: acc + pair[0], pairs, 0)
6
- Alternate
>>> pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
>>> sum(x[0] for x in pairs)
6
- Alternate
>>> pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
>>> sum(x for x, _ in pairs)
6



















