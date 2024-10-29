"""
# Excercise1:
    1. Create a Singleton Implementation which will generate a sequence of numbers to the callers.
        a. The idea is that there is only a single number/sequence generator and all the numbers follow a perfect sequence.
        b. So when we do a call to the generator using something like getNextNumber()
            we should get the next number in the sequence no matter how we obtained the generator.

  #Exercise2:
    1. Make the Singleton implementation thread safe. from exercise1
       a. how do you test it.
       b. how do know it is properly thread safe( THIS FILE )
"""
import threading


class SequenceGen:
    _instance = None
    _currentNumber = 0
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(SequenceGen, cls).__new__(cls)
            return cls._instance

    def getNextNumber(self):
        with self._lock:
            self._currentNumber += 1
            return self._currentNumber


def test_singleton_thread_safe():
    seq1 = SequenceGen()
    print(f'Number: {seq1.getNextNumber()=}' )
if __name__ == '__main__':

    threads=[]
    for i in range(5): #five threads
        thread=threading.Thread(target=test_singleton_thread_safe)
        threads.append(thread)
        thread.start()
    #wait for all threads to finish
    for thread in threads:
        thread.join()

