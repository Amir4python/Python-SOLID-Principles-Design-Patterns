from abc import abstractmethod, ABC


class Observer(ABC):
    @abstractmethod
    def update(self,symbol,price,change_in_price) -> None:
        pass


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass



class Stock():

    def __init__(self,symbol,price,change_in_price=0):
        self.symbol=symbol
        self.price=price
        self.change_in_price=change_in_price

        self.observers=[]

    def set_price(self,price):
        self.change_in_price=price-self.price
        self.price=price

        self.notify()

    def notify(self):
        for observer in self.observers:
            observer.update(self.symbol,self.price,self.change_in_price)

    def attach(self,observer):
        self.observers.append(observer)

    def detach(self,observer):
        self.observers.remove(observer)


class PriceDisplay(Observer):
    def update(self,symbol,price,change_in_price) -> None:
        print(f' {symbol} with price of {price}')

class ChangeDisplay(Observer):
    def update(self,symbol,price,change_in_price) -> None:
        print(f' {symbol} has change of {change_in_price}')



if __name__ == '__main__':

    pd1=PriceDisplay()
    cd1=ChangeDisplay()

    stock=Stock('Armavco stocks',10.2,3)
    stock.attach(pd1)
    stock.attach(cd1)

    stock.set_price(120.5)



