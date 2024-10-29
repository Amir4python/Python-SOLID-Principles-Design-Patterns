"""

text Editor with 4 states

1 defaultState:  the editor is currently in the default state,no formatting is applied to the text
2 BoldState: The editor is currently in bold state, any new text entered will be bolder
3 ItalicState: The editor is currently in italic state, any new text entered will be italic
4 UnderlineState: The editor is currently in underline state, any new text entered will be underlined

These are 4 states.
The editor should be able to maintain a history of formatting changes so that it can undo redo changes.

"""
from abc import ABC


class TextEditor(ABC):
    def __init__(self):
        pass

    def enter_text(self, text):
        pass

    def apply_bold(self,text):
        pass

    def apply_italic(self,text):
        pass

    def apply_underline(self,text):
        pass

    def undo(self, text):
        text.textState = text.textOperations.pop()(text)

    def redo(self, text):
        value = text.textOperations.pop()(text)
        text.textOperations.append(value)


class DefaultState:
    def enter_text(self, text):
        text.textState='default'
        print('default state --->',self.__class__.__name__)
        text.textOperations.append(DefaultState)




class BoldState:
    def apply_bold(self, text):
        text.textState='bold'
        print('bold state',self.__class__.__name__)
        text.textOperations.append(BoldState)


class ItalicState:
    def apply_italic(self, text):
        text.textState='italic'
        print('italic state',self.__class__.__name__)
        text.textOperations.append(ItalicState)

class UnderlineState:
    def apply_underline(self, text):
        text.textState='underline'
        print('underline state',self.__class__.__name__)
        text.textOperations.append(UnderlineState)


class Text:
    def __init__(self):
        self.textState=DefaultState()
        self.textOperations=[]


    def enter_text(self,text):
        text.textState.enter_text(self)

    def apply_bold(self):
        self.textState.apply_bold()

    def apply_italic(self,text):
        text.textState.apply_italic(self)

    def apply_underline(self,text):
        text.textState.apply_underline(self)

    def undo(self, text):
        text.textState.undo(self)

    def redo(self, text):
        text.textState.redo(self)


def main():
    text1 = Text()
    text1.enter_text()

    text1.apply_bold()


    print(text1.textOperations)

if __name__ == '__main__':
    main()