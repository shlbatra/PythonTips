- Python Type Checking
    - https://realpython.com/python-type-checking/#hello-types
- Code file
    - https://github.com/realpython/materials/tree/03cdde02660412c885694bf1ba02fd5c5bfe85d7/python-type-checking
- Type Systems
- All programming languages include some kind of type system that formalizes which categories of objects it can work with and how those categories are treated. 
- Dynamic Typing
- Python is a dynamically typed language. This means that the Python interpreter does type checking only as code runs, and that the type of a variable is allowed to change over its lifetime.
- type() returns the type of an object. the type of thing is allowed to change, and Python correctly infers the type as it changes.
- Static Typing
- Static type checks are performed without running the program. C & Java do when program is compiled. 
- Ex.
String thing;
thing = "Hello";
- PEP 484 introduced type hints, which make it possible to also do static type checking of Python code. type hints just suggest types. There are other tools that perform static type checking using type hints.

- Duck Typing
- Duck typing is a concept related to dynamic typing, where the type or the class of an object is less important than the methods it defines. Using duck typing you do not check types at all. Instead you check for the presence of a given method or attribute.
- Ex.
you can call len() on any Python object that defines a .__len__() method:

>>> class TheHobbit:
...     def __len__(self):
...         return 95022
...
>>> the_hobbit = TheHobbit()
>>> len(the_hobbit)
95022

- Hello Types
- add type hints to a function
- Ex.
def headline(text: str, align: bool = True) -> str:
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")
- Adding type hints like this has no runtime effect: they are only hints and are not enforced on their own. 
- rules to follow ->
    - Use normal rules for colons, that is, no space before and one space after a colon: text: str.
    - Use spaces around the = sign when combining an argument annotation with a default value: align: bool = True.
    - Use spaces around the -> arrow: def headline(...) -> str.
- The most common tool for doing type checking is Mypy
- Ex. mypy headlines.py
headlines.py:10: error: Argument "align" to "headline" has incompatible
                        type "str"; expected "bool"

- Advantages
    - type hints help catch certain errors. 
    - Type hints help document your code.
    - Type hints improve IDEs and linters. They make it much easier to statically reason about your code.
    - Type hints help you build and maintain a cleaner architecture.

- Time each import takes ->
    - python3.7 -X importtime import_typing.py

- Python supports the concept of gradual typing. This means that you can gradually introduce types into your code. Code without type hints will be ignored by the static type checker. Therefore, you can start adding types to critical components, and continue as long as it adds value to you.
- type hints should be used whenever unit tests are worth writing. type hints play a similar role as tests in your code: they help you as a developer write better code.

- Annotations
- They were simply a way to associate arbitrary expressions to function arguments and return values.
- Function Annotations -> you can annotate arguments and the return value
- Ex. 
def func(arg: arg_type, optarg: arg_type = default) -> return_type:
    ...
For arguments the syntax is argument: annotation, while the return type is annotated using -> annotation. 
- method.__annotations__     ( to inspect annotations)
- special Mypy expressions: reveal_type() and reveal_locals() and Mypy will dutifully report which types it has inferred.
Ex.
# reveal.py

import math
reveal_type(math.pi)   -> reveal.py:4: error: Revealed type is 'builtins.float'

radius = 1
circumference = 2 * math.pi * radius
reveal_locals()

Run as -> mypy reveal.py
O/P -> 
reveal.py:8: error: Revealed local types are:
reveal.py:8: error: circumference: builtins.float
reveal.py:8: error: radius: builtins.int

- Variable Annotations
Ex.
pi: float = 3.142
- Annotations of variables are stored in the module level __annotations__ dictionary
- You’re allowed to annotate a variable without giving it a value. This adds the annotation to the __annotations__ dictionary, while the variable remains undefined.
- Ex.
>>> nothing: str
>>> nothing
NameError: name 'nothing' is not defined

>>> __annotations__
{'nothing': <class 'str'>}

