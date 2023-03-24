- The language itself is built around dictionaries. 
- Modules, classes, objects, globals(), locals(): all of these are dictionaries. 
- Dictionaries map keys to values and store them in an array or collection.
- The keys must be of a hashable type, which means that they must have hash value that never change during the key’s lifetime.
- dictionaries are indexed by keys, 
- In Python 3.6 and beyond, dictionaries are ordered data structures, which means that they keep their elements in the same order in which they were introduced
- Iterate Through a Dictionary in Python
- Iterating Through Keys Directly
- To visualize the methods and attributes of any Python object, you can use dir()
- Ex.
>>> dir({})
['__class__', '__contains__', '__delattr__', ... , '__iter__', ...]
- For mappings (like dictionaries), .__iter__() should iterate over the keys.
- Ex.
>>> a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
>>> for key in a_dict:
...     print(key)             #  print(key, '->', a_dict[key])
...
color
fruit
pet
- Iterating Through .items()
- Ex.
>>> a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
>>> d_items = a_dict.items()
>>> d_items  # Here d_items is a view of items
dict_items([('color', 'blue'), ('fruit', 'apple'), ('pet', 'dog')])
- Ex. loop through it
>>> for item in a_dict.items():
...     print(item)
...
('color', 'blue')
('fruit', 'apple')
('pet', 'dog')
- Ex. unpack as tuple object
>>> for key, value in a_dict.items():
...     print(key, '->', value)
...
color -> blue
fruit -> apple
pet -> dog
- Iterating Through .keys()
- Ex.
>>> a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
>>> keys = a_dict.keys()
>>> keys
dict_keys(['color', 'fruit', 'pet'])
- Iterating Through .values()
- Ex. 
>>> a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
>>> values = a_dict.values()
>>> values
dict_values(['blue', 'apple', 'dog'])
- You can do membership tests
- Ex.
>>> a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
>>> 'pet' in a_dict.keys()
True
>>> 'apple' in a_dict.values()
True
- Modifying Values and Keys
- Ex.
>>> prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
>>> for k, v in prices.items():
...     prices[k] = round(v * 0.9, 2)  # Apply a 10% discount
...
>>> prices
{'apple': 0.36, 'orange': 0.32, 'banana': 0.23}
- Ex. delete key
>>> prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
>>> for key in list(prices.keys()):  # Use a list instead of a view
...     if key == 'orange':
...         del prices[key]  # Delete a key from prices
...
>>> prices
{'apple': 0.4, 'banana': 0.25}
- cannot delete with .keys directly
>>> # Python 3. dict.keys() returns a view object, not a list
>>> prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
>>> for key in prices.keys():  # .keys() returns a dictionary-view object, which yields keys on demand one at a time
...     if key == 'orange':
...         del prices[key]
...
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    for key in prices.keys():
RuntimeError: dictionary changed size during iteration

- Real-World Examples
- Ex. 1 Turning Keys Into Values and Vice Versa
>>> a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
>>> new_dict = {}
>>> for key, value in a_dict.items():
...     new_dict[value] = key
...
>>> new_dict
{1: 'one', 2: 'two', 3: 'thee', 4: 'four'}
- Ex. 2. Filtering Items
>>> a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
>>> new_dict = {}  # Create a new empty dictionary
>>> for key, value in a_dict.items():
...     # If value satisfies the condition, then store it in new_dict
...     if value <= 2:
...         new_dict[key] = value
...
>>> new_dict
{'one': 1, 'two': 2}
- Ex. 3 Doing Some Calculations
>>> incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
>>> total_income = 0.00
>>> for value in incomes.values():
...     total_income += value  # Accumulate the values in total_income
...
>>> total_income
14100.0

