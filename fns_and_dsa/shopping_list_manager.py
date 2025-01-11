def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            item = input("Enter the item name: ")
            shopping_list.append(item)
            print(f"Added {item} to the list")
            
        elif choice == 2:
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"Removed {item} from the list")
            else:
                print("Item not found in the list")
            
        elif choice == 3:
            if shopping_list:
                print("\nShopping List:")
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("Shopping list is empty")
            
        elif choice == 4:
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()