- Type Comments
- Backward compatibility to Python 2.Type comments are specially formatted comments that is used to add type hints compatible to older code. 
- Ex.
import math

def circumference(radius):
    # type: (float) -> float
    return 2 * math.pi * radius
- A type comment must start with the type: literal, and be on the same or the following line as the function definition. 
- Ex.
def headline(text, width=80, fill_char="-"):
    # type: (str, int, str) -> str
    return f" {text.title()} ".center(width, fill_char)

print(headline("type comments work", width=40))
OR
# headlines.py

def headline(
    text,           # type: str
    width=80,       # type: int
    fill_char="-",  # type: str
):                  # type: (...) -> str
    return f" {text.title()} ".center(width, fill_char)

print(headline("type comments work", width=40))

- type comments to variables . Ex. pi = 3.142  # type: float
- Use annotations if you can, use type comments if you must. Annotations provide a cleaner syntax keeping type information closer to your code. They are also the officially recommended way of writing type hints

- Python type system is quite powerful, and supports many kinds of more complex types. This is necessary as it needs to be able to reasonably model Python’s dynamic duck typing nature.

- Type Hinting Examples
- With simple types like str, float, and bool, adding type hints is as easy as using the type itself:
>>> name: str = "Guido"
>>> pi: float = 3.142
>>> centered: bool = False
- With composite types, you are allowed to do the same:
>>> names: list = ["Guido", "Jukka", "Ivan"]
>>> version: tuple = (3, 7, 1)
>>> options: dict = {"centered": False, "capitalize": True}
Above not define the elements type. So use typing module. These types add syntax for specifying the types of elements of composite types.
The typing module contains many more composite types, including Counter, Deque, FrozenSet, NamedTuple, and Set. 
- Ex.
>>> from typing import Dict, List, Tuple
>>> names: List[str] = ["Guido", "Jukka", "Ivan"]
>>> version: Tuple[int, int, int] = (3, 7, 1)
>>> options: Dict[str, bool] = {"centered": False, "capitalize": True}
- Ex.
def create_deck(shuffle: bool = False) -> List[Tuple[str, str]]:
    """Create a new deck of 52 cards"""
    deck = [(s, r) for r in RANKS for s in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck
- In many cases your functions will expect some kind of sequence, and not really care whether it is a list or a tuple. Using Sequence is an example of using duck typing. 
- Ex.
from typing import List, Sequence

def square(elems: Sequence[float]) -> List[float]:
    return [x**2 for x in elems]

- Type Aliases
- Ex.
def deal_hands(
    deck: List[Tuple[str, str]]
) -> Tuple[
    List[Tuple[str, str]],
    List[Tuple[str, str]],
    List[Tuple[str, str]],
    List[Tuple[str, str]],
]:
    """Deal the cards in the deck into four hands"""
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])
->  you can define your own type aliases by assigning them to new variables. 
- from typing import List, Tuple

Card = Tuple[str, str]
Deck = List[Card]

def deal_hands(deck: Deck) -> Tuple[Deck, Deck, Deck, Deck]:
    """Deal the cards in the deck into four hands"""
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])

- Functions Without Return Values ->  functions without an explicit return still return None
- Ex.
# play.py

def play(player_name: str) -> None:
    print(f"{player_name} plays")

ret_val = play("Filip")

-> mypy play.py
play.py:6: error: "play" does not return a value

- As a more exotic case, note that you can also annotate functions that are never expected to return normally. This is done using NoReturn:

from typing import NoReturn

def black_hole() -> NoReturn:  # Since black_hole() always raises an exception, it will never return properly.
    raise Exception("There is no going back ...")

- The Any Type
- Ex. choose() works for both lists of names and lists of cards 
import random
from typing import Any, Sequence

def choose(items: Sequence[Any]) -> Any:
    return random.choice(items)

names = ["Guido", "Jukka", "Ivan"]
reveal_type(names)

name = choose(names)
reveal_type(name)

