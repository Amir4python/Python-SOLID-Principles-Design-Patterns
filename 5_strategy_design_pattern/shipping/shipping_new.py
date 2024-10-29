from abc import ABC, abstractmethod


class ShippingCarrier(ABC):

    @abstractmethod
    def calculate_shipping_cost(self, weight):
        pass

class FedEx(ShippingCarrier):


    def calculate_shipping_cost(self, weight):
        return weight * 2.5
class UPS(ShippingCarrier):

    def calculate_shipping_cost(self, weight):
        return weight * 3

class DHL(ShippingCarrier):

    def calculate_shipping_cost(self, weight):
        return weight * 4

class Amazon(ShippingCarrier):

    def calculate_shipping_cost(self, weight):
        return weight * 3.25

class Shipping:

    def __init__(self, carrier):
        self.carrier = carrier

    def calculate_shipping_cost(self, weight):
        return self.carrier.calculate_shipping_cost(weight)


if __name__ == '__main__':
    print("Select a carrier for shipping:")
    print("1. FedEx")
    print("2. UPS")
    print("3. DHL")
    print("4. Amazon")

    choice = int(input("Enter the number corresponding to your choice: "))
    weight = float(input("Enter the weight of the package (in pounds): "))

    if choice == 1:
        carrier = FedEx()
    elif choice == 2:
        carrier = UPS()
    elif choice == 3:
        carrier = DHL()
    elif choice == 4:
        carrier = Amazon()
    else:
        print("Invalid choice!")
        exit(1)

    shipping_cost = Shipping(carrier).calculate_shipping_cost(weight)
    print(f"The shipping cost for {carrier} is ${shipping_cost:.2f}")