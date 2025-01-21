class Book:
    def __init__(self, title, author, year):
        """Initialize a new Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """Destructor method that prints a message when the book object is deleted."""
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """Return a string representation of the book in a readable format.
        
        Returns:
            str: A string in the format 'title by author, published in year'
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """Return an official string representation of the book that can recreate the object.
        
        Returns:
            str: A string that can be used to recreate the Book instance
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"