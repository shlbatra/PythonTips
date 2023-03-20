import logging 

#Custom Logs - seperate log file with information

logging.basicConfig(level=logging.INFO, 
                    filename="30 - Python Logging/log.log", 
                    filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)  #one logger for each python module, name represent python module

#handler set up to configure logger
handler = logging.FileHandler("30 - Python Logging/log1.log")
#set formatter and configure handler to formatter and add to logger
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("Test the custom loggers")