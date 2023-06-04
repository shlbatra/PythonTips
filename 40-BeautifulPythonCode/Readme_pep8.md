- How to Write Beautiful Python Code With PEP 8
    - https://realpython.com/python-pep8/
- The primary focus of PEP 8 is to improve the readability and consistency of Python code.
- A PEP is a document that describes new features proposed for Python and documents aspects of Python, like design and style, for the community.
- Naming Conventions
- Naming Styles
Type	        Naming Convention	                                                                        Examples
Function	    Use a lowercase word or words. Separate words by underscores to improve readability.	    function, my_function
Variable	    Use a lowercase single letter, word, or words. Separate words with underscores to improve readability.	   x, var, my_variable
Class	        Start each word with a capital letter. Do not separate words with underscores. This style is called camel case or pascal case.	        Model, MyClass
Method	        Use a lowercase word or words. Separate words with underscores to improve readability.	    class_method, method
Constant	    Use an uppercase single letter, word, or words. Separate words with underscores to improve readability.	        CONSTANT, MY_CONSTANT, MY_LONG_CONSTANT
Module	        Use a short, lowercase word or words. Separate words with underscores to improve readability.	        module.py, my_module.py
Package	        Use a short, lowercase word or words. Do not separate words with underscores.	        package, mypackage
- The best way to name your objects in Python is to use descriptive names to make it clear what the object represents.<br>
Ex.<br>
<pre>
    Not recommended                 Recommended <br>
    x = 'John Smith'                name = 'John Smith' <br>
    y, z = x.split()                first_name, last_name = name.split() <br>
    print(z, y, sep=', ')           print(last_name, first_name, sep=', ') <br>
</pre>
<br>
<pre>
    Not recommended                    Recommended  <br>
    def db(x):                          def multiply_by_two(x):  <br>
        return x * 2                        return x * 2
</pre>
<br>
- Code Layout<br>
- Blank Lines<br>
    - Surround top-level functions and classes with two blank lines.<br>
    - Surround method definitions inside classes with a single blank line.<br>
    - Use blank lines sparingly inside functions to show clear steps.<br>
- Maximum Line Length and Line Breaking<br>
- Python will assume line continuation if code is contained within parentheses, brackets, or braces<br>
Ex. 
def function(arg_one, arg_two,
             arg_three, arg_four):<br>
    return arg_one
- Use backslash to break lines <br>
from mypkg import example1, \ <br>
    example2, example3
- Break before Binary operator<br>
- Ex.<br>
Recommended<br>
total = (first_variable
         + second_variable
         - third_variable)<br>
- Indentation
- Tabs vs. Spaces
- The indentation level of lines of code in Python determines how statements are grouped together.
    - Use 4 consecutive spaces to indicate indentation.
    - Prefer spaces over tabs.
- If you’re using Python 3, you must be consistent with your choice. Otherwise, your code will not run.<br>
- Indentation Following Line Breaks<br>
<pre>
    1. align the indented block with the opening delimiter:
    Ex.
    def function(arg_one, arg_two,
                arg_three, arg_four):
        return arg_one
    x = 5
    if (x > 3 and
            x < 10):
        print(x)
    2. hanging indent. This is a typographical term meaning that every line but the first in a paragraph or statement is indented. 
    Ex.
    var = function(
        arg_one, arg_two,
        arg_three, arg_four)
    def function(
            arg_one, arg_two,
            arg_three, arg_four):
        return arg_one
</pre>

- Where to Put the Closing Brace
- Line up the closing brace with the first non-whitespace character of the previous line:
Ex.
list_of_numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
    ]
- Line up the closing brace with the first character of the line that starts the construct:
Ex.
list_of_numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]

- Comments
    - Limit the line length of comments and docstrings to 72 characters.
    - Use complete sentences, starting with a capital letter.
    - Make sure to update comments if you change your code.
- Block Comments
- They are useful when you have to write several lines of code to perform a single action, such as importing data from a file or updating a database entry. They are important as they help others understand the purpose and functionality of a given code block.
    - Indent block comments to the same level as the code they describe.
    - Start each line with a # followed by a single space.
    - Separate paragraphs by a line containing a single #.
