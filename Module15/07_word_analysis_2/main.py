def palindrome_compares(palindrome_symbal_list) -> list[str]:
    """
    Функция принимает список символов и создает новый список с элементами расположенными в обратном порядке.
    :param palindrome_symbal_list: Список строк
    :return: Список строк
    """
    revers_palindrome_list: list[str] = []
    for index in range(-1, -len(palindrome_symbal_list) - 1, -1):
        revers_palindrome_list.append(palindrome_symbal_list[index])
    return revers_palindrome_list




def main() -> None:
    """
    Функция запрашивает слово и создает список из символов этого слова, далее создает новый список с обратным
    расположением элементов с помощью функции palindrome_compares и сравнивает два списка, если списки равны слово
    является палиндромом.
    :return: None
    """
    palindrome: str = input("Введите слово: ")
    palindrome_symbal_list: list[str] = [sym for sym in palindrome]
    palindrome_symbal_list_revers = palindrome_compares(palindrome_symbal_list)
    if palindrome_symbal_list == palindrome_symbal_list_revers:
        print(f"Слово является палиндромом.")
    else:
        print(f"Слово не является палиндромом.")




main()