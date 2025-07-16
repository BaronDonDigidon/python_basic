from typing import Callable, Optional


class App:
    """
    Класс App хранит маршруты (пути) и соответствующие функции-обработчики.
    """

    def __init__(self) -> None:
        self.routes: dict[str, Callable[[], str]] = {}


    def get(self, route: str) -> Optional[Callable[[], str]]:
        """
        Получение функции по маршруту, если она зарегистрирована.

        :param route: путь, по которому ищется функция
        :return: функция или None, если путь не найден
        """
        return self.routes.get(route)


# Создаём экземпляр приложения
app = App()


# --- 👇 Глобальная функция-декоратор ---
def callback(route: str) -> Callable[[Callable[[], str]], Callable[[], str]]:
    """
    Глобальный декоратор для регистрации функции-обработчика маршрута в app.

    :param route: путь
    :return: функция-декоратор
    """
    def decorator(func: Callable[[], str]) -> Callable[[], str]:
        app.routes[route] = func
        return func
    return decorator


# Регистрируем функцию-обработчик
@callback('//')
def example() -> str:
    """Пример обработчика маршрута."""
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


# --- Основной код ---
route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
