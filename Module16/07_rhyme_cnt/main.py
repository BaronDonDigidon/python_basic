def the_counting_machine(list_1: list[int], num: int, start_index: int = 0) -> None:
    """
    Функция определяет начальную точку отсчёта и чисело которое выбывает, затем удаляет это число.
    :param list_1: список чисел
    :param num: шаг считалки
    :param start_index: индекс списка с которого начинается отсчёт
    :return: None
    """
    while len(list_1) > 1:
        print(f"Текущий круг людей: {list_1}\n"
              f"Начало счёта с номера {list_1[start_index]}\n"
              f"Выбывает человек под номером {list_1[(start_index + num) % len(list_1) - 1]}")
        new_start_index: int = (start_index + num) % len(list_1) - 1
        if new_start_index == -1:
            new_start_index = 0
        list_1.remove(list_1[(start_index + num) % len(list_1) - 1])
        start_index = new_start_index
    else:
        print(f"Остался человек под номером {list_1[0]}")




def menu() -> None:
    """
    Функция запрашивает кол-во человек в считалке, число шага, создает список чисел в соответсвии с кол-вом человек и
    выводит оставшегося человека используя функцию the_counting_machine
    :return:
    """
    number_of_people: int = int(input(f"Кол-во человек: "))
    number: int = int(input(f"Какое число в считалке: "))
    print(f"Значит, выбывает каждый {number}-й человек.")
    people_list: list[int] = [num for num in range(1, number_of_people + 1)]
    the_counting_machine(people_list, number)




menu()