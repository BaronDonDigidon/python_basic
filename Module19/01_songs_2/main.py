violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}




def calculate_total_duratioan(total_duration: int =  0) -> int:
    """
     Вычисляет общее время звучания выбранных песен.
    :param total_duration: Начальное значение общей продолжительности. По умолчанию равно 0.
    :return: Общее время звучания выбранных песен в минутах.
    """
    songs_num: int = int(input("Сколько песен выбрать? "))
    for i_song in range(1, songs_num + 1):
        song_name = input("Введите название {0}-ой песни ".format(i_song))
        total_duration += violator_songs[song_name]
    return total_duration




def menu() -> None:
    """
    Запускает меню для выбора песен и отображает общее время звучания.
    :return: None
    """
    total_time = calculate_total_duratioan()
    print(f"Общее время звучания песен: {total_time:.2f}")




menu()