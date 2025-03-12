def num_printer(num: int) -> int:
    """
    Принимает число num и выводит числа от 1 до num каждое на отдельной строке.
    :param num: Число введеное пользователем
    :return: Выводит числа от 1 до num каддое на отдельной строке
    """
    if num > 1:
        num_printer(num - 1)
    print(num)




number: int = int(input("Введите число: "))
num_printer(number)
