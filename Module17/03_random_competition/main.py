import random
first_team = [round(5 + (10 - 5) * random.random(), 2) for _ in range(20)]
second_team = [round(5 + (10 - 5) * random.random(),2) for _ in range(20)]
print("Победители тура:", [first_team[player] if first_team[player] >= second_team[player] \
                               else second_team[player] for player in range(20)])