from typing import Dict




site: Dict[str, Dict[str, Dict[str, str]]] = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}




def search_site(site: Dict[str, Dict[str, Dict[str, str]]], word: str,
                max_depth: int, current_depth: int = 1) -> str | None:
    """
    Функция просматривает структуру до заднной глубины, если находит значение искомого ключа возвращает его значение,
    если нет возвращает None.
    :param site: Словарь
    :param word: Искомый ключ
    :param max_depth: максимальная глубина поиска.
    :param current_depth: текущая глубина поиска
    :return: Возвращает значение искомого ключа или None.
    """
    if max_depth is not None and current_depth > max_depth:
        return None
    for key, value in site.items():
        if key == word:
            return value
        if isinstance(value, dict):
            result = search_site(value, word, max_depth,  current_depth + 1)
            if result:
                break
    else:
        result = None
    return result




def main_menu() -> None:
    """
    Функция запрашивает искомый ключ и максимальную глубину поиска, возвращает значение ключа на заданной глубине.
    :return: Значение ключа на заданной глубине.
    """
    word = input("Введите искомый ключ: ")
    depth_call = input("Хотите ввести максимальную глубину? Y/N:")
    depth: int = None
    if depth_call.lower() == "y":
        depth = int(input("Введите максимальную глубину: "))
    value = search_site(site, word, depth)
    print(f"Значение ключа: {value}")




main_menu()