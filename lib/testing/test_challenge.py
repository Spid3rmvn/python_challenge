"""Test script for library management system."""

import sys
import os
from testing.library import Library, Book, Member, Librarian

sys.path.append(os.path.abspath("/home/ian/Desktop/Phase3/python_challenge/lib"))

if __name__ == "__main__":
    central_library = Library()

    # Add some books
    central_library.add_book("PY101", Book("Data science", "John wick"))
    central_library.add_book("DS202", Book("Python Basics", "Jane Marry"))
    central_library.add_book("ALG303", Book("Algorithms", "Alice matheo"))
    central_library.add_book("BSK23", Book("Business", "Mac grengoo"))

    # Create people
    member1 = Member("Sarah jevo", "MEM001")
    librarian1 = Librarian("Danielle Librarian", "LIB001")

    # Demonstrate introductions
    print("\n--- Introductions ---")
    member1.introduce()
    librarian1.introduce()

    # Show available books
    print("\n--- Available Books ---")
    for book in central_library.list_available():
        print(book)

    # Member borrows a book
    python_book = Book("Python Basics", "Jane Merry")
    print(f"\n--- {member1.name} tries to borrow {python_book.title} ---")
    if member1.borrow(python_book, central_library):
        print("Borrow successful!")
    else:
        print("Borrow failed!")

    # Show borrowed books
    print(f"\n--- {member1.name}'s Borrowed Books ---")
    print(member1.list_borrowed())

    # Show available books after borrowing
    print("\n--- Available Books After Borrowing ---")
    for book in central_library.list_available():
        print(book)

    # Member returns the book
    print(f"\n--- {member1.name} tries to borrow {python_book.title} ---")
    if member1.return_book(python_book, central_library):
        print("Return successful!")
    else:
        print("Return failed!")

    # Final available books
print("\n--- Final Available Books ---")
for book in central_library.list_available():
    print(book)
