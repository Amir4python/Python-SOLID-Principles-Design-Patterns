from abc import abstractmethod, ABC

class MutliFunctionDevice(ABC):
    @abstractmethod
    def scan(self):
        pass

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def fax(self):
        pass

    @abstractmethod
    def copy(self):
        pass

class Printer(MutliFunctionDevice):
    def print(self):
        print('printing.....')

class Scanner(MutliFunctionDevice):
    def scan(self):
        print('scanning.....')

class Copier(MutliFunctionDevice):
    def copy(self):
        print('copying.....')

