def input_control(num: int, control_list: list[int]) -> None | str:
    """
    Функция осуществляет контроль ввода, не позволяя пользователю при создании списка вводить числа больше 200
    и последующие числа не больше предыдущего.
    :param num: Вес контейнера.
    :param control_list: Список контейнеров.
    :return: Возвращает в список значение веса контейнера или выводит сообщение об ошибке.
    """
    if num <= 200:
        if len(control_list) == 0:
            return control_list.append(num)
        elif control_list[len(control_list) - 1] >= num:
            return control_list.append(num)
        elif control_list[len(control_list)-1] < num:
            return print(f"Вес следующего контейнера не должен превышать {control_list[len(control_list)-1]}")
    return print("Вес контейнера должен не превышать 200")




def container_number_looking(length_list: int, weight_new_object: int, search_list: int) -> int:
    """
    Функция определяет номер под которым должен будет стоять новый контейнер.
    :param length_list: длина списка (кол-во контейнеров в созданом ранее списке)
    :param weight_new_object: вес нового контейнера
    :param search_list: список контейнеров
    :return: возвращает номер под которым должен стоять новый контейнер
    """
    for place_number in range(length_list):
        if search_list[place_number] < weight_new_object:
            new_place_number = place_number + 1
            return new_place_number
        elif length_list - 1 == place_number:
            new_place_number = place_number + 2
            return new_place_number



def main() -> None:
    """
    Функция запрашивает количество контейнеров, создает список с помощью функции input_control, запрашивает вес
    нового контейнера и определяет его номер с помощью функции container_number_looking.
    :return: None
    """
    number_containers: int = int(input("Введите количество контейнеров: "))
    containers_list: list[int] = []
    while number_containers != len(containers_list):
        container_weight: int  = int(input("Введите вес контейнера: "))
        input_control(container_weight, containers_list)
    while True:
        new_container_wieght: int = int(input("\nВведите вес нового контейнера: "))
        if new_container_wieght <= 200:
            print(f"\nНомер, который получит новый контейнер: "
                  f"{container_number_looking(number_containers, new_container_wieght, containers_list)}")
            break
        else:
            print("Вес контейнера должен не превышать 200")




main()