from car import Car, NotEnoughFuel, NegativeDistance

car1 = Car(consumption=0.1, fuel=20)
print(car1)
try:
    car1.go(float(input('Введите расстояние:')))
except NotEnoughFuel:
    print('Не хватает топлива!')
except NegativeDistance:
    print('Расстояние не может быть отрицательным!')

print(car1)
