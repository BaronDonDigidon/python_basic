numbers_list = [7, 14, 3, 18, 21, 10, 9, 6]
print("Чётные числа: ", end="")
print(*(numbers_list[i] for i in range(-1, -len(numbers_list) - 1, -1) if numbers_list[i] % 2 == 0), sep=", ")