def searching_divider(num):
    divider = 2
    while num % divider != 0:
        divider += 1
    return divider


num = int(input("Введите число: "))
if num < 2:
    print("Введите число больше 1!")
else:
    print(f"Наименьший делитель: {searching_divider(num)}")