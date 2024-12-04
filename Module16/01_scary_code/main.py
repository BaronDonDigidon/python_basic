basic_list = [1, 5, 3]
side_list_1 = [1, 5, 1, 5]
side_list_2 = [1, 3, 1, 5, 3, 3]

def list_extender_and_delet_search_num(basic_list: list[int], side_list: list[int],
                                       delete_num: int, key: int = 1) -> int:
    """
    Функция объединяет два списка после чего находит искомых чисел, если ключ
    равен 1 удаляет заданные числа из объединенного списка.
    :param basic_list: базовый список чисел
    :param side_list: побочный список чисел
    :param delete_num: искомое число
    :param key: ключ
    :return: количество искомых чисел в списке
    """
    basic_list.extend(side_list)
    counter_delete_num: int = basic_list.count(delete_num)
    if key:
        while delete_num in basic_list:
            basic_list.remove(delete_num)
    return counter_delete_num




def displayer() -> None:
    """
    Функция использует фунцкию list_extender_and_delet_search_num и выводит на экран количество искомых чисел,
    после двух операций объединения вывовдит итоговый список.
    :return:
    """
    print(f"Количество цифр 5 при первом объединении"
          f" {list_extender_and_delet_search_num(basic_list, side_list_1, 5, 1)}")
    print(f"Количество цифр 3 при втором объединении"
          f" {list_extender_and_delet_search_num(basic_list, side_list_2, 3, 0)}")
    print(f"Итоговый список: {basic_list}")



displayer()