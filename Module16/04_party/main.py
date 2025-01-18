guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']




def guest_adder(list_1: list[str], key_word: str, guest_name: str) -> None:
    """
    Функция добавляет имя в список если кол-во гостей не превышает 6 человек или удаляет имя из списка.
    :param list_1:
    :param key_word:
    :param guest_name:
    :return: None
    """
    if len(list_1) == 6 and key_word == "пришёл":
        print(f"Прости, {guest_name}, но мест нет.")
    elif key_word == "пришёл":
        list_1.append(guest_name)
        print(f"Привет, {guest_name}")
    elif key_word == "ушёл":
        list_1.remove(guest_name)
        print(f"Пока, {guest_name}")




def menu(list_1: list [str]) -> None:
    """
    Фунцкия запускает цикл который показывает сколько на вечеринке гостей, запрашивает пришёл или ушёл гость и
    добавляет гостя на вечеринку если количество гостей не превышает 6 человек.
    :param list_1: Список гостей
    :return: None
    """
    while True:
        print(f"Сейчас на вечеринке {len(list_1)} человек {list_1}")
        guest_key: str = input("Гость пришёл или ушёл? ")
        if guest_key.lower() == "пора спать":
            print("Вечеринка закончилась, пора спать.")
            break
        guest_name: str = input("Имя гостя: ")
        guest_adder(guests, guest_key, guest_name)




menu(guests)