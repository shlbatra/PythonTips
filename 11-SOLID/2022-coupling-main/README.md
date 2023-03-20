# 5 Tips To Achieve Low Coupling In Your Python Code

In this video I share 5 tips to help you write code that has low coupling. I'll show you several examples and also share a story of a technique I used several times in the past that has really help me reduce coupling and solve more complex software design problems.

- detect coupling before fixing it
- degree of interdependence between software modules
- measure of how closely connected two modules are
- strength of relationship between modules
- Prefer LOW coupling for maintaining code 

1. Avoid deep inheritance relationships
2. Seperate creating resources from using them 
3. Introduce Abstractions - ABC or protocols, 
    - reduce depedencies of code on other parts of code
    - easy to use, seperate and test them 
    - for any third party lib, use 2-3 methods mostly so use protocol, or type or callable - remove dependency 
    - testing easy as create a class that implements protocol. not SMTP directly
    - rely on structural typing so thord party lib function needs to have same signature without any inheritance relationships needed
    - lead to 
        - depedency injection
            - provide object to another class
        - depedency inversion 
4. Avoid inappropriate intimacy
    - Method gets lot more data than it needs,remove extra data and it simplifies the method
    - location changes than method changes, instead use geolocation directly 
5. Introduce Intermediate DataStructure
    - if code already too messy and coupled
    - use it as a seperation layer
    - ex. simulation of natural language to accident simulation
        a. Natural language to formal representation
        b. Formal representation to 3D simulation
            a. Car Movements into trajectories
            b. set of trajectories and collision pts into actual collisions and precise car motions
    - simplify things or throw info so that lower level can work with it and doesnt become coupled on how everything works at higher level 

