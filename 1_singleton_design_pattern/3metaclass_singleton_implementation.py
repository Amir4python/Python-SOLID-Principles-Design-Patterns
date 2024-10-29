class SingletonMeta(type):
    _instances = {}

    def __call__(cls):
        if cls not in cls._instances:
            # cls._instances[cls] = super(SingletonMeta, cls).__call__()
            instance = super().__call__()
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_logic(self):
        pass


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()

    print(s1 is s2)


"""
    s1 = Singleton()
    s2 = Singleton()

    print(s1 is s2)
    
    if you run this 
    Output:True
    
    if no code,
    nothing happens , so its lazy initialization
    

"""