from typing import List

violator_songs: list[list[str | float]] = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]




def song_searcher(song_list_1: list[str | float], song_list_2: list[str], total_title: float = 0) -> float:
    """
    Функция находит в первом музыкальном листе музыку из
    второго музыкального листа и возвращает ее общую продолжительность.
    :param song_list_1: лист с намименованием и продолжительностью всей доступной музыки.
    :param song_list_2: выбранная музыка
    :param total_title: общая продолжительность музыки
    :return: None
    """
    for song_1 in range(len(song_list_1)):
        for song_2 in range(len(song_list_2)):
            if song_list_1[song_1][0] == song_list_2[song_2]:
                total_title += song_list_1[song_1][1]
    return round(total_title, 2)




def menu() -> None:
    """
    Функция запрашивает сколько песен выбрать и их названия из общего списка музыки, используя функци song_searcher
    показывает их общее время звучания.
    :return: None
    """
    song_looking: list[str] = []
    song_choose = int(input("Сколько песен выбрать? "))
    for song in range(1, song_choose + 1):
        song_name = input(f"Название {song}-й песни: ")
        song_looking.append(song_name)
    print(f"Общее время звучания песен: {song_searcher(violator_songs, song_looking)}")




menu()