#Glocal variables 
var = 9
loop=True
newVar=23

def func(x):#avoid changing values of global variables within functions
    #also global variables doesnt allow for modularity
    newVar=7
    print(newVar)
    print(var) #refer to global variable
    #To change value of loop - global variable inside function
    global loop 
    loop=70
    if x == 5:
        return newVar  
  
def otherFunc():
    newVar=5
    print(newVar) #refer local variable scoped with this function
    
func(5) #newVar printed in func as newVar local scope to func
otherFunc()
print(loop) #True -> refer to Global variable even though value changed in function
#print(newVar) # NameError: name 'newVar' is not defined -> newVar defined is local 
#scope of func - local variable of func