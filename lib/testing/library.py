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

