- SOLID Principle
    1. Single Responsibility
    2. Open/Closed
    3. Liskov Substitution
    4. Interface Segregation
    5. Depedency Inversion
- Single Responsibility
    - Classes and methods to have single responsibility - high cohesion 
- Open/Closed
    - Write code open for extension to new functionality but closed for modification to original code.
    - Ex. create structure of classes and subclasses to add extra functionality for a payment type. 
    - Payment is abstract class and each paymenttype is subclass
- Liskov Substitution
    - Object in program - replace those objects with instance of subtype/subclass without altering correctness of program
    - Ex. remove security code from abstract class and move to init for each subclass. 
- Interface Segregation
    - Overall better if we have several specific interfaces as opposed to one general interface
    - ex. not all subclasses support 2fa. So adding auth() to abstract class wont work
    - create seperate interface for it. Ex. 2nd subclass of paymentprocess for 2fa
    - so have PaymentProcessor -> PaymentProcessor_sms. Now use PaymentProcessor for any subclass that doesnt 
    support 2fa else use PaymentProcessor_sms
    - Another way of do this is by Composition
        - Create class for sms auth seperately , now subclasses get object authorizer from class createdd:SMSAuth
        - seperate diff kinds of behavior in application
- Depedency Inversion
    - classes depend on abstraction and not on concrete subclasses. 
    - ex. paymentprocess depend on auth. so create abstract Authorizer class. 
    - Authorizer -> SMSAuth , Authorizer -> NotARobot