from typing import Tuple, Any


def tpl_sorter(tpl: Tuple[int]) -> Tuple[int]:
    """
    Сортирует по возрастанию кортеж
    :param tpl: кортеж целых чисел
    :return: отсортированный кортеж
    """
    list_tpl = list(tpl)
    for i in range(len(list_tpl)):
        for j in range(0, len(list_tpl) - i - 1):
            if list_tpl[j] > list_tpl[j + 1]:
                list_tpl[j], list_tpl[j + 1] = list_tpl[j + 1], list_tpl[j]
    return tuple(list_tpl)




def tpl_sort(tpl) -> Tuple[Any]:
    """
    Сортирует по возрастанию кортеж, состоящий из целых чисел, и возвращает его отсортированным.
    Если хотя бы один элемент не является целым числом, то функция возвращает исходный кортеж
    :param tpl: Tuple[Any]
    :return: Tuple[Any]
    """
    for elem in tpl:
        if type(elem) != int:
            return tpl
    return tpl_sorter(tpl)




# tpl = (6, 3, -1, 8, 4, 10, -5)

# print(tpl_sort(tpl))