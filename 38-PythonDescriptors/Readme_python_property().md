- Python's property(): Add Managed Attributes to Your Classes
    - https://realpython.com/python-property/
- With Python’s property(), you can create managed attributes in your classes. You can use managed attributes, also known as properties, when you need to modify their internal implementation without changing the public API of the class.
- Managing Attributes in Your Classes
- Attributes represent or hold the internal state of a given object, which you’ll often need to access and mutate. Either you can access and mutate the attribute directly or you can use methods.
- Typically, you have at least two ways to manage an attribute. Either you can access and mutate the attribute directly or you can use methods. 
- If you expose your attributes to the user, then they become part of the public API of your classes. Your user will access and mutate them directly in their code. The problem comes when you need to change the internal implementation of a given attribute.
- you should provide getter and setter methods, also known as accessors and mutators, respectively. These methods offer a way to change the internal implementation of your attributes without changing your public API.
- The Getter and Setter Approach in Python
- Ex. 
# point.py

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return self._y

    def set_y(self, value):
        self._y = value

>>> from point import Point
>>> point = Point(12, 5)
>>> point.get_x()   -> 12
>>> point.get_y()  -> 5
>>> point.set_x(42)

- The Pythonic Approach
Ex.
>>> class Point:
...     def __init__(self, x, y):
...         self.x = x
...         self.y = y
- Python provides handy tools that allow you to change the underlying implementation of your attributes without changing your public API. The most popular approach is to turn your attributes into properties.
- Properties represent an intermediate functionality between a plain attribute (or field) and a method. In other words, they allow you to create methods that behave like attributes. 
- Python’s property()
- This function allows you to turn class attributes into properties or managed attributes. With property(), you can attach getter and setter methods to given class attributes. 
- property(fget=None, fset=None, fdel=None, doc=None)
- Argument	    Description
    fget	    Function that returns the value of the managed attribute
    fset	    Function that allows you to set the value of the managed attribute
    fdel	    Function to define how the managed attribute handles deletion
    doc	        String representing the property’s docstring
- The return value of property() is the managed attribute itself. If you access the managed attribute, as in obj.attr, then Python automatically calls fget(). If you assign a new value to the attribute, as in obj.attr = value, then Python calls fset() using the input value as an argument. Finally, if you run a del obj.attr statement, then Python automatically calls fdel()
- Creating Attributes With property()
- Ex.  you create a class attribute called .radius to store the property object. To initialize the property, you pass the three methods as arguments to property(). You also pass a suitable docstring for your property.
# circle.py

class Circle:
    def __init__(self, radius):
        self._radius = radius

    def _get_radius(self):
        print("Get radius")
        return self._radius

    def _set_radius(self, value):
        print("Set radius")
        self._radius = value

    def _del_radius(self):
        print("Delete radius")
        del self._radius

    radius = property(
        fget=_get_radius,
        fset=_set_radius,
        fdel=_del_radius,
        doc="The radius property."
    )

- Use lambda functions as getter methods 
>>> class Circle:
...     def __init__(self, radius):
...         self._radius = radius
...     radius = property(lambda self: self._radius)

- Properties are class attributes that manage instance attributes. You can think of a property as a collection of methods bundled together. 
- access methods using Circle.radius.fget
- dir(Circle.radius)   -> Properties are also overriding descriptors. .__set__() and .__get__() in the list. These methods provide a default implementation of the descriptor protocol.The default implementation of .__set__(), for example, runs when you don’t provide a custom setter method. 
[..., '__get__', ..., '__set__', ...]

- Using property() as a Decorator
- decorator -> 
@decorator
def func(a):
    return a

eq. code below :

def func(a):
    return a
func = decorator(func)

- Ex. code using property decorator -> At the end of the process, you get a full-fledged property with the getter, setter, and deleter methods.
# circle.py

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """The radius property."""
        print("Get radius")
        return self._radius

    @radius.setter
    def radius(self, value):
        print("Set radius")
        self._radius = value

    @radius.deleter
    def radius(self):
        print("Delete radius")
        del self._radius
