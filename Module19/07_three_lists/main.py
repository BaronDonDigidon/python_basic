from typing import List

array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]




def looking_for_a_match_1(list_1: List[int], list_2: List[int], list_3: List[int]) -> None:
    """
    Находит совпадения между тремя списками и выводит их.
    :param list_1: Первый список целых чисел.
    :param list_2: Второй список целых чисел.
    :param list_3: Третий список целых чисел.
    :return: None
    """
    coincidences_sets = set(list_1) & set(list_2) & set(list_3)
    text = "Решение с множествами: "
    for i_set in coincidences_sets:
        text += " {0}".format(i_set)
    print(text)




def finding_the_difference_1(list_1: List[int], list_2: List[int], list_3: List[int]) -> None:
    """
    Находит элементы из первого списка, которые отсутствуют во втором и третьем списках.
    :param list_1: Первый список целых чисел.
    :param list_2: Второй список целых чисел.
    :param list_3: Третий список целых чисел.
    :return: None
    """
    difference_sets = set(list_1) - set(list_2) - set(list_3)
    text = "Решение с множествами: "
    for i_set in difference_sets:
        text += " {0}".format(i_set)
    print(text)




def looking_for_a_match_2(list_1: List[int], list_2: List[int], list_3: List[int]) -> None:
    """
    Находит совпадения между тремя списками без использования множеств и выводит их.
    :param list_1: Первый список целых чисел.
    :param list_2: Второй список целых чисел.
    :param list_3: Третий список целых чисел.
    :return: None
    """
    text = "Решение без множеств: "
    for item in set(list_1):
        if item in set(list_2) and item in set(list_3):
            text += " {0}".format(item)
    print(text)




def finding_the_difference_2(list_1: List[int], list_2: List[int], list_3: List[int]) -> None:
    """
    Находит элементы из первого списка, которые отсутствуют во втором и третьем списках без использования множеств.
    :param list_1: Первый список целых чисел.
    :param list_2: Второй список целых чисел.
    :param list_3: Третий список целых чисел.
    :return: None
    """
    text = "Решение без множеств: "
    for item in set(list_1):
        if item not in set(list_2) and item not in set(list_3):
            text += " {0}".format(item)
    print(text)




def tree_lists(list_1: List[int], list_2: List[int], list_3: List[int]) -> None:
    """
    Основная функция для выполнения задач по нахождению совпадений и различий между тремя списками.
    :param list_1: Первый список целых чисел.
    :param list_2: Второй список целых чисел.
    :param list_3: Третий список целых чисел.
    :return: None
    """
    print("Задача 1")
    looking_for_a_match_2(list_1, list_2, list_3)
    looking_for_a_match_1(list_1, list_2, list_3)
    print("Задача 2")
    finding_the_difference_2(list_1, list_2, list_3)
    finding_the_difference_1(list_1, list_2, list_3)




tree_lists(array_1, array_2, array_3)