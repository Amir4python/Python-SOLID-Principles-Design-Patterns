from abc import abstractmethod, ABC


class ScanMachine(ABC):
    @abstractmethod
    def scan(self):
        pass


class PrintMachine(ABC):
    @abstractmethod
    def print(self):
        pass


class FaxMachine(ABC):

    @abstractmethod
    def fax(self):
        pass


class CopyMachine(ABC):
    @abstractmethod
    def copy(self):
        pass


class Printer(PrintMachine):
    def print(self):
        print('printing.....')


class Scanner(ScanMachine):
    def scan(self):
        print('scanning.....')


class Copier(CopyMachine):
    def copy(self):
        print('copying.....')


class AllInOnePrinter(PrintMachine, ScanMachine, CopyMachine):
    def print(self):
        print('printing.....')

    def scan(self):
        print('scanning.....')

    def copy(self):
        print('copying.....')

if __name__=='__main__':
    printer = Printer()
    printer.print()

    scanner = Scanner()
    scanner.scan()

    copier = Copier()
    copier.copy()
    print(f'---{AllInOnePrinter}')
    allinone = AllInOnePrinter()
    allinone.print()
    allinone.scan()
    allinone.copy()