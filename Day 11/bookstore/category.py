from book import Book


class Category:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __str__(self):
        return f"Category: {self.name}, Books: {len(self.books)}"
