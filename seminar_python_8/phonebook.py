from os import listdir


class Contact:
    def __init__(self, surname, name, patronymic, phone_number):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone_number = phone_number

    def __repr__(self):
        return f"{self.surname} {self.name} {self.patronymic} {self.phone_number}"


class Phonebook:
    def __init__(self, file_name: str = "telephone_book.txt"):
        self.file_name = file_name

    def read_file(self):
        if self.file_name in listdir():
            with open(self.file_name, 'r', encoding='UTF-8') as f:
                print(f"Список контактов:\n {f.read()}\n")
        else:
            print("Списка контактов нет")

    def add_contact(self, contact: Contact):
        with open(self.file_name, "a", encoding="utf-8") as f:
            f.write(f"{contact}\n")
            print(f"Контакт {contact} добавлен в телефонный справочник")

    def find_contact(self, query: str):
        with open(self.file_name, "r", encoding="utf-8") as f:
            result = [line for line in f if query in line]
        print(f"Найденно {len(result)} контактов")
        print(*result, sep='') if result else print("Контактов не найденно")

    def delete_contact(self, query: str):
        with open(self.file_name, "r+", encoding="utf-8") as f:
            result = [line for line in f if query not in line]
        with open(self.file_name, "w", encoding="utf-8") as f:
            [f.write(f"{item}") for item in result if item]
            print(f"Контакт {query} удален")

    def edit_contact(self, query: str, new_data: str):
        with open(self.file_name, "r+", encoding="utf-8") as f:
            result = []
            for line in f:
                if query in line:
                    line = line.replace(query, new_data)
                result.append(line)
        with open(self.file_name, "w", encoding="utf-8") as f:
            [f.write(f"{item}") for item in result if item]
            print(f"{query} заменен на {new_data}")


if __name__ == '__main__':
    contact_1 = Contact("Курочкин", "Олег", "Тимофеевич", "+7 906 745 8980")
    phonebook = Phonebook()
    phonebook.add_contact(contact_1)
    phonebook.read_file()
    phonebook.find_contact("Чесноков")
    phonebook.delete_contact("Кузнецова Софья")
    phonebook.edit_contact("Агапов", "Андреев")