- Ex.
def quadratic(a, b, c, x):<br>
    \# Calculate the solution to a quadratic equation using the quadratic formula.<br>
    \# There are always two solutions to a quadratic equation, x_1 and x_2.<br>
    x_1 = (- b+(b**2-4*a*c)**(1/2)) / (2*a)<br>
    x_2 = (- b-(b**2-4*a*c)**(1/2)) / (2*a)<br>
    return x_1, x_2

- Inline Comments
- Inline comments explain a single statement in a piece of code.
        - Use inline comments sparingly.
        - Write inline comments on the same line as the statement they refer to.
        - Separate inline comments by two or more spaces from the statement.
        - Start inline comments with a # and a single space, like block comments.
        - Don’t use them to explain the obvious.
- Ex. 
x = 5  # This is an inline comment

- Documentation Strings
- Documentation strings, or docstrings, are strings enclosed in double (""") or single (''') quotation marks that appear on the first line of any function, class, method, or module. You can use them to explain and document a specific block of code. 
        - Surround docstrings with three double quotes on either side, as in """This is a docstring""".
        - Write them for all public modules, functions, classes, and methods.
        - Put the """ that ends a multiline docstring on a line by itself:
- Ex. Google Style Doc String<br>
<pre>
    """Gets and prints the spreadsheet's header columns

    Args:
        file_loc (str): The file location of the spreadsheet
        print_cols (bool): A flag used to print the columns to the console
            (default is False)

    Returns:
        list: a list of strings representing the header columns
    """<br>
    def fetch_smalltable_rows(
        table_handle: smalltable.Table,
        keys: Sequence[bytes | str],
        require_all_keys: bool = False,
    ) -> Mapping[bytes, tuple[str, ...]]:<br>
        """Fetches rows from a Smalltable.
        Retrieves rows pertaining to the given keys from the Table instance
        represented by table_handle.  String keys will be UTF-8 encoded.<br>
        Args:<br>
        table_handle:<br>
            An open smalltable.Table instance.
        keys:<br>
            A sequence of strings representing the key of each table row to
            fetch.  String keys will be UTF-8 encoded.
        require_all_keys:<br>
            If True only rows with values set for all keys will be returned.
        Returns:<br>
        A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a tuple of strings. For
        example:<br>
        {b'Serak': ('Rigel VII', 'Preparer'),
        b'Zim': ('Irk', 'Invader'),
        b'Lrrr': ('Omicron Persei 8', 'Emperor')}<br>
        Returned keys are always bytes.  If a key from the keys argument is
        missing from the dictionary, then that row was not found in the
        table (and require_all_keys must have been False).<br>
        Raises:
        IOError: An error occurred accessing the smalltable.
        """

    class SampleClass:<br>
        """Summary of class here.<br>
        Longer class information...<br>
        Longer class information...<br>
        Attributes:<br>
            likes_spam: A boolean indicating if we like SPAM or not.<br>
            eggs: An integer count of the eggs we have laid.<br>
        """
        def __init__(self, likes_spam: bool = False):<br>
            """Initializes the instance based on spam preference.<br>
            Args:<br>
            likes_spam: Defines if instance exhibits this preference.<br>
            """
            self.likes_spam = likes_spam<br>
            self.eggs = 0<br>
        def public_method(self):<br>
            """Performs operation blah."""
</pre><br>
- Whitespace in Expressions and Statements
- Whitespace Around Binary Operators
        - Assignment operators (=, +=, -=, and so forth)
        - Comparisons (==, !=, >, <. >=, <=) and (is, is not, in, not in)
        - Booleans (and, not, or)
- Note: When = is used to assign a default value to a function argument, do not surround it with spaces.
- Ex.<br>
Recommended <br>
def function(default_parameter=5):
    # ...
- it is better to only add whitespace around the operators with the lowest priority, especially when performing mathematical manipulation. Here are a couple examples:
<pre>
Ex.
Recommended <br>
y = x**2 + 5 <br>
z = (x+y) * (x-y) <br>

Recommended <br>
if x>5 and x%2==0: <br>
    print('x is larger than 5 and divisible by 2!') <br>
</pre>
- In slices, colons act as a binary operators.
<pre>
- Ex. 
list[3:4]
# Treat the colon as the operator with lowest priority
list[x+1 : x+2]
# In an extended slice, both colons must be
# surrounded by the same amount of whitespace
list[3:4:5]
list[x+1 : x+2 : x+3]
# The space is omitted if a slice parameter is omitted
list[x+1 : x+2 :]
</pre>
- When to Avoid Adding Whitespace
- The most important place to avoid adding whitespace is at the end of a line. This is known as trailing whitespace. 
- Before a comma, semicolon, or colon:
<pre>
- Ex.
x = 5
y = 6
# Recommended
print(x, y)
# Not recommended
print(x , y)
</pre>
- Immediately inside parentheses, brackets, or braces:
<pre>
- Ex. 
# Recommended
my_list = [1, 2, 3]
# Not recommended
my_list = [ 1, 2, 3, ]
</pre>
- Before the open parenthesis that starts the argument list of a function call:
<pre>
Ex.
def double(x):
    return x * 2
# Recommended
double(3)
# Not recommended
double (3)
</pre>
- Before the open bracket that starts an index or slice:
<pre>
- Ex.
# Recommended
list[3]
# Not recommended
list [3]
</pre>
- Between a trailing comma and a closing parenthesis:
<pre>
- Ex.
# Recommended
tuple = (1,)
# Not recommended
tuple = (1, )
</pre>
- To align assignment operators:
<pre>
- Ex. 
# Recommended
var1 = 5
var2 = 6
some_long_var = 7

# Not recommended
var1          = 5
var2          = 6
some_long_var = 7
</pre>
- There are other cases where PEP 8 discourages adding extra whitespace, such as immediately inside brackets, as well as before commas and colons. You should also never add extra whitespace in order to align operators.

- Programming Recommendations
- Don’t compare Boolean values to True or False using the equivalence operator (==).
<pre>
- Ex.
# Not recommended
my_bool = 6 > 5
if my_bool == True:
    return '6 is bigger than 5'
# Recommended
if my_bool:
    return '6 is bigger than 5'
</pre>
- Use the fact that empty sequences are falsy in if statements. 
- Ex. in Python any empty list, string, or tuple is falsy. 
<pre>
# Not recommended
my_list = []
if not len(my_list):
    print('List is empty!')
# Recommended
my_list = []
if not my_list:
    print('List is empty!')
</pre>
- Use is not rather than not ... is in if statements.
<pre>
- Ex.
# Recommended
if x is not None:
    return 'x exists!'
# Not recommended
if not x is None:
    return 'x exists!'
</pre>
- Don’t use if x: when you mean if x is not None
- Ex.A common mistake when checking if arg with default value None has been given a different value is to use the following:
<pre>
# Not Recommended
if arg:
    # Do something with arg...
# Recommended
if arg is not None:
    # Do something with arg...
</pre>
- You could have set arg = []. As we saw above, empty lists are evaluated as falsy in Python. So, even though the argument arg has been assigned, the condition is not met, and so the code in the body of the if statement will not be executed.

- Use .startswith() and .endswith() instead of slicing. 
<pre>
# Not recommended
if word[:3] == 'cat':
    print('The word starts with "cat"')
# Recommended
if word.startswith('cat'):
    print('The word starts with "cat"')
</pre>
- When to Ignore PEP 8 -> NEVER
- Exceptions to rule below:
        - If complying with PEP 8 would break compatibility with existing software
        - If code surrounding what you’re working on is inconsistent with PEP 8
        - If code needs to remain compatible with older versions of Python

- Tips and Tricks to Help Ensure Your Code Follows PEP 8
- Linters
- Linters are programs that analyze code and flag errors. They provide suggestions on how to fix the error. Linters are particularly useful when installed as extensions to your text editor, as they flag errors and stylistic problems while you write.
- pycodestyle is a tool to check your Python code against some of the style conventions in PEP 8.<br>
<pre>
    pip install pycodestyle
    pycodestyle code.py
</pre>
- flake8 is a tool that combines a debugger, pyflakes, with pycodestyle<br>
<pre>
    pip install flake8
    flake8 code.py
</pre>
- Autoformatters
- Autoformatters are programs that refactor your code to conform with PEP 8 automatically. 
- Once such program is black, which autoformats code following most of the rules in PEP 8.
<pre>
    pip install black
    black --line-length=79 code.py
</pre>
- Two other autoformatters, autopep8 and yapf, perform actions that are similar to what black does.


