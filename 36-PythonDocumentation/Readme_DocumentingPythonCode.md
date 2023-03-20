- Source Article 
    - https://realpython.com/documenting-python-code/#docstring-formats
- commenting is describing your code to/for developers. The intended main audience is the maintainers and developers of the Python code.Code tells you how; Comments tell you why
- 4 Rules
    - Keep comments as close to the code being described as possible. Comments that aren’t near their describing code are frustrating to the reader and easily missed when updates are made.
    - Don’t use complex formatting (such as tables or ASCII figures). Complex formatting leads to distracting content and can be difficult to maintain over time.
    - Don’t include redundant information. Assume the reader of the code has a basic understanding of programming principles and language syntax.
    - Design your code to comment itself. The easiest way to understand code is by reading it. When you design your code using clear, easy-to-understand concepts, the reader will be able to quickly conceptualize your intent. Use Type Hinting ->
Ex.
def hello_name(name: str) -> str:
    return(f"Hello {name}")

- Commenting your code serves multiple purposes, 
    - Planning and Reviewing
    - Code Description
    - Algorithmic Description
    - Tagging
- Documenting code is describing its use and functionality to your users. While it may be helpful in the development process, the main intended audience is the users. 

- Documenting Your Python Code Base Using Docstrings
- Since everything in Python is an object, you can examine the directory of the object using the dir() command
Ex. 
>>> dir(str)
['__add__', ..., '__doc__', ..., 'zfill'] # Truncated for readability
print(str.__doc__) -> doc strings stored here

Ex.
def say_hello(name):
    print(f"Hello {name}, is it me you're looking for?")

say_hello.__doc__ = "A simple function that says hello... Richie style"

Ex.
def say_hello(name):
    """A simple function that says hello... Richie style"""
    print(f"Hello {name}, is it me you're looking for?")

- Class Docstrings
    - A brief summary of its purpose and behavior
    - Any public methods, along with a brief description
    - Any class properties (attributes)
    - Anything related to the interface for subclassers, if the class is intended to be subclassed
- Class Methods
    - A brief description of what the method is and what it’s used for
    - Any arguments (both required and optional) that are passed including keyword arguments
    - Label any arguments that are considered optional or have a default value
    - Any side effects that occur when executing the method
    - Any exceptions that are raised
    - Any restrictions on when the method can be called

- Package and Module Docstrings
- Package docstrings should be placed at the top of the package’s __init__.py file. This docstring should list the modules and sub-packages that are exported by the package
- Module docstrings are similar to class docstrings. Instead of classes and class methods being documented, it’s now the module and any functions found within. Module docstrings are placed at the top of the file even before any imports. Module docstrings should include the following:
    - A brief description of the module and its purpose
    - A list of any classes, exception, functions, and any other objects exported by the module
- Script Docstrings
Scripts are considered to be single file executables run from the console. Docstrings for scripts are placed at the top of the file and should be documented well enough for users to be able to have a sufficient understanding of how to use the script. It should be usable for its “usage” message, when the user incorrectly passes in a parameter or uses the -h option.
Ex.argparse
def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'input_file',
        type=str,
        help="The spreadsheet file to pring the columns of"
    )
    args = parser.parse_args()
    get_spreadsheet_cols(args.input_file, print_cols=True)
if __name__ == "__main__":
    main()

- Google Style Example:
"""Gets and prints the spreadsheet's header columns

Args:
    file_loc (str): The file location of the spreadsheet
    print_cols (bool): A flag used to print the columns to the console
        (default is False)

Returns:
    list: a list of strings representing the header columns
"""

- Documenting Your Python Projects
- Ex.
    project_root/
    │
    ├── project/  # Project source code
    ├── docs/
    ├── README
    ├── HOW_TO_CONTRIBUTE
    ├── CODE_OF_CONDUCT
    ├── examples.py
- Private Projects
    - Readme: A brief summary of the project and its purpose. Include any special requirements for installation or operating the project.
    - examples.py: A Python script file that gives simple examples of how to use the project.
- Shared Projects
Shared projects are projects in which you collaborate with a few other people in the development and/or use of the project. The “customer” or user of the project continues to be yourself and those limited few that use the project as well.
    - Readme: A brief summary of the project and its purpose. Include any special requirements for installing or operating the project. Additionally, add any major changes since the previous version.
    - examples.py: A Python script file that gives simple examples of how to use the projects.
    - How to Contribute: This should include how new contributors to the project can start contributing.
- Public and Open Source Projects
- Public and Open Source projects are projects that are intended to be shared with a large group of users and can involve large development teams.
    - Readme
    - How to Contribute
    - Code of Conduct
    - License
    - docs
        - Tutorials
        - How To Guide
        - References
        - Explainations