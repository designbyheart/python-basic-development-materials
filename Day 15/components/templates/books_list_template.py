import tkinter as tk
from tkinter import font

from components.atoms.nav_link import NavLink


class BooksListTemplate(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bookstore Management")
        self.geometry("800x600")
        self.configure(bg="#fafafa")  # Overall background color

        self.main_frame = tk.Frame(self, bg="#fafafa")  # Content area for views
        self.main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        navBar = tk.Frame(self, bg="#fefefe", height=100)
        navBar.pack(side=tk.LEFT, fill=tk.X)

        nav_link2 = tk.Button(
            navBar,
            text="Popular",
            command=self.onClick,
            bg="#e7e7e7",
            font=("Sora", 12),
        )

    def onClick():
        print("Hello from button")