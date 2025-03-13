from typing import List, Tuple




def sorting_hoar_first_step(num_list: List[int]) -> Tuple[List[int], List[int], List[int]]:
    """
    Разбивает список на три списка:
    - less_reference_num: элементы меньше опорного (последнего элемента)
    - equal_reference_num: элементы равные опорному
    - more_reference_num: элементы больше опорного
    :param num_list:список чисел
    :return: Кортеж списковчисел.
    """
    reference_index = len(num_list) - 1
    less_reference_num: List[int] = []
    more_reference_num: List[int] = []
    equal_reference_num: List[int] = []


    for i_num in num_list:


        if i_num < num_list[reference_index]:
            less_reference_num.append(i_num)
        elif i_num == num_list[reference_index]:
            equal_reference_num.append(i_num)
        else:
            more_reference_num.append(i_num)


    return less_reference_num, equal_reference_num, more_reference_num




def sorting_hoar_second_step(num_list: List[int]) -> List[int]:
    """
    Рекурсивная функция быстрой сортировки.
    Если список содержит 0 или 1 элемент — возвращается он же,
    иначе список разбивается на три части, и функция рекурсивно сортирует
    части со значениями меньше и больше опорного.
    :param num_list: список чисел
    :return: отсортированный список чисел
    """


    if len(num_list) <= 1:
        return num_list

    less_reference_num, equal_reference_num, more_reference_num = sorting_hoar_first_step(num_list)
    return (sorting_hoar_second_step(less_reference_num) + equal_reference_num +
            sorting_hoar_second_step(more_reference_num))




if __name__ == "__main__":
    numbers: List[int] = [5, 8, 9, 4, 2, 9, 1, 8]
    print("Исходный список:", numbers)
    print("Отсортированный список:", sorting_hoar_second_step(numbers))