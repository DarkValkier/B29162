from Lesson_1.character import Character
from berserk import Berserk
from paladin import Paladin
from samurai import Samurai

p1 = Berserk(name='Berserk', hp=100, damage=8, armor=0)
p2 = Samurai(name='Samurai', hp=100, damage=10, armor=0)

while p1.hp > 0 and p2.hp > 0:
    print(p1)
    print(p2)
    p1.attack(p2)
    p2.attack(p1)
    print()

'''
import random

# С вероятностью в 30%
if random.randint(1, 100) <= 30:
    # Прокнуло
else:
    # Не прокнуло
'''