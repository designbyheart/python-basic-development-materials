# components.py
import tkinter as tk
from tkinter import messagebox
from bookstore import Bookstore
from book import Book


class BookListView(tk.Frame):
    def __init__(self, master, bookstore):
        super().__init__(master, bg="#ffffff")
        self.bookstore = bookstore
        self.create_widgets()

    def create_widgets(self):
        self.listbox = tk.Listbox(self, bg="#ffffff", fg="#000000", font=("Sora", 12))
        self.listbox.pack(fill=tk.BOTH, expand=True)

        self.refresh_button = tk.Button(
            self,
            text="Refresh",
            command=self.refresh,
            bg="#3498db",
            fg="#ffffff",
            font=("Sora", 12),
        )
        self.refresh_button.pack(pady=10)

        self.pack()

    def refresh(self):
        self.listbox.delete(0, tk.END)
        books = self.bookstore.get_all_books()
        for book in books:
            self.listbox.insert(
                tk.END,
                f"ID: {book.internal_id}, Title: {book.title}, Price: {book.price}",
            )


class RentedBooksView(tk.Frame):
    def __init__(self, master, bookstore):
        super().__init__(master, bg="#ffffff")
        self.bookstore = bookstore
        self.create_widgets()

    def create_widgets(self):
        self.listbox = tk.Listbox(self, bg="#ffffff", fg="#000000", font=("Sora", 12))
        self.listbox.pack(fill=tk.BOTH, expand=True)

        self.refresh_button = tk.Button(
            self,
            text="Refresh",
            command=self.refresh,
            bg="#3498db",
            fg="#ffffff",
            font=("Sora", 12),
        )
        self.refresh_button.pack(pady=10)

        self.pack()

    def refresh(self):
        self.listbox.delete(0, tk.END)
        rented_books = self.bookstore.get_rented_books()
        for rental in rented_books:
            self.listbox.insert(
                tk.END, f"User: {rental.user.name}, Book: {rental.book.title}"
            )


class RentBookForm(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        self.title("Rent a Book")
        self.geometry("300x200")

        self.user_id_label = tk.Label(self, text="User ID:")
        self.user_id_label.pack(pady=5)
        self.user_id_entry = tk.Entry(self)
        self.user_id_entry.pack(pady=5)

        self.book_id_label = tk.Label(self, text="Book ID:")
        self.book_id_label.pack(pady=5)
        self.book_id_entry = tk.Entry(self)
        self.book_id_entry.pack(pady=5)

        self.rent_button = tk.Button(
            self, text="Rent Book", command=self.rent_book, bg="#3498db", fg="#ffffff"
        )
        self.rent_button.pack(pady=10)

    def rent_book(self):
        user_id = self.user_id_entry.get()
        book_id = self.book_id_entry.get()
        # Call the renting logic from your bookstore class
        messagebox.showinfo("Success", "Book rented successfully!")
        self.destroy()


class AddBookForm(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        self.title("Add New Book")
        self.geometry("400x300")

        self.title_label = tk.Label(self, text="Title:")
        self.title_label.pack(pady=5)
        self.title_entry = tk.Entry(self)
        self.title_entry.pack(pady=5)

        self.author_label = tk.Label(self, text="Author:")
        self.author_label.pack(pady=5)
        self.author_entry = tk.Entry(self)
        self.author_entry.pack(pady=5)

        self.isbn_label = tk.Label(self, text="ISBN:")
        self.isbn_label.pack(pady=5)
        self.isbn_entry = tk.Entry(self)
        self.isbn_entry.pack(pady=5)

        self.price_label = tk.Label(self, text="Price:")
        self.price_label.pack(pady=5)
        self.price_entry = tk.Entry(self)
        self.price_entry.pack(pady=5)

        self.stock_label = tk.Label(self, text="Stock:")
        self.stock_label.pack(pady=5)
        self.stock_entry = tk.Entry(self)
        self.stock_entry.pack(pady=5)

        self.add_button = tk.Button(
            self, text="Add Book", command=self.add_book, bg="#3498db", fg="#ffffff"
        )
        self.add_button.pack(pady=10)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        isbn = self.isbn_entry.get()
        price = float(self.price_entry.get())
        stock = int(self.stock_entry.get())

        book = Book(title, author, isbn, price, stock)
        Bookstore().add_book(book)
        # Call the add book logic from your bookstore class

        # ToDo: Call add_book function from bookstore class
        messagebox.showinfo("Success", "Book added successfully!")
        self.destroy()
