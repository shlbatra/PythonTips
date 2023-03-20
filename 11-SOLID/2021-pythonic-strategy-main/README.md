## A Pythonic Strategy pattern 

- helps to reduce coupling, shorter and easier to implement
- allows to inject behavior in application without code knowing exactly what behavior does
- relies on interface - signature of stratergy fn to break up app and reduce coupling
- interface specifies methods and classes implement interface and create instance of those classes and inject objects to app
Context   <-    Stratergy 
                + execute()

                                |
    Concrete Stratergy A                Concrete Stratergy B
    + execute()                            + execute()

- classic stratergy pattern 
    - uses abstract classes and inheritance

- use protocols
    - not use inheritance in this case
    - python duct typing system figures it out

- use dunder methods 
    - used __call__ method here so call the object of class directly

- use functions 
    - dont need object oriented programming as only using function here for stratergy 
    - stratergy is functions 
    - blend functional programming with object oriented programming
    - Type is callable here -> doesnt matter use class method, class dundar method or normal fns here - instance of class will be callable as well
    - One issue -> if set parameters of stratergy, in class add instance variable with init
        - if pass parameter - how to use method approach
            - can add *args, **kwargs -> but then cust would need to know about the parameters

- Solution to above problem - use closures
    - create a function that returns the callable. Parameters are passed to the function 
    - closure keeps track of internal variables, similar to class
    - define local variables as well inside closure function - variables are protected here. Not accessible with object.variable -> would need closure dunder methods 
    - class with __call__ = functions = callables