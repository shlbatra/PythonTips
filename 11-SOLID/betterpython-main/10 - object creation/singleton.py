#use metaclass here -> type

from cmath import log10


class Singleton(type):
    _instances = {} #all instances of class mantained in dictionary
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances: #if no instance then create and return it (just 1)
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
        
class Logger(metaclass=Singleton):
    def __init__(self):
        print("Creating Logger")
    
    def log(self, msg):
        print(msg)

class CustomLogger(Logger):
    def __init__(self):
        print("Creating Custom logger")
        super().__init__()

#log1 and log2 same instance of class
log1 = Logger()
log2 = Logger()
log1.log("Hello")
log2.log("Hi")
#both objects point to same address
print(log1)
print(log2)


logger = CustomLogger()
logger2 = CustomLogger()
print(logger)
print(logger2)
logger.log("Hello")
logger2.log("Helloooo")
