from typing import List, Dict, Tuple, Any
students: Dict[int, Dict[str, Any]] = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}




def students_looking(students_dict: Dict[int, Dict[str, Any]], surname_length: int = 0,
                     list_interests: List[str] = []) -> Tuple[List[str], int]:
    """
    Принимает в качестве аргумента словарь и возвращает два значения: полный список интересов
    всех студентов и общую длину всех фамилий студентов.
    :param students_dict: словарь с информацицией по студентам
    :param surname_length: общую длину всех фамилий студентов
    :param list_interests: полный список интересов всех студентов
    :return:
    """
    if list_interests is None:
        list_interests = []


    for i_value in students_dict.values():
        for interests in i_value['interests']:
            list_interests.append(interests)
        surname_length += len(i_value['surname'])


    return list_interests, surname_length



# Список пар "ID студента — возраст"
list_duos: list[tuple[int, int]] = [(i_key, i_value["age"]) for i_key, i_value in students.items()]
print(f"Список пар 'ID студента — возраст': {list_duos}")


# Получение данных о студентах
studens_data = students_looking(students)
print(f"Полный список интересов всех студентов: {set(studens_data[0])}")
print(f"Общая длина всех фамилий студентов: {studens_data[1]}")