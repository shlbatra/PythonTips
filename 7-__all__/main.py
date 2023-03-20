# Anything included in __all__ will be imported in main , when using from module import *
#Ex. 
__all__ = [
    'public_function'
] 
#list of attributes and methods to be made available when user uses import * in main function
# To propograte code from subdirectory to directory level.
#Ex. 
from .module_1 import *
__all__ = module_1.__all__

#Ex. imports 
- use __all__ then can do 
from package import *  
#dundar method defines what to be included else everything will be included

# alternate way where we define entire path 
from package.sub_package_1.module_1 import module_1_function