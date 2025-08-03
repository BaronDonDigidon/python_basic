import re
from typing import List


def check_phone_numbers(phone_numbers: List[str]) -> None:
    """
    Проверяет список телефонных номеров на соответствие условиям:
    - Ровно 10 символов
    - Начинается с 8 или 9
    - Остальные символы — только цифры
    :param phone_numbers: список номеров в виде строк
    :type phone_numbers: List[str]
    :return: None (результат выводится в консоль)
    """
    pattern: str = r"[89]\d{9}"

    for i, number in enumerate(phone_numbers, start=1):
        if re.fullmatch(pattern, number):
            print(f"{i}-й номер: всё в порядке")
        else:
            print(f"{i}-й номер: не подходит")


numbers: List[str] = ['9999999999', '999999-999', '99999x9999']

check_phone_numbers(numbers)
