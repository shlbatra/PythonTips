- Source Article
    - https://realpython.com/python-modules-packages/
- Modular programming refers to the process of breaking a large, unwieldy programming task into separate, smaller, more manageable subtasks or modules.
- Functions, modules and packages are all constructs in Python that promote code modularization.
- Python Modules
    - A module can be written in Python itself.
    - A module can be written in C and loaded dynamically at run-time, like the re (regular expression) module.
    - A built-in module is intrinsically contained in the interpreter, like the itertools module.
- The Module Search Path
- import <modulename>
- When the interpreter executes the above import statement, it searches for mod.py in a list of directories assembled from the following sources:
1. The directory from which the input script was run or the current directory if the interpreter is being run interactively
2. The list of directories contained in the PYTHONPATH environment variable, if it is set. (The format for PYTHONPATH is OS-dependent but should mimic the PATH environment variable.)
3. An installation-dependent list of directories configured at the time Python is installed
- Check from : import sys;  sys.path
- Add folder path -> sys.path.append(r'C:\Users\john');   
- mod.__file__  -> this provides location of where module was found 

- import <module_name>
- The statement import <module_name> only places <module_name> in the caller’s symbol table. The objects that are defined in the module remain in the module’s private symbol table.
- From the caller, objects in the module are only accessible when prefixed with <module_name> via dot notation.  a module creates a separate namespace
- Ex. import mod
mod.s      mod.foo()

- from <module_name> import <name(s)>
- It allows individual objects from the module to be imported directly into the caller’s symbol table
- from mod import s, fo       You can call ->   s      fo()
- from <module_name> import *
- This will place the names of all objects from <module_name> into the local symbol table, with the exception of any that begin with the underscore (_) character.

- from <module_name> import <name> as <alt_name>
- It is also possible to import individual objects but enter them into the local symbol table with alternate names
- Ex. from mod import s as string, a as alist

- import <module_name> as <alt_name>
- You can also import an entire module under an alternate name
- Ex. import mod as my_module   -> my_module.a   , my_module.fo()

- try statement with an except ImportError clause can be used to guard against unsuccessful import attempts
- Ex. 
>>> try:
...     # Non-existent module
...     import baz
... except ImportError:
...     print('Module not found')

>>> try:
...     # Existing module, but non-existent object
...     from mod import baz
... except ImportError:
...     print('Object not found in module')

- The dir() Function
- The built-in function dir() returns a list of defined names in a namespace. Without arguments, it produces an alphabetically sorted list of names in the current local symbol table
- Ex.
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
'__package__', '__spec__']

>>> import mod
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
'__package__', '__spec__', 'mod']
- When given an argument that is the name of a module, dir() lists the names defined in the module:
- Ex. 
>>> import mod
>>> dir(mod)
['Foo', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
'__name__', '__package__', '__spec__', 'a', 'foo', 's']

- Executing a Module as a Script
- Ex. mod.py
s = "If Comrade Napoleon says it, it must be right."
a = [100, 200, 300]

def foo(arg):
    print(f'arg = {arg}')

class Foo:
    pass

print(s)
print(a)
foo('quux')
x = Foo()
print(x)

- python mod.py     OR import mod    both generate output below ->
If Comrade Napoleon says it, it must be right.
[100, 200, 300]
arg = quux
<__main__.Foo object at 0x02F101D0>

- When a .py file is imported as a module, Python sets the special dunder variable __name__ to the name of the module. However, if a file is run as a standalone script, __name__ is (creatively) set to the string '__main__'. Using this fact, you can discern which is the case at run-time and alter behavior accordingly
- Ex. updated mod.py below :
s = "If Comrade Napoleon says it, it must be right."
a = [100, 200, 300]

def foo(arg):
    print(f'arg = {arg}')

class Foo:
    pass

if (__name__ == '__main__'):
    print('Executing as standalone script')
    print(s)
    print(a)
    foo('quux')
    x = Foo()
    print(x)

- Modules are often designed with the capability to run as a standalone script for purposes of testing the functionality that is contained within the module. This is referred to as unit testing. 
- Ex. fact.py
def fact(n):
    return 1 if n == 1 else n * fact(n-1)

if (__name__ == '__main__'):
    import sys
    if len(sys.argv) > 1:
        print(fact(int(sys.argv[1])))

