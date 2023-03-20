- Source Article
    - https://realpython.com/python-descriptors/
- Descriptors are Python objects that implement a method of the descriptor protocol, which gives you the ability to create objects that have special behavior when they’re accessed as attributes of other objects.
- Ex.
__get__(self, obj, type=None) -> object
__set__(self, obj, value) -> None
__delete__(self, obj) -> None
__set_name__(self, owner, name)
If your descriptor implements just .__get__(), then it’s said to be a non-data descriptor. If it implements .__set__() or .__delete__(), then it’s said to be a data descriptor.
- Ex.
# descriptors.py
class Verbose_attribute():
    def __get__(self, obj, type=None) -> object:
        print("accessing the attribute to get the value")
        return 42
    def __set__(self, obj, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")

class Foo():
    attribute1 = Verbose_attribute()

my_foo_object = Foo()
x = my_foo_object.attribute1
print(x)    -> 42 
x = 3   -> raise attribute error

- Same ex. using property decorator
# property_decorator.py
class Foo():
    @property
    def attribute1(self) -> object:
        print("accessing the attribute to get the value")
        return 42

    @attribute1.setter
    def attribute1(self, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")

my_foo_object = Foo()
x = my_foo_object.attribute1
print(x)

- Same ex. using property method -> property(fget=None, fset=None, fdel=None, doc=None) -> object
# property_function.py
class Foo():
    def getter(self) -> object:
        print("accessing the attribute to get the value")
        return 42

    def setter(self, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")

    attribute1 = property(getter, setter)

my_foo_object = Foo()
x = my_foo_object.attribute1
print(x)

- Python descriptors in methods and functions
- The magic that transforms your obj.method(*args) call into method(obj, *args) is inside a .__get__() implementation of the function object that is, in fact, a non-data descriptor.


- How Attributes Are Accessed With the Lookup Chain
- In Python, every object has a built-in __dict__ attribute. This is a dictionary that contains all the attributes defined in the object itself. 
- in Python, everything is an object. A class is actually an object as well, so it will also have a __dict__ attribute that contains all the attributes and methods of the class.
- Ex.
class Vehicle():
    can_fly = False
    number_of_weels = 0

class Car(Vehicle):
    number_of_weels = 4

    def __init__(self, color):
        self.color = color

my_car = Car("red")
print(my_car.__dict__)          -> {'color': 'red'}
print(type(my_car).__dict__)       -> {'__module__': '__main__', 'number_of_weels': 4, '__init__': <function Car.__init__ at 0x10fdeaea0>, '__doc__': None}
print(Vehicle.__dict__)          -> {can_fly=False, number_of_wheels=0}

print(my_car.__dict__['color'])
print(type(my_car).__dict__['number_of_weels'])
print(type(my_car).__base__.__dict__['can_fly'])

- What happens when you access the attribute of an object with dot notation? 
- Lookup Chain comes in ->
1. First, you’ll get the result returned from the __get__ method of the data descriptor named after the attribute you’re looking for.
2. If that fails, then you’ll get the value of your object’s __dict__ for the key named after the attribute you’re looking for.
3. If that fails, then you’ll get the result returned from the __get__ method of the non-data descriptor named after the attribute you’re looking for.
4. If that fails, then you’ll get the value of your object type’s __dict__ for the key named after the attribute you’re looking for.
5. If that fails, then you’ll get the value of your object parent type’s __dict__ for the key named after the attribute you’re looking for.
6. If that fails, then the previous step is repeated for all the parent’s types in the method resolution order of your object.
7. If everything else has failed, then you’ll get an AttributeError exception.

- Descriptor Protocol 
- The most important methods of this protocol are .__get__() and .__set__(), which have the following signature:
__get__(self, obj, type=None) -> object
__set__(self, obj, value) -> None
When you implement the protocol, keep these things in mind:

- self is the instance of the descriptor you’re writing.
- obj is the instance of the object your descriptor is attached to.
- type is the type of the object the descriptor is attached to.

- Another important thing to know is that Python descriptors are instantiated just once per class. That means that every single instance of a class containing a descriptor shares that descriptor instance.
- Ex. class Foo that defines an attribute number, which is a descriptor. This descriptor accepts a single-digit numeric value and stores it in a property of the descriptor itself. However, this approach won’t work, because each instance of Foo shares the same descriptor instance. 

# descriptors2.py
class OneDigitNumericValue():
    def __init__(self):
        self.value = 0
    def __get__(self, obj, type=None) -> object:
        return self.value
    def __set__(self, obj, value) -> None:
        if value > 9 or value < 0 or int(value) != value:
            raise AttributeError("The value is invalid")
        self.value = value

class Foo():
    number = OneDigitNumericValue()

my_foo_object = Foo()
my_second_foo_object = Foo()

my_foo_object.number = 3
print(my_foo_object.number)    -> 3
print(my_second_foo_object.number)   -> 3

my_third_foo_object = Foo()
print(my_third_foo_object.number)   -> 3

Ex. good idea to use a dictionary to save all the values of the descriptor for all the objects it’s attached to. The downside here is that the descriptor is keeping a strong reference to the owner object. This means that if you destroy the object, then the memory is not released because the garbage collector keeps finding a reference to that object inside the descriptor
# descriptors3.py
class OneDigitNumericValue():
    def __init__(self):
        self.value = {}

    def __get__(self, obj, type=None) -> object:
        try:
            return self.value[obj]
        except:
            return 0

    def __set__(self, obj, value) -> None:
        if value > 9 or value < 0 or int(value) != value:
            raise AttributeError("The value is invalid")
        self.value[obj] = value

class Foo():
    number = OneDigitNumericValue()

my_foo_object = Foo()
my_second_foo_object = Foo()

my_foo_object.number = 3
print(my_foo_object.number)    -> 3
print(my_second_foo_object.number)      -> 0 

my_third_foo_object = Foo()
print(my_third_foo_object.number)     -> 0

- Ex. The best solution here is to simply not store values in the descriptor itself, but to store them in the object that the descriptor is attached to. when you set a value to the number attribute of your object, the descriptor stores it in the __dict__ attribute of the object it’s attached to using the same name of the descriptor itself.The only problem here is that when you instantiate the descriptor you have to specify the name as a parameter
# descriptors4.py
class OneDigitNumericValue():
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, type=None) -> object:
        return obj.__dict__.get(self.name) or 0

    def __set__(self, obj, value) -> None:
        obj.__dict__[self.name] = value

class Foo():
    number = OneDigitNumericValue("number")

my_foo_object = Foo()
my_second_foo_object = Foo()

my_foo_object.number = 3
print(my_foo_object.number)
print(my_second_foo_object.number)

my_third_foo_object = Foo()
print(my_third_foo_object.number)

- Ex. Best solution for Python >=3.6 is __set_name__(self, owner, name). With this new method, whenever you instantiate a descriptor this method is called and the name parameter automatically set.

# descriptors5.py
class OneDigitNumericValue():
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None) -> object:
        return obj.__dict__.get(self.name) or 0

    def __set__(self, obj, value) -> None:
        obj.__dict__[self.name] = value

class Foo():
    number = OneDigitNumericValue()

my_foo_object = Foo()
my_second_foo_object = Foo()

my_foo_object.number = 3
print(my_foo_object.number)
print(my_second_foo_object.number)

my_third_foo_object = Foo()
print(my_third_foo_object.number)

- Why Use Python Descriptors?
- Lazy Properties -> These are properties whose initial values are not loaded until they’re accessed for the first time. Then, they load their initial value and keep that value cached for later reuse.
- Ex. Get an answer after 3 secs everytime method is called 
# slow_properties.py
import time

class DeepThought:
    def meaning_of_life(self):
        time.sleep(3)
        return 42

my_deep_thought_instance = DeepThought()
print(my_deep_thought_instance.meaning_of_life())
print(my_deep_thought_instance.meaning_of_life())
print(my_deep_thought_instance.meaning_of_life())

- Ex. when you use the @LazyProperty descriptor, you’re instantiating a descriptor and passing to it .meaning_of_life(). This descriptor stores both the method and its name as instance variables. Since it is a non-data descriptor, when you first access the value of the meaning_of_life attribute, .__get__() is automatically called and executes .meaning_of_life() on the my_deep_thought_instance object. The resulting value is stored in the __dict__ attribute of the object itself. When you access the meaning_of_life attribute again, Python will use the lookup chain to find a value for that attribute inside the __dict__ attribute, and that value will be returned immediately.
# lazy_properties.py
import time

class LazyProperty:
    def __init__(self, function):
        self.function = function
        self.name = function.__name__

    def __get__(self, obj, type=None) -> object:
        obj.__dict__[self.name] = self.function(obj)
        return obj.__dict__[self.name]

class DeepThought:
    @LazyProperty
    def meaning_of_life(self):
        time.sleep(3)
        return 42

my_deep_thought_instance = DeepThought()
print(my_deep_thought_instance.meaning_of_life)
print(my_deep_thought_instance.meaning_of_life)
print(my_deep_thought_instance.meaning_of_life)

- if add code below for a data descriptor then trick of the lazy property stops working.
    def __set__(self, obj, value):
        pass

- DRY Code -> Every piece of knowledge must have a single, unambiguous, authoritative representation within a system
- Ex. Python descriptors give developers a great tool to write reusable code that can be shared among different properties or even different classes.
Consider an example where you have five different properties with the same behavior. Each property can be set to a specific value only if it’s an even number. Otherwise, it’s value is set to 0
- Bad way of doing it
# properties.py
class Values:
    def __init__(self):
        self._value1 = 0
        self._value2 = 0
        self._value3 = 0
        self._value4 = 0
        self._value5 = 0

    @property
    def value1(self):
        return self._value1

    @value1.setter
    def value1(self, value):
        self._value1 = value if value % 2 == 0 else 0

    @property
    def value2(self):
        return self._value2

    @value2.setter
    def value2(self, value):
        self._value2 = value if value % 2 == 0 else 0

    @property
    def value3(self):
        return self._value3

    @value3.setter
    def value3(self, value):
        self._value3 = value if value % 2 == 0 else 0

    @property
    def value4(self):
        return self._value4

    @value4.setter
    def value4(self, value):
        self._value4 = value if value % 2 == 0 else 0

    @property
    def value5(self):
        return self._value5

    @value5.setter
    def value5(self, value):
        self._value5 = value if value % 2 == 0 else 0

my_values = Values()
my_values.value1 = 1
my_values.value2 = 4
print(my_values.value1)
print(my_values.value2)

- Ex. Better implementation below -> 
# properties2.py
class EvenNumber:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None) -> object:
        return obj.__dict__.get(self.name) or 0

    def __set__(self, obj, value) -> None:
        obj.__dict__[self.name] = (value if value % 2 == 0 else 0)

class Values:
    value1 = EvenNumber()
    value2 = EvenNumber()
    value3 = EvenNumber()
    value4 = EvenNumber()
    value5 = EvenNumber()

my_values = Values()
my_values.value1 = 1
my_values.value2 = 4
print(my_values.value1)
print(my_values.value2)