$ mypy choose.py
choose.py:10: error: Revealed type is 'builtins.list[builtins.str*]'
choose.py:13: error: Revealed type is 'Any'
-> While Mypy will correctly infer that names is a list of strings, that information is lost after the call to choose() because of the use of the Any type:

- Type Theory
- Subtypes
-  we say that a type T is a subtype of U if the following two conditions hold:
    - Every value from T is also in the set of values of U type.
    - Every function from U type is also in the set of functions of T type.
- Ex. Since 0 and 1 are both integers, the first condition holds. Above you can see that Booleans can be added together, but they can also do anything else integers can. This is the second condition above. In other words, bool is a subtype of int.
>>> int(False)
0

>>> int(True)
1

>>> True + True
2

>>> issubclass(bool, int)
True
- subtype can always pretend to be its supertype
Ex. 
def double(number: int) -> int:
    return number * 2

print(double(True))  # Passing in bool instead of int
- all subclasses corresponds to subtypes, and bool is a subtype of int because bool is a subclass of int. However, there are also subtypes that do not correspond to subclasses. For instance int is a subtype of float, but int is not a subclass of float.

- Covariant, Contravariant, and Invariant
- is Tuple[bool] a subtype of Tuple[int]? The answer depends on the composite type, and whether that type is covariant, contravariant, or invariant. 
    - Tuple is covariant. This means that it preserves the type hierarchy of its item types: Tuple[bool] is a subtype of Tuple[int] because bool is a subtype of int.
    - List is invariant. Invariant types give no guarantee about subtypes. While all values of List[bool] are values of List[int], you can append an int to List[int] and not to List[bool]. In other words, the second condition for subtypes does not hold, and List[bool] is not a subtype of List[int].
    - Callable is contravariant in its arguments. This means that it reverses the type hierarchy. You will see how Callable works later, but for now think of Callable[[T], ...] as a function with its only argument being of type T. An example of a Callable[[int], ...] is the double() function defined above. Being contravariant means that if a function operating on a bool is expected, then a function operating on an int would be acceptable.

- Gradual Typing and Consistent Types
- Gradual typing is essentially made possible by the Any type. Somehow Any sits both at the top and at the bottom of the type hierarchy of subtypes. Any type behaves as if it is a subtype of Any, and Any behaves as if it is a subtype of any other type. The type T is consistent with the type U if T is a subtype of U or either T or U is Any.
- You can use Any to explicitly fall back to dynamic typing, describe types that are too complex to describe in the Python type system, or describe items in composite types. For instance, a dictionary with string keys that can take any type as its values can be annotated Dict[str, Any].

- Type Variables
- A type variable is a special variable that can take on any type, depending on the situation.
- Ex.Type variable that will effectively encapsulate the behavior of choose()
# choose.py

import random
from typing import Sequence, TypeVar

Choosable = TypeVar("Choosable")

def choose(items: Sequence[Choosable]) -> Choosable:
    return random.choice(items)

names = ["Guido", "Jukka", "Ivan"]
reveal_type(names)

name = choose(names)
reveal_type(name)

$ mypy choose.py
choose.py:12: error: Revealed type is 'builtins.list[builtins.str*]'
choose.py:15: error: Revealed type is 'builtins.str*'
- Restict type variables by listing the acceptable types
# choose.py

import random
from typing import Sequence, TypeVar

Choosable = TypeVar("Choosable", str, float)

def choose(items: Sequence[Choosable]) -> Choosable:
    return random.choice(items)

reveal_type(choose(["Guido", "Jukka", "Ivan"]))
reveal_type(choose([1, 2, 3]))
reveal_type(choose([True, 42, 3.14]))
reveal_type(choose(["Python", 3, 7])) -> choose.py:14: error: Value of type variable "Choosable" of "choose" cannot be "object"

- Optional
- Ex.
from typing import Sequence, Optional

def player_order(
    names: Sequence[str], start: Optional[str] = None      # Optional[str]  OR Union[None, Str]
) -> Sequence[str]:
    """Rotate player order so that start goes first"""
    if start is None:
        start = choose(names)
    start_idx = names.index(start)
    return names[start_idx:] + names[:start_idx]
