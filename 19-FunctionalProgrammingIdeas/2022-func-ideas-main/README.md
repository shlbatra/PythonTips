# 3 Simple Ideas From Functional Programming To Improve Your Code

Functional programming is a complex topic to dive into. However, there are 3 simple ideas from functional/declarative code that you can apply to your own code today - without becoming a Haskell expert! In this video, I dive into the details and show you a few examples in Python of how you can use these ideas in both object-oriented and functional/procedural code.

- OOP 
    - Classes with attributes and methods 
    - Imperative programming -> how to execute, defines control flow as statement that change a program state, specify step that computer must take to accomplish goal, also called algorithmic programming
- FP 
    - using functions 
    - declarative programming -> what to execute, defines program logic but not detailed control flow
    - ex. SQL -> not care how its done just what we need
    - ex. Excel
    - programs constructed by applying and composing functions

1. Group side effects and use pure functions
    - Side effect -> fn or methods relies on or modifies something on the outside of the fn.
    Ex - print on console that is outside fn, Reading/Writing to file, Interacting with database, Interacting with other services -> harder to mantain/test
    - Pure fn - just depend on input and return value depend on input and no external library , easy to test and use on other apps 
2. Functions are first class citizens
    - things compose, decompose, pass to other functions and return as value from fn
    - fn receives a fn as argument or returns fn then called higher order fn
    - pass fns so have control of whether to run that fn or not
    - partial fn application
        - create new fns that is based on original fn with some args applied
3. Use immutability to advantage
    - python variables can be changed anytime (imperative lang)
    - declarative lang - variable bound by expression and keep same value
    - solve multithreading problems where multiple threads try to change value at same time
    - program easier to understand/test if var never change
    - with mutable, lose original data - cant verify anymore
    - with immutable, setting test easy
    - with immutable, get extra flexibility -> can work on any sequence not mutable sequence
    - ex. dataclass with frozen - attributes dont change - easy to write tests
    - if change variable all time -> less often, turn to immutable - easy to mantain and test

