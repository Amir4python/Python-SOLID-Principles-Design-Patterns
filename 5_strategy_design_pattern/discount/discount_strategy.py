"""
Working with the Strategy Pattern Exercise #1
Implement a simple shopping cart with different discount strategies using the Strategy Design Pattern in Python as follows:



Create an interface called DiscountStrategy with a single method apply_discount that takes a float total as an argument and returns a float.

Implement three different discount strategies that inherit from DiscountStrategy:

a. NoDiscount: This strategy does not apply any discount and returns the original total.

b. PercentageDiscount: This strategy applies a percentage discount to the total.
 It should take a float percentage as an argument during initialization.

c. FixedAmountDiscount: This strategy applies a fixed amount discount to the total.
 It should take a float fixed_amount as an argument during initialization.

Implement a ShoppingCart class with the following methods:

a. __init__(self, discount_strategy: DiscountStrategy): Initializes a new shopping cart with a given discount strategy.

b. add_item(self, item: str, price: float): Adds an item with a specified price to the shopping cart.

c. remove_item(self, item: str): Removes an item from the shopping cart.

d. get_total(self) -> float: Calculates the total price of the items in the cart before applying the discount.

e. get_total_after_discount(self) -> float: Calculates the total price of the items in the cart after applying
the discount using the specified discount strategy.

Test your implementation with different discount strategies and a few items in the shopping cart.
For example, you can create a shopping cart with a 10% percentage discount, add a few items, and then calculate the total after applying the discount.
"""

from abc import ABC, abstractmethod

# Step 1: Create the DiscountStrategy interface
class DiscountStrategy(ABC):

    @abstractmethod
    def apply_discount(self, total: float) -> float:
        pass

# Step 2: Implement the discount strategies
# TODO: Implement NoDiscount, PercentageDiscount, and FixedAmountDiscount classes

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage=percentage
    def apply_discount(self, total):
        return total*(1-self.percentage/100)


class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, fixedAmount):
        self.fixedAmount=fixedAmount
    def apply_discount(self, total):
        return total-self.fixedAmount

class NoDiscount(DiscountStrategy):
    def __init__(self):
        pass
    def apply_discount(self, total):
        return total

# Step 3: Implement the ShoppingCart class
class ShoppingCart:

    def __init__(self, discount_strategy):
        # TODO: Initialize the shopping cart with the given discount_strategy and an empty items dictionary
        self._discount=discount_strategy
        self.items={}

    def add_item(self, item: str, price: float):
        # TODO: Add the item with its price to the items dictionary
        self.items[item]=price

    def remove_item(self, item: str):
        # TODO: Remove the item from the items dictionary if it exists
        if item in self.items:
            del self.items[item]

    def get_total(self) -> float:
        # TODO: Calculate and return the total price of the items in the cart
        total=0
        for item in self.items:
            total+=self.items[item]
        return total

    def get_total_after_discount(self) -> float:
        # TODO: Calculate and return the total price of the items in the cart after applying the discount
        return self._discount.apply_discount(self.get_total())

# Step 4: Test your implementation
if __name__ == "__main__":
    # TODO: Create a shopping cart with a discount strategy
    cart = ShoppingCart(PercentageDiscount(10))

    # TODO: Add a few items
    cart.add_item("Item 1", 10.0)
    cart.add_item("Item 2", 20.0)
    cart.add_item("Item 3", 30.0)

    # TODO: Calculate and print the total price before discount
    print("Total before discount:", cart.get_total())

    # TODO: Calculate and print the total price after applying the discount
    print("Total after discount:", cart.get_total_after_discount())