- The Optional type simply says that a variable either has the type specified or is None. An equivalent way of specifying the same would be using the Union type: Union[None, str]. Note that when using either Optional or Union you must take care that the variable has the correct type when you operate on it. 

- Duck Types and Protocols
- Ex.
def len(obj):
    return obj.__len__()
len() can return the length of any object that has implemented the .__len__() method.How can we add type hints to len(), and in particular the obj argument? The answer hides behind the academic sounding term structural subtyping. 

    - In a nominal system, comparisons between types are based on names and declarations. The Python type system is mostly nominal, where an int can be used in place of a float because of their subtype relationship.
    - In a structural system, comparisons between types are based on structure. You could define a structural type Sized that includes all instances that define .__len__(), irrespective of their nominal type. Adding in Python using Protocols. A protocol specifies one or more methods that must be implemented. For example, all classes defining .__len__() fulfill the typing.Sized protocol. We can therefore annotate len() as follows:

Ex of structural prototyping -> 
from typing import Sized

def len(obj: Sized) -> int:
    return obj.__len__()

Ex.custom protocol class 
from typing_extensions import Protocol

class Sized(Protocol):
    def __len__(self) -> int: ...

def len(obj: Sized) -> int:
    return obj.__len__()

- Type Hints for Methods
- First of all type hints for methods work much the same as type hints for functions. The only difference is that the self argument need not be annotated, as it always will be a class instance. 
- Ex.
class Card:
    SUITS = "♠ ♡ ♢ ♣".split()
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

    def __init__(self, suit: str, rank: str) -> None:    # init always has None as returntype
        self.suit = suit
        self.rank = rank

    def __repr__(self) -> str:
        return f"{self.suit}{self.rank}"

- Classes as Types
- There is a correspondence between classes and types. For example, all instances of the Card class together form the Card type. To use classes as types you simply use the name of the class.
- Ex.
class Deck:
    def __init__(self, cards: List[Card]) -> None:
        self.cards = cards

- You are allowed to use string literals in annotations. These strings will only be evaluated by the type checker later, and can therefore contain self and forward references. . Instead of evaluating annotations as Python expressions and storing their value, the proposal is to store the string representation of the annotation and only evaluate it when needed.
- Ex. 
class Deck:
    @classmethod
    def create(cls, shuffle: bool = False) -> "Deck":
        """Create a new deck of 52 cards"""
        cards = [Card(s, r) for r in Card.RANKS for s in Card.SUITS]
        if shuffle:
            random.shuffle(cards)
        return cls(cards)
Using future version, dont need the Deck as string format
from __future__ import annotations

class Deck:
    @classmethod
    def create(cls, shuffle: bool = False) -> Deck:
        ...

- Returning self or cls
- you should typically not annotate the self or cls arguments.
- There is one case where you might want to annotate self or cls, though. Consider what happens if you have a superclass that other classes inherit from, and which has methods that return self or cls:
- Ex.
# dogs.py

from datetime import date

class Animal:
    def __init__(self, name: str, birthday: date) -> None:
        self.name = name
        self.birthday = birthday

    @classmethod
    def newborn(cls, name: str) -> "Animal":
        return cls(name, date.today())

    def twin(self, name: str) -> "Animal":
        cls = self.__class__
        return cls(name, self.birthday)

class Dog(Animal):
    def bark(self) -> None:
        print(f"{self.name} says woof!")

fido = Dog.newborn("Fido")
pluto = fido.twin("Pluto")
fido.bark()
pluto.bark()

$ mypy dogs.py
dogs.py:24: error: "Animal" has no attribute "bark"
dogs.py:25: error: "Animal" has no attribute "bark"
The issue is that even though the inherited Dog.newborn() and Dog.twin() methods will return a Dog the annotation says that they return an Animal. The return type should match the type of self or the instance type of cls. This can be done using type variables that keep track of what is actually passed to self and cls:
- Ex. Fixed below :
# dogs.py

