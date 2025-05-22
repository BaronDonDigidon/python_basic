from typing import List
def read_zen_file(filename: str) -> List[str]:
    """
    Читает строки из файла и возвращает список строк.
    :param filename: файл с Дзен Пайтона!
    :return: Список строк
    """
    with open(filename, "r", encoding="UTF-8") as file:
        line_list = file.readlines()
    return line_list




def print_lines_reversed(lines) -> None:
    """
    Печатает строки в обратном порядке.
    :param lines: Список с стркоами.
    :return: Выводит на экран строки списка в обратном порядке.
    """
    for line in reversed(lines):
        print(line.strip())




def main() -> None:
    name_file = "zen.txt"
    lines = read_zen_file(name_file)
    print_lines_reversed(lines)

if __name__ == "__main__":
    main()
