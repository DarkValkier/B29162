class NotEnoughFuel(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)


class NegativeDistance(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)


class Car:
    def __init__(self, consumption: float = 1.0, fuel: float = 10.0):
        self.consumption = consumption
        self.fuel = fuel
        self.traveled = 0

    def __str__(self):
        return f'(consumption: {self.consumption}, fuel: {self.fuel})'

    def go(self, distance=1):
        if distance < 0:
            raise NegativeDistance('Расстояние не может быть меньше нуля!')
        counted_consumption = self.consumption * distance
        if self.fuel < counted_consumption:
            raise NotEnoughFuel('Не хватает топлива!')
        self.fuel -= counted_consumption
        self.traveled += distance


