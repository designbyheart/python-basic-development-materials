import tkinter as tk
from tkinter import font
from components import BookListView, RentedBooksView, RentBookForm, AddBookForm


class MainView(tk.Tk):
    def __init__(self, bookstore):
        super().__init__()
        self.bookstore = bookstore
        self.title("Bookstore Management")
        self.geometry("800x600")
        self.configure(bg="#f0f0f0")  # Overall background color

        self.create_sidebar()  # Create sidebar for navigation

        self.main_frame = tk.Frame(self, bg="#ffffff")  # Content area for views
        self.main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def create_sidebar(self):
        sidebar = tk.Frame(self, bg="#35424a", width=200)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)

        title_label = tk.Label(
            sidebar,
            text="Bookstore Menu",
            bg="#35424a",
            fg="#ffffff",
            font=("Sora", 16, "bold"),
        )
        title_label.pack(pady=10)

        btn_list_books = tk.Button(
            sidebar,
            text="List All Books",
            command=self.show_books,
            bg="#e7e7e7",
            font=("Sora", 12),
        )
        btn_list_books.pack(fill=tk.X, padx=10, pady=5)

        btn_list_rented = tk.Button(
            sidebar,
            text="List Rented Books",
            command=self.show_rented_books,
            bg="#e7e7e7",
            font=("Sora", 12),
        )
        btn_list_rented.pack(fill=tk.X, padx=10, pady=5)

        btn_rent_book = tk.Button(
            sidebar,
            text="Rent a Book",
            command=self.rent_book,
            bg="#e7e7e7",
            font=("Sora", 12),
        )
        btn_rent_book.pack(fill=tk.X, padx=10, pady=5)

        btn_add_book = tk.Button(
            sidebar,
            text="Add New Book",
            command=self.add_book,
            bg="#e7e7e7",
            font=("Sora", 12),
        )
        btn_add_book.pack(fill=tk.X, padx=10, pady=5)

        btn_exit = tk.Button(
            sidebar,
            text="Exit",
            command=self.quit,
            bg="#e74c3c",
            fg="#ffffff",
            font=("Sora", 12),
        )
        btn_exit.pack(fill=tk.X, padx=10, pady=10)

    def show_books(self):
        book_view = BookListView(self.main_frame, self.bookstore)
        book_view.pack(fill=tk.BOTH, expand=True)

    def show_rented_books(self):
        rented_books_view = RentedBooksView(self.main_frame, self.bookstore)
        rented_books_view.pack(fill=tk.BOTH, expand=True)

    def rent_book(self):
        rent_form = RentBookForm(self)
        rent_form.grab_set()  # Modally grab focus

    def add_book(self):
        add_book_form = AddBookForm(self)
        add_book_form.grab_set()  # Modally grab focus
