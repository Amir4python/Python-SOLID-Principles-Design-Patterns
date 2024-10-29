class ClassicSingleton:
    #class level variable to store singleton class instance

    _instance = None

    #override the __init__ to control initialization
    def __init__(self):
        print('init is called')
        raise RuntimeError(' USe get_instance() instead')

    @classmethod
    def get_instance(cls):
        print('get_instance is called')
        if not cls._instance:
            # create new instance of class
            cls._instance = cls.__new__(cls)
        # return single instace of the class
        # newly created instance or existing One
        return cls._instance


if __name__ == '__main__':
    s1 = ClassicSingleton.get_instance()
    s2 = ClassicSingleton.get_instance()

    print(s1 is s2)
    print(f'id of s1 is {id(s1)} and id of s2 is {id(s2)}')

"""
Output:
get_instance is called
get_instance is called
True
id of s1 is 2243022402768 and id of s2 is 2243022402768

You see that their memory location are same.
"""
