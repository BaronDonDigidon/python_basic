number: int = int(input("Введите число: "))
print(f"Список из нечётных чисел от одного до N: {[num for num in range(1, number + 1, 2)]}")