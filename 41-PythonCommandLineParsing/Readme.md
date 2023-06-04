- Build Command-Line Interfaces With Python's argparse
    - https://realpython.com/command-line-interfaces-python-argparse/
- Command-Line Example
- python [file].py [command] [options] NAME
<pre>
Ex. 
python [file].py hello Kyle     ->   Hello, Kyle!
python [file].py goodbye Kyle    ->    Goodbye, Kyle!
</pre>
- Usage w/ Options (Flags)
<pre>
Ex.
python [file].py hello --greeting=Wazzup Kyle   ->    Whazzup, Kyle!
python [file].py hello --greeting=Wazzup --caps Kyle      ->    WAZZUP, KYLE!
</pre>
- Features :
    - Commands (hello, goodbye)
    - Arguments (name)
    - Options/Flags (--greeting=<str>, --caps)
- The information exchange has flowed among humans, computer software, and hardware components. The shared boundary between any two of these elements is generically known as an interface. An interface is a special part of a given piece of software that allows interaction between components of a computer system.When it comes to human and software interaction, this vital component is known as the user interface.
- Command-line interfaces allow you to interact with an application or program through your operating system command line, terminal, or console. The command has a full-featured command-line interface with a useful set of options that you can use to customize the command’s behavior.
- Commands, Arguments, Options, Parameters, and Subcommands
    - Command: A program or routine that runs at the command line or terminal window. You’ll typically identify a command with the name of the underlying program or routine.
    - Argument: A required or optional piece of information that a command uses to perform its intended action. Commands typically accept one or many arguments, which you can provide as a whitespace-separated or comma-separated list on your command line.
    - Option, also known as flag or switch: An optional argument that modifies a command’s behavior. Options are passed to commands using a specific name, like -l in the previous example.
    - Parameter: An argument that an option uses to perform its intended operation or action.
    - Subcommand: A predefined name that can be passed to an application to run a specific action.
<pre>
Ex. ls -l sample/
ls -> command, -l -> option, sample -> parameter
pip install -r requirements.txt
pip -> command install -> subcommand, -r -> option, requirements.txt -> parameter
</pre>
- Argparse
- sys.argv -> This attribute automatically stores the arguments that you pass to a given program at the command line.
<pre>
Ex.
# ls_argv.py

import sys
from pathlib import Path

if (args_count := len(sys.argv)) > 2:
    print(f"One argument expected, got {args_count - 1}")
    raise SystemExit(2)
elif args_count < 2:
    print("You must specify the target directory")
    raise SystemExit(2)
target_dir = Path(sys.argv[1])
if not target_dir.is_dir():
    print("The target directory doesn't exist")
    raise SystemExit(1)
for entry in target_dir.iterdir():
    print(entry.name)
</pre>
<pre>
$ python ls_argv.py sample/
hello.txt
lorem.md
realpython.md
</pre>
- Creating a CLI With argparse
    - Parse command-line arguments and options
    - Take a variable number of parameters in a single option
    - Provide subcommands in your CLIs
1. Import argparse.
2. Create an argument parser by instantiating ArgumentParser.
3. Add arguments and options to the parser using the .add_argument() method.
4. Call .parse_args() on the parser to get the Namespace of arguments.
<pre>
- Ex. above code run using argparse
# ls.py v1
import argparse
from pathlib import Path
parser = argparse.ArgumentParser()
parser.add_argument("path")
args = parser.parse_args()
target_dir = Path(args.path)

if not target_dir.exists():
    print("The target directory doesn't exist")
    raise SystemExit(1)

for entry in target_dir.iterdir():
    print(entry.name)
</pre>
<pre>
$ python ls.py sample/
lorem.md
realpython.md
hello.txt
$ python ls.py
usage: ls.py [-h] path
ls.py: error: the following arguments are required: path
$ python ls.py -h
usage: ls.py [-h] path

positional arguments:
  path

options:
  -h, --help  show this help message and exit
</pre>
- Creating Command-Line Interfaces With Python’s argparse
- Cool feature of argparse is that it automatically generates usage and help messages for your CLI apps. The module also issues errors in response to invalid arguments and more.
    - Positional arguments, which you know as arguments - its relative position in the command construct defines its purpose.
    - Optional arguments, which you know as options, flags, or switches -  They allow you to modify the behavior of the command
