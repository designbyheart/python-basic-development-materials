from bookstore import Bookstore
from book import Book
from category import Category
from user import User
from ui.bookstore_ui import BookstoreUI
import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar

def runApp():
    root = tk.Tk()
    app = BookstoreUI(root)
    root.mainloop()
    
    # print("Oke, ovde krecemo :) ")
    # store = Bookstore()
    # store.load_books()
    # store.rent_book(1, "python")

    # # Example: add new book
    # new_book = Book(
    #     book_id="1",
    #     title="Python Programming",
    #     author="John Doe",
    #     category_id="1",
    #     publication_date="2019-07-11",
    # )
    # store.add_book(new_book)

    # Example: list books
    # books = store.list_books()
    # for book in books:
    #     print(book.to_dict())

    # Add other interactions here for testing each method


if __name__ == "__main__":
    runApp()
