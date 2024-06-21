import random

class Soldier:
    def __init__(self, number, team):
        self.number = number
        self.team = team

    def go_for_hero(self, hero):
        print(f"Солдат {self.number} Является следующим Героем {hero.number}")

class Hero:
    def __init__(self, number):
        self.number = number
        self.level = 1

    def increase_level(self):
        self.level += 1

team1_hero = Hero(1)
team2_hero = Hero(2)

team1_soldiers = []
team2_soldiers = []

for i in range(10):
    team = random.choice([1, 2])
    if team == 1:
        team1_soldiers.append(Soldier(i, 1))
    else:
        team2_soldiers.append(Soldier(i, 2))

if len(team1_soldiers) > len(team2_soldiers):
    team1_hero.increase_level()
else:
    team2_hero.increase_level()

print(f"Количество солдат в команде 1: {len(team1_soldiers)}")
print(f"количество солдат в команде 2: {len(team2_soldiers)}")

solder_to_follow = random.choice(team1_soldiers)
solder_to_follow.go_for_hero(team1_hero)
print(f"Количество солдат: {solder_to_follow.number}")
print(f"Количество солдат: {team1_hero.number}")
