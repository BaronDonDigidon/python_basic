def list_greater(elem_number: [int], num_list: list[int] = []):
    """
    Функция принимает на вход количество числ в списке, запрашивает числа и добавляет их в список.
    :param elem_number: Количество чисел в списке;
    :param num_list: Список чисел;
    :return: Лист с числами.
    """
    for _ in range(elem_number):
        num: int = int(input("Введите число: "))
        num_list.append(num)
    return num_list




def num_walker(list_num: list[int], step: int) -> list [int]:
    """
    Сдвигает числа списка на заданный шаг сдига.
    :param list_num: Список чисел;
    :param step: Шаг сдвига;
    :return: Список чисел.
    """
    new_num_list: int = []
    key_count: int = 0
    while key_count < len(list_num):
        key_count += 1
        new_num_list.append(list_num[-(step % len(list_num))])
        step -= 1
    return new_num_list



def main() -> None:
    """
    Запрашивает количество элементов списка и использует функцию list_greater для создания списка чисел, далее
    запрашивает шаг сдвига использует функцию num_walker для сдвига элементов списка.
    :return: None
    """
    number_elements: int = int(input("Введите количество элементов списка: "))
    num_list = list_greater(number_elements)
    shift_step: int = int(input("Введите шаг сдвига: "))
    return print(f"Сдвинутый список: {num_walker(num_list, shift_step)}")




main()