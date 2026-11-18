
contacts = {}

def add_contacts():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    if name in contacts:
        print("This contact already exists!")
    else:
        contacts[name] = phone
        print("Contact added successfully!")


def view_contacts():
    if not contacts:
        print("No contacts found!")
    else:
        for name, phone in contacts.items():
            print(f"Name: {name} | Phone: {phone}")


def search_contact():
    name = input("Enter contact name: ")

    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]}")
    else:
        print("Contact not found!")


def delete_contact():
    name = input("Enter contact name: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")


def chose():
    while True:
        print("\n===== Contact Book =====")
        print("1- Add Contact")
        print("2- View All Contacts")
        print("3- Search Contact")
        print("4- Delete Contact")
        print("5- Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contacts()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            delete_contact()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


chose()
