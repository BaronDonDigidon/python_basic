films: list[str] = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']




def films_chooser(film: str, films_list: list[str], film_lovers: list[str]) -> list[str] | None:
    """
    Проверят список фильмов видеотеки, если фильм есть в видеотеки добавляет его в избранные,
    если нет выводит сообщение ошибке.
    :param film: Название фильма;
    :param films_list: Список фильмов видеотеки;
    :param film_lovers: Список любимых фильмов;
    :return: Добавляет фильм в список или выводит сообщение об ошибке.
    """
    films_lower: list[str] = [film_title.lower() for film_title in films_list]
    if film.lower() in films_lower:
        film_lovers.append(films_list[films_lower.index(film.lower())])
        return film_lovers
    return print(f"Ошибка: фильма {film} у нас нет")




def main(film_list: list[str], lover_films: list[str] = []) -> tuple[list[str], str]:
    """
    Функций запрашивает сколько фильмов хочет добавить пользователь, затем запрашивает название фильма и использует
    функцию films_chooser для проверки фильма на наличие в видеотеке, в случае если фильм в видеотеке найден, добавляет
    фильм в список любимых фильмов.
    :param film_list: Список фильмов видеотеки;
    :param lover_films: Список любимых фильмов;
    :return: Возвращает кортеж, в который входит список фильмов и строка с любимыми фильмами пользователя.
    """
    film_counter: int = int(input("Сколько фильмов хотите добавить: "))
    for _ in range(film_counter):
        film_name = input("Введите название фильма: ")
        films_chooser(film_name, film_list, lover_films)
    return lover_films, f"Ваш список любимых фильмов: {', '.join(lover_films)}."




print(main(films)[1])