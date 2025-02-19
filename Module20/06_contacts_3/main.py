from typing import Dict, Tuple




def adds_a_contact(contact_dict: Dict[Tuple[str,str], int]) -> None | Dict[Tuple[str,str], int]:
    """

    :param contact_dict:
    :return:
    """
    contact_key = input("Введите имя и фамилию контакта (через пробел): ").split()


    if contact_key in contact_dict.values():
        print("Такой человек уже есть в контактах.")


    phone_number = int(input("Введите номер телефона: "))
    contact_dict[tuple(contact_key)] = phone_number
    return contact_dict




def contact_searcher(contact_dict) -> None:
    """
    Функция принимает словарь с контактами ищет и выводит данные контакта по фамилии.
    :param contact_dict: Словарь с контактами.
    :return: Выводит все контакты с запрашиваемой фамилией.
    """
    surname: str = input("Введите фамилию для поиска: ")
    found = False


    for i_name in contact_dict:
        if surname.lower() in i_name[1].lower():
            print(i_name, contact_dict[i_name])
            found = True


    if not found:
        print("Контакты с такой фамилией не найдены.")




def menu():
    contact_dict = {}
    while True:
        print(f"Введите номер действия: \n"
              f"1. Добавить контакт \n"
              f"2. Найти человека\n")


        comand = int(input())


        if comand == 1:
            adds_a_contact(contact_dict)
            print(f"Текущий словарь контактов: {contact_dict}")
        elif comand == 2:
            contact_searcher(contact_dict)




menu()