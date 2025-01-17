def creating_list(list_1: int = [], list_2: int = [], counter: int = 0) -> int:
    """
    ФУнкция принимает два обязательных параметра списки с размерами пар коньков которые есть наличии и
    список с размерами ног людей,  возвращает кол-во людей которые могут надеть коньки.
    :param list_1: список с размерами пар коньков в наличии
    :param list_2: список с размерами ног людей
    :param counter: кол-во людей которые могут надеть коньки
    :return: int
    """
    for size in range(len(list_2)):
        if list_2[size] in list_1:
            list_1.remove(list_2[size])
            counter += 1
    return counter




def the_possibility_of_renting(skates_list: list[int] = [], legs_list: list[int] = []) -> None:
    """
    Функция создает два спика чисел с размерами коньков и размерами ног людей, используя функцию
    creating_list подсчитывает и выводит кол-во людей которые могут одеть коньки.
    :param skates_list: Лист с парами коньков.
    :param legs_list: Лист с размерами ног людей
    :return: None
    """
    number_of_skates: int = int(input(f"Кол-во коньков: "))
    for skates in range(1, number_of_skates + 1):
        skates_size: int = int(input(f"Размер {skates}-й пары: "))
        skates_list.append(skates_size)
    number_of_people: int = int(input(f"Кол-во людей: "))
    for legs in range(1, number_of_people + 1):
        legs_size: int = int(input(f"Размер ноги {legs}-го человека: "))
        legs_list.append(legs_size)
    print(f"Наибольшее кол-во людей, которые могут взять ролики: {creating_list(skates_list, legs_list)}")




the_possibility_of_renting()