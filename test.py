from main import Library, Book, Member
from data import book_list, member_names

# Initialize a Library
lib = Library()

# Add books to the library
for title, author in book_list:
    lib.add_book(Book(title, author))
print(lib.books)
# Register members in the library
for name in member_names:
    lib.add_member(Member(name))

# Members borrow books
lib.borrow_book("Alice", "1984")
lib.borrow_book("Bob", "The Great Gatsby")
lib.borrow_book("Charlie", "Pride and Prejudice")

# Display list of all available books
print("Available Books:")
for book in lib.get_available_books():
    print(f"{book.title} by {book.author}")

# Members return books
lib.return_book("Alice", "1984")
lib.return_book("Bob", "The Great Gatsby")

# Display list of all available books after some books are returned
print("\nAvailable Books after some returns:")
for book in lib.get_available_books():
    print(f"{book.title} by {book.author}")

# test append from book_list
lib.add_book(book_list)
lib.borrow_book(book_list)

