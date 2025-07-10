import os
from typing import Generator

# При помощи модуля os (и функции join) сформируйте пути до файлов work_logs.txt и output.txt в папке data
# (output.txt может не быть в папке data, но его нужно будет там создать, при помощи кода)
input_file_path = os.path.join("data", "work_logs.txt")
output_file_path = os.path.join("data", "output.txt")
# Документация по join https://docs-python.ru/standart-library/modul-os-path-python/funktsija-join-modulja-os-path/

# Не забудьте проверить наличие файлов перед тем как начать работу с ними
# https://docs-python.ru/stSSandart-library/modul-os-path-python/funktsija-exists-modulja-os-path/
def error_log_generator(file_log: str) -> Generator[str, None, None]:
    """
    Получает на вход путь до файла с логами и возвращет строки из этого файла, которые содержат слово ERROR.
    :param file_log: Путь к файлу логов.
    :type file_log: str
    :yield: Строки, содержащие слово 'ERROR'.
    """
    with open(file_log, "r", encoding="UTF-8") as file:
        for line in file:
            if "ERROR" in line:
                yield line


def save_error_logs(file_log: str, output_file: str) -> None:
    """
    Сохраняет строки из лог файла содержащие слово ERROR.
    :param file_log: Путь к файлу логов.
    :type file_log: str
    :param output_file: Путь к файлу для сохранения ошибок.
    :type output_file: str
    """
    if not os.path.exists(file_log):
        print(f"Файл логов не найден.")


    if not os.path.exists(output_file):
        print(f"Файл  для сохранения ошибок не найден.")


    with open(output_file_path, 'w') as output:
        for error_line in error_log_generator(input_file_path):
            output.write(error_line)
    print("Файл успешно обработан.")


save_error_logs(input_file_path, output_file_path)