# Library Management System

class Book:
    def __init__(self, title, author,genre , publication_year):
        self.title = title  # Public as per requirements
        self.author = author  # Public as per requirements
        self.genre = genre
        self.publication_year = publication_year  # Public as per requirements
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    def get_details(self):
        """Return detailed information about the book."""
        return f"Title: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}\nPublication Year: {self.publication_year}"
        
    def is_recent(self):
        """Check if the book was published in or after 2010."""
        return self.publication_year >= 2010
