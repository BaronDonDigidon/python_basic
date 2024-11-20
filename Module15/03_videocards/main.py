number_cards: int = int(input("Введите количество видеокарт: "))
cards_list: list[int] = []
new_cards_list: list[int] = []
max_card: int = 0
for card_number in range(1, number_cards + 1):
    card: int = int(input(f"Видеокарта {card_number}: "))
    cards_list.append(card)
    if max_card < card:
        max_card = card
for new_card_number in range(number_cards):
    if cards_list[new_card_number] != max_card:
        new_cards_list.append(cards_list[new_card_number])
print(new_cards_list)





