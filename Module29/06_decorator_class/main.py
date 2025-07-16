import time
from typing import Callable, Any


class LoggerDecorator:
    """
    Класс-декоратор для логирования вызовов функции:
    - выводит имя функции
    - аргументы вызова
    - результат работы функции
    - время выполнения функции
    """
    def __init__(self, func: Callable) -> None:
        self.func = func

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        print(f"Вызов функции {self.func.__name__}")
        print(f"Аргументы: {args}, {kwargs}")
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        print(f"Результат: {result}")
        print(f"Время выполнения: {end_time - start_time} секунд")
        return result



@LoggerDecorator
def complex_algorithm(arg1: int, arg2: int) -> int:
    """
    Пример "сложного" алгоритма для демонстрации декоратора.
    """
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
            result += i + j
    return result


# Пример вызова функции с применением декоратора
result = complex_algorithm(10, 50)