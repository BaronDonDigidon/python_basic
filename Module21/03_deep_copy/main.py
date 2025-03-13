import copy
from typing import List, Dict


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}




def site_builder(site_dict: Dict[str, Dict[str, Dict[str, str]]],
                 product_name: str) -> Dict[str, Dict[str, Dict[str, str]]]:
    """
    Рекурсивно изменяет имя продаваемого продукта.
    :param site_dict: Словарь - шаблон сайта.
    :param product_name: Название продукта.
    :return: Словарь - шаблон сайта продаваемого продукта.
    """


    for i_key, i_value in site_dict.items():
        if isinstance(i_value, str):
            site_dict[i_key] = i_value.replace("телефон", product_name).replace("iphone", product_name)
        elif isinstance(i_value, dict):
            site_builder(i_value, product_name)


    return site_dict




def input_cheker() -> None | int:
    """
    Запрашивает количество треуемых сайтов и если введено не число выводит ошибку.
    :return: Целое число.
    """
    count_sites: int = int(input("Введите колличество сайтов: "))


    if isinstance(count_sites, int):
        result = count_sites
    else:
        print("Некорректный ввод. Введите целое число!")
        input_cheker()


    return result




def new_site_adder(site: Dict, site_num: int, site_list: List = None) -> None:
    """
    Создаёт список с сайтами для указанных пользователем продуктов.
    :param site: Словарь - шаблон сайта.
    :param site_num: кол-во сайтов.
    :param site_list: Лист с данными по созданным сайтам.
    :return: Возвращает словарь сайта к каждому продукту для которого пользователь запросил создание.
    """


    if site_list is None:
        site_list = []


    if site_num == 0:
        return site_list


    product_name = input("Введите название продукта для нового сайта: ")
    new_site = copy.deepcopy(site)
    site_builder(new_site, product_name)
    site_list.append((product_name, new_site))


    for prod, prod_site in site_list:
        print(f"Сайт для {prod}:")
        print(f"site = {prod_site}")


    new_site_adder(site, site_num - 1, site_list)



if __name__ == "__main__":
    new_site_adder(site, input_cheker())
















