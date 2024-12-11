from category import Category


class Bookstore:
    def __init__(self):
        self.categories = {}

    def add_category(self, category):
        self.categories[category.name] = category

    def add_book_to_category(self, category_name, book):
        if category_name in self.categories:
            self.categories[category_name].add_book(book)
        else:
            print(f"Category {category_name} does not exist!")

    def list_books_in_category(self, category_name):
        if category_name in self.categories:
            category = self.categories[category_name]
            print(f"Books in {category.name}:")
            for book in category.books:
                print(f"  - {book}")
        else:
            print(f"Category {category_name} does not exist!")

    def filter_books_by_year(self, category_name, year):
        if category_name in self.categories:
            print(f"Books in {category_name} published in {year}:")
            category = self.categories[category_name]
            for book in category.books:
                if book.publication_date.year == year:
                    print(f"  - {book}")
        else:
            print(f"Category {category_name} does not exist!")

    def list_categories(self):
        if not self.categories:
            print("No categories available.")
            return
        print("Bookstore Categories:")
        for category in self.categories.values():
            print(f"  - {category}")

    def summary(self):
        print("Bookstore Summary:")
        for category in self.categories.values():
            print(f"{category.name} ({len(category.books)} books)")
            for book in category.books:
                print(f"  - {book.title}")
