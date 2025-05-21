import zipfile
from collections import defaultdict
from typing import Dict


def extract_text_from_zip(zip_filename: str) -> str:
    """
    Извлекает текст из первого текстового файла внутри ZIP-архива.

    :param zip_filename: Путь к ZIP-архиву.
    :return: Содержимое первого найденного .txt файла как строка.
    :raises FileNotFoundError: Если внутри архива нет текстовых файлов.
    """
    with zipfile.ZipFile(zip_filename, 'r') as zip_file:
        file_list = zip_file.namelist()
        print("Файл(ы) в архиве:", file_list)

        for name in file_list:
            if name.lower().endswith('.txt'):
                with zip_file.open(name) as file:
                    return file.read().decode('utf-8')

        raise FileNotFoundError("Текстовый файл (.txt) не найден в архиве.")


def count_letter_frequencies(text: str) -> Dict[str, int]:
    """
    Подсчитывает частоту каждой буквы в тексте с учётом регистра.
    Учитываются все буквенные символы всех алфавитов.

    :param text: Исходный текст.
    :return: Словарь с буквами в качестве ключей и их количествами в качестве значений.
    """
    frequencies: Dict[str, int] = defaultdict(int)
    for char in text:
        if char.isalpha():
            frequencies[char] += 1
    return frequencies


def save_sorted_statistics(frequencies: Dict[str, int], output_file: str) -> None:
    """
    Сохраняет статистику частот букв в файл, отсортированную по убыванию частоты.

    :param frequencies: Словарь с частотами букв.
    :param output_file: Имя выходного файла для записи результатов.
    """
    # Сортируем по убыванию частоты
    sorted_letters = sorted(frequencies.items(), key=lambda x: -x[1])

    with open(output_file, 'w', encoding='utf-8') as file:
        for letter, count in sorted_letters:
            file.write(f"{letter} {count}\n")


def main() -> None:
    """
    Основная функция: извлекает текст из архива, считает частоты и сохраняет результаты.
    """
    zip_filename = 'voina-i-mir.zip'
    output_file = 'letter_stats.txt'

    text = extract_text_from_zip(zip_filename)
    frequencies = count_letter_frequencies(text)
    save_sorted_statistics(frequencies, output_file)

    print(f"Анализ завершён. Результат сохранён в {output_file}.")


if __name__ == "__main__":
    main()