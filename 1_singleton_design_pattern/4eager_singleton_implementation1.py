class SingletonMeta(type):
    _instances = {}

    #override: called during creation of sub-type
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        # eager loading of the class instance
        cls._instances[cls] = super().__call__()
        print('initializing <super>....')

    # return the singleton instance
    def __call__(cls, *args, **kwargs):
        return cls._instances[cls]


# singleton class derived from metaclass
class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        print('initalizing child ')
        self.attribute = 'I am singleton'


if __name__ == '__main__':
    # pass
    singleton1 = Singleton()
    singleton2 = Singleton()

    print(singleton1 is singleton2)
    print(singleton1.attribute)
    print(singleton2.attribute)

"""
with main

Output:
initalizing child 
initializing <super>....
True
I am singleton
I am singleton


without main just pass

initalizing child 
initializing <super>....


Here is eager loading
"""