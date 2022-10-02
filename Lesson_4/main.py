from character import CharacterWithItems
from item import Item

potion1 = Item('Зелье силы', stats={'damage': 2})
weapon1 = Item('Стальной меч', stats={'damage': 4},
               durability=1)
armor1 = Item('Кожанная броня', stats={'armor': 2},
              durability=400)

player1 = CharacterWithItems(
    name='Vasya', hp=30, damage=1, defence=0)
player2 = CharacterWithItems(
    name='Petya', hp=30, damage=1, defence=0)

player1.set_weapon(weapon1)
print(player1)
print(player2)

player1.attack(player2)
player2.attack(player1)

print(player1)
print(player2)

player1.attack(player2)
player2.attack(player1)

print(player1)
print(player2)