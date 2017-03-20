import logging
import logging.handlers

#logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger('mylogger')

formatter = logging.Formatter('[%(asctime)s: %(levelname)s/%(module)s] %(message)s')

fileHandler = logging.FileHandler('./testson.log')

fileHandler.setFormatter(formatter)

logger.addHandler(fileHandler)

logger.info('======================')
logger.debug("d m sg")
logger.info("info log")
logger.warning("warnnn")
logger.error("errorr")
logger.critical("high level error")

'''
log_file = './sontest.log'
log_level = 'DEBUG'
log_format = '[%(asctime)s: %(levelname)s/%(module)s] %(message)s'
logging.basicConfig(stream=open(log_file,'a'),format=log_format,level=logging.DEBUG)

logging.debug("d m sg")
logging.info("info log")
logging.warning("warnnn")
logging.error("errorr")
logging.critical("high level error")
'''



#logging.info("Hi")
#logging.warning("warn")