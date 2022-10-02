class Item:
    def __init__(self, name, stats=None,
                 durability=1, unbreakable=False):
        self.name = name
        self.stats = stats
        self.durability = durability
        self.unbreakable = unbreakable

    def use(self):
        if not self.unbreakable:
            if self.durability <= 0:
                return None
            self.durability -= 1
        return self.stats


class Weapon(Item):
