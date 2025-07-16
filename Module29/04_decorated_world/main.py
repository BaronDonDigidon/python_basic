from typing import Callable
import functools

def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    """
    Декоратор для декораторов.
    Позволяет передавать аргументы в любой декоратор.
    """
    @functools.wraps(decorator)
    def wrapper(*args, **kwargs) -> Callable:
        def real_decorator(func: Callable) -> Callable:
            return decorator(func, *args, **kwargs)
        return real_decorator
    return wrapper


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
    """
    Пользовательский декоратор, выводит переданные аргументы,
    затем вызывает оригинальную функцию.
    """
    @functools.wraps(func)
    def wrapper(*f_args, **f_kwargs):
        print(f"Переданные арги и кварги в декоратор: {args} {kwargs}")
        return func(*f_args, **f_kwargs)
    return wrapper



@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет,", text, num)


decorated_function("Юзер", 101)