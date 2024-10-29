
from abc import ABC,abstractmethod
class MyInterface(ABC):
    @abstractmethod
    def my_method(self):
        pass


class MyClass(MyInterface):
    def my_method(self):
        print("Hello, I am a method of MyClass")

class AnotherClass(MyInterface):
    def my_method(self):
        print("Hello, I am a method of AnotherClass")

if __name__=="__main__":
    obj=MyClass()
    obj.my_method()
    obj=AnotherClass()
    obj.my_method()