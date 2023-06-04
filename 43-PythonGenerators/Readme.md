- Source Article
    - https://realpython.com/introduction-to-python-generators/#using-generators
- Have you ever had to work with a dataset so large that it overwhelmed your machine’s memory? Or maybe you have a complex function that needs to maintain an internal state every time it’s called, but the function is too small to justify creating its own class
- generator functions are a special kind of function that return a lazy iterator. 
- Example 1: Reading Large Files
<pre>
- Ex.
csv_gen = csv_reader("some_csv.txt")
row_count = 0

for row in csv_gen:
    row_count += 1

print(f"Row count is {row_count}")
</pre>
- Bad way of loading everything in memory
<pre>
def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result
</pre>
- Good way of yielding 1 row at a time
<pre>
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row
</pre>
- generator expression
csv_gen = (row for row in open(file_name))
- Note
    - Using yield will result in a generator object.
    - Using return will result in the first line of the file only.
- Example 2: Generating an Infinite Sequence
<pre>
- Ex.
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
</pre>
- Use next to get the sequence now -> 
gen = infinite_sequence()
next(gen) -> 0
- Example 3: Detecting Palindromes
<pre>
- Ex.
def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return num
    else:
        return False
- 
>>> for i in infinite_sequence():
...     pal = is_palindrome(i)
...     if pal:
...         print(i)
--> prints till get memory error only palindrome numbers
</pre>
- Understanding Generators
- Generator functions use the Python yield keyword instead of return.
- the state of the function is remembered. That way, when next() is called on a generator object (either explicitly or implicitly within a for loop), the previously yielded variable num is incremented, and then yielded again. 
- Building Generators With Generator Expressions
- Ex. Generator Object
<pre>
>>> nums_squared_gc = (num**2 for num in range(5)) 
</pre>
- print(sys.getsizeof(nums_squared_gc))  -> 120 bytes 
- If the list is smaller than the running machine’s available memory, then list comprehensions can be faster to evaluate than the equivalent generator expression
<pre>
- Ex.
>>> import cProfile
>>> cProfile.run('sum([i * 2 for i in range(10000)])')
         5 function calls in 0.001 seconds
>>> cProfile.run('sum((i * 2 for i in range(10000)))')
         10005 function calls in 0.003 seconds
</pre>
- Understanding the Python Yield Statement
- When you call special methods on the generator, such as next(), the code within the function is executed up to yield.
- When the Python yield statement is hit, the program suspends function execution and returns the yielded value to the caller. State of the function is saved. This includes any variable bindings local to the generator, the instruction pointer, the internal stack, and any exception handling.
<pre>
- Ex.
>>> def multi_yield():
...     yield_str = "This will print the first string"
...     yield yield_str
...     yield_str = "This will print the second string"
...     yield yield_str
...
>>> multi_obj = multi_yield()
>>> print(next(multi_obj))
This will print the first string
>>> print(next(multi_obj))
This will print the second string
>>> print(next(multi_obj))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
</pre>
- Using Advanced Generator Methods
- How to Use .send()
- Ex. Upon encountering a palindrome, your new program will add a digit and start a search for the next one from there

- Creating Data Pipelines With Generators
- Ex. code below using generators :
<pre>
def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)     # yield is an expression, rather than a statement
            if i is not None:
                num = i
        num += 1
</pre>
- More importantly, it allows you to .send() a value back to the generator. When execution picks up after yield, i will take the value that is sent.
<pre>
pal_gen = infinite_palindromes()
for i in pal_gen:
    digits = len(str(i))
    pal_gen.send(10 ** (digits))    -> i value updated back in generator from here.  The program only yields a value once a palindrome is found. It uses len() to determine the number of digits in that palindrome. Then, it sends 10 ** digits to the generator. This brings execution back into the generator logic and assigns 10 ** digits to i. Since i now has a value, the program updates num, increments, and checks for palindromes again.
</pre>
-  coroutine, or a generator function into which you can pass data.

- old way for comparison
<pre>
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
</pre>
- How to Use .throw()
- .throw() allows you to throw exceptions with the generator. 
<pre>
- Ex.
pal_gen = infinite_palindromes()
for i in pal_gen:
    print(i)
    digits = len(str(i))
    if digits == 5:
        pal_gen.throw(ValueError("We don't like large palindromes"))
    pal_gen.send(10 ** (digits))
</pre>
- How to Use .close()
- .close() allows you to stop a generator.
<pre>
- Ex.
pal_gen = infinite_palindromes()
for i in pal_gen:
    print(i)
    digits = len(str(i))
    if digits == 5:
        pal_gen.close()  #  it raises StopIteration, an exception used to signal the end of a finite iterator
    pal_gen.send(10 ** (digits))
</pre>

- Stratergy for building data pipeline
1. Read every line of the file.
2. Split each line into a list of values.
3. Extract the column names.
4. Use the column names and lists to create a dictionary.
5. Filter out the rounds you aren’t interested in.
6. Calculate the total and average values for the rounds you are interested in.
<pre>
- Ex. code 
file_name = "techcrunch.csv"
lines = (line for line in open(file_name))
list_line = (s.rstrip()split(",") for s in lines)
cols = next(list_line)
company_dicts = (dict(zip(cols, data)) for data in list_line)
funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)
total_series_a = sum(funding)
print(f"Total series A fundraising: ${total_series_a}")
</pre>
- Steps done in script above -> 
    - Line 2 reads in each line of the file.
    - Line 3 splits each line into values and puts the values into a list.
    - Line 4 uses next() to store the column names in a list.
    - Line 5 creates dictionaries and unites them with a zip() call:
        - The keys are the column names cols from line 4.
        - The values are the rows in list form, created in line 3.
    - Line 6 gets each company’s series A funding amounts. It also filters out any other raised amount.
    - Line 11 begins the iteration process by calling sum() to get the total amount of series A funding found in the CSV.