def can_form_palindrome(input_string: str) -> bool:
    """
    Проверяет, можно ли переставить строку в палиндром.
    :param input_string: Строка для проверки.
    :return: True, если строку можно переставить в палиндром, иначе False.
    """
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
    return odd_count <= 1




def main() -> None:
    """
    Основная функция для взаимодействия с пользователем.
    :return: None.
    """
    user_input = input("Введите строку: ").strip()
    if can_form_palindrome(user_input):
        print("Можно сделать палиндромом")
    else:
        print("Нельзя сделать палиндромом")




if __name__ == "__main__":
    main()