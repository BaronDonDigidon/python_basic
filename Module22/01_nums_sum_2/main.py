from typing import List




def read_numbers_from_file(filename: str) -> List[int]:
    """
    Читает числа из файла и возвращает их в виде списка.
    :param filename: файл с числами
    :return: список чисел
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        number_strings = content.split()
        numbers = [int(num) for num in number_strings]
        return numbers




def write_sum_to_file(filename: str, total: int) -> None:
    """
    Записывает сумму чисел в файл.
    :param filename: файл для записи числа
    :param total: сумма чисел
    :return: None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(str(total) + '\n')




def main() -> None:
    numbers = read_numbers_from_file('numbers.txt')
    total_sum = sum(numbers)
    write_sum_to_file('answer.txt', total_sum)




if __name__ == '__main__':
    main()


