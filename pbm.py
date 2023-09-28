import os

# Create a new phonebook file
def create_phonebook_file(file_name):
    with open(file_name, 'w') as file:
        pass
    
# Read contacts from a phonebook file
def read_phonebook_file(file_name):
    try:
        with open(file_name, 'r') as file:
            contacts = file.readlines()
        return contacts
    except FileNotFoundError:
        print("File not found. Creating a new phonebook.")
        create_phonebook_file(file_name)
        return []

# Save contacts to a phonebook file
def save_phonebook_file(file_name, contacts):
    with open(file_name, 'w') as file:
        file.writelines(contacts)

# Add a contact to the list
def add_contact(contacts, name, number):
    contacts.append(f"{name} {number}\n")

# Delete a contact by name
def delete_contact(contacts, name):
    new_contacts = [contact for contact in contacts if not contact.startswith(name + ' ')]
    return new_contacts

def main():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    current_file = None
    
    while True:
        print("Phonebook Options:")
        print("1. Create a new phonebook file")
        print("2. Open an existing phonebook file")
        print("3. Add a contact")
        print("4. Delete a contact by name")
        print("5. Delete all contacts")
        print("6. Delete the phonebook file")
        print("7. Exit\n")
        
        if current_file:
            print(f"Current Phonebook: {current_file}\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            file_name = input("Enter the name of the new phonebook file with .txt at the end: ")
            file_path = os.path.join(script_directory, file_name)
            create_phonebook_file(file_path)
            contacts = []
            current_file = file_path
        elif choice == "2":
            file_name = input("Enter the name of the phonebook file (e.g., phonebook.txt): ")
            file_path = os.path.join(script_directory, file_name)
            if not os.path.exists(file_path):
                print("File not found.")
                continue
            contacts = read_phonebook_file(file_path)
            current_file = file_path
        elif choice == "3":
            if current_file is None:
                print("Please create or open a phonebook file first.")
                continue
            name = input("Enter the contact's name: ")
            number = input("Enter the contact's number: ")
            add_contact(contacts, name, number)
            save_phonebook_file(current_file, contacts)
        elif choice == "4":
            if current_file is None:
                print("Please create or open a phonebook file first.")
                continue
            name = input("Enter the name of the contact to delete: ")
            contacts = delete_contact(contacts, name)
            save_phonebook_file(current_file, contacts)
        elif choice == "5":
            if current_file is None:
                print("Please create or open a phonebook file first.")
                continue
            contacts = [] # Delete all contacts
            save_phonebook_file(current_file, contacts) # Save the empty list to clear the file
        elif choice == "6":
            if current_file is None:
                print("Please create or open a phonebook file first.")
                continue
            os.remove(current_file) # Delete the phonebook file
            current_file = None
            contacts = [] # Reset the contacts list
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please select a valid option.")


main()