- When you decorate the second .radius() method with @radius.setter (line 13), you create a new property and reassign the class-level name .radius (line 8) to hold it. This new property contains the same set of methods of the initial property at line 8 with the addition of the new setter method provided on line 14. Finally, the decorator syntax reassigns the new property to the .radius class-level name.
- Use above code same as before -> 
>>> from circle import Circle
>>> circle = Circle(42.0)
>>> circle.radius
Get radius
42.0
>>> circle.radius = 100.0
    - The @property decorator must decorate the getter method.
    - The docstring must go in the getter method.
    - The setter and deleter methods must be decorated with the name of the getter method plus .setter and .deleter, respectively.

- Providing Read-Only Attributes
- Ex.you need an immutable Point class that doesn’t allow the user to mutate the original value of its coordinates, x and y.  the default .__set__() implementation raises an AttributeError when you don’t define a proper setter method.

# point.py

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

>>> from point import Point

>>> point = Point(12, 5)

>>> # Read coordinates
>>> point.x
12
>>> point.y
5

>>> # Write coordinates
>>> point.x = 42
Traceback (most recent call last):
    ...
AttributeError: can't set attribute

- Ex. with more explicit error messages here -> 
# point.py

class WriteCoordinateError(Exception):
    pass

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        raise WriteCoordinateError("x coordinate is read-only")

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        raise WriteCoordinateError("y coordinate is read-only")

- Creating Read-Write Attributes
- eX. Say you want your Circle class to have a .diameter attribute. However, taking the radius and the diameter in the class initializer seems unnecessary because you can compute the one using the other. Here’s a Circle that manages .radius and .diameter as read-write attributes
# circle.py

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = float(value)

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

- In this case, the class initializer assigns the input value to the .radius property directly instead of storing it in a dedicated non-public attribute, such as ._radius. Why? Because you need to make sure that every value provided as a radius, including the initialization value, goes through the setter method and gets converted to a floating-point number.
>>> from circle import Circle

>>> circle = Circle(42)
>>> circle.radius
42.0

>>> circle.diameter
84.0

>>> circle.diameter = 100
>>> circle.diameter
100.0

>>> circle.radius
50.0

- Providing Write-Only Attributes
- you can make your getter method raise an exception every time a user accesses the underlying attribute value.
- Ex. handling passwords with a write-only property

# users.py

import hashlib
import os

class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @property
    def password(self):
        raise AttributeError("Password is write-only")

    @password.setter
    def password(self, plaintext):
        salt = os.urandom(32)
        self._hashed_password = hashlib.pbkdf2_hmac(
            "sha256", plaintext.encode("utf-8"), salt, 100_000
        )

>>> from users import User
>>> john = User("John", "secret")
>>> john._hashed_password
b'b\xc7^ai\x9f3\xd2g ... \x89^-\x92\xbe\xe6'
>>> john.password
Traceback (most recent call last):
    ...
AttributeError: Password is write-only

- Putting Python’s property() Into Action
- Ex.1 
- Validating Input Values
- the Point example, you may require the values of .x and .y to be valid numbers.
# point.py

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        try:
            self._x = float(value)
            print("Validated!")
        except ValueError:
            raise ValueError('"x" must be a number') from None

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        try:
            self._y = float(value)
            print("Validated!")
        except ValueError:
            raise ValueError('"y" must be a number') from None

>>> from point import Point

>>> point = Point(12, 5)
Validated!
Validated!
>>> point.x
12.0
>>> point.y
5.0
>>> point.x = 42
Validated!
>>> point.x
42.0
>>> point.x = "one"
Traceback (most recent call last):
     ...
ValueError: "x" must be a number

- Better implementation of above code eliminating repetition 
# point.py

class Coordinate:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        try:
            instance.__dict__[self._name] = float(value)
            print("Validated!")
        except ValueError:
            raise ValueError(f'"{self._name}" must be a number') from None

