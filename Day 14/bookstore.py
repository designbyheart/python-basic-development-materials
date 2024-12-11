from book import Book
from category import Category
from user import User
from utils.file_manager import load_csv, save_csv
from utils.constants import BOOKS_FILE, CATEGORIES_FILE, USERS_FILE, RENTED_BOOKS_FILE


class Bookstore:
    def __init__(self):
        self.books = load_csv(BOOKS_FILE, Book)
        self.categories = load_csv(CATEGORIES_FILE, Category)
        self.users = load_csv(USERS_FILE, User)
        self.rented_books = load_csv(RENTED_BOOKS_FILE)

    def load_books(self):
        self.books = load_csv(BOOKS_FILE, Book)
        print(f"books loaded: {len(self.books)}")

    def list_books(self):
        return self.books

    def search_books(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def add_book(self, book):
        self.books.append(book)
        save_csv(BOOKS_FILE, self.books)

    def add_user(self, user):
        self.users.append(user)
        save_csv(USERS_FILE, self.users)

    def update_book(self, book_id, new_data):
        for book in self.books:
            if book.book_id == book_id:
                book.title = new_data.get("title", book.title)
                book.author = new_data.get("author", book.author)
                save_csv(BOOKS_FILE, self.books)
                return True
        return False

    def delete_book(self, book_id):
        self.books = [book for book in self.books if book.book_id != book_id]
        save_csv(BOOKS_FILE, self.books)

    def rent_book(self, user_id, book_title):
        # 1. Does book exist?
        books_result = self.search_books(book_title)
        print(f"books_result: {len(books_result)}")
        if len(books_result) == 0:
            print("Books does not exists")
            return False
        # 2. Find book
        # 3. Is book available / rented?
        book = books_result[0]
        if book.available == False:
            print("Book is not available")
            return False

        # 4. Find user
        users_list = self.find_user(user_id)
        # 4.a Create user if it doesn't exist
        if len(users_list) == 0:
            user = User(user_id, "New user")
            self.add_user(user)
        else:
            user = users_list[0]
        # 5. Add book to rented (user_id, book_id)
        self.add_book_to_rented(book.book_id, user.user_id)

        # 6. Update book to not available
        self.update_book(book.book_id, {"available": False})
        save_csv(BOOKS_FILE, self.books)
        print("Book is rented successfully")
        return True

    def add_book_to_rented(self, book_id, user_id):
        self.rented_books.append({"user_id": user_id, "book_id": book_id})
        save_csv(RENTED_BOOKS_FILE, self.rented_books)

    def return_book(self, user_id, book_id):
        self.rented_books = [
            record
            for record in self.rented_books
            if not (record["user_id"] == user_id and record["book_id"] == book_id)
        ]
        for book in self.books:
            if book.book_id == book_id:
                book.available = True
                break
        save_csv(RENTED_BOOKS_FILE, self.rented_books)
        save_csv(BOOKS_FILE, self.books)

    def find_user(self, user_id):
        return [user for user in self.users if user_id.lower() in user.user_id.lower()]

    def get_all_books(self):

        return list(self.books.values())

    def get_rented_books(self):
        return self.rented_books
