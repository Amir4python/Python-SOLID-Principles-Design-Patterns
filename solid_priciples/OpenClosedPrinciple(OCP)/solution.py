from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


if __name__ == '__main__':
    shapes = [Square(5), Rectangle(10, 5), Circle(7)]
    for shape in shapes:
        print(shape.__class__.__name__, shape.area())
