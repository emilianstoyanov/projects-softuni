class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

    # ако извикаме директно само класа, неговата репрезентация:
    # def __repr__(self):
    #     return 'object of type order book'


book = Book('My Book', 'Me', '200')

# print(book) При извикване с подаване на  __repr__ -> object of type order book
print(book.name)
print(book.author)
print(book.pages)
