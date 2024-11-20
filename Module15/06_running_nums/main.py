number_elements: int = int(input("Введите количество элементов списка: "))
num_list: list[int] = []
for _ in range(number_elements):
    num: int = int(input("Введите число: "))
    num_list.append(num)
step: int = int(input("Введите шаг сдвига: "))
new_num_list: int = []
key_count: int = 0
while key_count < len(num_list):
    key_count += 1
    new_num_list.append(num_list[-(step % len(num_list))])
    step -= 1
print(f"Сдвинутый список: {new_num_list}")