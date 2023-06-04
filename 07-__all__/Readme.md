- Anything included in __all__ will be imported in main , when using from module import *
- List of attributes and methods to be made available when user uses import * in main function
- You can also use it to propograte code from subdirectory to directory level.
- Ex. you define __all__ as a list ->
    __all__ = [
        'public_function'
    ] 
- Ex. 
from .module_1 import *
__all__ = module_1.__all__

- alternate way where we define entire path 
from package.sub_package_1.module_1 import module_1_function