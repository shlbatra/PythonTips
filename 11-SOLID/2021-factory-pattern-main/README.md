# 7 The Factory Pattern in Python

The example is about video and audio exporting. In `before.py`, you find the original code. The `after.py` file contains a version where the factory pattern is used.

- Seperate creation from use
- create objects in diff place and where to use
- code doesnt need to know where objects created
- create exporter factory that gives us objects we need
- allow to group objects that belong together
- ex. webshop - settings per country ex currency or language or tax
- not work well if allow any combination of things - create factory class for every combination -> use composition and depedency inversion

# design principle under factory pattern using modern python constructs
    - seperate creation from use
    - inject objects of a subclass in another part of application without knowing what they are
    - Single responsibility - not have job of creating and using something at the same place
    - open close principle - open for extension but closed for modification 

# Use protocol classes
    - behaves as interface 
    - dont need to inherit to use 
    - structural typing -> objects of matching type if structures are same ex. objects have same methods
    - preferred over ABC -> similar with extra functionality
    - not doing inheritance - so missing partial implementations in super class
    - type checker cant point errors for method defintions
    - use them to define contract of what method is expecting in terms of objects with methods

# Use tuples instead of factory classes
    - factory class is container of objects or functions of create those objects
    - pass tuples instead of factory classes
    - tuples are container of objects
    - add config data to tuple - complicated (setting of audio/video objects)
    - all comb of video and audio on factory dictionary - loss of cohesion
    - order of export know - video exporter, audio exporter -> use named tuple or dunder methods 

# Use dataclasses and dunder methods 
    - easier access with classes flexibility for object construction
    - clean way of creating our exporters here
    - disadvantage -> use more memory/space and mutable
    - overall nice solution
