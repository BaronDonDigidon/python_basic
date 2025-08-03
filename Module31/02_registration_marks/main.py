from typing import List
import re

text = "А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666"

pattern_private_car: str = r"[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}"
pattern_taxi: str = r"[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}"

private_car: List[str] = re.findall(pattern_private_car, text)
taxi: List[str] = re.findall(pattern_taxi, text)
print("Список номеров частных автомобилей: ", private_car)
print("Список номеров такси: ", taxi)# TODO здесь писать код
