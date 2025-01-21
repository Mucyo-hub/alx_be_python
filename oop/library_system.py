class Book:
    """Base class for all types of books."""
    def __init__(self, title, author):
        """Initialize a book with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Class representing an electronic book."""
    def __init__(self, title, author, file_size):
        """Initialize an ebook with title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return string representation of the ebook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Class representing a physical printed book."""
    def __init__(self, title, author, page_count):
        """Initialize a print book with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return string representation of the print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class representing a library that can contain different types of books."""
    def __init__(self):
        """Initialize an empty library."""
        self.books = []

    def add_book(self, book):
        """Add a book to the library."""
        if isinstance(book, (Book, EBook, PrintBook)):
            self.books.append(book)
        else:
            raise ValueError("Only Book objects can be added to the library")

    def list_books(self):
        """List all books in the library."""
        if not self.books:
            print("The library is empty.")
            return
        
        for book in self.books:
            print(book)