import math
from typing import List, Optional




def get_sage_sqrt(number: Optional[int | float]) -> float| str:
    """
    Функция принимает на вход число и возвращает корень квадратный из переданного числа.
    :param number: число.
    """
    try:
        number = float(number)
        if number >= 0:
            return math.sqrt(number)
        else:
            return -math.sqrt(abs(number))
    except ValueError as ve:
        return f"Ошибка значения: {ve}"
    except TypeError as te:
        return f"Ошибка типа: {te}"
    except Exception as exc:
        return f"Произошла непредвиденная ошибка: {exc}"




# Тестовые случаи
numbers: List[any] = [16, 25, -9, 0, 4.5, "abc"]


for number in numbers:
    result: float | str = get_sage_sqrt(number)
    print(f"Квадратный корень numbers {number}: {result}")