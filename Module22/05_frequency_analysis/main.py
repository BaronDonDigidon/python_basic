from string import ascii_lowercase
from typing import Tuple, Dict


def symbol_counter(input_file: str) -> Tuple[Dict[str, int], int]:
    """
    Считает количество вхождений каждой буквы английского алфавита (в нижнем регистре)
    и общее количество таких букв в файле.

    :param input_file: Имя входного файла с текстом.
    :return: Кортеж (словарь с частотами букв, общее количество букв).
    """
    symbol_dict = {}
    count_letters = 0

    with open(input_file, "r", encoding="UTF-8") as file:
        for line in file:
            text = line.lower()
            for char in text:
                if char in ascii_lowercase:
                    count_letters += 1
                    symbol_dict[char] = symbol_dict.get(char, 0) + 1

    return symbol_dict, count_letters


def sorts_and_adds_data(input_file: str, output_file: str) -> None:
    """
    Сортирует буквы по убыванию их частоты, при равенстве частот — по алфавиту,
    и записывает результат с частотами в файл.

    :param input_file: Имя входного файла с текстом.
    :param output_file: Имя выходного файла для записи результатов.
    """
    sym_dict, count_letters = symbol_counter(input_file)
    # Сортируем по убыванию частоты, при равенстве — по алфавиту
    sorted_dict = dict(sorted(sym_dict.items(), key=lambda x: (-x[1], x[0])))

    with open(output_file, "w", encoding="UTF-8") as file:
        for char, count in sorted_dict.items():
            freq = count / count_letters
            file.write(f"{char} {freq:.3f}\n")


def main() -> None:
    input_file = "text.txt"
    output_file = "analysis.txt"
    sorts_and_adds_data(input_file, output_file)


if __name__ == "__main__":
    main()