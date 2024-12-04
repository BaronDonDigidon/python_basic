first_list: list[int] = [1, 3, 5, 7, 9]
second_list: list[int] = [2, 4, 5, 6, 8, 10]




def duplicate_number_deleter(list_1: list[int], list_2: list[int]) -> list[int]:
    """

    :param list_1:
    :param list_2:
    :return:
    """
    for index_num in range(len(list_1)):
        if list_1[index_num] in list_2:
            list_2.remove(list_1[index_num])
    return list_2




def list_sorted_merger(list_1: list[int], list_2: list[int]) -> None:
    """

    :param list_1:
    :param list_2:
    :return:
    """
    list_1.extend(duplicate_number_deleter(list_1, list_2))
    for i in range(len(list_1)):
        for j in range(len(list_1)):
            if list_1[i] < list_1[j]:
                list_1[i], list_1[j] = list_1[j], list_1[i]
    print(list_1)




list_sorted_merger(first_list, second_list)