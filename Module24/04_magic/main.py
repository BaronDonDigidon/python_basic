class Water:
    def __str__(self) -> str:
        return "Вода"

    def __add__(self, other: object) -> object | None:
        """
        Комбинация Воды с другими элементами.
        """
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Mud()
        return None


class Air:
    def __str__(self) -> str:
        return "Воздух"

    def __add__(self, other: object) -> object | None:
        """
        Комбинация Воздуха с другими элементами
        """
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Fire):
            return Lightning()
        return None


class Fire:
    def __str__(self) -> str:
        return "Огонь"

    def __add__(self, other: object) -> object | None:
        """
        Комбинация Огня с другими элементами
        """
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Air):
            return Lightning()
        return None


class Earth:
    def __str__(self) -> str:
        return "Земля"

    def __add__(self, other: object) -> object | None:
        """
        Комбинация Земли с другими элементами
        """
        if isinstance(other, Water):
            return Mud()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        return None


class Storm:
    def __str__(self) -> str:
        return "Шторм"


class Steam:
    def __str__(self) -> str:
        return "Пар"


class Mud:
    def __str__(self) -> str:
        return "Грязь"


class Lightning:
    def __str__(self) -> str:
        return "Молния"


class Dust:
    def __str__(self) -> str:
        return "Пыль"


class Lava:
    def __str__(self) -> str:
        return "Лава"


class ElementConverter:
    # Словарь для преобразования строки в объект класса
    element_list: dict[str, object] = {
        "вода": Water(),
        "воздух": Air(),
        "земля": Earth(),
        "огонь": Fire(),
        "шторм": Storm(),
        "пар": Steam(),
        "грязь": Mud(),
        "молния": Lightning(),
        "пыль": Dust(),
        "лава": Lava()
    }

    # Таблица преобразований для вывода пользователю
    convert_tab: list[str] = [
        "Вода + Воздух = Шторм;",
        "Вода + Огонь = Пар;",
        "Вода + Земля = Грязь;",
        "Воздух + Огонь = Молния;",
        "Воздух + Земля = Пыль;",
        "Огонь + Земля = Лава."
    ]

    def __init__(self, element: str) -> None:
        self.element = element.strip().lower()

    def element_class(self) -> object:
        """Возвращает объект класса, соответствующий введённому элементу."""
        return self.element_list[self.element]

    def convert_tab_info(self) -> None:
        """Выводит таблицу всех возможных преобразований."""
        for i_line in self.convert_tab:
            print(i_line)


def main() -> None:
    """Основной цикл программы с меню."""
    while True:
        print("\n1. Таблица преобразований.")
        print("2. Соединить элементы")
        print("3. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            ElementConverter("таблица").convert_tab_info()

        elif choice == "2":
            element_1: str = input("Введите название первого элемента: ").strip().lower()
            element_2: str = input("Введите название второго элемента: ").strip().lower()

            try:
                obj_1 = ElementConverter(element_1).element_class()
                obj_2 = ElementConverter(element_2).element_class()
                result = obj_1 + obj_2
            except:
                print("Ошибка: Один или оба элемента не распознаны.")
                continue

            if result is None:
                print(result)
            else:
                print(f"{obj_1} + {obj_2} = {result}")

        elif choice == "3":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()