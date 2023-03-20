1. Modules and packages
Module is individual python file
Package is directory containing python files
    - To make a folder a package, you need to include __init__.py file  
    - when import package, the code in __init__.py is run one time. Add initialization code or import packages reqd as well
    - from .forces import Forces #Called relative import, importing forces from current directory
2. 1 Class = 1 File, 
for object oriented style programming
naming file - snake case (all lower case, can use _)
naming class - pascal (capital on first word , no space and _)
3. Group related functionality together, think logically what things make sense together that group together
4 directories -> 
utils 
tests
docs
api
4. Seperate utility and helper functions -> in single file or folder
ex. convert date to string, distance between 2 points. 
Create utils package or module. 
5. Organize import statements -> sort inputs -> import third party library first, then built in imports then local files and relative imports and alphabet order imports (optional)
