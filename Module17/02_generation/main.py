num = int(input("Введите длину списка: "))
num_list = [num_i % 5 if num_i % 2 != 0 else 1 for num_i in range(num)]
print(f"Результат: {num_list}")



