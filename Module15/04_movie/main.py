films: list[str] = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
films_lower: list[str] = [film_title.lower() for film_title in films]
lover_films: list[str] = []




def choose_films(film: str):
    if film.lower() in films_lower:
        return lover_films.append(films[films_lower.index(film.lower())])
    return print(f"Ошибка: фильма {film} у нас нет")




film_cunter: int = int(input("Сколько фильмов хотите добавить: "))
for _ in range(film_cunter):
    film_name = input("Введите название фильма: ")
    choose_films(film_name)
print(f"Ваш список любимых фильмов: {', '.join(lover_films)}.")
