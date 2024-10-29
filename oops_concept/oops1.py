class Greeting:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)


class BetterGreeting(Greeting):


    def greet(self):
        super().greet()
        print("Hi", self.name, 'Welcome to Python Training')


if __name__ == "__main__":
    #invoke Greeting class

    # g=Greeting("sai")
    # g.greet()

    g = BetterGreeting('Mubarra')
    g.greet()
