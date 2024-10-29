class Author:
    def __init__(self, name, country):
        self.name = name

        self.country = country

    def author_info(self):
        return f'{self.name} from {self.country}'


class Book:
    def __init__(self,title,publication_year,author):
        self.title = title
        self.publication_year = publication_year
        self.author = author

    def get_book_info(self):
        return f'{self.title} was written by {self.author.name} from {self.author.country} in {self.publication_year}'


if __name__=="__main__":
    author = Author('Sachin Tendulkar', 'India')
    book = Book('The Godfather', 1972, author)


    print(book.get_book_info())