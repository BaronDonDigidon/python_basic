def building_a_symmetrical_sequence(numbers: int, numbers_list: list[int], num_list: list[int]) -> None:
    """
    Фунцкия создает семтричный список целых чисед.
    :param numbers: кол-во чисел
    :param numbers_list: список с числами
    :param num_list: список с числами которые необходимо добавить.
    :return: None
    """
    for i in range(numbers):
        numbers_list.insert(numbers, numbers_list[i])
        num_list.append(numbers_list[i])
        if numbers_list == numbers_list[:: -1]:
            print(f"Нужно приписать чисел: {i + 1}")
            print(f"Сами числа {num_list}")
            print(f"Симметричная последовательность: {numbers_list}")
            break


def menu(num_list: list[int] = []) -> None:
    """
    ФУнкция запришвает кол-во чисел, принимает на воод людые целые числа создавая из них список, проверяет список
    на семетричность, если список семтричен не изменяет его, если нет корректирует список минимальным кол-во итераций
    выводит семтричный список, список чисел которые требуется добавить и их кол-во
    :param num_list: пустой список для вывода чисел которые необходимо добавить
    :return: None
    """
    numbers: int = int(input('Кол-во чисел: '))
    numbers_list: list[int] = [int(input('Число: ')) for _ in range(numbers)]
    print()
    print('Последовательность:', numbers_list)
    if numbers_list == numbers_list[:: -1]:
        print(f"Последовательность является семмитричной, добавлять числа не нужно.")
    else:
        building_a_symmetrical_sequence(numbers, numbers_list, num_list)




menu()