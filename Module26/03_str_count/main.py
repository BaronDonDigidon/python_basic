import os
from typing import Generator


def count_code_lines_in_py_files(directory: str) -> Generator[tuple[str, int], None, None]:
    """
    Генератор, проходящий по всем .py-файлам в указанной директории (без вложенных)
    и возвращающий количество строк кода (исключая пустые строки и комментарии) в каждом файле.

    :param directory: Путь к директории, где нужно искать .py-файлы.
    :yield: Кортеж (имя файла, количество строк кода).
    """
    print(f"Поиск Python-файлов в директории: {directory}")

    try:
        for filename in os.listdir(directory):
            if filename.endswith(".py"):
                file_path = os.path.join(directory, filename)
                try:
                    with open(file_path, encoding="utf-8") as file:
                        code_lines = 0
                        for line in file:
                            striped_line = line.strip()
                            if striped_line and not striped_line.startswith("#"):
                                code_lines += 1
                        yield filename, code_lines
                except (UnicodeDecodeError, FileNotFoundError) as e:
                    print(f"Ошибка чтения файла {filename}: {e}")
    except FileNotFoundError:
        print("Указанная директория не найдена.")


user_path = input("Введите путь к директории: ")

for name, lines in count_code_lines_in_py_files(user_path):
    print(f"В файле '{name}' — {lines} строк кода.")

