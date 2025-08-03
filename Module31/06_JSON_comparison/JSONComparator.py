import json
from typing import Any, Dict, List


class JSONComparator:
    """
    Класс для сравнения двух JSON-файлов по заданному списку ключей (diff_list).
    Выявляет изменения только по нужным ключам и сохраняет результат в словарь или файл.
    """

    def __init__(self, old_path: str, new_path: str, diff_list: List[str]):
        """
        Инициализация компаратора: загружаются два JSON-файла и список ключей для отслеживания изменений.

        :param old_path: путь к старому JSON-файлу
        :param new_path: путь к новому JSON-файлу
        :param diff_list: список ключей, которые нужно проверять на изменения
        """
        self.old_data = self._load_json(old_path)["data"]
        self.new_data = self._load_json(new_path)["data"]
        self.diff_list = diff_list
        self.result: Dict[str, Any] = {}


    @classmethod
    def _load_json(cls, file_path: str) -> Dict[str, Any]:
        """
        Загружает JSON-файл и возвращает его содержимое как словарь.

        :param file_path: путь к JSON-файлу
        :return: содержимое JSON-файла в виде словаря
        """
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)


    def compare(self) -> str:
        """
        Сравнивает значения по ключам из diff_list на верхнем уровне внутри data.
        Добавляет в результат только те, которые действительно изменились.
        """
        for key in self.diff_list:
            old_value = self.old_data.get(key)
            new_value = self.new_data.get(key)
            if old_value != new_value:
                self.result[key] = new_value
        return json.dumps(self.result, ensure_ascii=False, indent=4)


    def _recursive_compare(self, old_node: Any, new_node: Any, path: str = ""):
        """
        Рекурсивно сравнивает два узла (dict или list) и сохраняет изменения по нужным ключам.

        :param old_node: значение из старого JSON
        :param new_node: значение из нового JSON
        :param path: путь до текущего элемента, используется для построения ключей вида "data.services.cost"
        """
        if isinstance(old_node, dict) and isinstance(new_node, dict):
            for key in old_node:
                new_path = f"{path}.{key}" if path else key
                self._recursive_compare(old_node[key], new_node.get(key), new_path)

        elif isinstance(old_node, list) and isinstance(new_node, list):
            for old_item, new_item in zip(old_node, new_node):
                self._recursive_compare(old_item, new_item, path)

        else:
            short_key = path.split(".")[-1]
            if short_key in self.diff_list and old_node != new_node:
                # Получаем новое значение из new_data по пути
                value = self._get_nested_value(self.new_data, path.split("."))
                self.result[short_key] = value


    @classmethod
    def _get_nested_value(cls, data: Any, path_parts: List[str]) -> Any:
        """
        Получает значение из вложенного словаря по пути.

        :param data: исходный словарь
        :param path_parts: список ключей для прохода по вложенности
        :return: значение по указанному пути
        """
        for part in path_parts:
            if isinstance(data, list):
                data = data[0]  # если список, берём первый элемент (как в services)
            data = data.get(part)
        return data

    def save_result(self, output_file: str = "result.json"):
        """
        Сохраняет результат сравнения (self.result) в JSON-файл.

        :param output_file: имя файла для сохранения результата
        """
        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(self.result, file, ensure_ascii=False, indent=4)
          
