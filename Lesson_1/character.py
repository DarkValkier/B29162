class Character:
    def __init__(self, name, hp, damage, defence):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.damage = damage
        self.defence = defence

    def __str__(self):
        return f'{self.name} (hp:{self.hp},' \
               f' damage:{self.damage},' \
               f' defence: {self.defence})'

    def take_damage(self, damage):
        self.hp -= abs(damage)

    def attack(self, target):
        target.take_damage(self.damage)
