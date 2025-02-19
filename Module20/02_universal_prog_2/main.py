from typing import List
iter_object_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
iter_object_2 = 'О Дивный Новый мир!'




def is_prime(num: int) -> bool:
    """
    Принимает на вход число если число простое возврашает True если нет False.
    :param num: число
    :return: True or False
    """
    if num < 2:
        return False


    for i in range(2, num):
        if num % i == 0:
            return False


    return True




def crypto(iter_object) -> List[any]:
    """
    Возвращающую список элементов итерируемого объекта (кортежа, строки, списка, словаря),
    у которых индекс — это простое число.
    :param iter_object: итерируемый объект
    :return: список элементов итерируемого объекта (кортежа, строки, списка, словаря),
    у которых индекс — это простое число.
    """
    return [elem for index, elem in enumerate(iter_object) if is_prime(index)]



# Выводим список элементов у которых индекс - это простое число
print(crypto(iter_object_1))
print(crypto(iter_object_2))