from abc import ABC, abstractmethod


class Sandwich():
    def __init__(self):
        self.sandwich=None
        self.sandwichName=None
        self.ingredients=[]

    def add_ingredients(self,ingredient):
        self.ingredients.append(ingredient)


    def display(self):
        print(f'{self.sandwichName} with ingredients: {self.ingredients}')




class SandwichBuilder(ABC):
    def __init__(self):
        self.sandwich=None
    def create_new_sandwich(self):
        self.sandwich = Sandwich()

    @abstractmethod
    def add_bread(self):
        pass
    @abstractmethod
    def add_filling(self):
        pass


class VeggieSandwichBuilder(SandwichBuilder):


    def add_bread(self):
        self.sandwich.add_ingredients('Wheat Bread')

    def add_filling(self):
        self.sandwich.add_ingredients('Tomato')
        self.sandwich.add_ingredients('Lettuce')
        self.sandwich.add_ingredients('Cheese')


    def get_sandwich(self):
        self.sandwich.sandwichName = 'Veggie Sandwich'
        return self.sandwich


class NuggetSandwichBuilder(SandwichBuilder):
    def add_bread(self):
        self.sandwich.add_ingredients('Maida Bread')

    def add_filling(self):
        self.sandwich.add_ingredients('Tomato')
        self.sandwich.add_ingredients('Nuggets')
        self.sandwich.add_ingredients('French Fries')
        self.sandwich.add_ingredients('Cheese')


    def get_sandwich(self):
        self.sandwich.sandwichName = 'Nugget Sandwich'
        return self.sandwich

class SandwichDirector():
    def __init__(self,sandwich_builder):
        self.sandwich_builder=sandwich_builder

    def build_sandwich(self):
        self.sandwich_builder.create_new_sandwich()
        self.sandwich_builder.add_bread()
        self.sandwich_builder.add_filling()
        return self.sandwich_builder.get_sandwich()


if __name__ == '__main__':


    veggieBuilder=VeggieSandwichBuilder()
    veggieDirector=SandwichDirector(veggieBuilder)
    veggie_sandwich=veggieDirector.build_sandwich()

    veggie_sandwich.display()

    nuggetBuilder=NuggetSandwichBuilder()
    nuggetDirector=SandwichDirector(nuggetBuilder)
    nugget_sandwich=nuggetDirector.build_sandwich()

    nugget_sandwich.display()