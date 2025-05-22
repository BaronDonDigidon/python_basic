from typing import List, Tuple


def read_participants(filename: str) -> List[Tuple[str, str, int]]:
    """
    Считывает участников из файла.
    Первый элемент файла — минимальный проходной балл во второй тур.
    Возвращает список участников, у которых баллы выше проходного.

    :param filename: Имя входного файла.
    :return: Список кортежей (фамилия, имя, баллы).
    """
    participants = []
    with open(filename, "r", encoding="UTF-8") as file:
        lines = file.readlines()

    passing_score = int(lines[0].strip())
    for line in lines[1:]:
        last_name, first_name, score_str = line.strip().split()
        score = int(score_str)
        if score > passing_score:
            participants.append((last_name, first_name, score))
    return participants


def write_second_tour(filename: str, participants: List[Tuple[str, str, int]]) -> None:
    """
    Записывает участников второго тура в файл, отсортированных по убыванию баллов.

    :param filename: Имя выходного файла.
    :param participants: Список участников (фамилия, имя, баллы).
    """
    participants.sort(key=lambda x: x[2], reverse=True)
    with open(filename, "w", encoding="UTF-8") as file:
        file.write(f"{len(participants)}\n")
        for index, (last_name, first_name, score) in enumerate(participants, start=1):
            initial = first_name[0] + "."
            file.write(f"{index}) {initial} {last_name} {score}\n")


def main() -> None:
    input_file = "first_tour.txt"
    output_file = "second_tour.txt"
    participants = read_participants(input_file)
    write_second_tour(output_file, participants)


if __name__ == "__main__":
    main()