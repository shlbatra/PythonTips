#1.Use same args for instance or function calls provided via dictionary

from tkinter import *
from constants import btn_layout

root=Tk()

btn1= Button(root,**btn_layout)  # Button(root,bg='BLACK')
btn2= Button(root,**btn_layout)  # Button(root,bg='BLACK')
btn3= Button(root,**btn_layout)

#root.mainloop()

#2 harder to test specific area of code. 

class Employee:
    def __init__(self,name):
        if len(name) <= 10: #validate name length here
            self.name=name
        else:
            raise Exception('Name longer than 10 chars')
        
    @property
    def last_char_name(self):
        return self.name[-1]
    
    def __repr__(self):
        return f"Employee(name={self.name})"

#debug using python shell for specific things. 
'''
import main 
from main import Employee
e1=Employee('Jim')
'''

#3. check instantiation works with dundar method - __repr__ methods, allows to debig and test specific area of code
'''
Employee(name='Jim')
create repr to get better representation
'''

#4. Example with decision making -> lots of if else statements , painful as extend if else statement for new kind 
#of decision, instead use dictionary

class Animal:
    
    supported_animals= {
            'dog' : 'BARK',
            'cat' : 'MEOW',
            'duck' : 'QUACK'
        }
    
    def __init__(self,a:str):
        self.a=a
        
    def speak(self):
        if self.a.lower()=='dog':
            print('BARK')
        elif self.a.lower()=='cat':
            print('MEOW')
        elif self.a.lower()=='duck':
            print('QUACK')
            
    def speak_optimized(self):
        print(Animal.supported_animals.get(self.a,'UNKNOWN!'))
        
animal1 = Animal('dog')
animal1.speak()
animal1.speak_optimized()
animal2 = Animal('bird')
animal2.speak() #No output as no defualt else option provided 
animal2.speak_optimized()

#5 Avoid using global statement in Python -> less readable and interpretable python files, it will make your functions 
#less dyanmic, Instead use parameter to functions

p1_age=20

def increase_p1_age():
    global p1_age #use global variable from global scope and overwrite its value from local scope
    p1_age+=1
    
increase_p1_age()
print(p1_age)

#increase age of any person 
def increase_age(p_age):
    return p_age+1

p1_age=increase_age(p1_age) # p1_age global variable
print(p1_age)
