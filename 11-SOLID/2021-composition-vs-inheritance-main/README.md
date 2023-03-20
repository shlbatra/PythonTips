# Why composition is better than inheritance
The example is about different employee types and reward structures. In the first version (`before.py`), there is no inheritance, just three classes (= three employee types) with low cohesion (lots of responsibilities per class), and code duplication. Then there is a version that tries to solve those issues with inheritance (`with_inheritance.py`), and another version that uses composition (`with_composition.py`).

- Code with higher Cohesion

- Inheritance (is a relationship) - adds coupling so be careful
    - Instead of putting everything in 1 big class, create sub classes 
    - mostly used with abstract base class - seperate diff parts of application and combine then together. 
    - mostly single layer of inheritance 
- Composition (has a relationship)
    - seperate classes to represent seperate things in your app. each of these classes use each other in some meaningful way. 

- Final Approach 
    - Abstract base class to define interface
    - Subclass for specific version of them 
    - Patch them up at the end 

- Coupling
    - Abstract base class reduces coupling between applications
    - Allowing class to depend on interface instead of direct instance 

- Inheritence adds coupling as subclasses depend on super class 

