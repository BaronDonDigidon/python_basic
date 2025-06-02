import random

class House:
    def __init__(self) -> None:
        """
        Инициализация дома с начальными запасами еды и денег.
        """
        self.food: int = 50     # Еда в холодильнике
        self.money: int = 0     # Деньги в тумбочке


class Person:
    def __init__(self, name: str, house: House) -> None:
        """
        Инициализация человека с именем, сытостью и привязкой к дому.
        :param name: Имя человека
        :param house: Объект дома, в котором он живёт
        """
        self.name: str = name
        self.satiety: int = 50  # Уровень сытости
        self.house: House = house

    def eat(self) -> None:
        """
        Метод для еды: человек съедает еду из холодильника и повышает сытость.
        """
        if self.house.food >= 10:
            self.house.food -= 10
            self.satiety += 10
            print(f"{self.name} поел. Сытость: {self.satiety}, Еда в доме: {self.house.food}")
        else:
            print(f"{self.name} хотел поесть, но еды не хватает!")

    def work(self) -> None:
        """
        Метод для работы: человек зарабатывает деньги, но теряет сытость.
        """
        self.house.money += 50
        self.satiety -= 10
        print(f"{self.name} поработал. Деньги в доме: {self.house.money}, Сытость: {self.satiety}")

    def play(self) -> None:
        """
        Метод для игры: человек развлекается, но тратит энергию (сытость).
        """
        self.satiety -= 10
        print(f"{self.name} поиграл. Сытость: {self.satiety}")

    def go_to_store(self) -> None:
        """
        Метод для похода в магазин: покупает еду за деньги.
        """
        if self.house.money >= 20:
            self.house.food += 20
            self.house.money -= 20
            print(f"{self.name} сходил в магазин. Еда в доме: {self.house.food}, Деньги: {self.house.money}")
        else:
            print(f"{self.name} хотел купить еду, но денег не хватает!")

    def live_one_day(self) -> bool:
        """
        Метод на 1 день жизни: выбирается действие по приоритетам.
        :return: True если жив, False если умер
        """
        if self.satiety <= 0:
            print(f"{self.name} умер от голода...")
            return False

        dice: int = random.randint(1, 6)  # Кубик от 1 до 6

        # Приоритет действий
        if self.satiety < 20:
            self.eat()
        elif self.house.food < 10:
            self.go_to_store()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play()

        return True


def main() -> None:
    """
    Основная функция симуляции жизни двух людей в течение 365 дней.
    """
    home: House = House()
    person1: Person = Person("Артем", home)
    person2: Person = Person("Оля", home)

    for day in range(1, 366):
        print(f"\nДень {day}")
        alive1: bool = person1.live_one_day()
        alive2: bool = person2.live_one_day()

        # Проверка, кто жив, а кто нет
        if not alive1 and not alive2:
            print("Все умерли... Эксперимент окончен.")
            break
        elif not alive1:
            print(f"{person1.name} погиб. {person2.name} жив.")
        elif not alive2:
            print(f"{person2.name} погиб. {person1.name} жив.")

if __name__ == "__main__":
    main()
