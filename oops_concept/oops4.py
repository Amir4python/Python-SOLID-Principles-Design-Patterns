# from abc import abstractmethod,ABC
# #THIS IS PURE ITERFACE
# class Animal(ABC):
#     @abstractmethod
#     def speak(self):
#         pass
#     @abstractmethod
#     def description(self):
#         pass
#
# class Dog(Animal):
#     def speak(self):
#         print("Bhow Bhow")
#     def description(self):
#         print("I am a dog")
#
# class Cat(Animal):
#     def speak(self):
#         print("Meow Meow")
#     def description(self):
#         print("I am a cat")
#
# if __name__ == "__main__":
#
#     c1,c2,d1,d2=Cat(),Cat(),Dog(),Dog()
#
#     for animal in [c1,d1,d2,c2]:
#         animal.speak()
#         animal.description()


from abc import abstractmethod, ABC


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def description(self):
        print(f"{self.__class__.__name__} says: {self.speak()}")


class Dog(Animal):
    def speak(self):
        return "Bhow Bhow"

    def description(self):
        super().description()
        print(f"Doggy  says: {self.speak()}")


class Cat(Animal):
    def speak(self):
        return "Meow Meow"

    def description(self):
        super().description()


if __name__ == "__main__":

    c1, c2, d1, d2 = Cat(), Cat(), Dog(), Dog()

    for animal in [c1, d1, d2, c2]:
        animal.speak()
        animal.description()