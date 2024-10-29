import logging
import threading


class SingletonMeta(type):
    _instances = {}

    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonLogger(metaclass=SingletonMeta):
    _logger = None

    def __init__(self):
        self._initialize_logger()

    def _initialize_logger(self):
        self._logger = logging.getLogger('myLogger')
        self._logger.setLevel(logging.DEBUG)

        # file handler with DEBUG level
        fileHandler = logging.FileHandler('mylog.log')
        fileHandler.setLevel(logging.DEBUG)

        # console handler with INFO level
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.INFO)

        # create format string for logging the log entries
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fileHandler.setFormatter(formatter)
        consoleHandler.setFormatter(formatter)

        self._logger.addHandler(fileHandler)
        self._logger.addHandler(consoleHandler)
    #getter method
    def getLoggerInstance(self):
        return self._logger


if __name__ == '__main__':
    logger = SingletonLogger().getLoggerInstance()
    #i dont like getting logger from getter method.
    logger.debug('this is debug message')
    logger.info('this is info message')
    logger.warning('this is warning message')
    logger.critical('critical message')
