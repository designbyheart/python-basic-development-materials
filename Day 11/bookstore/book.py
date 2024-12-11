from datetime import datetime

class Book:
    def __init__(self, title, author, publication_date, isbn):
        self.title = title
        self.author = author
        self.publication_date = datetime.strptime(publication_date, '%Y-%m-%d')
        self.isbn = isbn # jbmg for books

    def __str__(self):
        return f"{self.title} by {self.author}, Published: {self.publication_date.strftime('%Y-%m-%d')}"