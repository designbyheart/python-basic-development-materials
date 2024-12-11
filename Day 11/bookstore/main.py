from bookstore import Bookstore
from book import Book
from category import Category

# Create bookstore and categories
bookstore = Bookstore()
fiction = Category("Fiction")
non_fiction = Category("Non-fiction")
bookstore.add_category(fiction)
bookstore.add_category(non_fiction)

# Create and add books
book1 = Book("To Kill a Mockingbird", "Harper Lee", "1960-07-11", "1234567890")
book2 = Book("1984", "George Orwell", "1949-06-08", "0987654321")
book3 = Book("Sapiens", "Yuval Noah Harari", "2011-02-01", "1122334455")

bookstore.list_books_in_category("Fiction")

bookstore.add_book_to_category("Fiction", book1)
bookstore.add_book_to_category("Fiction", book2)
bookstore.add_book_to_category("Non-fiction", book3)

# List books in a category
bookstore.list_books_in_category("Fiction")
print("Filter books by year")

# Filter books by year in a category
bookstore.filter_books_by_year("Fiction", 1949)
print("list categories")
# Display categories and summary
bookstore.list_categories()
print("Books summary")
bookstore.summary()
