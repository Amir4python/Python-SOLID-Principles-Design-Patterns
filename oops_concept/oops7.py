
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

class OtherClass():
    def some_method(self):
        print("Hello, I am a method of OtherClass With NO INTERFACE")

def process_MyInterface_Object(obj:MyInterface):
    obj.my_method()
    print(f'{obj.__class__.__name__} invokes my_method()')

if __name__=="__main__":
    obj1=MyClass()

    obj2=AnotherClass()
    obj3=OtherClass()
    for obj in [obj1,obj2,obj3]:
        process_MyInterface_Object(obj)