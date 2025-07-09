from typing import Any

class MyDict(dict):
    """
    Класс MyDict. Родитель dict.
    Расширяющий поведение стандартного словаря.
    """
    def get(self, key: Any, default: int = 0) -> Any:
        """
        Переорпделенный класс get.
        :param key: ключ словаря
        :type key: Any
        :param default: значение которое возвращает функция если в словаре нет такого ключа.
        :return: значение по ключу или KeyError
        :rtype: Any
        """
        try:
            return self[key]
        except KeyError:
            return default

# Тест
test_dict = MyDict({'Банан': 3, 'Ананас': 4})
print(test_dict.get('Яблоко'))
print(test_dict.get('Банан'))

