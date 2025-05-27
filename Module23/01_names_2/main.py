from typing import List, Tuple


def read_and_process_file(filename: str) -> Tuple[int, List[str]]:
    """
    Читает файл, подсчитывает общее количество символов в строках.
    Если строка содержит менее 3 символов (без учёта \n),
    добавляет сообщение об ошибке в список и выводит его.

    :param filename: Имя файла с именами
    :return: Кортеж — общее количество символов и список ошибок
    """
    total_length: int = 0
    errors: List[str] = []


    try:
        with open(filename, "r", encoding="UTF-8") as file:
            lines = file.readlines()


            for line_number, line in enumerate(lines, start=1):


                try:
                    line_length = len(line.rstrip('\n'))

                    if line_length < 3:
                        raise ValueError(f"Ошибка: менее трёх символов в строке {line_number}.")

                    total_length += line_length

                except ValueError as e:
                    print(e)
                    errors.append(str(e))


    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    return total_length, errors




def write_errors_log(errors: List[str], log_filename: str = "errors.log") -> None:
    """
    Записывает список ошибок в лог-файл.
    :param errors: Список сообщений об ошибках
    :param log_filename: Имя файла для логов (по умолчанию 'errors.log')
    """
    if errors:
        try:
            with open(log_filename, "w", encoding="UTF-8") as log_file:
                for error in errors:
                    log_file.write(error + "\n")
        except Exception as e:
            print(f"Не удалось записать лог ошибок: {e}")




def main() -> None:
    """
    Основная функция запуска программы.
    """
    total, errors = read_and_process_file("people.txt")
    write_errors_log(errors)
    print(f"Общее количество символов: {total}")




if __name__ == "__main__":
    main()