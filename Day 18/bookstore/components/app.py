import tkinter as tk

from components.organisms.explore_books import BookFinderComponent
from components.organisms.book_form import BookForm


class AppUI:
    def __init__(self, root):
        # Configure app window
        self.root = root
        self.root.title("Bookstore Application")
        self.root.geometry("600x400")

        # Create components
        # self.book_finder_component = BookFinderComponent(self.root)
        self.book_form_component = BookForm(self.root)
