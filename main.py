from contact import Contact
from phonebook import PhoneBook


def main():
    """
    Главная функция для работы с телефонной книгой.
    """
    phone_book = PhoneBook("data.txt")
    while True:
        print("\nPhone Book Menu:")
        print("1. Display Contacts")
        print("2. Add Contact")
        print("3. Search Contacts")
        print("4. Edit Contact")
        print("5. Quit")

        choice = input("Select an option: ")

        if choice == "1":
            page_size = int(input("Enter page size: "))
            phone_book.display_data(page_size)
        elif choice == "2":
            last_name = input("Enter Last Name: ")
            first_name = input("Enter First Name: ")
            middle_name = input("Enter Middle Name: ")
            organization = input("Enter Organization: ")
            work_phone = input("Enter Work Phone: ")
            personal_phone = input("Enter Personal Phone: ")
            new_contact = Contact(last_name, first_name, middle_name, organization, work_phone, personal_phone)
            phone_book.add_data(new_contact)
        elif choice == "3":
            search_term = input("Enter search term: ")
            phone_book.search_contacts(search_term)
        elif choice == "4":
            edit_term = input("Enter search term for contact to edit: ")
            phone_book.edit_contact(edit_term)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