from datetime import date
from typing import Type, TypeVar

TAnimal = TypeVar("TAnimal", bound="Animal")  # return values instances of subclasses of Animal.Specifying bound means TAnimal will only be Animal or one of its subclasses.

class Animal:
    def __init__(self, name: str, birthday: date) -> None:
        self.name = name
        self.birthday = birthday

    @classmethod
    def newborn(cls: Type[TAnimal], name: str) -> TAnimal:  # typing.Type[] construct is the typing equivalent of type(), class method expects a class and returns an instance of that class.
        return cls(name, date.today())

    def twin(self: TAnimal, name: str) -> TAnimal:
        cls = self.__class__
        return cls(name, self.birthday)

class Dog(Animal):
    def bark(self) -> None:
        print(f"{self.name} says woof!")

fido = Dog.newborn("Fido")
pluto = fido.twin("Pluto")
fido.bark()
pluto.bark()

- Annotating *args and **kwargs
- Ex.even though names will be a tuple of strings, you should only annotate the type of each name.
class Game:
    def __init__(self, *names: str) -> None:
        """Set up the deck and deal cards to 4 players"""
        deck = Deck.create(shuffle=True)
        self.names = (list(names) + "P1 P2 P3 P4".split())[:4]
        self.hands = {
            n: Player(n, h) for n, h in zip(self.names, deck.deal(4))
        }
Similarly, if you have a function or method accepting **kwargs, then you should only annotate the type of each possible keyword argument.

- Callables
- Functions are first-class objects in Python. This means that you can use functions as arguments to other functions and need type hints.
- Functions, as well as lambdas, methods and classes, are represented by typing.Callable.
- Callable[[A1, A2, A3], Rt] represents function with three arguments with types A1, A2, and A3, resp. The return type of the function is Rt.
- 


- Extended Callable types
- Argument specifiers are special function calls that can specify the following aspects of an argument:
    - its type (the only thing that the basic format supports)
    - its name (if it has one)
    - whether it may be omitted
    - whether it may or must be passed using a keyword
    - whether it is a *args argument (representing the remaining positional arguments)
    - whether it is a **kwargs argument (representing the remaining keyword arguments)

The following functions are available in mypy_extensions for this purpose:
        def Arg(type=Any, name=None):
            # A normal, mandatory, positional argument.
            # If the name is specified it may be passed as a keyword.
        def DefaultArg(type=Any, name=None):
            # An optional positional argument (i.e. with a default value).
            # If the name is specified it may be passed as a keyword.
        def NamedArg(type=Any, name=None):
            # A mandatory keyword-only argument.
        def DefaultNamedArg(type=Any, name=None):
            # An optional keyword-only argument (i.e. with a default value).
        def VarArg(type=Any):
            # A *args-style variadic positional argument.
            # A single VarArg() specifier represents all remaining
            # positional arguments.
        def KwArg(type=Any):
            # A **kwargs-style variadic keyword argument.
            # A single KwArg() specifier represents all remaining
            # keyword arguments.
- Ex.
    1. MyFunc = Callable[[int, str, int], float] -> MyFunc = Callable[[Arg(int), Arg(str), Arg(int)], float]
    2. MyOtherFunc = Callable[..., int]  -> MyOtherFunc = Callable[[VarArg(), KwArg()], int]
    3. 
    def func(__a: int,  # This convention is for nameless arguments
         b: int,
         c: int = 0,
         *args: int,
         d: int,
         e: int = 0,
         **kwargs: int) -> int:
    ...

F = Callable[[int,  # Or Arg(int)
              Arg(int, 'b'),
              DefaultArg(int, 'c'),
              VarArg(int),
              NamedArg(int, 'd'),
              DefaultNamedArg(int, 'e'),
              KwArg(int)],
             int]

f: F = func

- For type relationships that are hard to express using Union or type variables, you can use the @overload decorator. 
Ex.
 suppose we want to write a custom container class that implements the __getitem__ method ([] bracket indexing). If this method receives an integer we return a single item. If it receives a slice, we return a Sequence of items.

