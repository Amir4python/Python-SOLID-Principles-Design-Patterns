import logging
import threading



class SingletonLogger:
    _instance=None
    _lock=threading.Lock()

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance=cls()
                    cls._instance._initialize_logger()
        return cls._instance

    def _initialize_logger(self):

        self.logger = logging.getLogger('myLogger')
        self.logger.setLevel(logging.DEBUG)

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

        self.logger.addHandler(fileHandler)
        self.logger.addHandler(consoleHandler)





if __name__ == '__main__':
    logger=SingletonLogger.getInstance().logger
    """Dont like the syntax on line 45. """
    logger.debug('this is debug message')
    logger.info('this is info message')
    logger.warning('this is warning message')
    logger.critical('critical message')
