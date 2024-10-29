from abc import ABC,abstractmethod


class TextTransform(ABC):
    @abstractmethod
    def transform(self, text):
        pass
class UpperCase(TextTransform):
    def transform(self, text):
        return text.upper()
class LowerCase(TextTransform):
    def transform(self, text):
        return text.lower()
class Capitalize(TextTransform):
    def transform(self, text):
        return text.capitalize()




class TextProcessor:
    def __init__(self, textTransform:TextTransform):

        self.textTransform=textTransform

    def operation(self,text):
        return self.textTransform.transform(text)


if __name__ == '__main__':

    print("Select a carrier for shipping:")
    print("1. lower")
    print("2. upper")
    print("3. capitalize")


    choice = int(input("Enter text operation : "))
    text = str(input("Enter the text: "))

    if choice == 1:
        operation = LowerCase()
    elif choice == 2:
        operation = UpperCase()
    elif choice == 3:
        operation = Capitalize()

    else:
        print("Invalid choice!")
        exit(1)

    strOutput = TextProcessor(textTransform=operation).operation(text)
    print(f"The shipping cost for {operation} is {strOutput}")