from typing import Any, Iterator, Generator

class Sequence:
    """
    Класс Sequence.
    Генерирует последовательность из квадратов чисел от 1 до number
    Args:
        number (int): конечное число последовательности
    Attributes:
        cur_val (int): начало последовательности
    """
    def __init__(self, number: int) -> None:
        self.cur_val: int = 0
        self.number: int = number


    def __iter__(self) -> "Sequence":
        return self


    def __next__(self):
        if  self.cur_val >= self.number:
            raise StopIteration


        self.cur_val += 1
        return self.cur_val ** 2


seq: Sequence = Sequence(10)

for i_value in seq:
    print(i_value, end=" ")
print("\n")


def seq_iter(number: int) -> Iterator[int]:
    """
    Генерирует последовательность из квадратов чисел от 1 до number.
    :param number: Число
    :type number: int
    :yield: итерируемый объект с числами
    """
    cur_val: int = 1
    for _ in range(number):
        yield cur_val ** 2
        cur_val += 1


seq: Iterator[int] = seq_iter(10)


for i_value in seq:
    print(i_value, end=" ")
print("\n")


seq: Generator[int | Any, Any, None] = (num ** 2 for num in range(1, 11))
for i_num in seq:
    print(i_num, end=" ")

