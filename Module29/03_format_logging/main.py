import functools
import time
from datetime import datetime
from typing import Callable, Any, Type, Union


def log_methods(_cls: Union[Type, None] = None, *, dt_format: str = "%Y-%m-%d %H:%M:%S") -> Callable[[Type], Type]:
    """
    Универсальный декоратор класса:
    - работает как @log_methods
    - и как @log_methods(format='...')
    Args:
        _cls: Экземпляр класса
        dt_format: Формат вывода даты и времени
    """

    def class_decorator(cls: Type) -> Type:
        for attr_name, attr_value in cls.__dict__.items():
            if attr_name.startswith("__") or not callable(attr_value):
                continue

            original_method = attr_value

            @functools.wraps(original_method)
            def wrapper(self, *args: Any, __method=original_method, **kwargs: Any) -> Any:
                start_time = time.time()
                now_str = datetime.now().strftime(dt_format)
                cls_name = self.__class__.__name__
                print(f"- Запускается '{cls_name}.{__method.__name__}'. Дата и время запуска: {now_str}")
                result = __method(self, *args, **kwargs)
                end_time = time.time()
                elapsed = end_time - start_time
                print(f"- Завершение '{cls_name}.{__method.__name__}', время работы = {elapsed:.3f}s")
                return result

            setattr(cls, attr_name, wrapper)
        return cls

    if _cls is not None and isinstance(_cls, type):
        return class_decorator(_cls)

    return class_decorator


@log_methods("%b %d %Y - %H:%M:%S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("%Y %d %b - %H:%M:%S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
