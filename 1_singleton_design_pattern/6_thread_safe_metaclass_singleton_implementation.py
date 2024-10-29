import threading
import time


class ThradSafeSingleton(type):
    _instances = {}

    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            # if the class is not in the dictionary, create a new instance
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        #return the exisiting instance or newly created instance
        return cls._instances[cls]

class Singleton(metaclass=ThradSafeSingleton):
    pass

def get_singleton_instance():
    s=Singleton()
    print(s)
    # time.sleep(2)


threads=[] #store threads

for i in range(10):
    t=threading.Thread(target=get_singleton_instance())
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()


if __name__ == '__main__':
    get_singleton_instance()
