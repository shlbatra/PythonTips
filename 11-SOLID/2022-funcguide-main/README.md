# The Ultimate Guide to Writing Functions

Video link: https://youtu.be/yatgY4NpZXE.

- Do one thing and do well
    - perform single task or sub task 
    - same level of abstraction
    - Ex. Does 2 things 
    - abs1 -> go thru collection (navigation), abs2 -> matches item and then updates. 
        def update_matching_item(thing):
            # update some item that lives in collection
            for item in collection:
                if matches(item, thing):
                    update(item)
                    break
    - Do one thing and do it very well
    - Seperate commands from queries (Command Query seperation)
        - retrieve info (query)
        - perform action (calculation)
    - function request information that it actually needs
        - make func call clear by using keyword args
        - force use of keyword args by adding * in func parameters
    - keep number of parameters minimal
        - too many parameters, risk fn do too many things
        - provide default values as an option if applicable
        - add abstraction using class -> protocol class
        - parameters
            - part of definition of fn def fn1(a)
        - arguments 
            - values set to parameters -> fn1(a=2)
    - Not create and use object in same place
        - Use dependency injection
        - not create object in function but pass it as an parameter
        - better add abstraction using abc or protocol classes
    - Not use flag parameters
        - basically 2 fns - one case boolean True and other False
    - Functions in python are objects (as is everything else)
        - fn as arg or return fn
    - naming function
        - not have and -> split
        - good arg name and shorten
        - fn name - verb and args - noun
        - use naming scheme - snakecase for Python