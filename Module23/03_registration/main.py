from typing import List, Dict


def classify_field(field: str) -> str:
    """
    Определяет тип переданного поля.
    Возвращает:
        - 'age' — если это число,
        - 'email' — если содержит '@' и '.',
        - 'name' — если состоит только из букв,
        - 'unknown' — если не соответствует ни одному из правил.
    """
    if field.isdigit():
        return 'age'
    elif '@' in field and '.' in field:
        return 'email'
    elif field.isalpha():
        return 'name'
    else:
        return 'unknown'


def custom_exception(line: List[str]) -> None:
    """
    Валидирует строку из трёх полей: имя, емейл, возраст.
    Вызывает исключения с сообщением, если:
        - Полей не три,
        - Имя содержит не только буквы,
        - Email не содержит @ и .,
        - Возраст не число от 10 до 99.
    """
    if len(line) != 3:
        raise IndexError("НЕ присутствуют все три поля")

    field_types: List[str] = [classify_field(p) for p in line]
    data: Dict[str, str] = dict(zip(field_types, line))

    if 'name' not in data:
        raise NameError("Поле «Имя» содержит НЕ только буквы")
    if 'email' not in data:
        raise SyntaxError("Поле «Имейл» НЕ содержит @ и . (точку)")
    if 'age' not in data:
        raise ValueError("Поле «Возраст» НЕ является числом от 10 до 99")

    name: str = data["name"]
    email_adress: str = data["email"]
    age_str: str = data["age"]

    if not name.isalpha():
        raise NameError("Поле «Имя» содержит НЕ только буквы")
    if "@" not in email_adress or "." not in email_adress:
        raise SyntaxError("Поле «Имейл» НЕ содержит @ и . (точку)")
    if not age_str.isdigit() or not (10 <= int(age_str) <= 99):
        raise ValueError("Поле «Возраст» НЕ является числом от 10 до 99")


def read_and_process_file(file_name: str) -> None:
    """
    Читает файл с регистрациями, проверяет каждую строку и записывает результат
    в соответствующий лог-файл: registrations_good.log или registrations_bad.log.
    """
    try:
        with open(file_name, "r", encoding="UTF-8") as file, \
                open("registrations_good.log", "w", encoding="UTF-8") as good_log, \
                open("registrations_bad.log", "w", encoding="UTF-8") as bad_log:

            i_line: str
            for i_line in file:
                line: List[str] = i_line.strip().split()
                try:
                    custom_exception(line)
                except (IndexError, NameError, SyntaxError, ValueError) as exc:
                    bad_log.write(f"{i_line.rstrip()}\t\t{exc}\n")
                else:
                    good_log.write(i_line)
    except FileNotFoundError:
        print("Выбранного файла не существует!")


def main() -> None:
    """
    Основная функция запуска программы.
    """
    file_name: str = "registrations.txt"
    read_and_process_file(file_name)


if __name__ == "__main__":
    main()

