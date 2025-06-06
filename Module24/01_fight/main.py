import random
import time


class Warrior:
    def __init__(self, name: str) -> None:
        """
        Инициализация воина с именем и здоровьем 100 очков.
        """
        self.name: str = name
        self.health: int = 100

    def is_alive(self) -> bool:
        """
        Проверка, жив ли воин.
        """
        return self.health > 0

    def take_damage(self, damage: int) -> None:
        """
        Применение урона к воину.
        """
        self.health = max(self.health - damage, 0)

    def attack(self, other: "Warrior") -> None:
        """
        Атака другого воина.
        """
        damage: int = 20
        print(f"{self.name} атакует {other.name}!")
        other.take_damage(damage)
        print(f"У {other.name} осталось {other.health} здоровья.\n")


class Battle:
    def __init__(self, warrior1: Warrior, warrior2: Warrior) -> None:
        """
        Инициализация битвы между двумя воинами.
        """
        self.warrior1: Warrior = warrior1
        self.warrior2: Warrior = warrior2

    def start(self) -> None:
        """
        Запуск битвы до победы одного из воинов.
        """
        print("Битва начинается!\n")

        attacker: Warrior
        defender: Warrior

        while self.warrior1.is_alive() and self.warrior2.is_alive():
            attacker = random.choice([self.warrior1, self.warrior2])
            defender = self.warrior2 if attacker == self.warrior1 else self.warrior1
            attacker.attack(defender)
            time.sleep(1)

        winner: Warrior = self.warrior1 if self.warrior1.is_alive() else self.warrior2
        print(f"{winner.name} победил!\n")


# Основной блок
if __name__ == "__main__":
    w1: Warrior = Warrior("Артур")
    w2: Warrior = Warrior("Ланселот")

    battle: Battle = Battle(w1, w2)
    battle.start()