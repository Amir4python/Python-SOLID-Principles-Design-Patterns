"""
Working with Class Encapsulation
Create a class named Fraction that represents a simple fraction with a numerator and a denominator and includes methods to perform basic arithmetic operations.

Class "Fraction":

Properties:

numerator (an integer representing the numerator of the fraction)

denominator (an integer representing the denominator of the fraction)

Methods:

__init__(self, numerator, denominator): Initializes the fraction with the given numerator and denominator. The denominator must be non-zero.

add(self, other): Adds the current fraction and the other fraction and returns the result as a new Fraction object.

subtract(self, other): Subtracts the other fraction from the current fraction and returns the result as a new Fraction object.

multiply(self, other): Multiplies the current fraction and the other fraction and returns the result as a new Fraction object.

divide(self, other): Divides the current fraction by the other fraction and returns the result as a new Fraction object. The other fraction must have a non-zero numerator.

simplify(self): Simplifies the current fraction to the simplest form and returns a new Fraction object with the simplified numerator and denominator.

__str__(self): Returns the string representation of the fraction in the format "numerator/denominator".
"""

import math


class Fraction:
    def __init__(self, numerator, denominator):
        # Initialize the numerator and denominator properties
        # Check that the denominator is non-zero
        self.numerator = numerator
        if denominator == 0:
            raise ValueError('Denominator cannot be zero.')
        self.denominator = denominator

    def add(self, other):
        # Add the current fraction and the other fraction
        # Return the result as a new Fraction object
        num = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        dem = self.denominator * other.denominator
        return Fraction(num, dem)

    def subtract(self, other):
        # Subtract the other fraction from the current fraction
        # Return the result as a new Fraction object
        num = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        dem = self.denominator * other.denominator
        return Fraction(num, dem)

    def multiply(self, other):
        # Multiply the current fraction and the other fraction
        # Return the result as a new Fraction object
        num = self.numerator * other.numerator
        dem = self.denominator * other.denominator
        return Fraction(num, dem)

    def divide(self, other):
        # Divide the current fraction by the other fraction
        # Check that the other fraction has a non-zero numerator
        # Return the result as a new Fraction object
        if other.numerator == 0:
            raise ValueError("Cannot divide by a fraction with a zero numerator.")

        num = self.numerator * other.denominator
        dem = other.numerator * self.denominator
        return Fraction(num, dem)

    def simplify(self):
        # Simplify the current fraction to its simplest form
        # Return a new Fraction object with the simplified numerator and denominator
        common_factor = math.gcd(self.numerator, self.denominator)
        simplified_num = self.numerator // common_factor
        simplified_dem = self.denominator // common_factor
        return Fraction(simplified_num, simplified_dem)

    def __str__(self):
        # Return the string representation of the fraction in the format "numerator/denominator"
        return f"{self.numerator}/{self.denominator}"

if __name__=='__main__':

    # Test your implementation
    fraction1 = Fraction(1, 4)
    fraction2 = Fraction(1, 2)

    fraction3 = fraction1.add(fraction2)
    print(fraction3)  # Should output "6/8"

    fraction4 = fraction3.simplify()
    print(fraction4)  # Should output "3/4"
