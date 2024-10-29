from abc import ABC,abstractmethod

class Shape(ABC):
    def __init__(self,color):
        self.color=color

    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

    def description(self):
        print(f'{self.__class__.__name__} has color {self.color} and area {self.area()} and perimeter {self.perimeter()}')

class Rectangle(Shape):
    def __init__(self,color,length,width):
        super().__init__(color)
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)

class Circle(Shape):
    def __init__(self,color,radius):
        super().__init__(color)
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    def perimeter(self):
        return 2*3.14*self.radius

def process_shape_info(obj:Shape):
    obj.description()


if __name__=='__main__':
    r=Rectangle('blue',10,20)
    c=Circle('red',5)
    process_shape_info(r)
    process_shape_info(c)