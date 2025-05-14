#!/usr/bin/env python3

"""This module provides classes and functions for managing 
a library system including books, members, and transactions."""

class Book:
    """Represents a book in the library with title, author, and availability status."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Member:
    """Represents a member in the library with name, and member_id."""
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        ''''''
    def get_name(self):
        """Represents a book in the library with title, author, and availability status."""
        return self.name

    def introduce(self):
        """Represents a book in the library with title, author, and availability status."""

        print(f"I am {self.name}, a library member.")

    def borrow(self, book, library):
        """Represents a book in the library with title, author, and availability status."""

        return library.borrow_book(book, self)

    def return_book(self, book, library):
        """Represents a book in the library with title, author, and availability status."""

        return library.return_book(book, self)

    def list_borrowed(self):
        """Represents a book in the library with title, author, and availability status."""

        return self.borrowed_books

class Librarian:
    """Represents a book in the library with title, author, and availability status."""

    def __init__(self, name, librarian_id):
        self._name = name
        self.librarian_id = librarian_id

    def introduce(self):
        """Represents a book in the library with title, author, and availability status."""

        print(f"I am {self._name}, a librarian.")

class Library:
    """Represents a book in the library with title, author, and availability status."""

    def __init__(self):
        self.books = {}  # id -> book

    def add_book(self, book_id, book):
        """Represents a book in the library with title, author, and availability status."""

        self.books[book_id] = book

    def list_available(self):
        """Represents a book in the library with title, author, and availability status."""

        return list(self.books.values())

    def borrow_book(self, book, member):
        """Represents books borrowed."""

        for key, value in self.books.items():
            if value.title == book.title:
                member.borrowed_books.append(value)
                del self.books[key]
                return True
        return False

    def return_book(self, book, member):
        """Represents a book in the library with title, author, and availability status."""

        if book in member.borrowed_books:
            self.books[book.title] = book
            member.borrowed_books.remove(book)
            return True
        return False
