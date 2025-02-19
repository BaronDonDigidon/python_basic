from typing import Dict, Tuple, List
players: Dict[Tuple[str, str], Tuple[int, int, int]] = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}




def dict_recompos(players_dict: Dict[Tuple[str, str], Tuple[int, int, int]]) -> List[Tuple[str, str, int, int, int]]:
    """
    Объединяет ключ словаря со значением в один кортеж, и возвращает список с кортежами.
    :param players_dict: словарь со значениями и ключами кортежами
    :return: список кортежей
    """
    return [i_key + i_value for i_key, i_value in players_dict.items()]



# Выводим список кортежей
print(dict_recompos(players))