- Absolute vs Relative Imports 
    - https://realpython.com/absolute-vs-relative-python-imports/
- A Python module is a file that has a .py extension
- a Python package is any folder that has modules inside it (or, in Python 2, a folder that contains an __init__.py file).
- The first thing Python will do is look up the import name in sys.modules.
- Python will proceed to search through a list of built-in modules. 
- Python then searches for it in a list of directories defined by sys.path. This list usually includes the current directory, which is searched first.
- When Python finds the module, it binds it to a name in the local scope. This means that packagename is now defined and can be used in the current file without throwing a NameError. If the name is never found, you’ll get a ModuleNotFoundError.
- importing a package essentially imports the package’s __init__.py file as a module

- Absolute Imports
- absolute import specifies the resource to be imported using its full path from the project’s root folder
- Ex.
└── project
    ├── package1
    │   ├── module1.py
    │   └── module2.py
    └── package2
        ├── __init__.py
        ├── module3.py
        ├── module4.py
        └── subpackage1
            └── module5.py
package1/module2.py contains a function, function1.
package2/__init__.py contains a class, class1.
package2/subpackage1/module5.py contains a function, function2.

Valid examples ->
from package1 import module1
from package1.module2 import function1
from package2 import class1
from package2.subpackage1.module5 import function2

- Relative Imports
- A relative import specifies the resource to be imported relative to the current location—that is, the location where the import statement is.

from .some_module import some_class
from ..some_package import some_function
from . import some_class

- A single dot means that the module or package referenced is in the same directory as the current location. Two dots mean that it is in the parent directory of the current location—that is, the directory above. 

Ex.
└── project
    ├── package1
    │   ├── module1.py
    │   └── module2.py
    └── package2
        ├── __init__.py
        ├── module3.py
        ├── module4.py
        └── subpackage1
            └── module5.py
package1/module2.py contains a function, function1.
package2/__init__.py contains a class, class1.
package2/subpackage1/module5.py contains a function, function2.

from .module2 import function1  #in file module1.py
from . import class1   #module3.py
from .subpackage1.module5 import function2  #module3.py