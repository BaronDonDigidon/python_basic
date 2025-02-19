from typing import Tuple, Generator, Dict, Iterable




def custom_zip(iter_object_1: Iterable, iter_object_2: Iterable) -> Generator[Tuple, None, None]:
    """

    :param iter_object_1:
    :param iter_object_2:
    :return:
    """
    return ((iter_object_1[i], iter_object_2[i]) for i in range(min(len(iter_object_1), len(iter_object_2))))


# Данные для тестов

# object_1: str = "abcd"
# object_2: Tuple[int, int, int, int] = (10, 20, 30, 40)
# zipuem = custom_zip(object_1, object_2)
# print(zipuem)
# print(*zipuem, sep="\n")


object_1: Dict[str, int] = {"apr" : 12, "afsd" : 232, "keni" : 3215, "rubius" : 15125, "albus" : 251123}
object_2: Tuple[int, int, int, int] = (10, 20, 30, 40)
zipuem = custom_zip(list(object_1), list(object_2))
print(zipuem)
print(*zipuem, sep="\n")