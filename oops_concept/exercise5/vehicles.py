"""
Working with Interface Contracts Exercise#1
Create an abstract base class Vehicle and three derived classes, Car, Bicycle, and Boat. Implement the abstract method move in each derived class. Then, create a function start_vehicle that takes a Vehicle object and calls its move method.



Create an abstract base class Vehicle:

Import the ABC (Abstract Base Class) and abstractmethod from the abc module.

Make the Vehicle class inherit from ABC.

Define an abstract method: move.

Create a class Car that inherits from Vehicle:

Implement the move method for the Car class, returning the string "The car is driving."

Create a class Bicycle that inherits from Vehicle:

Implement the move method for the Bicycle class, returning the string "The bicycle is pedaling."

Create a class Boat that inherits from Vehicle:

Implement the move method for the Boat class, returning the string "The boat is sailing."

Create a function start_vehicle(vehicle):

The function should take a Vehicle object as its argument.

The function should call the move method of the given vehicle object and print the returned string.
"""
#THIS IS ABSTRACT CLASS

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    # Implement the move method for the Car class
    def move(self):
        return "The car is driving."

class Bicycle(Vehicle):
    # Implement the move method for the Bicycle class
    def move(self):
        return "The bicycle is pedaling."

class Boat(Vehicle):
    # Implement the move method for the Boat class
    def move(self):
        return "The boat is sailing."

def start_vehicle(vehicle:Vehicle):
    # Call the move method of the given vehicle object and print the returned string
    print(vehicle.move())
if __name__ == '__main__':

    # Test your implementation
    car = Car()
    bicycle = Bicycle()
    boat = Boat()

    start_vehicle(car)
    start_vehicle(bicycle)
    start_vehicle(boat)
