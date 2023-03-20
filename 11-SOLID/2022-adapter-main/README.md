# Let's Take The Adapter Design Pattern To The Next Level

The Adapter pattern is really useful if you need to connect your application with another system, but you can't change the code of that system and you want to reduce coupling. In this video I show you how the pattern works, and then show you a functional variant of the pattern using partial application.

- reduce coupling and make it easy to change or extend code
- Ex. read from json but want to read from any file ex. XML - use beautifulsoup , get data diff -> class with getters 
- need to manually change code either main or experiment class accept any generic type.
- adaptor provide interface between xml reader and json reader and experiment use info that comes from that config
- Adaptor pattern - adapt existing system to use in your app -> create adaptor layer between existing system and code
- Ex. put adapator between usbc connector and micro usb input
- 2 versions 
    - object based version (better - rely on composition)

    client uses <interface> Target +operation() <- Adapter  + operation()  - Adaptee +specificoperation()
    Adaptor has instance of adaptee
    - class based version - rely on inheritance

    client(Expt) uses <interface> Target(config) +operation() <- Adapter(xml)  + operation()  <- Adaptee(bs) +specificoperation()
    Adaptor subclass of adaptee

    Client o-- Target : uses
    Target(interface) <|-- Adapter
    Adaptee <|-- Adapter

    For class version -> override get method for bs -> other things rely on bs might not work anymore - class dangerous; 
    -> mixes up definition and interfaces of original of adaptee with what have in adapter
    -> composition - bs passed as object and object exposes new interface that has new definition seperate from adaptee def

- Use partial functions 
    - reduce code
    - In ex, just call get method -> provide fn to experiment class than object; pass key and return value
    - 