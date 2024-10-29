from abc import ABC, abstractmethod


class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass


class FlyingBird(Bird):
    def fly(self):
        print("I can fly")


class NonFlyingBird(Bird):
    def fly(self):
        print("I can't fly")


class Penguin(NonFlyingBird):
    def __init__(self, name):
        self.name = name
        print(f'{self.name} penguin is created')

    def __del__(self):
        print(f'{self.name} penguin is deleted')


if __name__ == '__main__':
    p = Penguin('Propper')

    p.fly()
