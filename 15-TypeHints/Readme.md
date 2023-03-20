- Issues with Typehints
    - Type programmed languages (statically typed) need to define type explicitly
    - ex.  method - type of args and return 
    - python - dynamically typed - types not reqd but can provide type hints 
    - Why not do type hinting ?
        - typing will never be enforced in python
        - always stay dyanmically typed
        - artificially limit code as generic methods might work with any type
        - not all libraries have type hints
        - extra work but interpretor ignore them
        - add type test as unit test
    - Why do type hinting 
        1. Type help me write shorter documentation
            - doc easy outdated and manually check for it
            - harder to read if too much doc 
            - type standardized way of what arg look like and what method returns 
        2. Type helpful while writing code 
            - ide detect sooner if passing wrong data structure or autocomplete
            - pep support
            - identify error while writing code rather than run code
        3. Type hints make coupling more explicit
            - see which modules are coupled or impacted when make change
            - ex use beautifulsoup to parse html. So, if change beautifulsoup, then know which area of code change for where object of beautifulsoup is being used
        4. Type hints forces you to be explicit about your data structures
            - clear idea of what data looks like 
            - discourage bahviour that lead to messy code - change data structure on fly, dynamically add attributes or large data structures
        5. Type driven development 
            - Explain to type checker how your data will be structured and how its going to interact
        6. Type hints simplify code
            - reduce if conditions to check getting correct args
            - use pydentic - that fails while importing the bad data
    - type hints vs unit tests
        - type hint faster for complex data structures
        - unit test focus more on testing actual behavior of functsions and methods










