class Searchable:
    def search_books(self, title, author, genre):
        pass

class Borrowable:
    def borrow_book(self, user):
        pass

    def return_book(self, user):
        pass

class ReportGenerator:
    def generate_reports(self):
        pass

class Library(Searchable, Borrowable, ReportGenerator):
    def add_book(self, book):
        pass

    def remove_book(self, book):
        pass

# Usage
library = Library()
library.search_books("Title", "Author", "Genre")
library.borrow_book(user)
library.return_book(user)
library.generate_reports()
