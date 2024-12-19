# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a variable to keep track of rows
row = 0

# While loop to iterate through each row
while row < size:
    # For loop to print asterisks for each column in the row
    for col in range(size):
        print("*", end="")
    # Print a newline after each row
    print()
    # Increment the row counter
    row += 1
