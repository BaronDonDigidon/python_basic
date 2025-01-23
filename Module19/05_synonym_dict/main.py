from typing import Dict, List

def creates_a_dictionary_of_synonym_pairs(number_of_pairs: int,
                                          synonym_pairs_dict: Dict[str, str] = None) -> Dict[str, str]:
    """
    Создает словарь синонимов на основе введенных пар слов.
    :param number_of_pairs: Количество пар синонимов, которые нужно ввести.
    :param synonym_pairs_dict: Словарь синонимов (по умолчанию пустой).
    :return: Словарь синонимов, содержащий пары слов.
    """
    if synonym_pairs_dict is None:
        synonym_pairs_dict = {}
    for num in range(1, number_of_pairs + 1):
        dict_synonym: List[str] = input(f"{num}-я пара: ").strip().split("-")
        word_1 = dict_synonym[0].strip()
        word_2 = dict_synonym[1].strip()
        if len(dict_synonym) == 2:
            synonym_pairs_dict[word_1] = word_2
        else:
            print("Вводите слова в формате 'Cлово1 - Слово2")
            creates_a_dictionary_of_synonym_pairs(number_of_pairs, synonym_pairs_dict)
    return synonym_pairs_dict




def dict_reverser(synonym_pairs_dict: Dict[str, str]) -> Dict[str, str]:
    """
    Меняет местами ключи и значения словаря.
    :param synonym_pairs_dict: Словарь синонимов.
    :return: Словарь.
    """
    reversed_dict_synonym: Dict[str, str] = {i_value : i_key for i_key, i_value in synonym_pairs_dict.items()}
    return reversed_dict_synonym




def checking_for_a_synonym(synonym_pairs_dict: Dict[str, str]) -> None:
    """
    Запрашивает у пользователя слово и выводит его синоним.
    :param synonym_pairs_dict: Словарь синонимов для поиска.
    :return: None
    """
    reversed_dict = dict_reverser(synonym_pairs_dict)
    while True:
        word = input("Введите слово: ").strip().lower()
        for i_key in synonym_pairs_dict:
            if i_key.lower() == word:
                print(synonym_pairs_dict.get(i_key))
                checking_for_a_synonym(synonym_pairs_dict)
        else:
            for i_key in reversed_dict:
                if i_key.lower() == word:
                    print(reversed_dict.get(i_key))
                    checking_for_a_synonym(synonym_pairs_dict)
            else:
                print("Такого слова в словаре нет.")





def dictionary_of_synonyms() -> None:
    """
    Основная функция для работы со словарем синонимов.
    Запрашивает количество пар синонимов и запускает процесс создания словаря и поиска синонимов.
    :return: None
    """
    synonym_num = int(input("Введите количество пар слов: "))
    synonym_dict: Dict[str, str] = creates_a_dictionary_of_synonym_pairs(synonym_num)
    checking_for_a_synonym(synonym_dict)


if __name__ == "__main__":
    dictionary_of_synonyms()