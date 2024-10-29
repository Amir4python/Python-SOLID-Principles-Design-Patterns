"""
Working with Interface Contracts Exercise#2
Create an abstract base class ElectronicDevice and three derived classes, Smartphone, Laptop, and Smartwatch. Implement the abstract method battery_life in each derived class. Then, create a function display_battery_life that takes an ElectronicDevice object and calls its battery_life method.



Create an abstract base class ElectronicDevice:

Import the ABC (Abstract Base Class) and abstractmethod from the abc module.

Make the ElectronicDevice class inherit from ABC.

Define an abstract method: battery_life.

Create a class Smartphone that inherits from ElectronicDevice:

Implement the battery_life method for the Smartphone class, returning the string "Smartphone battery life: 10 hours."

Create a class Laptop that inherits from ElectronicDevice:

Implement the battery_life method for the Laptop class, returning the string "Laptop battery life: 5 hours."

Create a class Smartwatch that inherits from ElectronicDevice:

Implement the battery_life method for the Smartwatch class, returning the string "Smartwatch battery life: 24 hours."

Create a function display_battery_life(device):

The function should take an ElectronicDevice object as its argument.

The function should call the battery_life method of the given device object and print the returned string.
"""

from abc import ABC, abstractmethod

class ElectronicDevice(ABC):

    @abstractmethod
    def battery_life(self):
        pass

class Smartphone(ElectronicDevice):
    # Implement the battery_life method for the Smartphone class
    def battery_life(self):
        return "Smartphone battery life: 10 hours."

class Laptop(ElectronicDevice):
    # Implement the battery_life method for the Laptop class
    def battery_life(self):
        return "Laptop battery life: 5 hours."

class Smartwatch(ElectronicDevice):
    # Implement the battery_life method for the Smartwatch class
    def battery_life(self):
       return "Smartwatch battery life: 24 hours."
def display_battery_life(device):
    # Call the battery_life method of the given device object and print the returned string
    print(device.battery_life())
# Test your implementation

if __name__=="__main__":

    smartphone = Smartphone()
    laptop = Laptop()
    smartwatch = Smartwatch()

    display_battery_life(smartphone)
    display_battery_life(laptop)
    display_battery_life(smartwatch)
