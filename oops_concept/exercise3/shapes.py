"""
Working with Abstract Classes
Create an abstract base class named Shape and two derived classes named Rectangle and Circle to represent different shapes using abstract classes.



Abstract class "Shape":

Properties:

color (a string representing the shape's color)

Methods:

__init__(self, color): Initializes the shape with the given color.

area(self): An abstract method that calculates and returns the area of the shape.

perimeter(self): An abstract method that calculates and returns the perimeter of the shape.

Class "Rectangle" (inherits from Shape):

Properties:

length (a float representing the length of the rectangle)

width (a float representing the width of the rectangle)

Methods:

__init__(self, color, length, width): Initializes the rectangle with the given color, length, and width.

area(self): Calculates and returns the area of the rectangle.

perimeter(self): Calculates and returns the perimeter of the rectangle.

Class "Circle" (inherits from Shape):

Properties:

radius (a float representing the radius of the circle)

Methods:

__init__(self, color, radius): Initializes the circle with the given color and radius.

area(self): Calculates and returns the area of the circle.

perimeter(self): Calculates and returns the perimeter of the circle.


"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    def __init__(self, color):
        # Initialize the color property
        self.color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, color, length, width):
        # Call the parent constructor and initialize the length and width properties
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        # Calculate and return the area of the rectangle
        return self.length * self.width

    def perimeter(self):
        # Calculate and return the perimeter of the rectangle
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, color, radius):
        # Call the parent constructor and initialize the radius property
        super().__init__(color)
        self.radius = radius

    def area(self):
        # Calculate and return the area of the circle
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        # Calculate and return the perimeter of the circle
        return math.pi * self.radius * 2

if __name__=='__main__':
    # Test your implementation
    rectangle1 = Rectangle("red", 4, 5)
    print(rectangle1.area())  # Should output 20
    print(rectangle1.perimeter())  # Should output 18

    circle1 = Circle("blue", 3)
    print(circle1.area())  # Should output approximately 28.274333882308138
    print(circle1.perimeter())  # Should output approximately 18.84955592153876
