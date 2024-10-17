'''
5. Create a class Library that manages a list of books. Write methods to add a book, remove a book, and display all books in the library.
'''

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        return f"Book '{book}' added."

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            return f"Book {book} removed."
        return "Book not found."
    
    def display_books(self):
        if self.books:
            return f"Book in library: {', '.join(self.books)}"
        return "No books in library."

lib = Library()
print(lib.add_book("The great Gatsby"))
print(lib.add_book("1992"))
print(lib.display_books())
print(lib.remove_book("1992"))
# print(lib.remove_book("The great Gatsby"))
print(lib.display_books())