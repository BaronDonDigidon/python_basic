from typing import NoReturn


def palindrome_compares(palindrome_symbal_list) -> list[str]:
    revers_palindrome_list: list[str] = []
    for index in range(-1, -len(palindrome_symbal_list) - 1, -1):
        revers_palindrome_list.append(palindrome_symbal_list[index])
    return revers_palindrome_list




def main() -> NoReturn:
    palindrome: str = input("Введите слово: ")
    palindrome_symbal_list: list[str] = [sym for sym in palindrome]
    palindrome_symbal_list_revers = palindrome_compares(palindrome_symbal_list)
    if palindrome_symbal_list == palindrome_symbal_list_revers:
        print(f"Слово является палиндромом.")
    else:
        print(f"Слово не является палиндромом.")




main()