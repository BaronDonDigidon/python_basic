import os
from typing import Tuple


def get_directory_info(path: str) -> Tuple[int, int, int]:
    """
    Рекурсивно подсчитывает количество подкаталогов, файлов и общий размер файлов в каталоге.

    :param path: Путь к каталогу.
    :return: Кортеж (кол-во подкаталогов, кол-во файлов, размер файлов в байтах).
    """
    dir_count = 0
    file_count = 0
    dir_size = 0

    for entry in os.listdir(path):
        item_path = os.path.join(path, entry)
        if os.path.isdir(item_path):
            dir_count += 1
            sub_dirs, sub_files, sub_size = get_directory_info(item_path)
            dir_count += sub_dirs
            file_count += sub_files
            dir_size += sub_size
        elif os.path.isfile(item_path):
            file_count += 1
            dir_size += os.path.getsize(item_path)

    return dir_count, file_count, dir_size


def print_directory_summary(path: str) -> None:
    """
    Выводит сводную информацию о каталоге: размер, количество подкаталогов и файлов.

    :param path: Путь к каталогу.
    """
    dir_count, file_count, dir_size = get_directory_info(path)
    size_kb = round(dir_size / 1024, 2)

    print(f"\nПуть: {path}")
    print(f"Размер каталога (в Кб): {size_kb}")
    print(f"Количество подкаталогов: {dir_count}")
    print(f"Количество файлов: {file_count}")


def main() -> None:
    """
    Основная функция для запуска программы.
    Запрашивает путь и выводит информацию, если путь корректен.
    """
    path = input("Введите путь к папке: ").strip()

    if not os.path.isdir(path):
        print("Указанный путь не существует или это не папка.")
        return

    print_directory_summary(path)


if __name__ == "__main__":
    main()
