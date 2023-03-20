- help standardize process
- ex. order flow standard for when cust places order. steps diff for digital vs physical prod.
- cust support ticket handling. process similar but steps diff based on complexity for ticket 

Abstract Class      <-     ConcreteClass
+templateMethod()
#method1()                  #method1()
#method2()                  #method2()


this.method1() 
this.method2()

- Bridge pattern -> 2 seperate things that vary, ex. exchanges diff and diff trading bots
- add extra exchange or bots without doing anyside of bridge.
- mechanism to have 2 diff class hierarchies / variations that can change independetly from each other. ex. add extra exchange without changing trading bot and vice versa


Abstraction             <-         Implementor
-impl: Implementor              +implementation()
+function()
    |                                   |
Refined avstraction          Concreteimplementor
+refinedFunction()              + implementation()


this.impl.implementation()