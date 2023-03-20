- python property decorator
    -  https://www.freecodecamp.org/news/python-property-decorator/
- Advantages
    - The syntax used to define properties is very concise and readable.
    - You can access instance attributes exactly as if they were public attributes while using the "magic" of intermediaries (getters and setters) to validate new values and to avoid accessing or modifying the data directly.
    - By using @property, you can "reuse" the name of a property to avoid creating new names for the getters, setters, and deleters.
- Decorators
- Note: In general, we would write @<decorator_function_name>
- Ex. A decorator function is basically a function that adds new functionality to a function that is passed as argument.
def decorator(f):
    def new_function():
        print("Extra Functionality")
        f()
    return new_function

@decorator
def initial_function():
    print("Initial Functionality")

initial_function()

Ex. 
class House:

	def __init__(self, price):
		self.price = price

# Access value
obj.price

# Modify value
obj.price = 40000

- let's say that you are asked to make this attribute protected (non-public) and validate the new value before assigning it.
- Way 1 wont work as need to change everywhere using getter and setter methods ->
# Changed from obj.price
obj.get_price()

# Changed from obj.price = 40000
obj.set_price(40000)

- With @property, you will able to add getters and setters "behind the scenes" without affecting the syntax that you used to access or modify the attribute when it was public.
- Better implementation below -> 
class House:

	def __init__(self, price):
		self._price = price

	@property
	def price(self):
		return self._price
	
	@price.setter
	def price(self, new_price):
		if new_price > 0 and isinstance(new_price, float):
			self._price = new_price
		else:
			print("Please enter a valid price")

	@price.deleter
	def price(self):
		del self._price

# Access value
obj.price

# Modify value
obj.price = 40000

# Delete value
del obj.price

- Specifically, you can define three methods for a property:

    - A getter - to access the value of the attribute.
    - A setter - to set the value of the attribute.
    - A deleter - to delete the instance attribute.

- 