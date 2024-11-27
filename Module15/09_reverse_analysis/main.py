numbers_list = [7, 14, 3, 18, 21, 10, 9, 6]



def loocking_count_even_numbers(num_list: list[int]) -> int:
    """
    Функция принимает список целых чисел и выводит их количество в списке.
    :param num_list: Список целых чисел;
    :return: Целое число.
    """
    count_even_numbers: int = 0
    for i in range(-1, -len(num_list) - 1, -1):
        if num_list[i] % 2 == 0:
            count_even_numbers += 1
    return count_even_numbers




def looking_even_numbers(num_list: list[int], even_numbers_count: int) -> None:
    """
    Функция принимает список целых чисел, перебирает его в обратно порядке, находит чётные числа
    и выводит их на экран.
    :param num_list: Список целых чисел;
    :param even_numbers_count: Количество целых чисел в списке;
    :return: None
    """
    counter: int = 1
    for i in range(-1, -len(num_list) - 1, -1):
        if num_list[i] % 2 == 0 and  counter != even_numbers_count:
            counter += 1
            print(num_list[i], end=", ")
        elif num_list[i] % 2 == 0 and  counter == even_numbers_count:
            print(num_list[i], end=".")




def main(num_list: list[int]) -> None:
    """
    Функция объединяет работу функций loocking_count_even_numbers и looking_even_numbers -
    принимает список целых чисел и извлекает из него чётные числа и выводит их в обратном порядке.
    :param num_list: Список целых чисел;
    :return: None.
    """
    print("Чётные числа: ", end="")
    looking_even_numbers(num_list, loocking_count_even_numbers(num_list))




main(numbers_list)