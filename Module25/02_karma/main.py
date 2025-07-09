from typing import Final, TextIO
from random import randint, choice

class LifeException(Exception):
    """Базовый класс для исключений жизни"""
    def __init__(self, message: str = "Произошла ошибка в жизненном цикле"):
        self.message = message
        super().__init__(message)


class KillError(LifeException):
    """Исключение: убийство"""
    def __init__(self, message: str = "Неожиданное убийство!"):
        super().__init__(message)


class DrunkError(LifeException):
    """Исключение: опьянение"""
    def __init__(self, message: str = "Случай алкогольного опьянения"):
        super().__init__(message)


class CarCrashError(LifeException):
    """Исключение: авария"""
    def __init__(self, message="Автомобильная авария"):
        super().__init__(message)


class GluttonyError(LifeException):
    """Исключение: обжорство"""
    def __init__(self, message="Случай чревоугодия"):
        super().__init__(message)


class DepressionError(LifeException):
    """Исключение: депрессия"""
    def __init__(self, message="Приступ депрессии"):
        super().__init__(message)


class User:
    """
    Базовый класс пользователя.

    Args:
        name (str): Имя пользователя
    """
    def __init__(self, name: str) -> None:
        """
        Инициализация пользователя.
        :param name: имя пользователя
        :type name: str
        """
        self.__name = name
        self.__karma_point = 0


    @property
    def karma_point(self) -> int:
        """
        Гетер для __karma_point.
        :return: __karma_point
        :rtype: int
        """
        return self.__karma_point


    @karma_point.setter
    def karma_point(self, enlightenment_point: int) -> None:
        """
        Сеттер для __karma_point
        :param enlightenment_point: очки кармы
        :type enlightenment_point: int
        """
        if isinstance(enlightenment_point, int):
            self.__karma_point = enlightenment_point
        else:
            raise ValueError("Неверное значение")


    @property
    def name(self) -> str:
        """
        Гетер для __name.
        :return: __name
        :rtype: str
        """
        return self.__name


    @name.setter
    def name(self, name):
        """
        Сеттер для __name
        :param name: очки кармы
        :type name: str
        """
        if not isinstance(name, str):
            raise ValueError("Имя должно быть строкой")
        self.__name = name


class Enlightenment:
    """
    Базовый класс пути к просветлению.

    Atributes:
        KARMA_CONSTANT (int): константа очков кармы которой необходимо достич чтоб обрести просветление.
    """
    KARMA_CONSTANT: Final = 500


    @staticmethod
    def probability_exception() -> bool:
        """
        Статический метод выдающий с шансом 10% True или False.
        :return: True or False
        :rtype: bool
        """
        return randint(1, 10) == 1


    @staticmethod
    def random_exception_choice() -> LifeException:
        """
        Статический метод возвращает случайную ошибку из списка.
        :return: случайная ошибка из списка.
        :rtype: LifeException
        """
        return choice([
            KillError(),
            DrunkError(),
            CarCrashError(),
            GluttonyError(),
            DepressionError()
        ])

    @staticmethod
    def log_error(file: TextIO, day: int, user: User, exc: LifeException) -> None:
        """
        Выводит сообщение об ошибки в день получения кармы и записывает ее в лог файл.
        :param file: лог файл с ошибками.
        :type file: TextIO
        :param day: номер дня на пути к проствелению
        :type day: int
        :param user: пользователь
        :type user: User
        :param exc: исключения в жизни
        :type exc: LifeException
        :return:
        """
        message = (f"День {day}. У пользователя {user.name} возникла ошибка: "
                   f"{exc.__class__.__name__} - {exc}")
        print(message)
        file.write(message + "\n")


    def karma_announcement(self, user_data: User, day: int) -> None:
        """
        Анонсирует изменение кармы.
        :param user_data: данные пользователя
        :type user_data: User
        :param day: день на пути к просветлению
        :type day: int
        """
        if user_data.karma_point < self.KARMA_CONSTANT:
            print(f"День {day} пути к просветлению. Карма пользователя  "
                  f"{user_data.name}: {user_data.karma_point}")
        else:
            print(f"Поздравляю {user_data.name} вы достигли просветления за {day} дней! "
                  f"Ваша карма равна {user_data.karma_point}.")

    def karma_value_protect(self, user_data: User) -> None:
        """
        Защищает значение кармы от превышения константы KARMA_CONSTANT
        :param user_data: данные пользователя
        :type user_data: User
        """
        if user_data.karma_point > self.KARMA_CONSTANT:
            user_data.karma_point = self.KARMA_CONSTANT

    def one_day(self) -> LifeException | int:
        """
        Возвращает количество очков кармы от 1 до 7 или выдает ошибку с вероятность. 10%
        """
        if self.probability_exception():
            raise self.random_exception_choice()
        else:
            return randint(1,  7)



def main():
    enlightenment_path = Enlightenment()
    # Запрашиваем имя пользователя
    user_name: str = input("Введите имя пользователя: ").strip()
    user: User = User(user_name)
    day: int = 1

    with open("karma.log", "w", encoding="UTF-8") as file_log:
        while user.karma_point < enlightenment_path.KARMA_CONSTANT:
            try:
                # Вычисляем количество полученной сегодня кармы или получаем ошибку
                karma_today = enlightenment_path.one_day()
                user.karma_point += karma_today
                # Защита кармы от перенасыщения
                enlightenment_path.karma_value_protect(user)
                # Анонсируем изменение кармы
                enlightenment_path.karma_announcement(user, day)
            except LifeException as exc:
                # Запись ошибки в файл
                enlightenment_path.log_error(file_log, day, user, exc)
            day += 1


if __name__ == "__main__":
    main()
