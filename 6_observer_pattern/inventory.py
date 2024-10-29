"""

Implement a Product Inventory System with Observer Design Pattern:

Create a product inventory system that uses the Observer Design Pattern to notify registered store managers whenever
 the stock level of a product goes below a certain threshold. Implement the following components:

Define the Observer and Subject interfaces:

The Observer interface should have a single method update which takes two arguments: the product name and the new stock level.

The Subject interface should have three methods: attach, detach, and notify.

Create the StoreManager class that implements the Observer interface:

The StoreManager class should have a name attribute to identify the manager.

The update method should display a message indicating that the stock level for the product
 has gone below the threshold and the manager has been notified.

Create the Inventory class that implements the Subject interface:

The Inventory class should maintain a dictionary of products, where the keys are product names and the values are stock levels.

The attach, detach, and notify methods should be implemented to manage the observers (store managers) and notify them of stock level changes.

Implement a method update_stock that takes two arguments: the product name and the new stock level.
 This method should update the stock level for the product and call notify if the stock level is below the specified threshold.

Test the implementation by performing the following tasks:

Create an Inventory instance and add a few products with their stock levels.

Create a few StoreManager instances and attach them to the inventory.

Update the stock levels of the products in the inventory and ensure the store managers get
 notified when the stock level goes below the threshold.

Detach a store manager and update the stock levels again to verify that the detached manager no longer receives notification

"""

from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, product_name: str, new_stock: int) -> None:
        pass


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self,product_name,new_stock) -> None:
        pass


class StoreManager(Observer):
    def __init__(self, name: str):
        self._name = name

    def update(self, product_name: str, new_stock: int) -> None:
        # TODO: Implement the update method to display a message indicating the stock level update
        print(f"{self._name} was notified that {product_name} stock level is now {new_stock}")


class Inventory(Subject):
    def __init__(self,threshold=10):
        self._observers = []
        self._products = {}
        self._threshold=threshold

    def attach(self, observer: Observer) -> None:
        # TODO: Implement the attach method to add an observer
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        # TODO: Implement the detach method to remove an observer
        self._observers.remove(observer)

    def notify(self,product_name,new_stock) -> None:
        # TODO: Implement the notify method to notify all observers

        for obsever in self._observers:

                obsever.update(product_name,new_stock)

    def update_stock(self, product_name: str, new_stock: int) -> None:
        # TODO: Implement the update_stock method to update the stock level and call notify if necessary
        self._products[product_name] = new_stock
        if new_stock<self._threshold:
            self.notify(product_name=product_name,new_stock=new_stock)


if __name__ == "__main__":
    inventory = Inventory()

    # Adding products to inventory
    inventory._products = {
        "Apples": 10,
        "Oranges": 25,
        "Bananas": 50,
    }

    manager1 = StoreManager("Alice") #subscriber
    manager2 = StoreManager("Bob") #subscriber

    # Attaching store managers
    inventory.attach(manager1)
    inventory.attach(manager2)

    # Updating stock levels and checking notifications
    print("Stock level update 1:")
    inventory.update_stock("Apples", 5)  # Should notify both managers
    print("\nStock level update 2:")
    inventory.update_stock("Bananas", 60)  # Should not notify as stock level increased

    # Detaching manager1
    inventory.detach(manager1)

    # Updating stock levels again
    print("\nStock level update 3:")
    inventory.update_stock("Oranges", 8)  # Should notify only manager2