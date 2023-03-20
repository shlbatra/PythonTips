- Error Condition - happen during run time and handled during execution of code
- Ex. auth code not valid, device not found, internet connection lost
- Syntax errors happen at compile and interpretation time
- Run time errors
- Handling errors while interpreting or handling errors while run time are both done using exceptions
- Python has Exception class. Every exception should be a sub class of super class - Exception
- handle exception at low level ex SQLLite in db.py, then handle it at API level so even if database changes, exceptions remain consistent
- Exceptions at multiple levels so right info is transferred, handle exception at right layer
- Context managers provide bit more control over when objects are created and destroyed - free up resources accordingly . Ex. open file using with keyword . Create class with enter and exit method -> object of that class will be used as context manager
- retry decorator
    - ex. db connection - retry something , function here models this behaviour, decorator wrap around function that keeps track of retries
- logging decorator
    - automatically log exceptions,
- Issues with exceptions
    - Introduce second hidden control flow -> harder to grasp what happens in program in case of error
    - if not careful,then resource leaks. ex. not releasing memory or database connection 
    - introduce coupling as high level systems need to know about low level objects 
    - never sure code handles all exceptions properly
- Alternate way of dealing 
    - terminate program (BAD)
    - fn raise exception - return error code instead of value - Break type systems
    - call error handler fn on error (Javascript) -> leads to callback hell
    - return dumy value from fn and set global error somewhere else -> global error stack (again coupling)
    - deferred error handling (Go) -> return legal value and set error flag (Least bad soln)
- Flaws with Error Handling Video
    - retreive data using SQL query - string interpretation to construct SQL query - bad (SQL injection attacks)
    NO -> cur.execute(f"select * from blogs where id='{id}'")
    YES -> cur.execute(f"select * from blogs where id=?",[id])
    use orams - sqlalchemy - take care of sql injection issues for you
    - error handling by catching all exceptions -> python uses exceptions both while running and interpreting code -> if all errors then not differentiate name errors from typos
    except Exception as e:
        print(e)
        return []
    BAD PRACTICE below as this will never give error in Python . Any error is ignored ->
    try:
        something
    except Exception:
        pass
    Handle errors that you know what to do with. 

- Monadic Error Handling
    - Used in Functional Programming -> monads
    - instead of using exception, rewrite fn return 2 things 
        - success value if computation succeeds
        - fail value if computation errors out
    - When combine fns (Chain functions)
        - return success/failure
        - accept both success/failure track as inputs
        - Get Success track and Failure track
        - Call ray way oriented programming
    - Monad -> combining success (int/float) with exceptions (div by 0, value not found) and getting resulting fn in a container
    - Implemented using dry-python library
    - no hidden control flow here - success and failure handled explicitly
    - handle resource clean up - context manager tie in well