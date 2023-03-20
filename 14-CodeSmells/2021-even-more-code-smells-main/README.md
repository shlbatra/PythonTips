## Even More Code Smells

- Point Sales System that handles orders and processes payments 
- Code smells are not bugs but hint some problem in code or design problems. Overall program will work fine. 
- Issue when mantain or extend code in future. 
- Code Smell -> verb/subject -> method that gets a single object, dont ask object to do computations but call method that does computation for you 
- Backpeddling -> call method and not provide all data it needs - method look around for implementation details it doesnt need - principle of least knowledge ->try design seperate units need limited knowledge of other units, avoid calls self.obj1, self.obj2 and so on