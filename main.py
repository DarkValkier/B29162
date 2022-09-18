def sum(a, b):
    return a + b


print('Калькулятор')
a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
print(f'{a} + {b} = {sum(a, b)}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')