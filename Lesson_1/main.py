from character import Character

player1 = Character(name='Vasya', hp=100, damage=10, defence=0)
player2 = Character(name='Petya', hp=90, damage=12, defence=0)
print(player1)
print(player2)

player1.attack(player2)
player2.attack(player1)

print(player1)
print(player2)