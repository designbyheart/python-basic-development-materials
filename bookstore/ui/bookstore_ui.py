import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar
from bookstore import Bookstore

class BookstoreUI:
    def __init__(self, root):
        # Configure app window 
        self.root = root
        self.root.title("Bookstore Application")
        self.root.geometry("400x400")
        
        self.bookstore = Bookstore()
        '''
        Creates all the visual elements (widgets) of your application
        Positions them in the window
        Sets up their configurations and event handlers
        It's like saying "build and set up all the visual parts of my application now." 
        Without this line, your window would be empty because none of the GUI elements 
        would be created.
        '''
        self.create_widgets()
        
        self.populate_book_list()

    def create_widgets(self):
        # Create listbox to display books
        self.book_list = Listbox(self.root, width=50)
        self.book_list.pack(pady=20) 
        '''
        Tkinter layout command:
        1. pack() - This is a geometry manager method that places (or "packs") 
        the widget (book_list) into the parent window
        2. pady=20 - Creates 20 pixels of vertical padding (space)
        above and below the widget
        +------------------+
        |                  |  ← 20 pixels of padding above
        |   [Book List]    |
        |                  |  ← 20 pixels of padding below
        +------------------+
        The pack() method is one of three main geometry managers in Tkinter:
        - pack(): Packs widgets in blocks before placing them in the parent widget
        - grid(): Places widgets in a table-like structure
        - place(): Places widgets using exact coordinates
        '''

        # Create scrollbar for the listbox
        self.scrollbar = Scrollbar(self.root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # connects the Listbox to the Scrollbar for vertical scrolling. 
        # It's part of a two-way connection between the listbox and scrollbar
        # The listbox tells the scrollbar where to position its slider, X or Y coordinate
        self.book_list.config(yscrollcommand=self.scrollbar.set)
        # The scrollbar tells the listbox what portion to display
        self.scrollbar.config(command=self.book_list.yview)

        # Create button to show book details
        self.details_button = tk.Button(self.root, text="Show Details", command=self.show_book_details)
        self.details_button.pack(pady=10)

    def populate_book_list(self):
        # Load books and add them to the listbox
        self.book_list.delete(0, tk.END)  # Clear the listbox
        for book in self.bookstore.list_books():
            self.book_list.insert(tk.END, f"{book.title} by {book.author}")

    def show_book_details(self):
        try:
            selected_index = self.book_list.curselection()[0]
            selected_book = self.bookstore.books[selected_index]
            details = (
                f"Title: {selected_book.title}\n"
                f"Author: {selected_book.author}\n"
                f"ISBN: {selected_book.isbn}\n"
                f"Publication Date: {selected_book.publication_date}\n"
                f"Available: {'Yes' if selected_book.available else 'No'}"
            )
            messagebox.showinfo("Book Details", details)
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a book from the list.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BookstoreUI(root)
    root.mainloop()
