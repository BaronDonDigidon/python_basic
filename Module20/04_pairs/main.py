from random import randint
from typing import List, Tuple

# Создаем список из 10 случайных целых чисел
random_num_list: List[int] = [randint(0, 100) for _ in range(10)]


# Делим числа списка random_num_list на пары кортежей внутри списка
new_random_num_list: List[Tuple[int, int]] = list(zip(random_num_list[::2], random_num_list[1::2]))


#
print(new_random_num_list)