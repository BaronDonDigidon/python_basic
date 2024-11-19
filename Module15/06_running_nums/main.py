number_elements: int = int(input("Введите количество элементов списка: "))
num_list: list[int] = []
for _ in range(number_elements):
    num: int
    num_list.append(num)
step: int = int(input("Введите шаг сдвига: "))
new_num_list: int = []
index: int = -step
while index != len(num_list) - step:
    new_num_list.append(num_list[index])
    index += 1
print(new_num_list)