import random

def ask_user_input() -> int:
    """
    Запрашивает у пользователя целое число.

    :return: Введённое пользователем число (int)
    """
    while True:
        try:
            return int(input("Введите число: "))
        except ValueError:
            print("Ошибка: введите целое число.")


def maybe_throw_exception() -> None:
    """
    С вероятностью 1 к 13 выбрасывает исключение,
    имитируя случайную неудачу.

    :raises Exception: Сообщение о неудаче
    """
    if random.randint(1, 13) == 1:
        raise Exception("Вас постигла неудача!")


def append_to_file(filename: str, number: int) -> None:
    """
    Добавляет введённое число в файл, с новой строки.

    :param filename: Имя файла для дозаписи
    :param number: Число, которое нужно записать
    """
    with open(filename, "a", encoding="UTF-8") as file:
        file.write(f"{number}\n")


def run_lucky_number_game(filename: str = "out_file.txt") -> None:
    """
    Основная логика программы:
    - Запрашивает числа от пользователя.
    - Случайным образом выбрасывает исключение (1 к 13).
    - Записывает каждое число в файл.
    - Повторяется до тех пор, пока сумма всех чисел не станет >= 777.
    - В случае исключения программа завершает выполнение досрочно.

    :param filename: Имя выходного файла для записи введённых чисел
    """
    total: int = 0

    try:
        while total < 777:
            number: int = ask_user_input()
            maybe_throw_exception()
            append_to_file(filename, number)
            total += number
    except Exception as e:
        print(e)
    else:
        print("Вы успешно выполнили условие для выхода из порочного цикла!")


if __name__ == "__main__":
    run_lucky_number_game()