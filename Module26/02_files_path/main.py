import os
from typing import Generator


def gen_files_path(root_path: str = "/", target_folder: str = "") -> Generator[str, None, None]:
    """
    Рекурсивно обходит директории, начиная с root_path, и ищет каталог с именем target_folder.
    Если каталог найден — генерирует пути ко всем файлам внутри него.

    :param root_path: Путь, с которого начинается обход (по умолчанию — корень файловой системы).
    :type root_path: str
    :param target_folder: Название искомой папки.
    :type target_folder: str
    :yield: Полные пути к файлам, находящимся в найденной папке.
    """
    print(f"Начат поиск папки '{target_folder}' в директории '{root_path}'...\n")

    for current_path, dirs, files in os.walk(root_path):
        if os.path.basename(current_path) == target_folder:
            print(f"Найдена целевая папка: {current_path}")
            for dir_path, _, file_names in os.walk(current_path):
                for file in file_names:
                    file_path = os.path.join(dir_path, file)
                    print(f"Найден файл: {file_path}")
                    yield file_path
            return

    print("Папка не найдена.")


for path in gen_files_path("C:/Users", "Documents"):
    print(path)
