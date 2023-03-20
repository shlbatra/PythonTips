"""
Basic example showing how to read and validate data from a file using Pydantic.
1. Field validation - data cleaned and defined in a way you expect it to be.
2. Model validation - all fields ex. make sure every book has either isbn10 or isbn13
"""

import json
from typing import List, Optional

import pydantic


class ISBNMissingError(Exception):
    """Custom error that is raised when both ISBN10 and ISBN13 are missing."""

    def __init__(self, title: str, message: str) -> None:
        self.title = title
        self.message = message
        super().__init__(message)


class ISBN10FormatError(Exception):
    """Custom error that is raised when ISBN10 doesn't have the right format."""

    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)


class Author(pydantic.BaseModel):
    name: str
    verified: bool

#create class that inherits from pydantic
class Book(pydantic.BaseModel):
    """Represents a book with that you can read from a JSON file."""

    title: str
    author: str
    publisher: str
    price: float
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    subtitle: Optional[str]
    author2: Optional[Author]

    #model validation - check isbn10 or isbn13 or both
    @pydantic.root_validator(pre=True) #validate before 
    @classmethod
    def check_isbn_10_or_13(cls, values): #values dictionaru
        """Make sure there is either an isbn_10 or isbn_13 value defined"""
        if "isbn_10" not in values and "isbn_13" not in values:
            raise ISBNMissingError(
                title=values["title"],
                message="Document should have either an ISBN10 or ISBN13",
            )
        return values

    # add data validation - weighted sum of numbers divisible by 11
    @pydantic.validator("isbn_10")
    @classmethod
    def isbn_10_valid(cls, value) -> None: #value to vdalidate
        """Validator to check whether ISBN10 is valid"""
        chars = [c for c in value if c in "0123456789Xx"] #get valid characters only
        if len(chars) != 10: #added custom error type here
            raise ISBN10FormatError(value=value, message="ISBN10 should be 10 digits.")

        def char_to_int(char: str) -> int:
            if char in "Xx":
                return 10
            return int(char)
        weighted_sum = sum((10 - i) * char_to_int(x) for i, x in enumerate(chars))
        if weighted_sum % 11 != 0:
            raise ISBN10FormatError(
                value=value, message="ISBN10 digit sum should be divisible by 11."
            )
        return value

    # add to base model to change settings
    class Config:
        """Pydantic config class"""

        allow_mutation = False  #create immutable object, update book will give error
        anystr_lower = True # convert string values to lower case


def main() -> None:
    """Main function."""

    # Read data from a JSON file
    with open("./data.json") as file:
        data = json.load(file)  # ** -> unpacking items to keyword args
        books: List[Book] = [Book(**item) for item in data] #list of books from data read from JSON file
        # print(books)
        print(books[0]) #nicely formatted using pydantic
        #books[0].title="abcd"  # error 
        print("\n\n")
        print(books[0].title)
        #convert model to dictionary using dict method
        print(books[0].dict)
        # print(books[0].dict(exclude={"price"}))
        # print(books[0].dict(include={"price"}))
        # print(books[1].copy()) #copy of book
        #if model has nested list then use print(books[1].copy(deep=True)) 


if __name__ == "__main__":
    main()
