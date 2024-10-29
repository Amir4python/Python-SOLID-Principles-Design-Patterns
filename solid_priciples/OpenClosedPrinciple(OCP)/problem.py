class AreaCalculator:
    @staticmethod
    def area(shape):
        if isinstance(shape, Square):
            return shape.length * shape.length
        elif isinstance(shape, Rectangle):
            return shape.length * shape.width
        elif isinstance(shape, Circle):
            return 3.14 * shape.radius * shape.radius
        else:
            return 0
class Square:
    def __init__(self, length):
        self.length = length

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Circle:
    def __init__(self, radius):
        self.radius = radius

if __name__=='__main__':
    shapes = [Square(5), Rectangle(10, 5), Circle(7)]
    for shape in shapes:
        print(shape.__class__.__name__,AreaCalculator.area(shape))