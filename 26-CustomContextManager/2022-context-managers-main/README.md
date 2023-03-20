# Building A Custom Context Manager In Python: A Closer Look

- Context managers in Python allow you to robustly control setup and teardown of resources. 
- minimize the chance of you forgetting to do teardown especially in presence of exceptions
- Ex. with to open a file. Good example of managing resources
    with open("my_file.txt", exncoding="utf-8") as file:
        data = file.read()
- with  (Behind the scenes, enter and exit part and exit for exception as well) ->
    with expression as variable:
        # do something with variable
        # ...
- sqllite -> connection automatically commit or rollback txn but object not close connection - needs to manually done
    with sqllite3.connect('application.db') as conn:
        cursor = connection.cursor()
        cursor.execute("select * from blogs")

- create own custom context manager
    - create custom manager class that handles close connection for you
    - decorator
    - async and await syntac
        - aiosqlite handles both asynchronous operations and auto closing of connections v
- use:
    - allocate and clean up resources
    - ex. file, database, network connection
- not use:
    - when not clean up resources 
    - unnecessary code identation and new scope

