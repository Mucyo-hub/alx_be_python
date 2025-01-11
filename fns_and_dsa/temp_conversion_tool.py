#!/usr/bin/env python3
"""
Temperature conversion tool that demonstrates variable scope using global conversion factors
"""

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FREEZING_POINT_OFFSET = 32

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit temperature to Celsius
    Args:
        fahrenheit (float): Temperature in Fahrenheit
    Returns:
        float: Temperature in Celsius
    """
    try:
        return (float(fahrenheit) - FREEZING_POINT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius temperature to Fahrenheit
    Args:
        celsius (float): Temperature in Celsius
    Returns:
        float: Temperature in Fahrenheit
    """
    try:
        return (float(celsius) * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_OFFSET
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def main():
    """Main program function"""
    try:
        # Get temperature input from user
        temp = input("Enter the temperature to convert: ")
        
        # Get temperature unit from user
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
        
        # Validate unit input
        if unit not in ['C', 'F']:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            
        # Perform conversion based on input unit
        if unit == 'F':
            converted_temp = convert_to_celsius(temp)
            print(f"{float(temp)}°F is {converted_temp}°C")
        else:
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{float(temp)}°C is {converted_temp}°F")
            
    except ValueError as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()