- Design Patterns 
    - Creational 
        - control over creating objects in various ways. ex. Singleton
    - Structural 
        - how assemble classes and objects into larger structures while keeping those structures flexible and efficient. organize diff parts of your application. ex. brdige pattern
    - Behavioral 
        - choose between algo or how diff parts of application communicate. ex. stratergy and observer

- Questionable Object Creation patterns
- Singleton pattern
    - allow one single instance of class. 
    - ex. graphics device manager, logger, event manager
    - anti pattern
        - break oop principle -> inherit multiple subclasses - multiple instances created
        - no control over creation -> existing or newly created 
        - testing hard - each test cant have an instance
        - not work for multi threading as multiple instances for multiple threads
        - python use module 


Singleton
- instance: Singleton
- Singleton() 
+ GetInstance() : Singeton

2 mechanisms of object orientation
    - static/class method - access to instance
    - private access modifier - access to method inside class . constructor private
    - python not have access modifiers to make constructor private

- Object Pool
    - manages fixed number of instances / manage a pool of objects
    - 2 lists, list1 - objects in use, list2 - objects that are free
    - objects expensive -> need for short time - managing db connections, graphics objects containing lot of mesh data
    - use context manager that automatically acquires and releases objects
    - use metaclasses for restriction. ex . block instance from calling method not acquired from the pool 
    - when release, reset back to fresh state to be used by someone
    - if not reset objects, leaking info ex. token, multi threading issues for multiple threads have access to same object at the same time



