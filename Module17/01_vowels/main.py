text = input("Введите текст: ")
text_list = [text[symbal_i] for symbal_i in range(len(text)) if text[symbal_i] in "уеёыаоэяию"]
print(f"Список гласных букв: {text_list}")
print(f"Длина списка: {len(text_list)}")