from contact import Contact


class PhoneBook:
    def __init__(self, file_name, encoding='utf-8'):
        """
        Создает объект телефонной книги.

        :param file_name: Имя файла для хранения данных
        :param encoding: Кодировка файла
        """
        self.file_name = file_name
        self.encoding = encoding

    def add_data(self, contact: Contact):
        """
        Добавляет новый контакт в телефонную книгу.

        :param contact: Объект контакта для добавления
        """
        with open(self.file_name, "a") as file:
            file.write(
                f"{contact.last_name}:{contact.first_name}:{contact.middle_name}:"
                f"{contact.organization}:{contact.work_phone}:{contact.personal_phone}\n"
            )

    def display_data(self, page_size: int):
        """
        Выводит записи из телефонной книги постранично.

        :param page_size: Количество записей на одной странице
        """
        with open(self.file_name, "r", encoding=self.encoding) as file:
            contacts = file.readlines()
            num_contacts = len(contacts)
            current_page = 1
            start_index = 0

            for i in range(start_index, num_contacts, page_size):
                for contact in contacts[i:i + page_size]:
                    fields = contact.strip().split(':')
                    print(contact)
                    if len(fields) == 6:  # Проверяем, что у нас есть все 6 полей
                        last_name, first_name, middle_name, organization, work_phone, personal_phone = fields
                        print("Last Name:", last_name)
                        print("First Name:", first_name)
                        print("Middle Name:", middle_name)
                        print("Organization:", organization)
                        print("Work Phone:", work_phone)
                        print("Personal Phone:", personal_phone)
                        print("")
                    else:
                        print("Invalid data format:", contact)
                command = input("Enter 'n' for next page, 'q' to quit: ")
                if command == "n":
                    current_page += 1
                    start_index += page_size
                elif command == "q":
                    break

    def search_contacts(self, search_term: str):
        """
        Поиск контактов по заданному поисковому термину.

        :param search_term: Поисковый термин
        """
        found_contacts = []
        with open(self.file_name, "r", encoding=self.encoding) as file:
            contacts = file.readlines()
            for contact in contacts:
                if search_term.lower() in contact.lower():
                    found_contacts.append(contact)
        print(' '.join(''.join(found_contacts).strip().split(':')))

    def edit_contact(self, search_term: str):
        """
        Редактирование контакта, соответствующего заданному поисковому термину.

        :param search_term: Поисковый термин
        """
        found_contacts = []
        with open(self.file_name, "r", encoding=self.encoding) as file:
            contacts = file.readlines()
            for i, contact in enumerate(contacts):
                if search_term.lower() in contact.lower():
                    found_contacts.append((i, contact))

        if found_contacts:
            print("Found contacts:")
            for i, contact in found_contacts:
                fields = contact.strip().split(":")
                last_name, first_name, middle_name, organization, work_phone, personal_phone = fields
                print("Index:", i)
                print("Last Name:", last_name)
                print("First Name:", first_name)
                print("Middle Name:", middle_name)
                print("Organization:", organization)
                print("Work Phone:", work_phone)
                print("Personal Phone:", personal_phone)
                print("")

            edit_index = int(input("Enter the index of the contact to edit: "))
            if 0 <= edit_index < len(contacts):
                fields = contacts[edit_index].strip().split(":")
                last_name, first_name, middle_name, organization, work_phone, personal_phone = fields
                new_data = Contact(
                    input(f"Enter new Last Name ({last_name}): ") or last_name,
                    input(f"Enter new First Name ({first_name}): ") or first_name,
                    input(f"Enter new Middle Name ({middle_name}): ") or middle_name,
                    input(f"Enter new Organization ({organization}): ") or organization,
                    input(f"Enter new Work Phone ({work_phone}): ") or work_phone,
                    input(f"Enter new Personal Phone ({personal_phone}): ") or personal_phone
                )
                contacts[edit_index] = f"{new_data.last_name}:{new_data.first_name}:{new_data.middle_name}:\
{new_data.organization}:{new_data.work_phone}:{new_data.personal_phone}\n"

                with open(self.file_name, "w", encoding=self.encoding) as file:
                    file.writelines(contacts)

                print("Contact edited successfully.")
            else:
                print("Invalid index.")
        else:
            print("No contacts found.")

