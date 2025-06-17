contacts = {}

while True:
    print('\nContact Book App')
    print('1. Create Contact')
    print('2. View Contact')
    print('3. Update Contact')
    print('4. Delete Contact')
    print('5. Search Contact')
    print('6. Count Contact')
    print('7. Exit')

    choice = input('Enter your choice = ')
    
    if choice == '1':
        name = input("Enter your name: ")
        if name in contacts:
            print(f"Contact name {name} already exists!")
        else:
            age = input("Enter age: ")
            email = input("Enter email: ")
            number = input("Enter mobile number: ")
            contacts[name] = {'age': int(age), 'email': email, 'number': number}
            print(f"Contact {name} has been created successfully!")

    elif choice == '2':
        name_input = input("Enter contact name to view: ")
        found = False
        for name in contacts:
            if name.lower() == name_input.lower():
                contact = contacts[name]
                print(f"Name: {name}, Age: {contact['age']}, Email: {contact['email']}, Number: {contact['number']}")
                found = True
                break
        if not found:
            print("Contact not found!")


    elif choice == '3':
        name = input("Enter contact name to update details: ")
        if name in contacts:
            age = input("Enter updated age: ")
            email = input("Enter updated email: ")
            number = input("Enter updated mobile number: ")
            contacts[name] = {'age': int(age), 'email': email, 'number': number}
            print(f"Contact {name} has been updated.")
        else:
            print("Contact not found!")

    elif choice == '4':
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact name {name} has been deleted successfully!")
        else:
            print("Contact not found!")   

    elif choice == '5':
        search_name = input("Enter contact name to search: ")
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"Found - Name: {name}, Age: {contact['age']}, Email: {contact['email']}, Number: {contact['number']}")
                found = True
        if not found:
            print("No contact found with that name!")       
            
    elif choice == '6':
        print(f"Total number of contacts in your book are: {len(contacts)}")

    elif choice == '7':
        print("Goodbye! Closing the program...")
        break
    
    else:
        print("Invalid input!")
