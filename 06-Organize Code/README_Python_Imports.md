- Python Import System
    - https://realpython.com/python-import/#the-python-import-system
- import keyword to make code in one module available in another
- Modules
    -  a module usually corresponds to one .py file containing Python code
- namespace
    - keeps all the attributes of the module together. 
    - dir(math)   -> list contents of namespace 
    - Ex. from math import pi -> pi works and math.pi failes as pi in global workspace and not within math namespace
    - Directories without an __init__.py file are still treated as packages by Python. However, these won’t be regular packages, but something called namespace packages.
- package
    - further organize your modules
    - To create a Python package yourself, you create a directory and a file named __init__.py inside it. The __init__.py file contains the contents of the package when it’s treated as a module. It can be left empty.
    - you can use __init__.py to include any or all submodules and subpackages if you want.
    - Importing a module both loads the contents and creates a namespace containing the contents.
    - Module namespace is implemented as a Python dictionary and is available at the .__dict__ attribute
    - Python’s global namespace is also a dictionary. You can access it through globals().
    - Common to import subpackages and submodules in an __init__.py file to make them more readily available to your users. 
- Ex. Code :
# world/africa/__init__.py  (Empty file)

# world/africa/zimbabwe.py
print("Shona: Mhoroyi vhanu vese")
print("Ndebele: Sabona mhlaba")

# world/europe/__init__.py
from . import greece
from . import norway

# world/europe/greece.py
print("Greek: Γειά σας Κόσμε")

# world/europe/norway.py
print("Norwegian: Hei verden")

# world/europe/spain.py
print("Castellano: Hola mundo")

# world/__init__.py
from . import africa    # dot refers to current package and statement is example of relative import
                        # alternate -> from world import africa

- Absolute and Relative Imports
    - Relative -> from . import africa
    - Absolute -> from world import africa

- Python’s Import Path
    - Python looks for modules and packages in its import path. 
    - inspect Python’s import path by printing sys.path
    - Look for packages in following order -> 
        1. The directory of the current script (or the current directory if there’s no script, such as when Python is running interactively)
        2. The contents of the PYTHONPATH environment variable
        3. Other, installation-dependent directories

- Example: Structure Your Imports
    - structure/
        │
        ├── files.py
        └── structure.py

    - structure/
        │
        ├── structure/
        │   ├── files.py
        │   └── structure.py
        │
        └── cli.py

        cli.py ->
        from structure.structure import main

        if __name__ == "__main__":
            main()

        - main() isn’t run when structure is imported because of the if test on line 25 in structure.py. That means you need to run main() explicitly.

        - python cli.py structure -> fails - no module files, by starting the app with cli.py, you’ve changed the location of the current script, which in turn changes the import path -> solution is change python import path -> sys.path.insert(0, str(pathlib.Path(__file__).parent))

- Create and Install a Local Package
    - When you install a package from PyPI, that package is available to all scripts in your environment, same for packages installed from local computer
    - setup.cfg for local packages
        # setup.cfg
        [metadata]
        name = local_structure
        version = 0.1.0

        [options]
        packages = structure
    - Install using python -m pip install -e .
    -   # Local imports - works everywhere now 
        from structure import files
    - script is meant to be run and library is meant to be imported

- Namespace Packages
    - A namespace package is created automatically if you have a directory containing a .py file but no __init__.py
    - Ex.
    third_party/
        │
        └── serializers/
            ├── json.py
            └── xml.py
    - now create a new serializer called -> YamlSerializer to serializers package without touching third party package 
    - add following directory on local system ->
    local/
        │
        └── serializers/
            └── yaml.py
    - now run this command as well -> from serializers.yaml import YamlSerializer
    - make sure that your local library is available like a normal package. you can do this either by running Python from the proper directory or by using pip to install the local library as well.
    - also mess with sys path -> Put the third_party and local directories inside the same folder
    - Ex.
    import sys
    sys.path.extend(["third_party", "local"])
    from serializers import json, xml, yaml
    json
    <module 'serializers.json' from 'third_party/serializers/json.py'>
    yaml
    <module 'serializers.yaml' from 'local/serializers/yaml.py'>

    - Organize imports into groups: first standard library imports, then third-party imports, and finally local application or library imports. Use isort and reorder-python-imports. 

- Resource Imports
    - you’ll have code that depends on data files or other resources
    - importlib.resources gives access to resources within packages. In this context, a resource is any file located within an importable package.
    - your resource files must be available inside a regular package ie directory containing __init__.py file
    - Ex. 
    books/
        │
        ├── __init__.py
        ├── alice_in_wonderland.png
        └── alice_in_wonderland.txt

    from importlib import resources
    with resources.open_text("books", "alice_in_wonderland.txt") as fid:
        alice = fid.readlines()
    print("".join(alice[:7]))

    - Having a __main__.py file allows your package to be executed with python -m <packagename>

- Dynamic Imports
    - you can shadow any Python object that is built into the interpreter.
    - Ex. print = lambda *args, **kwargs: None -> print("Sahil") -> doesnt print anything 
    eq code -> def print(*args, **kwargs): pass
