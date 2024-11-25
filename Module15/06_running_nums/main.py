def list_greater(elem_number: [int], num_list: list[int] = []):
    for _ in range(elem_number):
        num: int = int(input("Введите число: "))
        num_list.append(num)
    return num_list




def num_walker(list_num: list[int], step: int) -> list [int]:
    new_num_list: int = []
    key_count: int = 0
    while key_count < len(list_num):
        key_count += 1
        new_num_list.append(list_num[-(step % len(list_num))])
        step -= 1
    return new_num_list



def main() -> None:
    number_elements: int = int(input("Введите количество элементов списка: "))
    num_list = list_greater(number_elements)
    shift_step: int = int(input("Введите шаг сдвига: "))
    return print(f"Сдвинутый список: {num_walker(num_list, shift_step)}")




main()