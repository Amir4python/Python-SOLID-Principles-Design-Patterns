import logging
import threading
from abc import ABC, abstractmethod, ABCMeta


class SingletonMeta(metaclass=ABCMeta):
    _instances = {}

    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class BaseLogger(SingletonMeta):
    @abstractmethod
    def debug(cls, message):
        pass

    @abstractmethod
    def critical(cls, message):
        pass

    @abstractmethod
    def error(cls, message):
        pass

    @abstractmethod
    def warning(cls, message):
        pass

    @abstractmethod
    def info(cls, message):
        pass


class SingletonLogger( BaseLogger):


    def __init__(self):

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

    def debug(self,message):
        self._logger.debug(message)

    def info(self,message):
        self._logger.info(message)

    def warning(self,message):
        self._logger.warning(message)

    def critical(self,message):
        self._logger.critical(message)

    def error(self,message):
        self._logger.error(message)




if __name__ == '__main__':
    logger = SingletonLogger()
    #i dont like getting logger from getter method. 
    logger.debug('this is debug message')
    logger.info('this is info message')
    logger.warning('this is warning message')
    logger.critical('critical message')