- Using importlib
    - Ex. 
    import importlib
    module_name = input("Name of module? ")
    module = importlib.import_module(module_name)
    print(module.__doc__)
    -> import_module() returns a module object that you can bind to any variable
- Example: Factory Method With Namespace Packages

- The Python Import System
- Import Internals - At a high level, three things happen when you import a module (or package):
    - Searched for
    - Loaded
    - Bound to a namespace
- Ex. from math import pi as PI
    PI -? 3.141592653589793
    OR 
    import importlib
    _tmp = importlib.import_module("math")
    PI = _tmp.pi
    del _tmp
    PI -> 3.14...
- even when you import only one attribute from a module, the whole module is loaded and executed. -> kept in module cache 
Ex. sys.modules["math"].cos(pi)
- if Python finds a module in the module cache, then it won’t bother searching import path for module
- Example: Singletons as Modules -> singleton is a class with at most one instance.

- Reloading Modules 
        import number
- Ex.   import importlib
        importlib.reload(number)  # number is a module object 

- Finders and Loaders
- local file with same name replace import from file but not from built in module.
Ex - replace math but not time 
- sys.builtin_module_names > provides built in module names 
- There are several steps involved when importing a module:

    1. Python checks if the module is available in the module cache. If sys.modules contains the name of the module, then the module is already available, and the import process ends.
    2. Python starts looking for the module using several finders. A finder will search for the module using a given strategy. The default finders can import built-in modules, frozen modules, and modules on the import path.
    3. Python loads the module using a loader. Which loader Python uses is determined by the finder that located the module and is specified in something called a module spec.
- sys.meta_path controls which finders are called during the import process
- sys.modules -> module cache
- Ex. finder 
    # debug_importer.py
    import sys
    class DebugFinder:
        @classmethod
        def find_spec(cls, name, path, target=None):
            print(f"Importing {name!r}")
            return None
    sys.meta_path.insert(0, DebugFinder)

    # ban_importer.py
    import sys
    BANNED_MODULES = {"re"}
    class BanFinder:
        @classmethod
        def find_spec(cls, name, path, target=None):
            if name in BANNED_MODULES:
                raise ModuleNotFoundError(f"{name!r} is banned")
    sys.meta_path.insert(0, BanFinder)

- Handle Packages Across Python Versions
- Ex. importlib after 3.7 and importlib_resources before 3.7
try:
    from importlib import resources
except ImportError:
    import importlib_resources as resources
alternate -> 
import sys
if sys.version_info >= (3, 7):
    from importlib import resources
else:
    import importlib_resources as resources

- Handle Missing Packages: Use an Alternative
- Ex.
try:
    import ujson as json
except ImportError:
    import json

- Handle Missing Packages: Use a Mock Instead
- Ex.
# optional_color.py

try:
    from colorama import init, Back, Cursor, Fore, Style
except ImportError:
    from collections import UserString

    class ColoramaMock(UserString):
        def __call__(self, *args, **kwargs):
            return self
        def __getattr__(self, key):
            return self

    init = ColoramaMock("")
    Back = Cursor = Fore = Style = ColoramaMock("")

- Import Scripts as Modules
- scripts typically do something, whereas libraries provide functionality.  
- the difference is in how the file is meant to be used: 
    - should it be executed with python file.py or 
    - imported with import file inside another script
Ex. json library 
script -> python -m json.tool colors.json --sort-keys
- the value of the special __name__ module variable is set at runtime based on whether the module is imported or run as a script
Ex.
# feel_young.py

def make_young(text):
    words = [replace_by_age(w) for w in text.split()]
    return " ".join(words)

def replace_by_age(word, new_age=24, age_range=(25, 120)):
    if word.isdigit() and int(word) in range(*age_range):
        return str(new_age)
    return word

if __name__ == "__main__": # allows to run as script with python feel_young.py else import feel_young
    text = input("Tell me something: ")
    print(make_young(text))

- Run Python Scripts From ZIP Files
- If you give the Python interpreter a ZIP file, then it’ll look for a file named __main__.py inside the ZIP archive, extract it, and run it. 
- Ex. 
package app as zip file -> python -m zipapp population_quiz -m population_quiz:main -p "/usr/bin/env python"
it creates an entry point and packages your application.The __main__ file uses -m for how app 
should be started. __main__() will include ->
import population_quiz
population_quiz.main()

Files loaded to ZIP archive named population_quiz.pyz. Run file using -> ./population_quiz.pyz 

population_quiz/
│
├── data/
│   ├── __init__.py
│   └── WPP2019_TotalPopulationBySex.csv
│
└── population_quiz.py

- Handle Cyclical Imports
- A cyclical import happens when you have two or more modules importing each other
- The reason it doesn’t end up in endless recursion is our old friend the module cache
- The issues associated with recursive imports start popping up when you actually use the other module at import time instead of just defining functions that will use the other module later.
- this isn’t a problem so long as your modules define only attributes, functions, classes, and so on. The second tip is to keep your modules free of side effects at import time.
- do your imports locally inside functions.

- Profile Imports
- Ex. Measures and prints how much time each module takes to import
python -X importtime -c "import datetime"






