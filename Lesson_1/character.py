class Character:
    def __init__(self, name, hp, damage, armor):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.damage = damage
        self.armor = armor

    def __str__(self):
        return f'{self.name} (hp:{self.hp},' \
               f' damage:{self.damage},' \
               f' armor: {self.armor})'

    def take_damage(self, damage):
        self.hp -= abs(damage)

    def attack(self, target):
        target.take_damage(self.damage)