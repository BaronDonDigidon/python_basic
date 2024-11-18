films: list[str] = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
lover_films: list[str] = []


def choose_films(film: str):
    if film in films:
        return lover_films.append(films[films.index(film)])
    return print(f"Ошибка фильма {film} у нас нет")




film_cunter: int = int(input("Сколько фильмов хотите добавить: "))
for _ in range(film_cunter):
    film_name = input("Введите название фильма: ")
    choose_films(film_name)
print(f"Ваш список любимых фильмов: {', '.join(lover_films)}.")
