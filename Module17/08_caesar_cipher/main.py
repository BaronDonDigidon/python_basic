def encrypts(text: str, shift: list[int]) -> None:
    """
    Функция заменяет каждую букву текста на следующую по алфавиту через shift позиций по кругу.
    :param shift: Шаг сдвига.
    :return:
    """
    alphabet: list[str] = [chr(i) for i in range(1072, 1104)]
    new_text_list = [(alphabet[(alphabet.index(symbal) + shift) % 32 ] if symbal != " " else " ") for symbal in text]
    print(*new_text_list, sep="")




def menu() -> None:
    """
    Функция запрашивает тект и шаг сдвига, затем зашифровывает его с помощью функции encrypts.
    :return: None
    """
    text: str = input("Введите сообщение: ")
    shift: int = int(input("Введите сдвиг: "))
    print("Зашифрованное сообщение: ", end="")
    encrypts(text, shift)




menu()