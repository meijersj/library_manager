'''
Case Study: Library Management System

You're tasked with designing a simple library management system. This system needs to keep track of books, library members, and the books that members have borrowed.

Requirements:

A Book class to represent a book. It should have attributes like title, author, and is_borrowed to keep track of whether it's currently borrowed or not.
A Member class to represent a library member. It should have attributes like name and borrowed_books (a list to keep track of books the member has currently borrowed).
A Library class to manage the books and members. It should include methods to add books, register members, borrow books, and return books.

Task 1: Object Oriented Design

Design the three classes: Book, Member, and Library. Implement methods to borrow and return books.

(Bonus) Task 2: List Comprehension

Implement a method in the Library class to get a list of all available books (books not currently borrowed) using list comprehension. Similarly, implement a method in the Member class to get a list of titles of all borrowed books.

Expected Output:

Demonstrate the functionality of your classes by creating a few books and members, and by borrowing and returning some books.
'''


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.borrowed = []
    def add_book(self,Book):
        self.books.append(Book)
    def add_member(self,Member):
        self.members.append(Member)

    def borrow_book (self,Member,Book):
        if Book in self.books and Member in self.members:
            self.books.remove(Book)
        #key-value? self.books_borrowed[Member] = Book
    def get_member(self):
        return self.members
    def get_books(self):
        return self.books



class Member:
    def __init__(self, name,surname="",address="",phone="" ):
        self.name = name
        self.surname = surname
        self.address = address
        self.phone = phone