- Creating a Command-Line Argument Parser
<pre>
- Ex.
>>> from argparse import ArgumentParser

>>> parser = ArgumentParser()
>>> parser
ArgumentParser(
    prog='',
    usage=None,
    description=None,
    formatter_class=<class 'argparse.HelpFormatter'>,
    conflict_handler='error',
    add_help=True
)
</pre>
- Adding Arguments and Option -> use the .add_argument() method of your ArgumentParser instance
- The first argument to the .add_argument() method sets the difference between arguments and options. This argument is identified as either name or flag. So, if you provide a name, then you’ll be defining an argument. In contrast, if you use a flag, then you’ll add an option
<pre>
- Ex.
# ls.py v2

import argparse
import datetime
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument("path")

parser.add_argument("-l", "--long", action="store_true")

args = parser.parse_args()

target_dir = Path(args.path)

if not target_dir.exists():
    print("The target directory doesn't exist")
    raise SystemExit(1)

def build_output(entry, long=False):
    if long:
        size = entry.stat().st_size
        date = datetime.datetime.fromtimestamp(
            entry.stat().st_mtime).strftime(
            "%b %d %H:%M:%S"
        )
        return f"{size:>6d} {date} {entry.name}"
    return entry.name

for entry in target_dir.iterdir():
    print(build_output(entry, long=args.long))
</pre>
<pre>
$ python ls.py -l sample/
  2609 Oct 28 14:07:04 lorem.md
   428 Oct 28 14:07:04 realpython.md
    83 Oct 28 14:07:04 hello.txt
</pre>
- The syntactical difference between arguments and options is that option names start with - for shorthand flags and -- for long flags.
- an action argument set to "store_true" accompanies the -l or --long option, which means that this option will store a Boolean value. If you provide the option at the command line, then its value will be True. If you miss the option, then its value will be False. 

- Parsing Command-Line Arguments and Options
- The argument parsing happens on the line containing the args = parser.parse_args() statement. This statement calls the .parse_args() method and assigns its return value to the args variable. The return value of .parse_args() is a Namespace object containing all the arguments and options provided at the command line and their corresponding values.
<pre>
- Ex.
>>> from argparse import ArgumentParser

>>> parser = ArgumentParser()

>>> parser.add_argument("site")
_StoreAction(...)

>>> parser.add_argument("-c", "--connect", action="store_true")
_StoreTrueAction(...)

>>> args = parser.parse_args(["Real Python", "-c"])
>>> args
Namespace(site='Real Python', connect=True)

>>> args.site
'Real Python'
>>> args.connect
True
</pre>
- Setting Up Your CLI App’s Layout and Build System
- You can add a __main__.py module to any Python package if you want to make that package directly executable.
<pre>
- Ex.
hello_cli/
│
├── hello_cli/
│   ├── __init__.py
│   ├── __main__.py   -> provides the application’s entry-point script or executable file.
│   ├── cli.py      -> provides the application’s command-line interface; view-controller role in the MVC-based architecture.
│   └── model.py    -> contains the code that supports the app’s main functionalities; model role in your MVC layout.
│
├── tests/
│   ├── __init__.py
│   ├── test_cli.py
│   └── test_model.py
│
├── pyproject.toml
├── README.md
└── requirements.txt
</pre>
<pre>
- # pyproject.toml - need to add entry point script
[project.scripts]
hello_cli = "hello_cli.__main__:main"
</pre>
- Customizing Your Command-Line Argument Parser
- Tweaking the Program’s Help and Usage Content
- Setting the Program’s Name
By default, argparse uses the first value in sys.argv to set the program’s name
Ex. parser = argparse.ArgumentParser(prog="ls")

- Define the Program’s Description and Epilog Message
- You can also define a general description for your application and an epilog or closing message.
<pre>
- Ex.
parser = argparse.ArgumentParser(
    prog="ls",
    description="List the content of a directory",
    epilog="Thanks for using %(prog)s! :)",
)
</pre>
<pre>
- O/P -> 
$ python ls.py -h
usage: ls [-h] [-l] path

