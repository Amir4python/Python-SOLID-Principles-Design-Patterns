class Singleton:
    #class level variable to store singleton class instance

    _instance = None

    #override the __init__ to control how new objects are created
    def __new__(cls):
        print('--new method called--')
        if not cls._instance:
            # create new instance of class and store it in _instance
            cls._instance = super().__new__(cls)
        # return single instance of the class either
        # newly created instance or existing One
        return cls._instance


    def __init__(self):
        print('init method called')

if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()

    print(s1 is s2)
    print(f'id of s1 is {id(s1)} and id of s2 is {id(s2)}')

"""
Output:
--new method called--
--new method called--
True
id of s1 is 2234292622480 and id of s2 is 2234292622480
"""