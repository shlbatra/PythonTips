## Protocol Or ABC In Python - When to use which one?

When should you use protocol classes vs abstract base classes? Here's an example where I use both, talk about the trade-offs and give you a suggestion of when to use each of them.

- Example is internet of things service

- Abstract Base Class 
    - Inherit provide explicitly
    - need to import either where inheriting from it or using its objects
    - type checking tool point error at point of creating instance 
    - use nominal typing -> typing relationship explicit in code. ex use inheritance
    - Errors out at the point of creating instance 
    - class hierarchy - allows you to reuse any super class methods in sub classes

- Protocol (python 3.8) -> Allows interface segregation
    - work diff than abc
    - structural typing -> python looks at structure of objects,ex. same methods or properties - assume type matched, no inheritance relationship here 
    - mainly defines interface expected to other parts of program that use protocol in some way- works with python run time type checking system that treats two objects same if they have same methods / properties - duct typing 
    - Errors out at the point of using instance at place where expecting to implement that protocol
    - reduces coupling -> service not know about devices connect, disconnect and all methods , limiting interface and definition of interface 
    - ex. split protocol class into two so each part of program - service or diagnostics use what they need to 
    - protocol belong to thing that defines how it needs the protocol
    - define interface of what another part of program expects and pass object that adheres to that interface that implements that protocol. 
    - put at the place where use -> connect diff libraries and reduce coupling
    - same protocol multiple times -> same class in multiple files
