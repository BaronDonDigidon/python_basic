from typing import Dict




def orders_number_dict(orders_number: int, orders_dict: Dict[str, Dict[str, int]] = None) \
        -> Dict[str, Dict[str, int]]:
    """
    Обрабатывает заказы пиццы и возвращает словарь с количеством заказанных пицц для каждого клиента.
    :param orders_number: Количество заказов, которые нужно обработать.
    :param orders_dict: Словарь, содержащий заказы. Если не передан, создается новый.
    :return: Словарь, где ключи - имена клиентов, а значения - словари с названиями пицц и их количеством.
    """
    if orders_dict == None:
        orders_dict = {}
    for i in range(orders_number):
        order = input(f"{i + 1}-й заказ: ").strip().split(" ")
        name = order[0]
        pizza =  order[1]
        number: int = int(order[2])
        if name not in orders_dict:
            orders_dict[name] = {}
        if pizza in orders_dict[name]:
            orders_dict[name][pizza] += number
        else:
            orders_dict[name][pizza] = number
    return orders_dict




def printing_orders(orders_dict: Dict[str, Dict[str, int]]) -> None:
    """
    Печатает заказы в удобочитаемом формате.
    :param orders_dict:Словарь с заказами, где ключи - имена клиентов,
    а значения - словари с названиями пицц и их количеством.
    :return:None
    """
    for i_key, i_value in orders_dict.items():
        print(i_key)
        for item in sorted(i_value):
            print("    " + item + ": " + str(i_value[item]))




def pizzeria() -> None:
    """
    Основная функция для запуска программы. Запрашивает количество заказов, обрабатывает их и выводит результаты.
    :return: None
    """
    orders_number = int(input("Введите количество заказов: "))
    orders_dict = orders_number_dict(orders_number)
    printing_orders(orders_dict)




if __name__ == "__main__":
    pizzeria()
