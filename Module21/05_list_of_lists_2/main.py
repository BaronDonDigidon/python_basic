from typing import Any


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]




def list_straightening(list_num: list[Any], new_list_num: list[int]=None) -> list[int]:
    """
    Функция принимает список с неограниченным кол-во эллементов и "выпрямляет" его.
    :param list_num: Лисчт чисел с разными уровнями.
    :param new_list_num: Новый лист чисел.
    :return: Возвращает "выпрямленный" лист чисел.
    """
    if new_list_num is None:
        new_list_num = []


    for item in list_num:
        if isinstance(item, int):
            new_list_num.append(item)
        elif isinstance(item, list):
            list_straightening(item, new_list_num)


    return new_list_num




print(list_straightening(nice_list))





