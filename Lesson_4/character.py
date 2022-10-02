from Lesson_1.character import Character
from item import Item


class CharacterWithItems(Character):
    def __init__(self, name, hp, damage, defence):
        Character.__init__(self, name, hp, damage, defence)
        self.weapon = None
        self.armor = None

    def set_weapon(self, item: Item = None):
        self.weapon = item

    def set_armor(self, item: Item = None):
        self.armor = item

    def attack(self, target):
        try:
            additional_damage = self.weapon.use()['damage']
        except Exception as error:
            additional_damage = 0
        target.take_damage(self.damage + additional_damage)