List the content of a directory

positional arguments:
  path

options:
  -h, --help  show this help message and exit
  -l, --long

Thanks for using ls! :)
</pre>
- Display Grouped Help for Arguments and Options -> They allow you to group related commands and arguments, which will help you organize the app’s help message. 
<pre>
- Ex.
general = parser.add_argument_group("general output")
general.add_argument("path")

detailed = parser.add_argument_group("detailed output")
detailed.add_argument("-l", "--long", action="store_true")
</pre>
<pre>
- O/P
python ls.py -h
usage: ls [-h] [-l] path

List the content of a directory

options:
  -h, --help  show this help message and exit

general output:
  path

detailed output:
  -l, --long

Thanks for using ls! :)
</pre>
- Providing Global Settings for Arguments and Options
- Common use case of argument_default is when you want to avoid adding arguments and options to the Namespace object. In this situation, you can use the SUPPRESS constant as the default value.
Ex.
parser = argparse.ArgumentParser(
    prog="ls",
    description="List the content of a directory",
    epilog="Thanks for using %(prog)s! :)",
    argument_default=argparse.SUPPRESS,#By passing SUPPRESS to ArgParser const, you prevent nonsupplied arguments from stored in arguments Namespace object. 
)
for entry in target_dir.iterdir():
    try:
        long = args.long
    except AttributeError:
        long = False
- load argument values from an external file.
<pre>
Ex.
# fromfile.py

import argparse
parser = argparse.ArgumentParser(fromfile_prefix_chars="@")
parser.add_argument("one")
parser.add_argument("two")
parser.add_argument("three")
args = parser.parse_args()
print(args)

args.txt -> 
first
second
third
 
