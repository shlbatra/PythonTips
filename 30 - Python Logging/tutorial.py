import logging 
from pathlib import Path

#in order of severence, by default warning and above
#using root logger by default
#logging.debug("debug")
#logging.info("info")
#logging.warning("warning")
#logging.error("error")
#logging.critical("critical")

#configure logger to file with additional info 
cwd = Path.cwd()
print(cwd)
#logs based on time - filename based on current time, run once only
#for format, look for python documentation

logging.basicConfig(level=logging.WARNING, 
                    filename="30 - Python Logging/log.log", 
                    filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

#log variable values and stack trace
x = 2

logging.warning(f"the value of x is {x}")

#exceptions

try:
    1/0
except ZeroDivisionError as e:
    logging.error("ZeroDivisionError", exc_info=True) #log exception occur
    
try:
    1/0
except ZeroDivisionError as e:
    logging.exception("ZeroDivisionError") #log exception occur


