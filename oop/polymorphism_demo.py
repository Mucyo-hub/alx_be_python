from math import pi

class Shape:
    """Base class for all shapes."""
    def area(self):
        """Calculate the area of the shape.
        
        This is an abstract method that should be implemented by all derived classes.
        """
        raise NotImplementedError("Area calculation not implemented for this shape")

class Rectangle(Shape):
    """A rectangle shape with length and width attributes."""
    def __init__(self, length, width):
        """Initialize rectangle with length and width.
        
        Args:
            length (float): The length of the rectangle
            width (float): The width of the rectangle
        """
        self.length = length
        self.width = width
    
    def area(self):
        """Calculate the area of the rectangle.
        
        Returns:
            float: The area of the rectangle (length × width)
        """
        return self.length * self.width

class Circle(Shape):
    """A circle shape with a radius attribute."""
    def __init__(self, radius):
        """Initialize circle with radius.
        
        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """Calculate the area of the circle.
        
        Returns:
            float: The area of the circle (π × radius²)
        """
        return pi * self.radius ** 2