python fromfile.py @args.txt # call 
Namespace(one='first', two='second', three='third')   #  O/P
Ex.
# abbreviate.py

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--argument-with-a-long-name")
args = parser.parse_args()
print(args.argument_with_a_long_name)
$ python abbreviate.py --argument-with-a-long-name 42
42
$ python abbreviate.py --argument 42
42
</pre>
- replace with parser = argparse.ArgumentParser(allow_abbrev=False)
<pre>
$ python abbreviate.py --argument 42
usage: abbreviate.py [-h] [--argument-with-a-long-name ...]
abbreviate.py: error: unrecognized arguments: --argument 42
</pre>
- Fine-Tuning Your Command-Line Arguments and Options
- Setting the Action Behind an Option
- When you add an option or flag to a command-line interface, you’ll often need to define how you want to store the option’s value in the Namespace object that results from calling .parse_args().
<pre>
Allowed Value	        Description
store	                Stores the input value to the Namespace object   ( ## DEFAULT)
store_const	            Stores a constant value when the option is specified
store_true	            Stores the True Boolean value when the option is specified and stores False otherwise
store_false	            Stores False when the option is specified and stores True otherwise
append	                Appends the current value to a list each time the option is provided
append_const	        Appends a constant value to a list each time the option is provided
count	                Stores the number of times the current option has been provided
version	                Shows the app’s version and terminates the execution
</pre>
- Ex.
<pre>
# actions.py

import argparse
parser = argparse.ArgumentParser()
parser.add_argument(
    "--name", action="store"
)  # Equivalent to parser.add_argument("--name")
parser.add_argument("--pi", action="store_const", const=3.14)
parser.add_argument("--is-valid", action="store_true")
parser.add_argument("--is-invalid", action="store_false")
parser.add_argument("--item", action="append")
parser.add_argument("--repeated", action="append_const", const=42)
parser.add_argument("--add-one", action="count")   #Ex. verbosity level, -v or -vv
parser.add_argument(
    "--version", action="version", version="%(prog)s 0.1.0"
)
args = parser.parse_args()
print(args)
- O/P
$ python actions.py \
    --name Python \
    --pi \
    --is-valid \
    --is-invalid \
    --item 1 --item 2 --item 3 \
    --repeat --repeat --repeat \
    --add-one --add-one --add-one
Namespace(
    name='Python',
    pi=3.14,
    is_valid=True,
    is_invalid=False,
    item=['1', '2', '3'],
    repeated=[42, 42, 42],
    add_one=3
)
</pre>
<pre>
$ python actions.py --version
actions.py 0.1.0
</pre>
- Creating custom actions by subclassing the argparse.Action class. If you decide to do this, then you must override the .__call__() method, which turns instances into callable objects.
<pre>
Ex.
# custom_action.py

import argparse
class VerboseStore(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print(f"Storing {values} in the {option_string} option...")
        setattr(namespace, self.dest, values)
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", action=VerboseStore)
args = parser.parse_args()
print(args)
</pre>
- O/P
<pre>
$ python custom_action.py --name Python
Storing Python in the --name option...
Namespace(name='Python')
</pre>
- Customizing Input Values in Arguments and Options
- Setting the Type of Input Values
<pre>
- Ex.
# divide.py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--dividend", type=int)
parser.add_argument("--divisor", type=int)
args = parser.parse_args()
print(args.dividend / args.divisor)
</pre>
<pre>
- O/P
$ python divide.py --dividend "42" --divisor "2"
21.0

$ python divide.py --dividend 42 --divisor 2.0
usage: divide.py [-h] [--dividend DIVIDEND] [--divisor DIVISOR]
divide.py: error: argument --divisor: invalid int value: '2.0'
</pre>
- Taking Multiple Input Values
- The nargs argument tells argparse that the underlying argument can take zero or more input values depending on the specific value assigned to nargs.
<pre>
Allowed Value	            Meaning
?	                    Accepts a single input value, which can be optional
*	                    Takes zero or more input values, which will be stored in a list
+	                    Takes one or more input values, which will be stored in a list
argparse.REMAINDER	    Gathers all the values that are remaining in the command line
</pre>
- Ex1
<pre>
# point.py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--coordinates", nargs=2)
args = parser.parse_args()
print(args)
</pre>
<pre>
O/P ->
$ python point.py --coordinates 2 3
Namespace(coordinates=['2', '3'])

$ python point.py --coordinates 2
usage: point.py [-h] [--coordinates COORDINATES COORDINATES]
point.py: error: argument --coordinates: expected 2 arguments
</pre>
- Ex2
<pre>
# sum.py

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("numbers", nargs="*", type=float)
args = parser.parse_args()
print(sum(args.numbers))
</pre>
<pre>
O/P ->
$ python sum.py 1 2 3 4 5 6
21.0

$ python sum.py
0
</pre>
- Challenging to use when providing multiple arguments
<pre>
# cooking.py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("veggies", nargs="+")
parser.add_argument("fruits", nargs="*")
args = parser.parse_args()
print(args)
</pre>
<pre>
O/P ->
$ python cooking.py pepper tomato apple banana
Namespace(veggies=['pepper', 'tomato', 'apple', 'banana'], fruits=[])
</pre>
- Fix issue below :
<pre>
# cooking.py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--veggies", nargs="+")
parser.add_argument("--fruits", nargs="*")
args = parser.parse_args()
print(args)
</pre>
<pre>
O/P ->
$ python cooking.py --veggies pepper tomato --fruits apple banana
Namespace(veggies=['pepper', 'tomato'], fruits=['apple', 'banana'])
</pre>
- Providing Default Values
Ex. general.add_argument("path", nargs="?", default=".")    # Path set to cwd if no provided, all the command-line arguments in argparse are required, and setting nargs to either ?, *, or + is the only way to skip the required input value. 

- Specifying a List of Allowed Input Values
- a list of accepted values using the choices argument of .add_argument().
<pre>
- Ex.
# size.py

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--size", choices=["S", "M", "L", "XL"], default="M")
args = parser.parse_args()
print(args)
</pre>
<pre>
O/P ->
$ python size.py --size S
Namespace(size='S')
$ python choices.py --size A
usage: choices.py [-h] [--size {S,M,L,XL}]
choices.py: error: argument --size: invalid choice: 'A'
    (choose from 'S', 'M', 'L', 'XL')

- Ex. my_parser.add_argument("--weekday", type=int, choices=range(1, 8))
</pre>
- Providing and Customizing Help Messages in Arguments and Options
- you’ll use the help and metavar arguments of .add_argument()
<pre>
- Ex.
general = parser.add_argument_group("general output")
general.add_argument(
    "path",
    nargs="?",
    default=".",
    help="take the path to the target directory (default: %(default)s)",
)

detailed = parser.add_argument_group("detailed output")
detailed.add_argument(
    "-l",
    "--long",
    action="store_true",
    help="display detailed directory content",
)
</pre>
- The metavar argument comes in handy when a command-line argument or option accepts input values. It allows you to give this input value a descriptive name that the parser can use to generate the help message.
<pre>
Ex.
# point.py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument(
    "--coordinates",
    nargs=2,
    metavar=("X", "Y"),
    help="take the Cartesian coordinates %(metavar)s",
)
args = parser.parse_args()
print(args)
</pre>
<pre>
O/P - 
$ python coordinates.py -h
usage: coordinates.py [-h] [--coordinates X Y]

options:
  -h, --help         show this help message and exit
  --coordinates X Y  take the Cartesian coordinates ('X', 'Y')
</pre>
- Defining Mutually Exclusive Argument and Option Groups
- This feature comes in handy when you have arguments or options that can’t coexist in the same command construct.
<pre>
- Ex.
# groups.py
import argparse
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-s", "--silent", action="store_true")
args = parser.parse_args()
print(args)
</pre>
- Adding Subcommands to Your CLIs<br>
Ex. pip -> pip install, pip download, pip uninstall, pip list 
- for subcommands use the .add_subparsers() method of ArgumentParser.
<pre>
- Ex.
# calc.py
import argparse
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b

global_parser = argparse.ArgumentParser(prog="calc")
subparsers = global_parser.add_subparsers(
    title="subcommands", help="arithmetic operations"
)
arg_template = {                # sensitive values for the required arguments of .add_argument()
    "dest": "operands",         # Each argument will be called operands and will consist of two floating-point values.
    "type": float,
    "nargs": 2,
    "metavar": "OPERAND",
    "help": "a numeric value",
}
add_parser = subparsers.add_parser("add", help="add two numbers a and b")
add_parser.add_argument(**arg_template)         # use dictionary unpacking operator here
add_parser.set_defaults(func=add)               # to assign the add() callback function to the add subparser or subcommand.
sub_parser = subparsers.add_parser("sub", help="subtract two numbers a and b")
sub_parser.add_argument(**arg_template)
sub_parser.set_defaults(func=sub)
mul_parser = subparsers.add_parser("mul", help="multiply two numbers a and b")
mul_parser.add_argument(**arg_template)
mul_parser.set_defaults(func=mul)
div_parser = subparsers.add_parser("div", help="divide two numbers a and b")
div_parser.add_argument(**arg_template)
div_parser.set_defaults(func=div)
args = global_parser.parse_args()
print(args.func(*args.operands))
</pre>
<pre>
O/P ->
$ python calc.py add 3 8
11.0
</pre>
- Handling How Your CLI App’s Execution Terminates
- exit the app while emitting an error code or exit status so that other apps or the operating system can understand that the app has terminated because of an error in its execution.
- In Python, you’ll commonly use integer values to specify the system exit status of a CLI app. If your code returns None, then the exit status is zero, which is considered a successful termination. Any nonzero value means abnormal termination. Most systems require the exit code to be in the range from 0 to 127, and produce undefined results otherwise.
- The argparse module, specifically the ArgumentParser class, has two dedicated methods for terminating an app when something isn’t going well:
<pre>
Method	                                    Description
.exit(status=0, message=None)	            Terminates the app, returning the specified status and printing message if given
.error(message)	                            Prints a usage message that incorporates the provided message and terminates the app with a status code of 2
Both methods print directly to the standard error stream,
</pre>
<pre>
- Ex.
target_dir = Path(args.path)

if not target_dir.exists():
    parser.exit(1, message="The target directory doesn't exist")
O/P
$ python ls.py non_existing/
The target directory doesn't exist

$ echo $?
1
</pre>






