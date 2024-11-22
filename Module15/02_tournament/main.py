participants_list_1:  list[str] = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]




def participants_selecter(candidate_list: list [str], selected_list: list [str] = []) -> None:
    """
    Функция принимает список строк и возвращает новый список включающий каждый нечётный элемент базового списка.
    :param candidate_list: Список строк;
    :param selected_list: Список сформированный из списка candidate_list путём добавления каждого нечётного элемента,
    необязательный параметр;
    :return: Возвращает список строк каждого нечётного элемента списка candidate_list;
    """
    for participants in range(0, len(candidate_list), 2):
        selected_list.append(candidate_list[participants])
    return print(f"Первый день: {selected_list}.")




participants_selecter(participants_list_1)