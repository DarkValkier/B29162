from Lesson_1.character import Character

'''
    Samurai — каждый удар добавляет 10% к базовому урону; 
    суммируется до 5 раз (максимальный множитель +50%), 
    после чего множитель обнуляется;
'''

class Samurai(Character):
    def __init__(self, name, hp, damage, armor):
        Character.__init__(self, name, hp, damage, armor)
        self.combo_rate = 0.1
        self.combo_count = 0
        self.combo_max = 5

    def count_damage(self):
        return self.damage + self.damage * self.combo_rate * self.combo_count

    def add_combo(self):
        self.combo_count += 1
        if self.combo_count > self.combo_max:
            self.combo_count = 0
        # self.combo_count = (self.combo_count + 1) % (self.combo_max + 1)

    def attack(self, target):
        target.take_damage(self.count_damage())
        self.add_combo()