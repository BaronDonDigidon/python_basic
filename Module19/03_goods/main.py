from typing import Union, Dict

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}




def store_calculator(goods_dict: Dict[str, int], store_dict: Dict[str, Union[list, Dict[str, int]]]) -> None:
    """
    Подсчитывает общее количество и стоимость товаров в магазине на основе предоставленных данных.
    :param goods_dict: Словарь с кодами товаров.
    :param store_dict: Словарь со списками кол-ва разнообразных товаров.
    :return: None. Функция выводит на экран информацию о количестве и стоимости товаров.
    Если товар отсутствует в магазине, выводится соответствующее сообщение.
    """
    for key, value in goods_dict.items():
        if value in store_dict.keys():
            quantity = sum(item['quantity'] for item in store_dict[value])
            price = sum(item['price'] * item['quantity'] for item in store_dict[value])
            print("{0} - {1} штук, стоимость {2} рубля".format(key, quantity, price))
        else:
            print("{0} - отсутствует в магазине".format(key))




store_calculator(goods, store)