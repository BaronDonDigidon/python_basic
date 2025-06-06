import random
from typing import List

class Student:
    """
    Модель студента с ФИО, номером группы и списком пяти оценок.
    """
    def __init__(self, name, group, grade) -> None:
        """
        :param full_name: Фамилия и имя студента
        :param group_number: Номер группы
        :param grades: Список из пяти оценок (1–5)
        """
        self.name = name
        self.group = group
        self.grade = grade

    def average_grade(self) -> float:
        """
        Возвращает средний балл по списку оценок.
        """
        return sum(self.grade)/len(self.grade)

    def info(self) -> None:
        """Читаемое представление студента с его средней успеваемостью."""
        print("ФИ: {}.Номер группы: {}.Успеваемость: {}.".format(self.name, self.group, self.grade))


class Student_class_sorted:
    """
    Отвечает за создание списка студентов, их сортировку и вывод.
    """
    def __init__(self, num: int, auto_generate: bool = False) -> None:
        """
        :param num: сколько студентов создать
        :param auto_generate: если True, ФИО и группу подставлять рандомно
        """
        self.student_list: List[Student] = []
        for i_student in range(1, num + 1):
            if auto_generate:
                name: str = "Иванов Иван"
                group: str = f"{random.randint(1, 10)}A"
            else:
                name: str = input("Введите фамилию и имя: ")
                group: str = input("Введите номер группы: ")
            grade = [random.randint(1,5) for _ in range(5)]
            self.student_list.append(Student(name, group, grade))

    def sorted_list(self) -> None:
        """
        Сортирует список студентов по возрастанию среднего балла.
        """
        self.student_list.sort(key=lambda s: s.average_grade())

    def print_student_list(self) -> None:
        """
        Выводит в консоль всех студентов из текущего списка.
        """
        for i_student in self.student_list:
            i_student.info()


if __name__ == "__main__":
    student_group: Student_class_sorted  = Student_class_sorted(5, True)
    student_group.sorted_list()
    student_group.print_student_list()