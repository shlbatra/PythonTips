"""
Example application showing Python 3.10 structural pattern matching to parse and interpret variety of commands.
"""

import shlex
from dataclasses import dataclass
from typing import List

"""
Example code (Simple pattern match example) -
def run_command(command: str) -> None:
     match command:
        case "quit":
            print("Quitting program")
            quit()
        case "reset":
            print("Resetting the system)
        case other:
            print(f"Unknown command: {other!r}.")
            
def main() -> None:
    while True:
        command = input("$ ")
        run_command(command)
    
"""

def run_command_v1(command: str) -> None:
    match command:
        case "quit":
            print("Quitting the program.")
        case "reset":
            print("Resetting the system.")
        case other:
            print(f"Unknown command '{other}'.")

def run_command_v2(command: str) -> None:
    match command.split():  #get list of commands and arguments you provide and match with cases 
        case ["load", filename]:
            print(f"Loading filename {filename}.")
        case ["save", filename]:
            print(f"Saving filename {filename}.") #*rest any other elements in array
        case ["quit" | "exit" | "bye", *rest]:   #handle diff variety of keywords in the same case
            if "--force" in rest or "-f" in rest:
                print("Sending SIGTERM to all processes and quitting the program.")
            else:
                print("Quitting the program.")
            quit()
        case _:
            print(f"Unknown command '{command}'.")

def run_command_v3(command: str) -> None:
    match command.split():  #command here a string and relying on it instead 
        case ["load", filename]: 
            print(f"Loading filename {filename}.")
        case ["save", filename]:
            print(f"Saving filename {filename}.")  
        case ["quit" | "exit" | "bye", *rest] if "--force" in rest or "-f" in rest:
            print("Sending SIGTERM to all processes and quitting the program.")
            quit()
        case ["quit" | "exit" | "bye"]:
            print("Quitting the program.")
            quit()
        case _:  #unused variable 
            print(f"Unknown command {command!r}.")

#command using objects - class command containing command info
#pattern matching on attributes of object
@dataclass
class Command:
    """Class that represents a command."""
    
    command: str
    arguments: List[str]

def run_command_v4(command: Command) -> None:
    match command:
        case Command(command="load", arguments=[filename]):
            print(f"Loading filename {filename}.")
        case Command(command="save", arguments=[filename]):
            print(f"Saving filename {filename}.")
        case Command(command="quit" | "exit" | "bye", arguments=["--force" | "-f", *rest]): #nested pattern , commands at top level and arguments at next level 
            print("Sending SIGTERM to all processes and quitting the program.")
            quit()
        case Command(command="quit" | "exit" | "bye"):
            print("Quitting the program.")
            quit()
        case _:
            print(f"Unknown command {command!r}.")


def main() -> None:
    """Main function."""

    while True:
        # command = input("$ ")
        # run_command_v3(command)
        # read a command with arguments from the input
        command, *arguments = shlex.split(input("$ "))  #create instance of command class

        # run the command
        run_command_v4(Command(command, arguments))


if __name__ == "__main__":
    main()
