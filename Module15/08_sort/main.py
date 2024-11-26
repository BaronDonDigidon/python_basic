def num_list_greater(number_elements: int) -> list[int]:
    """

    :param number_elements:
    :return:
    """
    num_list: list[int] = []
    for _ in range(number_elements):
        num: int = int(input("Введите число: "))
        num_list.append(num)
    return num_list




def num_sorter(num_list: list[int]) -> list[int]:
    """

    :param num_list:
    :return:
    """
    for index_num_1 in range(len(num_list)):
        for index_num_2 in range(len(num_list)):
            if num_list[index_num_1] < num_list[index_num_2]:
                save_num: int = num_list[index_num_2]
                num_list[index_num_2] = num_list[index_num_1]
                num_list[index_num_1] = save_num
    return num_list




def main() -> None:
    """

    :return:
    """
    number_elements: int = int(input("Введите количество элементов списка: "))
    print(f"Отсортированный список: {num_sorter(num_list_greater(number_elements))}")




main()