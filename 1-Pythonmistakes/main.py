# name shadowing
# name used is a built in name or already defined another variable in score
database = {
    1:"hello",
    2:"world"
}

def get_database_record(id): #already have existing id() function, avoid names such as max and min
    #id(1)
    return database.get(id)

get_database_record(1) #overridden built in id() with id=1

#another issue when use name from global scope
def get_database_record(id, database):
    #which database - local or global database 
    return database.get(id)

############################################################
# Using mutable object as default parameter for optional argument 
#mutable object ex. list, dict, sets
def mutable_parameter(lst=[]): # optional parameter mutable called list 
    lst.append(1)
    lst.append(2)
    return lst 

print(mutable_parameter()) 
print(mutable_parameter())
print(mutable_parameter()) #get unexpected output as change it, On every call, list not recreated but created only once 
#as default value works accordingly 

#Better way to code it 
def mutable_parameter(lst=None): # optional parameter mutable called list 
    if lst is None:
        lst=[]
    lst.append(1)
    lst.append(2)
    return lst 

print(mutable_parameter()) 
print(mutable_parameter())
print(mutable_parameter()) #List recreated with every function call

print("\n\n\n")
############################################################
# modify iterable object whle iterating through 

lst = [1,2,3,4,5,6,7,8,9,10]

for i,val in enumerate(lst): #while iteraing changing list at the same time
    print(i,lst)
    if i%2 == 0:#index div by 2 then pop this index from list
        lst.pop(i)
        
print(lst)#[2, 3, 5, 6, 8, 9] -> weird result because modifying iterable object while looping through it 
#expected result -> [1,3,5,7,9]
'''
for i in range(len(lst)): #while iteraing changing list at the same time so get error as list len changes
    if i%2 == 0:#index div by 2 then pop this index from list
        lst.pop(i)
'''
# store modification somewhere, iterate list entirely and make specific modifications

print("\n\n\n")
############################################################
# name clashing -> name python file same as built in module or thrid party module you have installed

print("\n\n\n")
############################################################
# naked except -> except block accepts any exception, dont know why I crashed 
# as hard to debig code. Handle each individual exception 

try:
    file = open("tim.txt","r")
    x=1/0
#except: #dont know which reason failed program -> unable to find the reason
except ZeroDivisionError as e: #e provides the exception string message
    print(e)
    print("I tried to divide by zero")
    print("I crashed")    
except FileNotFoundError as e:
    print(e)
    print("I couldnot find the file")
    print("i crashed")
    
    
print("\n\n\n")
############################################################
# using wrong datastructure -> operations inefficient if use wrong dS -> time complexity for fast opn
    

from collections import deque #double ended queue -> remove from begin or end in o(1)
#3 core datastructures 
#list=[] -> ordered collection and care abt frequency , lookup is O(N)
#set->set() -> care abot presence of element in set or not lookup O(1)
#dict={} -> Store key value pair and access element really fast , lookup O(1)

[1,2,3,4,5,6,7,8,9,10] #list perfom any opn 
#.pop() - o(1) (remove last item)
#.pop(0) - o(n) (remove first item) -> use queue or deque

############################################################
# global variables and using global keyword 

global_var=10 #global variable

def bar(x):
    global global_var #access name treat global var on top
    print(global_var)
    global_var=x
    print(global_var)
    
def foo(x):
    print(global_var) #UnboundLocalError: local variable 'global_var' referenced before assignment
    #defined local var inside this function below so reference global_var in local here that is not assigned yet
    global_var=x
    print(global_var)
    
print(global_var)
bar(20) #this function executes fine
foo(10)
print(global_var)


