# Library Management System

class Book:
    def __init__(self, title, author,genre , publication_year,isbn):
        self.title = title  # Public as per requirements
        self.author = author  # Public as per requirements
        self.genre = genre
        self.publication_year = publication_year  # Public as per requirements
        self.isbn = isbn  # Public as per requirements
    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.genre}, {self.publication_year}, {self.isbn})"
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    def get_details(self):
        """Return detailed information about the book."""
        return f"Title: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}\nPublication Year: {self.publication_year}\nISBN: {self.isbn}"
        
    def is_recent(self):
        """Check if the book was published in or after 2010."""
        return self.publication_year >= 2010
