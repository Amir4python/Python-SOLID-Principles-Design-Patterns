"""
Working with the Factory Method Pattern Exercise #1
In this exercise you will create a simplified, parameterized version of the Factory Method pattern for creating different types of vehicles.



The factory will receive a parameter to determine which vehicle type to create.

Your Task is to: Create a Vehicle Factory that can create different types of vehicles
 (e.g., Car, Motorcycle, Bicycle) based on the input parameter. Make sure that the input parameters are defined as an enumeration.

Create an abstract Vehicle class.

Create concrete vehicle classes, e.g., Car, Motorcycle, and Bicycle, that inherit from the Vehicle class.

Create a VehicleFactory class with a create_vehicle method that takes a parameter to determine which type of vehicle to create.

Test the VehicleFactory class to create different types of vehicles.

"""
from abc import ABC, abstractmethod
from enum import Enum


class VehicleType(Enum):
    CAR = "Car"
    MOTORCYCLE = "Motorcycle"
    BICYCLE = "Bicycle"
class Vehicle(ABC):
    @abstractmethod
    def description(self):
        pass


class Car(Vehicle):
    def description(self):
        print("This is a car")



class Motorcycle(Vehicle):
    def description(self):
        print("This is a motorcycle")


class Bicycle(Vehicle):
    def description(self):
        print("This is a bicycle")



class VehicleFactory():
    def create_vehicle(self,vehicle_type):
        if vehicle_type == 'car':
            return Car()
        elif vehicle_type == 'motorcycle':
            return Motorcycle()
        elif vehicle_type == 'bicycle':
            return Bicycle()
        else:
            raise Exception('Invalid vehicle type')

if __name__ == '__main__':
    vehicle_factory = VehicleFactory()
    vehicle = vehicle_factory.create_vehicle('car')
    vehicle.description()
    vehicle = vehicle_factory.create_vehicle('motorcycle')
    vehicle.description()
    vehicle = vehicle_factory.create_vehicle('bicycle')
    vehicle.description()