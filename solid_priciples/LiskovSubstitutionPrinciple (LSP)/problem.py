from abc import ABC, abstractmethod
class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

class Penguin(Bird):
    def fly(self):
        print("I can fly")