- Using Comprehensions
-  they need two expressions separated with a colon followed by for and if (optional) clauses. When a dictionary comprehension is run, the resulting key-value pairs are inserted into a new dictionary in the same order in which they were produced.
- Ex. two lists of data, and you need to create a new dictionary from them
>>> objects = ['blue', 'apple', 'dog']
>>> categories = ['color', 'fruit', 'pet']
>>> a_dict = {key: value for key, value in zip(categories, objects)}
>>> a_dict     ->   {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
- Turning Keys Into Values and Vice Versa: Revisited
- Ex. new_dict = {value: key for key, value in a_dict.items()}
- Filtering Items: Revisited
- Ex. new_dict = {k: v for k, v in a_dict.items() if v <= 2}
- Doing Some Calculations: Revisited
- Ex. total_income = sum([value for value in incomes.values()])
- Better way to do above to save memory -  A generator expression is an expression that returns an iterator. It looks like a list comprehension, but instead of brackets you need to use parentheses to define it. generator expressions yield elements on demand so store 1 element at a time 
- Ex. total_income = sum(value for value in incomes.values())   OR total_income = sum(incomes.values())
- Removing Specific Items
- Key-view objects also support common set operations. 
- Ex. 
>>> incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
>>> non_citric = {k: incomes[k] for k in incomes.keys() - {'orange'}}
>>> non_citric
{'apple': 5600.0, 'banana': 5000.0}
- Sorting a Dictionary
- Ex. sorted(incomes) returns a list of sorted keys that you can use to generate the new dictionary sorted_dict
>>> # Python 3.6, and beyond
>>> incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
>>> sorted_income = {k: incomes[k] for k in sorted(incomes)}
>>> sorted_income
{'apple': 5600.0, 'banana': 5000.0, 'orange': 3500.0}

- Iterating in Sorted Order
- When you call sorted(iterable), you get a list with the elements of iterable in sorted order.
- Sorted by Keys
- If you need to iterate through a dictionary in Python and want it to be sorted by keys, then you can use your dictionary as an argument to sorted().
- Ex.
>>> incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
>>> for key in sorted(incomes):
...     print(key, '->', incomes[key])
...
apple -> 5600.0
banana -> 5000.0
orange -> 3500.0
- Sorted by Values
- Use sorted() but with a second argument called key. The key keyword argument specifies a function of one argument that is used to extract a comparison key from each element you’re processing.
- Ex. 
>>> incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
>>> def by_value(item):
...     return item[1]
...
>>> for k, v in sorted(incomes.items(), key=by_value):
...     print(k, '->', v)
...
('orange', '->', 3500.0)
('banana', '->', 5000.0)
('apple', '->', 5600.0)
- Alternate directly sort with values but return values only without keys 
>>> for value in sorted(incomes.values()):
...     print(value)
- Reversed
- Ex.
>>> incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
>>> for key in sorted(incomes, reverse=True):
...     print(key, '->', incomes[key])
...
orange -> 3500.0
banana -> 5000.0
apple -> 5600.0
- sorted() doesn’t really modify the order of the underlying dictionary. What really happen is that sorted() creates an independent list with its element in sorted order, so incomes remains the same:

- Iterating Destructively With .popitem()
- 
- Ex.
# File: dict_popitem.py

- Iterating Destructively With .popitem()
- .popitem(), which will remove and return an arbitrary key-value pair from a dictionary. On the other hand, when you call .popitem() on an empty dictionary, it raises a KeyError.
- Ex. 
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
while True:
    try:
        print(f'Dictionary length: {len(a_dict)}')
        item = a_dict.popitem()
        # Do something with item here...
        print(f'{item} removed')
    except KeyError:
        print('The dictionary has no item now...')
        break

- Using Some of Python’s Built-In Functions
- map()
- Python’s map() is defined as map(function, iterable, ...) and returns an iterator that applies function to every item of iterable, yielding the results on demand.
- Ex.
>>> prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
>>> def discount(current_price):
...     return (current_price[0], round(current_price[1] * 0.95, 2))
...
>>> new_prices = dict(map(discount, prices.items()))
>>> new_prices
{'apple': 0.38, 'orange': 0.33, 'banana': 0.24}
- filter()
- filter(function, iterable) and returns an iterator from those elements of iterable for which function returns True.
- Ex.
>>> prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
>>> def has_low_price(price):
...     return prices[price] < 0.4
...
>>> low_price = list(filter(has_low_price, prices.keys()))
>>> low_price
['orange', 'banana']

- Using collections.ChainMap
- ChainMap, which is a dictionary-like class for creating a single view of multiple mappings (like dictionaries). With ChainMap, you can group multiple dictionaries together to create a single, updateable view.
- Ex.
>>> from collections import ChainMap
>>> fruit_prices = {'apple': 0.40, 'orange': 0.35}
>>> vegetable_prices = {'pepper': 0.20, 'onion': 0.55}
>>> chained_dict = ChainMap(fruit_prices, vegetable_prices)
>>> chained_dict  # A ChainMap object
ChainMap({'apple': 0.4, 'orange': 0.35}, {'pepper': 0.2, 'onion': 0.55})
>>> for key in chained_dict:
...     print(key, '->', chained_dict[key])
...
pepper -> 0.2
orange -> 0.35
onion -> 0.55
apple -> 0.4

- Using itertools
- Iteration tasks
- Cyclic Iteration With cycle() ->  you can use itertools.cycle(iterable), which makes an iterator returning elements from iterable and saving a copy of each. When iterable is exhausted, cycle() returns elements from the saved copy. This is performed in cyclic fashion, so it’s up to you to stop the cycle.
- Ex. 
>>> from itertools import cycle
>>> prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
>>> times = 3  # Define how many times you need to iterate through prices
>>> total_items = times * len(prices)
>>> for item in cycle(prices.items()):
...     if not total_items:
...         break
...     total_items -= 1
...     print(item)
...
('apple', 0.4)
('orange', 0.35)
('banana', 0.25)
('apple', 0.4)
('orange', 0.35)
('banana', 0.25)
('apple', 0.4)
('orange', 0.35)
('banana', 0.25)
- Chained Iteration With chain()
- chain(*iterables), which gets some iterables as arguments and makes an iterator that yields elements from the first iterable until it’s exhausted, then iterates over the next iterable and so on, until all of them are exhausted.
- Ex.
>>> from itertools import chain
>>> fruit_prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
>>> vegetable_prices = {'pepper': 0.20, 'onion': 0.55, 'tomato': 0.42}
>>> for item in chain(fruit_prices.items(), vegetable_prices.items()):
...     print(item)
...
('apple', 0.4)
('orange', 0.35)
('banana', 0.25)
('pepper', 0.2)
('onion', 0.55)
('tomato', 0.42)

- Using the Dictionary Unpacking Operator (**)
- merge the two dictionaries into a new one and then iterate through it
- Ex. 
>>> fruit_prices = {'apple': 0.40, 'orange': 0.35}
>>> vegetable_prices = {'pepper': 0.20, 'onion': 0.55}
>>> # How to use the unpacking operator **
>>> {**vegetable_prices, **fruit_prices}
{'pepper': 0.2, 'onion': 0.55, 'apple': 0.4, 'orange': 0.35}
>>> # You can use this feature to iterate through multiple dictionaries
>>> for k, v in {**vegetable_prices, **fruit_prices}.items():
...     print(k, '->', v)
...
pepper -> 0.2
onion -> 0.55
apple -> 0.4
orange -> 0.35
- if the dictionaries you’re trying to merge have repeated or common keys, then the values of the right-most dictionary will prevail
