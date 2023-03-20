# You Are Going To Like These New Features In Python 3.11

Python 3.11 is finally here! Not all of the changes are immediately noticeable when you look through the release notes. However, today I will cover 7 new Python 3.11 features that you are going to love because they'll make your life a lot easier.

Video link: https://youtu.be/b3_THpKM4EU.

- tomblib (Tom's Obvious Minimal Language) part of standard library
    - defining config files (settings.toml)
- add notes to exception objects (add_note method) -> add extra info
- Tracebacks more precise - beyond line error occured. 
- new literalstring type -> ex. Literal["ArjanCodes"] -> only accept this value
    - LiteralString -> invoking SQL query for sql injection attacks.  
- Self type -> method returns type of class of which method part of (name of class between "" or use _future)
- StrEnum type 
    - create string values using auto() 
    - Ex. 
    class Color(StrEnum):
    WHITE = auto()
    BLACK = auto()

    print(Color.BLACK.value)  -> black

- Improved performance (C python 25% faster)

