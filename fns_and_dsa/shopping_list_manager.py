def display_menu():
    """Function to display menu options"""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    return

def main():
    # Initialize the shopping list as an empty array
    shopping_list = []
    
    while True:
        # Call the display_menu function
        display_menu()
        
        try:
            # Implement choice input as a number
            choice = int(input("Enter your choice (1-4): "))
            
            if choice == 1:
                item = input("Enter the item name: ").strip()
                shopping_list.append(item)
                print(f"'{item}' has been added to the list.")
            
            elif choice == 2:
                if not shopping_list:
                    print("The shopping list is empty.")
                else:
                    item = input("Enter the item name to remove: ").strip()
                    if item in shopping_list:
                        shopping_list.remove(item)
                        print(f"'{item}' has been removed from the list.")
                    else:
                        print(f"'{item}' was not found in the list.")
            
            elif choice == 3:
                if not shopping_list:
                    print("The shopping list is empty.")
                else:
                    print("\nCurrent Shopping List:")
                    for index, item in enumerate(shopping_list, 1):
                        print(f"{index}. {item}")
            
            elif choice == 4:
                print("\nThank you for using Shopping List Manager. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()