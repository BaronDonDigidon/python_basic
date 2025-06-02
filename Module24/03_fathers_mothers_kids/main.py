from typing import Dict, List
import threading
import random
import time


class Child:
    # Словари состояний ребенка
    state_calm: Dict[int, str] = {0: "Плачет", 1: "Злой", 2: "Рад", 3: "Спокоен"}
    state_hunger: Dict[int, str] = {0: "Голоден", 1: "Сыт"}

    def __init__(self, name: str, age: int, state_calm_index: int, state_hunger_index: int) -> None:
        self.name: str = name
        self.age: int = age
        self.state_calm_index: int = state_calm_index
        self.state_hunger_index: int = state_hunger_index
        threading.Thread(target=self._hunger_timer, daemon=True).start()
        threading.Thread(target=self._calm_timer, daemon=True).start()

    def display_info(self) -> None:
        """Вывод информации о ребенке."""
        print(
            "Имя: {}\nВозраст: {}\nСостояние спокойствия: {}\nСостояние голода: {}".format(
                self.name, self.age, self.state_calm[self.state_calm_index],
                self.state_hunger[self.state_hunger_index])
        )

    def _calm_timer(self) -> None:
        """Таймер, по истечении которого ребенок становится беспокойным."""
        time.sleep(random.randint(5, 8))
        self.state_calm_index = random.randint(0, 1)
        print("\n{} {}, успокойте ребенка".format(self.name, self.state_calm[self.state_calm_index]))

    def _hunger_timer(self) -> None:
        """Таймер, по истечении которого ребенок становится голодным."""
        time.sleep(3)
        self.state_hunger_index = 0
        print("\n{} {}, ребенка надо покормить".format(self.name, self.state_hunger[self.state_hunger_index]))

    def calm(self) -> None:
        """Успокоить ребенка."""
        self.state_calm_index = random.randint(2, 3)
        print("\n{} теперь {}".format(self.name, self.state_calm[self.state_calm_index]))
        threading.Thread(target=self._calm_timer, daemon=True).start()

    def feed(self) -> None:
        """Покормить ребенка."""
        self.state_hunger_index = 1
        print("\n{} теперь {}".format(self.name, self.state_hunger[self.state_hunger_index].lower()))
        threading.Thread(target=self._hunger_timer, daemon=True).start()


class Parent:
    def __init__(self, parent_name: str, parent_age: int, child_count: int) -> None:
        self.parent_name: str = parent_name
        self.parent_age: int = parent_age
        self.children: List[Child] = []

        for _ in range(child_count):
            while True:
                name: str = input("Введите имя ребенка: ").strip()
                try:
                    age: int = int(input("Введите возраст ребенка: "))
                except ValueError:
                    print("Возраст должен быть числом.")
                    continue

                if self.parent_age - age < 16:
                    print("Ребенок должен быть минимум на 16 лет младше родителя!")
                else:
                    break

            state_calm_index: int = random.randint(0, 3)
            state_hunger_index: int = random.randint(0, 1)
            self.children.append(Child(name, age, state_calm_index, state_hunger_index))

    def display_family_info(self) -> None:
        """Вывод информации о родителе и всех детях."""
        print("Имя: {}\nВозраст: {}\nСписок детей:".format(self.parent_name, self.parent_age))
        for child in self.children:
            child.display_info()

    def feed_hungry_children(self) -> None:
        """Покормить всех голодных детей."""
        for child in self.children:
            if child.state_hunger_index == 0:
                child.feed()

    def calm_disturbed_children(self) -> None:
        """Успокоить всех расстроенных детей."""
        for child in self.children:
            if child.state_calm_index in (0, 1):
                child.calm()


def main() -> None:
    family = Parent("Ольга", 38, 2)

    while True:
        print("\n1. Инфо о семье")
        print("2. Покормить голодных детей")
        print("3. Успокоить ребенка(детей)")
        print("4. Выход")
        choice: str = input("Выберите действие: ")

        if choice == "1":
            family.display_family_info()
        elif choice == "2":
            family.feed_hungry_children()
        elif choice == "3":
            family.calm_disturbed_children()
        elif choice == "4":
            print("Выход из симуляции.")
            break
        else:
            print("Неверный выбор.")


if __name__ == "__main__":
    main()