class User:
    """
    Базовый класс пользователя.
    """
    def __init__(self) -> None:
        """
        Инициализация пользователя, заправшивает количество денег пользователя.
        """
        self.__money: float = self.input_positive_float("Введите количество ваших денег: ")


    @staticmethod
    def input_positive_float(prompt: str) -> float:
        """
        Статический метод класса, для контроля ввода.
        :param prompt: Текст запроса.
        :type prompt str
        :return: Положительное число.
        :rtype: int
        """
        while True:
            # Запрашивает данные для ввода
            user_input: str = input(prompt)
            # Преобразует введенный пользователем данные в число.
            try:
                value: float = float(user_input)
                if value < 0:
                    raise ValueError("Число недолжно быть отрицательным.")
                return value
            except ValueError as e:
                print(f"Ошибка: {e}")


    def can_pay(self, tax: float) -> bool:
        """
        Проверяет есть ли возможность уплатить налог.
        :param tax:
        :type tax: float
        :return: True or False
        :rtype: bool
        """
        return self.__money >= tax


    @property
    def money(self) -> float:
        """
        Геттер для аргумента __money
        """
        return self.__money


    @money.setter
    def money(self, money: float) -> None:
        """
        Сеттер для аргумента __money
        :param money: Числовое значение денег пользователя
        :type money: int
        """
        if money < 0:
            raise ValueError("Денег не может быть меньше нуля")
        self.__money = money


    def pay(self, tax: float) -> bool:
        """
        Проверяет возможность уплатить налог, если такая есть вычитает сумму налога из денежных средств пользователя.
        :param tax: сумма к уплате налога не имущество
        :type tax: float
        :return: True or False
        :rtype: False
        """
        if self.can_pay(tax):
            self.__money -= tax
            return True
        return False


class Property:
    """
    Базовый класс для имущества, описывающий стоимость имущества и методы вычисления налога.

    Args:
        worth (int): стоимость имущества
    """
    def __init__(self, worth: float = None) -> None:
        """
        Инициализация имущества, cтоимость имущества можно определить позже.
        :param worth: Стоимость имущества
        :type worth: int
        """
        self.__worth: float = worth


    @property
    def worth(self) -> float:
        """
        Геттер для получения стоимости имущества.
        :return: __worth
        :rtype: int
        """
        return self.__worth


    @worth.setter
    def worth(self, worth: float) -> None:
        """
        Сеттер для установления стоимости имущества.
        :param worth: стоимость имущества
        :type worth: int
        """
        if worth < 0:
            raise ValueError("Стоимость должна быть числом больше 0.")
        else:
            self.__worth = worth


    def calculates_the_tax(self) -> None:
        """
        Метод расечатывающий описание методики расчета налога для каждого типа имущества
        """
        print("Налог на квартиру вычисляется как 1/1000 её стоимости, на машину — 1/200, на дачу — 1/500.")


class Apartment(Property):
    """
    Класс Квартира. Родитель: Property

    Args:
        worth (int): стоимость имущества
    """
    def __init__(self, worth: float = None) -> None:
        super().__init__(worth)


    def calculates_the_tax(self) -> float:
        """
        Расчитывает налог на кварти.
        :return: размер налога в числовом значении
        :rtype: float
        """
        return self.worth / 1000


class Car(Property):
    """
    Класс Машина. Родитель: Property

    Args:
        worth (int): стоимость имущества
    """
    def __init__(self, worth: float = None) -> None:
        super().__init__(worth)


    def calculates_the_tax(self) -> float:
        """
        Расчитывает налог на машину.
        :return: размер налога в числовом значении
        :rtype: float
        """
        return self.worth / 200


class CountryHouse(Property):
    """
    Класс Дача. Родитель: Property

    Args:
        worth (int): стоимость имущества
    """
    def __init__(self, worth: float = None) -> None:
        super().__init__(worth)


    def calculates_the_tax(self) -> float:
        """
        Расчитывает налог на дачу.
        :return: размер налога в числовом значении
        :rtype: float
        """
        return self.worth / 500


class Menu:
    """
    Базоый класс меню, описывает функции меню.
    """
    def __init__(self):
        self.__property_value = self.input_positive_float("Введите стоимость недвижимости: ")


    def __str__(self) -> str:
        return ("Для какого типа недвижимости вы ходите расчитать налог"
                "(введите число в зависимости от типа имущества):"
                "\n1) Квартира\n2) Машина\n3) Дача\n")


    @property
    def property_value(self) -> float:
        """
        Геттер для property_value
        :return: __property_value
        :rtype: int
        """
        return self.__property_value


    @property_value.setter
    def property_value(self, property_value: float) -> None:
        """
        Сеттер для property_value
        :param property_value: Стоимость имущества, числовое значение
        :type property_value: int
        """
        if property_value <= 0:
            raise ValueError("Стоимость имущества не может быть равна нулю или отрицальной")
        else:
           self.__property_value = property_value

    @staticmethod
    def input_positive_float(prompt: str) -> float:
        """
        Контролирует ввод положительного числового значения.
        :param prompt: Текст запроса.
        :type prompt str
        :return: Положительное число.
        :rtype: int
        """
        while True:
            user_input: str = input(prompt)
            try:
                value: float = float(user_input)
                if value <= 0:
                    raise ValueError("Число должно быть больше нуля.")
                return value
            except ValueError as e:
                print(f"Ошибка: {e}")

    @staticmethod
    def choice_type_property() -> Property:
        """
        Часть меню помогающая определить требуемый класс имущества.
        :return: Объект одного из классов недвижимости
        :rtype: Property
        """
        while True:
            try:
                choice_digit = float(input("Введи число 1,2 или 3 для выбора типа имущества для которого"
                                         "нужно расчитать налог."))
                if choice_digit == 1:
                    return Apartment()
                elif choice_digit == 2:
                    return Car()
                elif choice_digit == 3:
                    return CountryHouse()
                else:
                    print("Ошибка: нужно ввести 1, 2 или 3!")
            except ValueError as e:
                print(f"Ошибка: {e}")


def main():
    user = User()
    menu = Menu()

    # Выводим меню выбор типа имущества
    print(menu)

    # Запрашиваем стоимость имущества
    worth = menu.property_value

    # Определяем тип имущества
    type_property: Property = menu.choice_type_property()
    type_property.worth = worth
    # Расчитываем налог который требуется уплатить
    tax: float | None = type_property.calculates_the_tax()
    if user.pay(tax):
        print(f"Налог уплачен, оставшиеся денежные средства: {user.money:.2f} коин(а)")
    else:
        print(f"Для уплаты налога нехватает {tax - user.money:.2f} коин(а)")


if __name__ == "__main__":
    main()
