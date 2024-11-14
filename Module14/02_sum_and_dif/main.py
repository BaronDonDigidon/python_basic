def adding_numbers(num):
    summ_num = 0
    while num > 0:
        summ_num += num % 10
        num //= 10
    return summ_num

def number_of_digits(num):
    counter = 0
    while num > 0:
        counter += 1
        num //= 10
    return counter

num = int(input("Введите число: "))
print(f"Сумма чисел: {adding_numbers(num)}")
print(f"Количество цифр в числе: {number_of_digits(num)}")
print(f"Разность суммы и количества цифр: {adding_numbers(num) - number_of_digits(num)}")