from typing import Final, TextIO
from random import randint, choice

class LifeException(Exception):
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
        if randint(1, 10) == 1:
            return True
        return False


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


    def one_day(self, user_data: User, karma_loge: TextIO, day: int) -> None:
        """
        Запускает де
        :param user_data: данные пользователя
        :type user_data: User
        :param karma_loge: лог файл для записи ошибок
        :type karma_loge: TextIO
        :param day: день на пути к просветлению
        :type day: int
        """
        try:
            if self.probability_exception():
                raise self.random_exception_choice()
            else:
                user_data.karma_point += randint(1,  7)


                # Защита от перенасыщения кармы
                if user_data.karma_point < self.KARMA_CONSTANT:
                    print(f"День {day} пути к просветлению. Карма пользователя  "
                          f"{user_data.name}: {user_data.karma_point}")
                else:
                    user_data.karma_point = self.KARMA_CONSTANT
                    print(f"Поздравляю {user_data.name} вы достигли просветления за {day} дней! "
                          f"Ваша карма равна {user_data.karma_point}.")


        except LifeException as exc:
            karma_loge.write(f"День {day}. У пользователя {user_data.name} возникла ошибка: "
                             f"{exc.__class__.__name__} - {exc}\n")
            print(f"День {day}. У пользователя {user_data.name} возникла ошибка: "
                  f"{exc.__class__.__name__} - {exc}")


def main():
    # ЗАпрашиваем имя пользователя
    user_name: str = input("Введите имя пользователя: ").strip()
    user: User = User(user_name)
    day: int = 1


    with open("karma.log", "w", encoding="UTF-8") as file_log:
        while user.karma_point < Enlightenment().KARMA_CONSTANT:
            Enlightenment().one_day(user, file_log, day)
            if user.karma_point < Enlightenment.KARMA_CONSTANT:
                day += 1


if __name__ == "__main__":
    main()
