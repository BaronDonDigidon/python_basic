import functools
from collections.abc import Callable
from typing import Any

# Список прав пользователя
user_permissions: list[str] = ['admin']


def check_permission(permission: str) -> Callable:
    """
    Декоратор, проверяющий наличие прав у пользователя для выполнения функции.
    :param permission: необходимое разрешение (например, 'admin')
    :type permission: str
    :return: обёртка вокруг функции, которая проверяет права перед выполнением
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            try:
                if permission not in user_permissions:
                    raise PermissionError("PermissionError")
                return func(*args, **kwargs)
            except PermissionError as exc:
                print(f"{exc}: У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}")

        return wrapper

    return decorator


@check_permission('admin')
def delete_site() -> None:
    """Удаление сайта (доступно только для админов)."""
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment() -> None:
    """Добавление комментария (требуется доступ от пользователя)."""
    print('Добавляем комментарий')


delete_site()
add_comment()