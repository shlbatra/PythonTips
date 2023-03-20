# A Simple & Very Effective Way To Improve Python Performance

There's a very simple way to improve Python performance of your code. And you know what's so nice about this performance improvement? It also nudges you to use good Python software design practices - it's a win-win!

- Classes store attribute values in dict dunder object 
- attributes created dyanmically in init dunder method (can be any method)
- more info in dict than just the key value pair -> dynamic python cannot allocate static amt of memory at object creation to store all attributes - lot of RAM usage for objects
- implemented as hashmap, lookup fast still hashing and access can be slow
- Descriptors 
    - attribute value that has one of the methods in descriptor protocol
    - methods are get, set and delete dundar methods 
    - descriptors in python are implemented in C and very efficient
- object.__dict__ -> print dictionary of attributes. 
- attributes are dyanmic so can change
- if dont want to change attributes of class use Slots
- Slots
    - make attributes of class static
    - define instance variables statically so cant change them afterwards
    - in dataclass, can provide slot as argument to decorator -> slots = True/False
    - slots added recenlty so not change default behavour of something as core as classes
    - limitations
        - using mix ins and multiple inheritance 
        - cant perform multiple inheritence when classes have slots because python doesnt know which version of the slots object to use
        - can combine slots with non slots class for multiple inheritance case
        - cant dyanimically add attributes - overall good thing as define datastructures early on in your project
    - slots with dyanmic attributing can be done by adding
        - __slots__ = "name", "address", "email", "__dict__"
    - use in example where reading from database. ex. sqlalchemy uses it

