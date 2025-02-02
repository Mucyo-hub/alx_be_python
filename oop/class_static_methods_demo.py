class Calculator:
    """
    A calculator class demonstrating the use of class methods and static methods.
    
    Class Attributes:
        calculation_type (str): Describes the type of calculations performed
    """
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        Prints the calculation type before performing multiplication.
        
        Args:
            cls: Class reference (automatically passed)
            a: First number
            b: Second number
            
        Returns:
            The product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b