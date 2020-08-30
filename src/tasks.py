from logger_manager import logger
import time

def hello(data):
    logger.info('Hello '+ str(data['msg']))
    time.sleep(2)