class Point:
    x = Coordinate()
    y = Coordinate()

    def __init__(self, x, y):
        self.x = x
        self.y = y

- Providing Computed Attributes
- If you need an attribute that builds its value dynamically whenever you access it, then property() is the way to go. They’re handy when you need them to look like eager attributes, but you want them to be lazy. optimize computation costs when you access the attribute often.
- Ex.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height
The read-only property .area computes and returns the area of the current rectangle every time you access it.

- Ex. provide an auto-formatted value for a given attribute:
class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = float(price)

    @property
    def price(self):
        return f"${self._price:,.2f}"

- Ex. You want to provide polar coordinates for your point so that you can use them in a few computations
# point.py

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def distance(self):
        return round(math.dist((0, 0), (self.x, self.y)))

    @property
    def angle(self):
        return round(math.degrees(math.atan(self.y / self.x)), 1)

    def as_cartesian(self):
        return self.x, self.y

    def as_polar(self):
        return self.distance, self.angle

>>> from point import Point
>>> point = Point(12, 5)
>>> point.x
12
>>> point.y
5
>>> point.distance
13
>>> point.angle
22.6
>>> point.as_cartesian()
(12, 5)
>>> point.as_polar()
(13, 22.6)

- Caching Computed Attributes
- if you’re creating an attribute that you use frequently, then computing it every time can be costly and wasteful. A good strategy is to cache them once the computation is done.
- you can cache the computed value and save it in a non-public dedicated attribute for further reuse.
- To prevent unexpected behaviors, you need to think of the mutability of the input data.
- Ex. it has the drawback that if you ever change the value of .radius, then .diameter won’t return a correct value:
# circle.py

from time import sleep

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._diameter = None

    @property
    def diameter(self):
        if self._diameter is None:
            sleep(0.5)  # Simulate a costly computation
            self._diameter = self.radius * 2
        return self._diameter

>>> from circle import Circle
>>> circle = Circle(42.0)
>>> circle.radius
42.0
>>> circle.diameter  # With delay
84.0
>>> circle.diameter  # Without delay
84.0
>>> circle.radius = 100.0
>>> circle.diameter  # Wrong diameter
84.0

- Ex. Fix above implementation to change diameter when radius changes - If the input data for a computed attribute mutates, then you need to recalculate the attribute. The setter method of the .radius property resets ._diameter to None every time you change the value of the radius.
# circle.py

from time import sleep

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._diameter = None
        self._radius = value

    @property
    def diameter(self):
        if self._diameter is None:
            sleep(0.5)  # Simulate a costly computation
            self._diameter = self._radius * 2
        return self._diameter
>>> from circle import Circle
>>> circle = Circle(42.0)
>>> circle.radius
42.0
>>> circle.diameter  # With delay
84.0
>>> circle.diameter  # Without delay
84.0
>>> circle.radius = 100.0
>>> circle.diameter  # With delay
200.0

- Another way to create cached properties is to use functools.cached_property(). The property computes its value only once and caches it as a normal attribute during the lifetime of the instance
- Ex. 
# circle.py

from functools import cached_property
from time import sleep

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @cached_property
    def diameter(self):
        sleep(0.5)  # Simulate a costly computation
        return self.radius * 2
Here, .diameter computes and caches its value the first time you access it. This kind of implementation is suitable for those computations in which the input values don’t mutate.So if radius changes, then diameter doesnt change. 
>>> # Allow direct assignment
>>> circle.diameter = 200
>>> circle.diameter  # Cached value
200
- It does allow direct assignment so add property to cache to disallow setting direct assignment. Ex. 
# circle.py

from functools import cache
from time import sleep

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    @cache
    def diameter(self):
        sleep(0.5) # Simulate a costly computation
        return self.radius * 2

