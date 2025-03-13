from typing import Any




def custom_sum(*args: Any) -> int:
    """
    Функция принимает набор чисел или список с числами и возвращает их сумму.
    :param args: Числа или список с числами.
    :return: Число.
    """
    total = 0
    for num in args:
        if isinstance(num, (int, float)):
            total += num
        elif isinstance(num, (list, tuple)):
            total += custom_sum(*num)
    return total




print(custom_sum([[1, 2, [3]], [1], 3]))
print(custom_sum(1, 2, 3, 4, 5))
