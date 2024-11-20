number_elements: int = int(input("Введите количество элементов списка: "))
num_list: list[int] = []
for _ in range(number_elements):
    num: int = int(input("Введите число: "))
    num_list.append(num)
for index_num_1 in range(len(num_list)):
    for index_num_2 in range(len(num_list)):
        if num_list[index_num_1] < num_list[index_num_2]:
            save_num: int = num_list[index_num_2]
            num_list[index_num_2] = num_list[index_num_1]
            num_list[index_num_1] = save_num
print(f"Отсортированный список: {num_list}")