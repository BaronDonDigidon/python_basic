from typing import Any, Dict, List, Union

data: Dict[str, Union[str, int, Dict[str, int], List[Dict[str, Any]]] ] = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "total_in": 444,
        "total_out": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 3
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 5
        }
    ]
}




def prints_out_the_dictionary(data_dict: Dict[str, Any], space_count: int = 0):
    """
    Рекурсивно выводит ключи и значения словаря с отступами.
    :param data_dict: Словарь для обработки.
    :param space_count: Уровень отступа для форматирования вывода.
    :return: None
    """
    for key, value in data_dict.items():
        print(" " * space_count + f"Ключ: {key}")
        if isinstance(value, dict):
            print(" " * space_count + f"Значение: {{")
            prints_out_the_dictionary(value, space_count + 4)
            print(" " * space_count + f"}}")
        elif isinstance(value, list):
            print(" " * space_count + f"Значение: [")
            for item in value:
                if isinstance(item, dict):
                    print(" " * (space_count + 4) + "{")
                    prints_out_the_dictionary(item, space_count + 8)
                    print(" " * (space_count + 4) + "}")
                else:
                    print(" " * (space_count + 4) + str(item))
            print(" " * space_count + f"]")
        else:
            print(" " * space_count + f"Значение: {value}")






def delete_and_amount(data_dict: Dict[str, Any]) -> None:
    """
    Удаляет ключи и их значения из словаря "tokens". ДОбавляет сумму этих значений по ключю "ETH"total_out".
    :param data_dict: Словарь для обработки.
    :return: None
    """
    total_sum = 0
    for key in data_dict["tokens"]:
        total_out = key.pop("total_out", 0)
        total_sum += total_out
    data_dict["ETH"]["total_out"] += total_sum


data["ETH"]["total_diff"] = 100
data["tokens"][0]["fst_token_info"]["name"] = "doge"
data["tokens"][1]["sec_token_info"]["total_price"] = data["tokens"][1]["sec_token_info"]["price"]
delete_and_amount(data)
prints_out_the_dictionary(data)
