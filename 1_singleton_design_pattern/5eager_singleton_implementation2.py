class SingletonMeta(type):
    _instances = {}

    #override: called during creation of sub-type
    def __new__(cls, *args, **kwargs):
        print(' initializing <super> ....')
        new_class= super().__new__(cls, *args, **kwargs)
        # eager loading of the class instance
        cls._instances[new_class] = super(SingletonMeta,new_class).__call__()
        return new_class


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
 initializing <super> ....
initalizing child 
True
I am singleton
I am singleton

without main just pass

 initializing <super> ....
initalizing child 


Here is eager loading
"""