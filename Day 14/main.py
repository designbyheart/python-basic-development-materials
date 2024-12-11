# from bookstore import Bookstore
from bookstore import Bookstore
from views import MainView

if __name__ == "__main__":
    bookstore = Bookstore()  # Initialize your bookstore logic
    app = MainView(bookstore)
    app.mainloop()
