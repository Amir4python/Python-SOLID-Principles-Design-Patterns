import logging

logger=logging.getLogger('myLogger')
logger.setLevel(logging.DEBUG)


#file handler with DEBUG level
fileHandler=logging.FileHandler('mylog.log')
fileHandler.setLevel(logging.DEBUG)

#console handler with INFO level
consoleHandler=logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)

#create format string for logging the log entries
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fileHandler.setFormatter(formatter)
consoleHandler.setFormatter(formatter)


logger.addHandler(fileHandler)
logger.addHandler(consoleHandler)


if __name__ == '__main__':
    logger.debug('this is debug message')
    logger.info('this is info message')
    logger.warning('this is warning message')
    logger.critical('critical message')
