import requests
import json
from typing import List, Dict


class SWAPIClient:
    """Клиент для работы с API swapi.tech"""

    BASE_URL: str = "https://www.swapi.tech/api/"

    @staticmethod
    def get_url(url: str) -> dict:
        """
        Выполняет GET-запрос по указанному URL и возвращает результат в формате словаря (JSON).

        :param url: Полный URL для запроса.
        :return: Ответ API в формате JSON (словарь).
        :raises Exception: Если статус ответа не 200.
        """
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Ошибка запроса: {url}, статус: {response.status_code}")

    def search(self, category: str, name: str) -> dict:
        """
        Выполняет поиск объекта по имени в заданной категории (например, starships, people).

        :param category: Категория поиска (например, 'starships').
        :param name: Имя объекта для поиска.
        :return: Первый найденный результат (словарь с данными объекта).
        :raises ValueError: Если ничего не найдено.
        """
        url = f"{self.BASE_URL}{category}/?name={name}"
        data = self.get_url(url)
        results = data.get("result", [])
        if not results:
            raise ValueError(f"{category.capitalize()} '{name}' не найден.")
        return results[0]


class Planet:
    """Класс, представляющий планету."""

    def __init__(self, url: str, client: SWAPIClient) -> None:
        """
        Загружает данные о планете по URL и сохраняет имя и ссылку.

        :param url: URL планеты.
        :param client: Экземпляр клиента для запросов к API.
        """
        planet_data = client.get_url(url)["result"]["properties"]
        self.name: str = planet_data["name"]
        self.url: str = url

    def to_dict(self) -> Dict[str, str]:
        """
        Представляет объект в виде словаря.

        :return: Словарь с данными о планете.
        """
        return {
            "name": self.name,
            "url": self.url
        }


class Pilot:
    """Класс, представляющий пилота звездолёта."""

    def __init__(self, url: str, client: SWAPIClient) -> None:
        """
        Загружает данные о пилоте и его родной планете.

        :param url: URL пилота.
        :param client: Экземпляр клиента для запросов к API.
        """
        data = client.get_url(url)["result"]["properties"]
        self.name: str = data["name"]
        self.height: str = data["height"]
        self.mass: str = data["mass"]
        self.homeworld: Planet = Planet(data["homeworld"], client)

    def to_dict(self) -> Dict[str, str]:
        """
        Представляет объект в виде словаря.

        :return: Словарь с данными о пилоте.
        """
        return {
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "homeworld": self.homeworld.name,
            "homeworld_url": self.homeworld.url
        }


class Starship:
    """Класс, представляющий звездолёт."""

    def __init__(self, name: str, client: SWAPIClient) -> None:
        """
        Загружает данные о звездолёте, включая пилотов.

        :param name: Название звездолёта.
        :param client: Экземпляр клиента для запросов к API.
        """
        result = client.search("starships", name)
        data = result.get("properties")

        self.name: str = data["name"]
        self.max_speed: str = data["max_atmosphering_speed"]
        self.starship_class: str = data["starship_class"]
        self.pilot_urls: List[str] = data["pilots"]
        self.pilots: List[Pilot] = [Pilot(url, client) for url in self.pilot_urls]

    def to_dict(self) -> Dict[str, any]:
        """
        Представляет объект в виде словаря.

        :return: Словарь с данными о звездолёте и пилотах.
        """
        return {
            "name": self.name,
            "max_atmosphering_speed": self.max_speed,
            "starship_class": self.starship_class,
            "pilots": [pilot.to_dict() for pilot in self.pilots]
        }

    def save_to_file(self, filename: str) -> None:
        """
        Сохраняет данные о звездолёте в JSON-файл.

        :param filename: Имя файла.
        """
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=4, ensure_ascii=False)

    def print_info(self) -> None:
        """
        Выводит данные о звездолёте в консоль в читаемом виде.
        """
        print(json.dumps(self.to_dict(), indent=4, ensure_ascii=False))


# --- Основной запуск программы ---
if __name__ == "__main__":
    client = SWAPIClient()
    xwing = Starship("X-wing", client)
    xwing.print_info()
    xwing.save_to_file("xwing_info.json")

