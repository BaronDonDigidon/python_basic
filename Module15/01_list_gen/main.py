num: int = int(input("Введите число: "))
list_of_odd_numbers: list[int] = []
for digit in range(1, num + 1, 2):
     list_of_odd_numbers.append(digit)
print(f"Список из нечётных чисел от одного до N: {list_of_odd_numbers}")
