# The Ultimate Guide to Writing Classes in Python

In this video, I'll share 5 essential tips for writing Python classes that will help you take your object-oriented programming skills to the next level.

- Think class as data vs behaviour focussed
    - Data focus
        - structured objects
    - Behaviour focus
        - grouping methods that belong together
- make classes small and focussed
- Make class easy to use
    - property
        - access directly like instance ( not need for paranthesis)
    - dundar methods
- Dependency Injection
    - testing easier if we pass object class directly
    - use abstraction with protocol / ABC
- Do we need classes here ?
    - if need single instance of class then use functions with module
    - ex. here email sender - just need single instance 
- Encapsulation
    - hide info (wrapper around data)
    - methods to alter data
    - data class not support encapsulation
    - python not have access modifiers so cant mark attributes as private
    - use __ before instance variable name