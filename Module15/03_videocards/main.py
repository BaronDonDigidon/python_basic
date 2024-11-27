number_cards: int = int(input("Введите количество видеокарт: "))




def card_adding(new_card_adding: int, card_list: list[int] = []) -> list[int]:
    """
    Функция создает новый список или добавляет в уже существующий в базу видеокарт присваивая им порядковый номер.
    :param new_card_adding: Целое число, кол-во добавляемых в базу видеокарт;
    :param card_list: Список видеокарт, необязательный параметр;
    :return: Возвращает список видеокарт с добавленными в базу номерами видеокарт.
    """
    for card_number in range(len(card_list) + 1, len(card_list) + new_card_adding + 1):
        card: int = int(input(f"Видеокарта {card_number}: "))
        card_list.append(card)
    print(f"Старый список видеокарт: {card_list}")
    return card_list




def max_card_deleter(card_list: list[int], max_card: int = 0) -> None:
    """
    Функция находит и удаляет наибольшие элементы списка.
    :param card_list: Список элементов представленных в виде целых чисел;
    :param max_card: Наибольший элемент списка;
    :return: Возвращает строку со списком новых видеокарт.
    """
    for card_number in range(len(card_list)):
        if card_list[card_number] > max_card:
            max_card = card_list[card_number]
    while max_card in card_list:
        card_list.remove(max_card)
    return print(f"Новый список видеокарт: {card_list}")




max_card_deleter(card_adding(number_cards))