Run as below ->
1. module
    from fact import fact
    fact(6)
2. standalone
    python fact.py 6

- Reloading a Module
- For reasons of efficiency, a module is only loaded once per interpreter session.So executable statements are run only once when the module is imported first time. 
Ex. mod.py
a = [100, 200, 300]
print('a =', a)

>>> import mod
a = [100, 200, 300]
>>> import mod

- change code then need to reload module again 
>>> import importlib
>>> importlib.reload(mod)

- Python Packages
- Packages allow for a hierarchical structuring of the module namespace using dot notation. In the same way that modules help avoid collisions between global variable names, packages help avoid collisions between module names.
- Ex/.
        pkg
            mod1.py
            mod2.py

import pkg.mod1, pkg.mod2
from pkg.mod1 import foo
from pkg.mod2 import Bar as Qux
from pkg import mod1     -> mod1.foo()
from pkg import mod2 as quux        -> quux.bar()

import pkg - not useful as it does not place any of the modules in pkg into the local namespace.
pkg.mod1   -> AttributeError: module 'pkg' has no attribute 'mod1'

- Package Initialization
- If a file named __init__.py is present in a package directory, it is invoked when the package or a module in the package is imported. This can be used for execution of package initialization code, such as initialization of package-level data.
- Ex.
__init__.py

print(f'Invoking __init__.py for {__name__}')
A = ['quux', 'corge', 'grault']

        pkg
            mod1.py
            mod2.py
            __init__.py 

-> import pkg     -> pkg.A works 

- __init__.py can also be used to effect automatic importing of modules from a package.
- Ex. 
__init__.py

print(f'Invoking __init__.py for {__name__}')
import pkg.mod1, pkg.mod2
- when you execute import pkg, modules mod1 and mod2 are imported automatically
>>> import pkg
Invoking __init__.py for pkg
>>> pkg.mod1.foo()
[mod1] foo()
>>> pkg.mod2.bar()
[mod2] bar()

- Starting with Python 3.3, Implicit Namespace Packages were introduced. These allow for the creation of a package without any __init__.py file. Of course, it can still be present if package initialization is needed. But it is no longer required.

- Importing * From a Package
- You have already seen that when import * is used for a module, all objects from the module are imported into the local symbol table, except those whose names begin with an underscore
- Ex. 
            pkg
                mod1.py
                mod2.py
                mod3.py
                mod4.py 

- from <package_name> import *
- dir()   -> Stays the same because if the __init__.py file in the package directory contains a list named __all__, it is taken to be a list of modules that should be imported when the statement from <package_name> import * is encountered.
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
'__package__', '__spec__']

- Ex. if create __init__.py file ->
pkg/__init__.py

__all__ = [
        'mod1',
        'mod2',
        'mod3',
        'mod4'
        ]
>>> from pkg import *
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
'__package__', '__spec__', 'mod1', 'mod2', 'mod3', 'mod4']

- By the way, __all__ can be defined in a module as well and serves the same purpose: to control what is imported with import *. For example, modify mod1.py as follows:

pkg/mod1.py

__all__ = ['foo']

def foo():
    print('[mod1] foo()')

class Foo:
    pass

from pkg.mod1 import *   -> foo() works and Foo fails with name 'Foo' bit defined

- For a package, when __all__ is not defined, import * does not import anything.
- For a module, when __all__ is not defined, import * imports everything (except—you guessed it—names starting with an underscore).

- Subpackages
- Packages can contain nested subpackages to arbitrary depth.
- Ex.
        pkg 
            sub_pkg1
                mod1.py
                mod2.py
            sub_pkg2
                mod3.py
                mod4.py
- additional dot notation is used to separate package name from subpackage name:
- imports below 
import pkg.sub_pkg1.mod1    -> pkg.sub_pkg1.mod1.foo()
from pkg.sub_pkg1 import mod2  -> mod2.bar()
from pkg.sub_pkg2.mod3 import baz    -> baz()

- In addition, a module in one subpackage can reference objects in a sibling subpackage
- absolute import 
    - pkg/sub__pkg2/mod3.py
        - from pkg.sub_pkg1.mod1 import foo

- relative import 
    - pkg/sub__pkg2/mod3.py
        - from ..sub_pkg1.mod1 import foo








































































