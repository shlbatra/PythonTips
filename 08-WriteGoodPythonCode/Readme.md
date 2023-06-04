- PEP8 -> Style guide for Python
- 1. Any line cannot exceed 80 chars -> use auto formatter to fix these issues. 
   - Ex. pip install black
   - go to settings, search python format provider -> select black
   - search format -> check format on save
- 2. Indentation is spaces -> 4
    - view -> command template -> indent using spaces -> 4
- 3. follow consistent code -> single quotes around strings everywhere
- 4. Naming convention 
    - variable (lowercase_lowercase) - snake case. ex. hello_world
    - constants (uppercase_uppercase) - snake case. ex. BG_COLOR
    - modules / python file names (lower case) - snake case. prefer one word
    - functions (lower_case_lowercase) - snake case ex. def hello_world
    - class (upper case first word, upper case second word). Pascal case. ex. class BaseClass
    - exception (pascal case as its a class). Ex. class XException
- 5. Parameter naming convention for methods in class
    class Test:
        def test(self):   #first parameter in instance method is self
            pass

        @classmethod
        def cls_method(cls):   #first paramter in class method is cls
            pass
- 6. Function and Class Spacing -> 
 -- top level space by 2 lines
 -- methods inside class space by 1 line
    class Test:
        pass

    
    class Foo:
        def __init__(self):
            pass

        def foo(self):
            pass


def bar():
    pass

- 7. imports go at top of file and next line from each other. 
     If import multiple things from module then put on same line 
     Not use wild card import -> from os import *   #imports everything so avoid it
     module doc string can be on top and then imports 
    Ex. 

    """
    module doc string
    """

    import os
    import sys
    from os import path, stat

    GLOBALLY DEFINED VARIABLES AND CONSTANTS

    Top Level Functions 

    Classes

- 8 Strings -> Single or Double Quotes (Both are same and always stay consistent)
''
"" 

'"' -> put double quot inside single
"'" -> put single quot inside double 
'\'' -> can use single quot inside single quot with escape character

For doc strings, use double quot 
"""
"""

- 9 Incorrect use of whitespaces
# Correct :
spam(ham[1], {eggs: 2})
# Incorrect :
spam( ham[ 1 ], { eggs: 2 })

# Correct :
foo = (0,) # no whitespace between trailing comma and paranthesis
# Incorrect :
foo = (0, )

# Correct :
spam(1) # no whitespace between fn call and paranthesis in fn call
# Incorrect :
spam (1)

# Correct :
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
# Incorrect :
i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)

# Correct :
def complex(real, imag=0.0):  #whitespaces for args not reqd. 
    return magic(r=real, i=imag)

# Incorrect :
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)

- 10. Inline Comments -> comment same line as expression. Need 2 spaces after line and start of comment and start with upper case

# Correct :
COLOR = (0, 255, 0)  #  This is correct

# Incorrect :
COLOR = (0, 255, 0)  #this is correct

- 11. Check value is none 

x = None 
# Incorrect :
if x:     # trigger both for x = None or x = False/0/"" 
    pass 
# Correct :
if x is None:   # not use ==
    pass

# Correct 
if foo is not None:  #check value is not something, or if foo is not "x"
    pass

# Incorrect
if not foo is None:   # basically does this -> if not (foo is None)
    pass

- 12. Try and Except

# Correct 
try:
    import platform_specific_module
except ImportError:              # Always except specific exception 
    platform_specific_module = None
except ImportError2:              # add another except specific exception 
    platform_specific_module = None

# Incorrect
try:
    import platform_specific_module
except:
    platform_specific_module = None

- 13. String Prefix and Suffix - Check string starts with or ends with something.

# Correct
if foo.startswith("bar"):       # foo.endswith("bar")
    pass 

# Incorrect
if foo[:3] == "bar":
    pass


