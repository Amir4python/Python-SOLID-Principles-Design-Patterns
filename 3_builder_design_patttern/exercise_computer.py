"""

Working with the Builder Pattern Exercise
In this exercise you will implement the Builder Design Pattern for constructing a customized computer system.

Task: Implement the Builder Design Pattern to create a custom computer system.

Instructions:

Define a class Computer with attributes: processor, memory, storage, graphics_card, operating_system, and extras.

Initialize these attributes in the __init__ method.

Create an abstract class ComputerBuilder with the following abstract methods:

add_processor, add_memory, add_storage, add_graphics_card, add_operating_system, and add_extras.

Implement a concrete class CustomComputerBuilder that inherits from ComputerBuilder.

This class should override the abstract methods and set the attributes of a Computer object.

Create a class ComputerDirector that takes a ComputerBuilder instance and
has a method build_computer that calls the add_* methods of the ComputerBuilder in the desired order.

Instantiate a CustomComputerBuilder, pass it to the ComputerDirector, and create a computer using the build_computer method.

Test your code.
"""

from abc import ABC, abstractmethod


class Computer:
    def __init__(self):
        # Initialize the attributes
        self.processor = None
        self.memory = None
        self.storage = None
        self.graphics_card = None
        self.operating_system = None
        self.extras = []


class ComputerBuilder(ABC):
    @abstractmethod
    def add_processor(self,p):
        pass

    @abstractmethod
    def add_memory(self,m):
        pass

    @abstractmethod
    def add_storage(self,s):
        pass

    @abstractmethod
    def add_graphics_card(self,c):
        pass

    @abstractmethod
    def add_operating_system(self,o):
        pass

    @abstractmethod
    def add_extras(self,e):
        pass


class CustomComputerBuilder(ComputerBuilder):
    def __init__(self):
        # Initialize a Computer object
        self.computer = Computer()

    def add_processor(self,p):
        self.computer.processor=p

    def add_memory(self,m):
        self.computer.memory=m

    def add_storage(self,s):
        self.computer.storage=s


    def add_graphics_card(self,c):
        self.computer.graphics_card=c

    def add_operating_system(self,o):
        self.computer.operating_system=o


    def add_extras(self,e):
        self.computer.extras=e

        # Override abstract methods and set Computer attributes


class ComputerDirector:
    def __init__(self, builder):
        self.computer=builder

    # Initialize the builder instance

    def build_computer(self, specs):
        self.computer.add_processor(specs['processor'])
        self.computer.add_memory(specs['memory'])
        self.computer.add_storage(specs['storage'])
        self.computer.add_graphics_card(specs['graphics_card'])
        self.computer.add_operating_system(specs['operating_system'])
        self.computer.add_extras(specs['extras'])


# Call the add_* methods of the builder with the specs
if __name__ == '__main__':

    # Helper function to test the computer building process
    def test_computer_building(specs, expected_output):
        builder = CustomComputerBuilder()
        director = ComputerDirector(builder)
        director.build_computer(specs)
        computer = builder.computer
        assert computer.__dict__ == expected_output, f"Expected {expected_output}, but got {computer.__dict__}"


    # Test cases
    test_specs = {
        'processor': 'Intel Core i5',
        'memory': '8GB',
        'storage': '512GB SSD',
        'graphics_card': 'Integrated',
        'operating_system': 'Windows 11',
        'extras': ['Wi-Fi']
    }

    expected_output = {
        'processor': 'Intel Core i5',
        'memory': '8GB',
        'storage': '512GB SSD',
        'graphics_card': 'Integrated',
        'operating_system': 'Windows 11',
        'extras': ['Wi-Fi']
    }

    test_computer_building(test_specs, expected_output)

    print("All tests passed!")

"""
We define the Computer class, which represents a computer system with the following attributes: processor, memory, storage, graphics_card, operating_system, and extras. The constructor initializes all attributes to None.

We create the abstract ComputerBuilder class that inherits from the ABC (Abstract Base Class) and has abstract methods for each component that will be added to the computer: add_processor, add_memory, add_storage, add_graphics_card, add_operating_system, and add_extras. Each method takes a parameter that represents the value to be set for that specific attribute.

We implement the concrete CustomComputerBuilder class that inherits from the abstract ComputerBuilder class. In its constructor, it initializes a Computer object. This class overrides all abstract methods defined in the ComputerBuilder class, and each method sets the corresponding attribute of the Computer object. For example, the add_processor method sets the processor attribute of the Computer object.

We create the ComputerDirector class that takes an instance of a ComputerBuilder in its constructor. The director class has a build_computer method, which receives a dictionary containing the specifications for the computer. This method calls the add_* methods of the builder instance with the values provided in the specifications.

To test the solution, we instantiate a CustomComputerBuilder object and pass it to the ComputerDirector. We define a dictionary of specifications and pass it to the build_computer method of the director. The director builds the computer by calling the appropriate add_* methods of the builder with the values from the specifications.

After the build_computer method is executed, the CustomComputerBuilder instance will have a fully constructed Computer object with the specified attributes. We can access the computer object through the computer attribute of the builder and print its attributes using the __dict__ property.

In summary, the solution implements the Builder Design Pattern to create a customizable computer system. The ComputerBuilder abstract class enforces a consistent interface for building computer systems, while the CustomComputerBuilder class provides a concrete implementation for constructing a computer with custom specifications.
 The ComputerDirector class controls the building process by invoking the appropriate methods of the ComputerBuilder instance based on the provided specifications.
"""
