from typing import Dict, List




def prints_out_the_dictionary(symbal_dict_for_print: Dict[str, int], sorted_key: int = 0) -> None:
    """
     Выводит словарь частот на экран.
    :param symbal_dict_for_print: Словарь частот для вывода, где ключи — символы, значения — их частота.
    :param sorted_key: Флаг для сортировки по ключам (0 - без сортировки, 1 - с сортировкой).
    :return: None
    """
    if sorted_key == 0:
        for i_key, i_value in symbal_dict_for_print.items():
            print(i_key, ":", i_value)
    else:
        for j_key, j_value in sorted(symbal_dict_for_print.items()):
            print(j_key, ":", j_value)




def reverses_the_dictionary_of_symbols(symbal_dict: Dict[str, int]) -> Dict[int, List[str]]:
    """
     Инвертирует словарь частот символов.
    :param symbal_dict: Оригинальный словарь частот, где ключи — символы, значения — их частота.
    :return: Инвертированный словарь с частотой как ключом и списком символов как значением.
    """
    symbal_dict_inverted = {}
    for key, value in symbal_dict.items():
        if value not in symbal_dict_inverted:
            symbal_dict_inverted[value] = []
        symbal_dict_inverted[value].append(key)
    return symbal_dict_inverted




def great_dict(text: str) -> Dict[str, int]:
    """
    Создает словарь частот символов из текста.
    :param text: Входной текст для анализа.
    :return: Словарь с символами как ключами и их частотой как значениями.
    """
    symbal_dict = {sym: text.count(sym) for sym in text}
    return symbal_dict




def frequency_histogram() -> None:
    """
    Выполняет анализ частоты символов в тексте и выводит оригинальный и инвертированный словари.
      Запрашивает ввод текста у пользователя и выводит результаты анализа.
    :return: None
    """
    text = input("Введите текст: ")
    sym_dict: Dict[str, int] = great_dict(text)
    prints_out_the_dictionary(sym_dict)
    prints_out_the_dictionary(reverses_the_dictionary_of_symbols(sym_dict), 1)




if __name__ == "__main__":
    frequency_histogram()