"""
# Excercise1:
    1. Create a Singleton Implementation which will generate a sequence of numbers to the callers.
        a. The idea is that there is only a single number/sequence generator and all the numbers follow a perfect sequence.
        b. So when we do a call to the generator using something like getNextNumber()
            we should get the next number in the sequence no matter how we obtained the generator.

  #Exercise2:
    1. Make the Singleton implementation thread safe. from exercise1
       a. how do you test it.( THIS FILE )
       b. how do know it is properly thread safe


"""
import threading


class SequenceGen:
    _instance = None
    _currentNumber = 0
    _lock = threading.Lock()

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super(SequenceGen, cls).__new__(cls)
        return cls._instance

    def getNextNumber(self):
        with self._lock:
            self._currentNumber += 1
            return self._currentNumber


if __name__ == '__main__':
    seq1 = SequenceGen()
    print(seq1.getNextNumber())
    print(seq1.getNextNumber())
    print(seq1.getNextNumber())
    print(seq1.getNextNumber())

    seq2 = SequenceGen()
    print(seq1.getNextNumber())
    print(seq1.getNextNumber())
    print(seq1.getNextNumber())
    print(seq1.getNextNumber())

    print(seq1 is seq2)