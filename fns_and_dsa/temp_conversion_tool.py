#!/usr/bin/env python3
"""
Temperature conversion tool demonstrating global variables and scope
"""

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit temperature to Celsius"""
    try:
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
        return celsius
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def convert_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit"""
    try:
        celsius = float(celsius)
        fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
        return fahrenheit
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def main():
    """Main program function"""
    while True:
        try:
            # Get temperature input
            temperature = input("Enter the temperature to convert: ")
            
            # Get unit input
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
            
            # Validate unit input
            if unit.upper() not in ['C', 'F']:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
                continue
                
            # Perform conversion based on unit
            if unit.upper() == 'F':
                result = convert_to_celsius(temperature)
                print(f"{float(temperature)}°F is {result}°C")
            else:
                result = convert_to_fahrenheit(temperature)
                print(f"{float(temperature)}°C is {result}°F")
            
            break
            
        except ValueError as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()