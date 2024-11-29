def contact_book():
    contacts = {}
    while True:
        print("\nContact Book Options:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            number = input("Enter phone number: ")
            contacts[name] = number
            print("Contact added.")
        elif choice == '2':
            print("\nYour Contacts:")
            for name, number in contacts.items():
                print(f"{name}: {number}")
        elif choice == '3':
            search_name = input("Enter name to search: ")
            if search_name in contacts:
                print(f"{search_name}: {contacts[search_name]}")
            else:
                print("Contact not found.")
        elif choice == '4':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice.")

contact_book()
