- oop
- functional programming (Typescrip & React)
1. Combine FP & OOP - support Python
    - Class and functions(functools)
2. Make classes either behavior oriented or data oriented
    - dataclass - structure data as single object
    - behavior - methods mostly, grouping behavior - can turn into functions as well
    - alternate , make behaviour class as a module with functions in it
3. Be careful with inheritance
    - mainly used to define interface
    - avoid deep hierarchy of classes
    - think about how levels interact, things do in super class interact with things in subclasses - in 2 diff places - can get messy
4. Use dependency injection
    - help in decouple things
    - not create object in method but pass that object as argument so it can be used directly in method - hard to test when create object
    - connect things, dirty details in single place in code - patch at one place and rest independent
    - add depedency inversion by using ABC or protocol classes for StripePaymentHandler
5. Dont abuse python power features
    - allow control over lot of internal things. Ex. using dundar methods/instance variable - redesign if using way too much lower level code
    - ex. override __new__ method