We can precisely encode this relationship between the argument and the return type by using overloads like so:

from typing import Sequence, TypeVar, Union, overload

T = TypeVar('T')

class MyList(Sequence[T]):
    @overload
    def __getitem__(self, index: int) -> T: ...

    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...

    def __getitem__(self, index: Union[int, slice]) -> Union[T, Sequence[T]]:
        if isinstance(index, int):
            # Return a T here
        elif isinstance(index, slice):
            # Return a sequence of Ts here
        else:
            raise TypeError(...)

- Static Type Checking of Python Code
- The Mypy Project
- With Mypy installed, you can run it as a regular command line program:
$ mypy my_program.py
- First of all, if you are using third-party packages without type hints, you may want to silence Mypy’s warnings about these. This can be done with the --ignore-missing-imports option.
- Ignore warnings for specific old package with no type hints
- Ex. import numpy as np  # type: ignore
- Alternate keep configuration file :
If you have several files, it might be easier to keep track of which imports to ignore in a configuration file. Mypy reads a file called mypy.ini in the current directory if it is present. This configuration file must contain a section called [mypy] and may contain module specific sections of the form [mypy-module].

The following configuration file will ignore that Numpy is missing type hints:

# mypy.ini

[mypy]

[mypy-numpy]
ignore_missing_imports = True

- Adding Stubs
- Ex. parse package ->
# parse_name.py

import parse

def parse_name(text: str) -> str:
    patterns = (
        "my name is {name}",
        "i'm {name}",
        "i am {name}",
        "call me {name}",
        "{name}",
    )
    for pattern in patterns:
        result = parse.parse(pattern, text)
        if result:
            return result["name"]
    return ""

answer = input("What is your name? ")
name = parse_name(answer)
print(f"Hi {name}, nice to meet you!")
- Type check code above ->
$ mypy parse_name.py 
parse_name.py:3: error: Cannot find module named 'parse'
parse_name.py:3: note: (Perhaps setting MYPYPATH or using the
                       "--ignore-missing-imports" flag would help)
- $ mypy parse_name.py --ignore-missing-imports -> It will miss small big - "return result" instead of return result["name"] 
-  A better solution would be to add type hints to the Parse package itself. As Parse is open source you can actually add types to the source code and send a pull request. you can add the types in a stub file. A stub file is a text file that contains the signatures of methods and functions, but not their implementations. Their main function is to add type hints to code that you for some reason can’t change.
-> Add stub files inside one common directory, and set the MYPYPATH environment variable to point to this directory.
    - export MYPYPATH=/home/gahjelle/python/stubs  (Create file inside your stubs directory that you call parse.pyi)
- Ex. code to add below :
# parse.pyi

from typing import Any, Mapping, Optional, Sequence, Tuple, Union

class Result:
    def __init__(
        self,
        fixed: Sequence[str],
        named: Mapping[str, str],
        spans: Mapping[int, Tuple[int, int]],
    ) -> None: ...
    def __getitem__(self, item: Union[int, str]) -> str: ...
    def __repr__(self) -> str: ...

def parse(
    format: str,
    string: str,
    evaluate_result: bool = ...,
    case_sensitive: bool = ...,
) -> Optional[Result]: ...
$ mypy parse_name.py
parse_name.py:16: error: Incompatible return value type (got
                         "Result", expected "str")

- Typeshed
- Typeshed is a Github repository that contains type hints for the Python standard library, as well as many third-party packages. Typeshed comes included with Mypy so if you are using a package that already has type hints defined in Typeshed, the type checking will just work.

- Using Types at Runtime
- the type hints are available at runtime in the __annotations__ dictionary, and you can use those to do type checks if you desire. Before you run off and write your own package for enforcing types, you should know that there are already several packages doing this for you. Have a look at Enforce, Pydantic, or Pytypes for some examples.
- Another use of type hints is for translating your Python code to C and compiling it for optimization. The popular Cython project uses a hybrid C/Python language to write statically typed Python code.