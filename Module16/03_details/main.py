from typing import Tuple, Any

shop: list[any] = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]




def cost_calculater(product: str, shop_list: list[str | int]) -> tuple[int, int]:
    """
    Функция принимает название требуемой детали и список названий деталей и их стоимостей,
    находит количество и стоимость требуемой детали.
    :param product: Требуемая деталь
    :param shop_list: Название деталей и их стоимостей
    :return: кортеж чисел
    """
    cost = 0
    count_products = 0
    for i in range(len(shop_list)):
        if shop_list[i][0] == product:
            cost += shop_list[i][1]
            count_products += 1
    return count_products, cost




def menu() -> None:
    """
    Функция запрашивает название требуемой детали, далее испольуя функцию cost_calculater подсчитывает кол-во деталей
    и ее стоимость.
    :return: Показывает пользователю стоимость и кол-во деталей.
    """
    product: str = input("Название детали: ")
    print(f"Кол-во деталей - {cost_calculater(product, shop)[0]}\n"
          f"Общая стоимость - {cost_calculater(product, shop)[1]}")




menu()