# You Can Do Really Cool Things With Functions In Python

In this video I cover a couple of not so common things you can do with functions in Python, including closures and partial function application. Functions are incredibly powerful and you can use them to write code that's really clean and often a lot shorter than when relying on classes and object-oriented programming.

- Functional Programming Stratergy
    - fns group operations and call from one or more places
    - python fns type callable -> define type alias, pass as args,
    - functools -> call functions partially
    - if dont store state, then functions provide great way to achieve stratergy pattern
    - no way to pass parameters to these functions as expect these fns to have a particular type -> ex. callable with list of prices only so not pass max price or window size
    - Solution is to use Fn Closure
    - in class soln, use init to store them as state 

- Function Closures
    - fn return is still a function that uses list of prices. Closure fn gets extra parameters

- Partial Fns
    - more elegant soln for parameter passing to methods
    - fixes no of args in original fn and returns new fns without those args
    - Querying -> fn with multiple args replace with sequence of fn taking single arg(diff). used in theoritical comp science
    - flexibility in way we define our functions and supply extra args. - partially applied fns with args to resolve args