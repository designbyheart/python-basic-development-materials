class Book:

    def __init__(
        self,
        book_id,
        title,
        author,
        category_id,
        publication_date,
        isbn=None,
        available=True,
    ):
        self.book_id = book_id
        self.isbn = isbn
        self.title = title
        self.author = author
        self.category_id = category_id
        self.available = available
        self.publication_date = publication_date

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "category_id": self.category_id,
            "available": self.available,
            "isbn": self.isbn,
            "publication_date": self.publication_date,
        }
