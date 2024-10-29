import threading

class ThreadSafeSingleton:
    _instance = None #class level variable to store the single instance
    _lock = threading.Lock()  # class level lock to ensure thread safety

    def __new__(cls): #override the __new__ method to create single instance of the class

        with cls._lock: #acquire the lock
                if not cls._instance:  # check if the instance is already created
                    cls._instance = super().__new__(cls) # create new instance of the class
        return cls._instance # return the single instance

if __name__ == '__main__':
    s1=ThreadSafeSingleton()
    s2=ThreadSafeSingleton()
    print(s1 is s2)