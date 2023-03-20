# try operation and not know if it will work or not based on what user might be doing
#Ex is validating a form 

text=input("Username: ") #validate username is only numbers

try:
    number=int(text)
    print(number)
except:
    print("Invalid username")