- Logging Attribute Access and Mutation
- Sometimes you need to keep track of what your code does and how your programs flow. A way to do that in Python is to use logging. This module provides all the functionality you would require for logging your code. It’ll allow you to constantly watch the code and generate useful information about how it works.If you ever need to keep track of how and when you access and mutate a given attribute, then you can take advantage of property() for that, too:
- Ex. 
# circle.py

import logging

logging.basicConfig(
    format="%(asctime)s: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S"
)

class Circle:
    def __init__(self, radius):
        self._msg = '"radius" was %s. Current value: %s'
        self.radius = radius

    @property
    def radius(self):
        """The radius property."""
        logging.info(self._msg % ("accessed", str(self._radius)))
        return self._radius

    @radius.setter
    def radius(self, value):
        try:
            self._radius = float(value)
            logging.info(self._msg % ("mutated", str(self._radius)))
        except ValueError:
            logging.info('validation error while mutating "radius"')

- Managing Attribute Deletion
- Ex. Say you’re implementing your own tree data type. A tree is an abstract data type that stores elements in a hierarchy. The tree components are commonly known as nodes. Each node in a tree has a parent node, except for the root node. Nodes can have zero or more children. Now suppose you need to provide a way to delete or clear the list of children of a given node. 
# tree.py

class TreeNode:
    def __init__(self, data):
        self._data = data
        self._children = []

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, value):
        if isinstance(value, list):
            self._children = value
        else:
            del self.children
            self._children.append(value)

    @children.deleter
    def children(self):
        self._children.clear()

    def __repr__(self):
        return f'{self.__class__.__name__}("{self._data}")'

>>> from tree import TreeNode
>>> root = TreeNode("root")
>>> child1 = TreeNode("child 1")
>>> child2 = TreeNode("child 2")
>>> root.children = [child1, child2]
>>> root.children
[TreeNode("child 1"), TreeNode("child 2")]
>>> del root.children
>>> root.children
[]

- Creating Backward-Compatible Class APIs
- you need to guarantee that modifications to the internal implementation don’t affect how end users work with your classes.
- If you ever need to modify how you compute a given public attribute, then you can turn it into a property. Properties make it possible to perform extra processing, such as data validation, without having to modify your public APIs.
- Ex. 
class Currency:
    def __init__(self, units, cents):
        self.units = units
        self.cents = cents

    # Currency implementation...
- Now say that your requirements change, and you decide to store the total number of cents instead of the units and cents.
# currency.py

CENTS_PER_UNIT = 100

class Currency:
    def __init__(self, units, cents):
        self._total_cents = units * CENTS_PER_UNIT + cents

    @property
    def units(self):
        return self._total_cents // CENTS_PER_UNIT

    @units.setter
    def units(self, value):
        self._total_cents = self.cents + value * CENTS_PER_UNIT

    @property
    def cents(self):
        return self._total_cents % CENTS_PER_UNIT

    @cents.setter
    def cents(self, value):
        self._total_cents = self.units * CENTS_PER_UNIT + value

    # Currency implementation...

- Overriding Properties in Subclasses
- when you override an existing property from a parent class, you override the whole functionality of that property. In this example, you reimplemented the getter method only. Because of that, .name lost the rest of the functionality from the base class. You don’t have a setter method any longer.
- Ex. 
# persons.py

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # Person implementation...

class Employee(Person):
    @property
    def name(self):
        return super().name.upper()

    # Employee implementation...

>>> from persons import Employee, Person

>>> person = Person("John")
>>> person.name
'John'
>>> person.name = "John Doe"
>>> person.name
'John Doe'

>>> employee = Employee("John")
>>> employee.name
'JOHN'
>>> employee.name = "John Doe"        #setter method is lost from parent class as only getter defined in sub class. Need to define setter in subclass as well 
Traceback (most recent call last):
    ...
AttributeError: can't set attribute

- A property is a special type of class member that provides functionality that’s somewhere in between regular attributes and methods. Properties allow you to modify the implementation of instance attributes without changing the public API of the class. Properties are the Pythonic way to create managed attributes in your classes. 
