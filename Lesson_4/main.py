from character import CharacterWithItems
from item import Item
from character import CharacterStats as stat

potion1 = Item('Зелье силы',
               stats={
                   stat.DAMAGE: 2,
                   stat.DEFENCE: 2
               })
weapon1 = Item('Стальной меч', stats={stat.DAMAGE: 4},
               durability=1)
armor1 = Item('Кожанная броня', stats={stat.DEFENCE: 2},
              durability=400)


player1 = CharacterWithItems(
    name='Vasya', hp=30, damage=1, defence=0)
player2 = CharacterWithItems(
    name='Petya', hp=30, damage=1, defence=0)

player1.set_weapon(weapon1)

print(player1)
print(player2)

while player1.hp > 0 and player2.hp > 0:
    player1.attack(player2)
    player2.attack(player1)

    print(player1)
    print(player2)